#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
测试csv库demo示例
'''
import csv

# csv.reader类
# 官方解释可以任意可迭代的对象，也可以是文件（open文件需要参数newline，定义行与行的分割界限）


def test_reader():
    with open("userscore.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
            print(','.join(row))


def test_writer():
    with open("eggs.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['spam'] * 5 + ['Baked Beans'])
        csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def test_writer_2():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['10002', 'LiSi', '20'])
        writer.writerow(['10001', 'ZhangSan', 18])


def csv_dict_write(path, head, data):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writeheader()
        writer.writerows(data)
        return True


def csv_dict_read(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, dialect='excel')
        for row in reader:
            print(row['Name'])


if __name__ == "__main__":
    # test_reader()
    # test_writer()
    # test_writer_2()

    # head = ['Name', 'Age']
    # data = [
    #     {'Name': 'Keys', 'Age': 28},
    #     {'Name': 'HongPing', 'Age': 29},
    #     {'Name': 'WenChao', 'Age': 15}
    # ]
    # csv_dict_write('test2.csv', head, data)

    csv_dict_read('test2.csv')

