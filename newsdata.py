import psycopg2

# Answers the question of the most popular article
# def art:
connection = psycopg2.connect(database='news')
cursor = connection.cursor()
cursor.execute(
    "SELECT articles.title, count(*) AS num FROM articles JOIN log ON log.path LIKE concat('%', articles.slug, '%') GROUP BY articles.title ORDER BY num DESC LIMIT 3"
)
results = cursor.fetchall()
print(results)
connection.close()


# Answers the question of the most popular author
# def auth:
connection = psycopg2.connect(database='news')
cursor = connection.cursor()
cursor.execute(
    "SELECT authors.name, count(*) AS num FROM authors, articles, log WHERE authors.id = articles.author AND log.path like concat('%', articles.slug, '%') GROUP BY authors.name ORDER BY num DESC"
)
results = cursor.fetchall()
print(results)
connection.close()


# Answers the question of which days had 1% or more errors
connection = psycopg2.connect(database='news')
cursor = connection.cursor()
cursor.execute(
    "SELECT CAST(time as date) as date, percent FROM (SELECT CAST(time as date), round(count(CASE status WHEN '404 NOT FOUND' THEN 1 ELSE null END) * 100 / sum(count(status)) OVER (PARTITION by CAST(time as date)), 1) as percent FROM log GROUP BY CAST(time as date)) as date WHERE percent >= 1"
)
results = cursor.fetchall()
print(results)
connection.close()