#!/usr/bin/env python

import psycopg2
import calendar

connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()
cursor.execute('select * from title_to_count limit 3')
results = cursor.fetchall()

for result in results:
    print result[0] + ' -- ' + str(result[1]) + ' views'

print('\n')

cursor.execute(
    'select name, sum(count) from author_name_to_visits group by name order \
     by sum desc')
results = cursor.fetchall()

for result in results:
    print result[0] + ' -- ' + str(result[1]) + ' views'

print('\n')

cursor.execute('select date, \
    CAST(fail AS FLOAT)/CAST(count AS FLOAT)*100 as rate \
    from total_visits_and_fails_by_day where CAST(fail AS FLOAT)/CAST(count \
    AS FLOAT) > 0.01')
results = cursor.fetchall()
for result in results:
    print str(result[0]) + ' -- ' + str(round(result[1], 2)) + '% errors'
connection.close()
