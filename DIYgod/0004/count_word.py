# -*- coding: utf-8 -*-
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count(filepath):
    f = open(filepath, 'rb')
    s = f.read()
    words = re.findall(r'[a-zA-Z0-9]+', s)
    return len(words)

if __name__ == '__main__':
    num = count('count_test.txt')
    print num
