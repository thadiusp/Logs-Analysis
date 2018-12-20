import psycopg2

#Answers the question of the most popular article
#def art:
connection = psycopg2.connect('news')
cursor = connection.cursor()
cursor.execute(
    'SELECT articles.title, count(*) AS num FROM articles JOIN log ON log.path LIKE concat("%", articles.log, "%") GROUP BY articles.title ORDER BY num DESC LIMIT 3'
)
results = cursor.fetchall()
print(results)
connection.close()


#Answers the question of the most popular author
#def auth:
connection = psycopg2.connect('news')
cursor = connection.cursor()
cursor.execute(
    ''
)
results = cursor.fetchall()
print(results)
connection.close()