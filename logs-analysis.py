import psycopg2

DB_NAME = "news"

def top_3_articles(name):
    db = psycopg2.connect(database=name)
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
top_3_articles(DB_NAME)
top_3_authors()