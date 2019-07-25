# LogAnalysis

Run command line "python LogAnalysis.py" to run the program.


#create view slugCount as select SUBSTRING(path, 10, length(path)), 
#count(*) from log where status='200 OK' 
#group by path order by count desc

#create view title_to_count as select articles.title, 
#slugCount.count from articles join slugCount 
#on articles.slug = slugCount.substring;

#create view authorNameToTitleTable as select 
#authors.name, articles.title from articles join 
#authors on articles.author = authors.id;

#create view total_visit_by_day 
#as select date(time), count(*) 
#from log group by date(time);

#create view total_fail_by_day as select date(time), count(*) 
#from log where status != '200 OK' 
#group by date(time);

#create view author_name_to_visits as select authornametotitletable.name, title_to_count.count 
#from authornametotitletable join title_to_count 
#on authornametotitletable.title = title_to_count.title;

#create view total_visits_and_fails_by_day as select total_visit_by_day.date, total_visit_by_day.count, 
#total_fail_by_day.count as fail from 
#total_visit_by_day join total_fail_by_day 
#on total_visit_by_day.date = total_fail_by_day.date;