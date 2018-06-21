from mysql import connector


class sql_con():
    def __init__(self, user, password, database, host='127.0.0.1'):
        try:
            self.conn = connector.connect(
                user=user, password=password, database=database, host=host)
        except ConnectionError as e:
            print(e)

    def create_table(self):
        self.cursor = self.conn.cursor()
        sql = """CREATE TABLE `stu` (
                  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
                  `studentnum` varchar(30) DEFAULT NULL,
                  `name` varchar(30) DEFAULT NULL,
                  `gender` varchar(10) DEFAULT NULL,
                  `classnum` varchar(30) DEFAULT NULL,
                  `major` varchar(40) DEFAULT NULL,
                  `college` varchar(60) DEFAULT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE = InnoDB DEFAULT CHARSET = utf8; """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
        except Exception as e:
            return e

    def set_info(self, data):
        self.cursor = self.conn.cursor()
        sql = f"""INSERT INTO stu 
        ( studentnum, name, gender, classnum, major, college )
        VALUES
        ( \"{data[0]}\", \"{data[1]}\", \"{data[2]}\", \"{data[3]}\", \"{data[4]}\", \"{data[5]}\" );"""
        self.cursor.execute(sql)
        self.conn.commit()
        self.cursor.close()
