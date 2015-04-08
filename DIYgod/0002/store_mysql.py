# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import mysql.connector

def store_mysql(filepath):
    conn = mysql.connector.connect(user = 'root', password = '1207', database = 'ShowMeTheCode')
    cursor = conn.cursor()

    # 判断表是否已经存在
    cursor.execute('show tables in ShowMeTheCode;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
                CREATE TABLE `ShowMeTheCode`.`code` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(10) NOT NULL,
                PRIMARY KEY (`id`));
        ''')

    f = open(filepath, 'rb')
    for line in f.readlines():
        code = line.strip()
        cursor.execute("insert into ShowMeTheCode.code (code) values(%s);", [code])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_mysql('Activation_code.txt')
