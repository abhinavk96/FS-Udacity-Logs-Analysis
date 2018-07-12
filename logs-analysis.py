import psycopg2

DB_NAME = "news"

def top_3_articles(name):
    db = psycopg2.connect(database=name)
    c = db.cursor()
    c.execute("select count(*), path from log where path like '/article/%' group by path order by count(*) desc limit 3;")
    articles = c.fetchall()
    titles = []
    views = []
    for article in articles:
        slug = article[1].replace("/article/", "")
        views.append(article[0])
        c.execute("select title from articles where slug = '{}'".format(slug))
        titles.append(c.fetchone()[0])
    for title, view in zip(titles, views):
        print('"{}" - {} views'.format(title, view))
    db.close()

top_3_articles(DB_NAME)