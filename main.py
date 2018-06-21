import sys
import requests
import sqltool
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor

urls = 'http://jwzx.cqupt.edu.cn/jwzxtmp/pubBjsearch.php?action=bjStu'
stu = 'http://jwzx.cqupt.edu.cn/jwzxtmp/'


def work(url):
    data = requests.get(url=url)
    extractor = Extractor(''.join(data.text))
    extractor.parse()
    result = extractor.return_list()
    del result[0]
    for i in result:
        del i[0]
        del i[4]
        del i[-3:]
        sql.set_info(i)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(f'Usage: {sys.argv[0]} [username] [password] [database]\n')
        exit(-1)
    sql = sqltool.sql_con('root', 'Li19638176', 'school')
    sql.create_table()
    data = requests.get(url=urls)
    soup = BeautifulSoup(data.text, 'lxml')
    link = soup.find_all('a', target='_blank')
    for i in link:
        work(stu + i['href'])
        sp = i['href'].split('=')
        print(f'{sp[1]} done')
