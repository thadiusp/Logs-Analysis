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
