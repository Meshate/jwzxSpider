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
                  `student_num` varchar(30) DEFAULT NULL,
                  `name` varchar(30) DEFAULT NULL,
                  `class_num` varchar(20) DEFAULT NULL,
                  `major` varchar(50) DEFAULT NULL,
                  `college` varchar(50) DEFAULT NULL,
                  `gender` varchar(10) DEFAULT NULL,
                  `birthday` varchar(20) DEFAULT NULL,
                  `mz` varchar(20) DEFAULT NULL,
                  PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.cursor.close()

    def insert_data(self, data):
        self.cursor = self.conn.cursor()
        sql = f"""INSERT INTO stu 
        ( student_num, name, gender, class_num, major, college, birthday, mz )
        VALUES
        ( %s, %s, %s, %s, %s, %s, %s, %s );"""
        try:
            self.cursor.execute(sql, (
            data['xh'], data['xm'], data['xb'], data['bj'], data['zym'], data['yxm'], data['csrq'], data['mz']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.cursor.close()
