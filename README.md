# jwzxSpider
一个内网环境下的教务在线信息爬虫

## Last update

1. **火速适配全新教务在线3.0**

2. 删减了一些第三方库的依赖
3. 对数据库逻辑进行了优化(应该)

## Based on

#### Environment

- Python3.6 or later
- mysql5.7

#### pip package

- requests
- mysql-connector-python
- tqdm

#### install pip package

`pip install tqdm requests mysql-connector-python`

## To run
### Notice

**Make sure there is no table named "stu" in the current database**

#### To download

`$ git clone https://github.com/Meshate/jwzxSpider.git && cd jwzxSpider `

#### If local mysql

`$ python main.py [username] [password] [database]`

#### If mysql server

`$ python main.py [username] [password] [database] [server]`

## To do

- faster crawl