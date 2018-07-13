#!/usr/bin/env python3
import psycopg2

DB_NAME = "news"


def top_3_articles():
    """
    Prints the top 3 articles from the database,
    sortedin descending order according to views
    """
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute('''SELECT COUNT(*), articles.title FROM log,articles
             WHERE (log.path like '/article/%'
             AND log.status = '200 OK'
             AND substr(log.path,10) = articles.slug)
             GROUP BY articles.title ORDER BY COUNT(*) DESC limit 3;
             ''')
    articles = c.fetchall()
    for article in articles:
        print('* "{}" - {} views'.format(article[1], article[0]))
    db.close()


def popular_authors():
    """
    Prints the list of authors and the number of times
    their articles have been viewed in descending order of views
    """
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute('''SELECT COUNT(*), authors.name FROM log,articles,authors
            WHERE (log.path like '/article/%'
            AND log.status = '200 OK'
            AND substr(log.path,10) = articles.slug
            AND articles.author=authors.id )
            GROUP BY authors.name ORDER BY COUNT(*) DESC;
            ''')
    authors = c.fetchall()
    for author in authors:
        print('* {} - {} views'.format(author[1], author[0]))
    db.close()


def error_significant():
    """
    Prints the dates from logs on which the percentage
    of requests resulting in error is greater than 1.
    """
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute('''SELECT CAST(COUNT(CASE status WHEN '200 OK'
             THEN NULL ELSE 1 END)*100.00/COUNT(*) as DECIMAL(18,2)),
             TO_CHAR(time, 'FMMonth DD, YYYY') FROM log
             GROUP BY TO_CHAR(time, 'FMMonth DD, YYYY')
             having CAST(COUNT(CASE status WHEN '200 OK'
             THEN NULL ELSE 1 END)*100.00/COUNT(*)
             as DECIMAL(18,2)) > 1.00;
             ''')
    errors = c.fetchall()
    for error in errors:
        print('* {} - {}% errors'.format(error[1], error[0]))
    db.close()


def generate_report():
    """
    Formats the output and calls other functions to generate report.
    """
    padding = "\n===============================================\n"
    print("*********************\nLog Analysis Report\n*********************")
    print("{}The most popular three articles of all time:{}"
          .format(padding, padding))
    top_3_articles()
    print("{}The most popular article authors of all time:{}"
          .format(padding, padding))
    popular_authors()
    print("{}The day on which more than 1% of requests lead to errors:{}"
          .format(padding, padding))
    error_significant()
    print("\n*********************\nEnd of Report\n*********************")

generate_report()
