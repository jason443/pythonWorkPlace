#!/usr/bin/env python3
# -*- coding: utf-8 -*-

___author__ = '3115005056'


import math


def create_data_set():
    data_set = [['SUNNY', 'HOT', 'HIGH', 'WEAK ', 'NO'],
               ['SUNNY', 'HOT', 'HIGH', 'STRONG ', 'NO'],
               ['OVEREAST', 'HOT', 'HIGH', 'WEAK ', 'YES'],
               ['RAIN', 'MILD', 'HIGH', 'WEAK ', 'YES'],
               ['RAIN', 'COOL', 'NORMAL', 'WEAK ', 'YES'],
               ['RAIN', 'COOL', 'NORMAL', 'STRONG ', 'NO']]
    attribute = ['outlook', 'temperature', 'humidity', 'wind']
    return data_set, attribute


def create_tree(data_set, attribute):
    label_list = [labels[-1] for labels in data_set]
    print(label_list)


#逐个属性计算信息增益gain
def find_split(data_set):
    attribute_count = len(data_set[0]) - 1
    base_entropy = calculate_entropy(data_set)
    best_gain = 0.0
    best_attribute = -1
    for i in range(attribute_count):
        attribute_value = [example[i] for example in data_set]
        attribute_set = set(attribute_value) #




def calculate_entropy(data_set):
    count = len(data_set)
    label_count = {}    #标签相同的纪录的条数，key为标签，值为数量
    for data in data_set:
        current_label = data[-1]
        if current_label not in label_count.keys():
            label_count[current_label] = 0
        label_count[current_label] += 1

    entropy = 0.0

    for key in label_count:
        prob = float(label_count[key])/count
        if prob != 0:
            entropy -= prob * math.log(prob, 2)
    return entropy


# data_set, attribute = create_data_set()
# tree = create_tree(data_set, attribute)

