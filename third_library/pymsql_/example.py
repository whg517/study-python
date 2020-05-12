# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  example.py
@Date: 2019/1/3 10:30
@Description:
"""

__author__ = 'wanghuagang'

import pymysql


def example_1():
    try:
        # 创建连接
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="000000", db='pyadmin_customs',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor
                               )
        # 创建游标
        cursor = conn.cursor()
        # 执行mysql语句，并返回执行的结果
        cursor.execute("show tables;")

        print(cursor.fetchall())  # fetchall 获取所有返回结果

        res = cursor.execute('SELECT * from auth_user')  # res 接受返回结果长度

        for i in range(res):
            print(cursor.fetchone())

        # conn.commit() 不会自动 commit，如果修改表，要手动 commit

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def example_2():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="000000", db='pyadmin_customs',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor
                           )

    # 使用 with 管理上下文，在操作完成后自动关闭右边连接
    with conn.cursor() as cursor:
        cursor.execute('SELECT * from auth_user')
        # cursor 本身也是可迭代的对象
        for i in cursor:
            print(i)


def example_3():
    # 使用 with 自动管理 mysql 连接
    with pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="000000", db='pyadmin_customs',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor
                         ) as conn:
        # 使用 with 管理上下文，在操作完成后自动关闭右边连接
        with conn.cursor() as cursor:
            cursor.execute('SELECT * from auth_user')
            # cursor 本身也是可迭代的对象
            for i in cursor:
                print(i)


class MysqlHelper(object):

    def __init__(self,
                 host='127.0.0.1',
                 port=3306,
                 user='root',
                 passwd='',
                 db='test',
                 charset='utf8',
                 cursorclass=pymysql.cursors.DictCursor
                 ):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    passwd=passwd,
                                    db=db,
                                    charset=charset,
                                    cursorclass=cursorclass)

    # # 此作用类似于 Java Class.get() 方法
    # @property
    # def cursor(self):
    #     return self.conn.cursor()

    def show_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SHOW TABLES')
            return cursor.fetchall()

    def select(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            for i in cursor:
                yield i  # 返回生成器，防止数据全部加载到内存

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    example_2()
