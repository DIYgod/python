# -*- coding: utf-8 -*-
# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis

def store_redis(filepath):
    r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
    f = open(filepath, 'rb')
    for line in f.readlines():
        code = line.strip()
        r.lpush('code', code)

if __name__ == '__main__':
    store_redis('Activation_code.txt')
