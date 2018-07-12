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


top_3_articles(DB_NAME)