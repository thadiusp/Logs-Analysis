import psycopg2

#Answers the question of the most popular article
connection = psycopg2.connect('news')
cursor = connection.cursor()
cursor.execute(
    'SELECT articles.title, count(*) AS num FROM articles JOIN log ON log.path LIKE concat("%", articles.log, "%") GROUP BY articles.title ORDER BY num DESC LIMIT 3'
)
results = cursor.fetchall()
print(results)
connection.close()