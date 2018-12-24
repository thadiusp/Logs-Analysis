#!/usr/bin/env python3

import psycopg2
from prettytable import from_db_cursor


# Answers the question of the most popular articles
print('What are the most popular three articles of all time?')
connection = psycopg2.connect(database='news')

with connection:
    cursor = connection.cursor()
    cursor.execute(
        """SELECT articles.title, count(log.path) AS views
        FROM articles JOIN log ON log.path LIKE concat('%', articles.slug, '%')
        GROUP BY articles.title ORDER BY views DESC LIMIT 3"""
    )

    x = from_db_cursor(cursor)
print(x)
connection.close()


# Answers the question of the most popular author
print('Who are the most popular article authors of all time?')
connection = psycopg2.connect(database='news')

with connection:
    cursor = connection.cursor()
    cursor.execute(
        """SELECT authors.name, count(log.path) AS views
        FROM authors, articles, log
        WHERE authors.id = articles.author AND log.path
        like concat('%', articles.slug, '%')
        GROUP BY authors.name ORDER BY views DESC"""
    )

    x = from_db_cursor(cursor)
print(x)
connection.close()


# Answers the question of which days had 1% or more errors
print('On which days did more than 1% of requests lead to errors?')
connection = psycopg2.connect(database='news')

with connection:
    cursor = connection.cursor()
    cursor.execute(
        """SELECT CAST(time as date) as date, percent
        FROM (SELECT CAST(time as date),
        round(count(CASE status WHEN '404 NOT FOUND' THEN 1 ELSE null END)
        * 100 / sum(count(status))
        OVER (PARTITION by CAST(time as date)), 1) as percent
        FROM log GROUP BY CAST(time as date)) as date WHERE percent >= 1"""
    )

    x = from_db_cursor(cursor)
print(x)
connection.close()
