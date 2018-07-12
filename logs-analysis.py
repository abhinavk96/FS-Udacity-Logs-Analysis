import psycopg2

DB_NAME = "news"

def top_3_articles():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select count(*), articles.title from log,articles where (log.path like '/article/%' AND log.status = '200 OK' AND substr(log.path,10) = articles.slug) group by articles.title order by count(*) desc limit 3;")
    articles = c.fetchall()
    for article in articles:
        print('"{}" - {} views'.format(article[1], article[0]))
    db.close()

def top_3_authors():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select count(*), authors.name from log,articles,authors where (log.path like '/article/%' AND log.status = '200 OK' AND substr(log.path,10) = articles.slug AND articles.author=authors.id ) group by authors.name order by count(*) desc;")
    authors = c.fetchall()
    for author in authors:
        print('"{}" - {} views'.format(author[1], author[0]))
    db.close()

def error_significant():
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select CAST(count(case status when '200 OK' then null else 1 end)*100.00/count(*) as DECIMAL(18,2)) , TO_CHAR(time, 'FMMonth DD, YYYY') from log group by TO_CHAR(time, 'FMMonth DD, YYYY') having CAST(count(case status when '200 OK' then null else 1 end)*100.00/count(*) as DECIMAL(18,2)) > 1.00;")
    errors = c.fetchall()
    for error in errors:
        print('{} - {}% errors'.format(error[1], error[0]))
    db.close()
top_3_articles()
top_3_authors()
error_significant()


