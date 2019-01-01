# News website Log Analysis

this project uses PostgreSQL to access a website news database
newsdata.py uses psycopg2 to create a report to answer the following questions...

1. What are the three most popular articles of all time?
2. Who are the most popular authors?
3. On which days did more than 1% of requests lead to errors?

## Database

There are three tables... articles, authors, log
The articles table includes the author id, title, slug, body, and a unique story id
The authors table includes the name, a bio, and a unique author id
The log table includes the path, status (indicates successful connection or not), and a unique id

## Requirements

Vagrant
Virtualbox
Python
PostgreSQL
psycopg2
PrettyTable
newsdata.sql

## Dependencies

```bash
pip3 install psycopg2
```

```bash
pip3 install PrettyTable
```

```bash
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```

## Process

Import newsdata.sql

psql -d news -f newsdata.sql

Run the code

python3 newsdata.py