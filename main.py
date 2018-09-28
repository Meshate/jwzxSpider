import sys
import requests
import sqltool
from tqdm import tqdm
import json

url = 'http://jwzx.cqupt.edu.cn/data/json_StudentSearch.php?searchKey='

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(
            f'Usage: $ python {sys.argv[0]} [username] [password] [database]\n')
        exit(-1)
    if len(sys.argv) == 4:
        sql = sqltool.sql_con(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        sql = sqltool.sql_con(sys.argv[1], sys.argv[2], sys.argv[3],
                              sys.argv[4])
    sql.create_table()

    pbar = tqdm(total=632)

    for i in '012345678':
        for j in '0123456':
            pbar.update(10)
            for k in '0123456789':
                search_by = '201' + i + '21' + j + k
                data = requests.get(url=url + search_by)
                part = json.loads(data.text)['returnData']
                if len(part) == 0:
                    break
                else:
                    for any in part:
                        sql.insert_data(any)

    for i in ['L1', 'L2']:
        data = requests.get(url=url + i)
        part = json.loads(data.text)['returnData']
        for any in part:
            sql.insert_data(any)
        pbar.update(1)
