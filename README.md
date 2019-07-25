# LogAnalysis

A project showing most-viewed books, and authors.

1. Download and unzip LogAnalysis-master.zip from https://github.com/den330/LogAnalysis/archive/master.zip
2. Run the following sql command.
3. Run command line "python LogAnalysis.py" to run the program.

```sql
Create view slugCount AS SELECT SUBSTRING(path, 10, length(path)), 
count(*) FROM log WHERE status='200 OK' 
GROUP BY path ORDER BY count DESC

Create view title_to_count AS SELECT articles.title, 
slugCount.count FROM articles JOIN slugCount 
ON articles.slug = slugCount.substring;

Create view authorNameToTitleTable AS SELECT 
authors.name, articles.title FROM articles JOIN 
authors ON articles.author = authors.id;

Create view total_visit_by_day 
AS SELECT date(time), count(*) 
FROM log GROUP BY date(time);

Create view total_fail_by_day AS SELECT date(time), count(*) 
FROM log WHERE status != '200 OK' 
GROUP BY date(time);

Create view author_name_to_visits AS SELECT authornametotitletable.name, title_to_count.count 
FROM authornametotitletable JOIN title_to_count 
ON authornametotitletable.title = title_to_count.title;

Create view total_visits_and_fails_by_day AS SELECT total_visit_by_day.date, total_visit_by_day.count, 
total_fail_by_day.count AS fail FROM 
total_visit_by_day JOIN total_fail_by_day 
ON total_visit_by_day.date = total_fail_by_day.date;
```