# jwzxSpider
一个通用版的教务在线信息爬虫

## Based on

#### Environment

- Python3.6 or later
- mysql5.7

#### pip package

- requests
- html-table-extractor
- beautifulsoup4
- mysql-connector-python

## To run
### Notice

**Make sure there is no table named stu in the current database**

#### If local mysql

`python main.py [username] [password] [database]`

#### If mysql server

`python main.py [username] [password] [database] [server]`

## To do

- faster crawl