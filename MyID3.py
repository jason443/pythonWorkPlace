#!/usr/bin/env python3
# -*- coding: utf-8 -*-

___author__ = '3115005056'


import math

#初始化数据集
def create_data_set():
    data_set = [['SUNNY', 'HOT', 'HIGH', 'WEAK ', 'NO'],
               ['SUNNY', 'HOT', 'HIGH', 'STRONG ', 'NO'],
               ['OVEREAST', 'HOT', 'HIGH', 'WEAK ', 'YES'],
               ['RAIN', 'MILD', 'HIGH', 'WEAK ', 'YES'],
               ['RAIN', 'COOL', 'NORMAL', 'WEAK ', 'YES'],
               ['RAIN', 'COOL', 'NORMAL', 'STRONG ', 'NO']]
    attribute = ['outlook', 'temperature', 'humidity', 'wind']
    return data_set, attribute


#构建决策树
def create_tree(data_set, attribute):
    label_list = [labels[-1] for labels in data_set]

    best_attribute_num = find_split(data_set)
    best_attribute = attribute[best_attribute_num]
    tree = {best_attribute: {}}
    attribute_values = [data[best_attribute_num] for data in data_set]
    attribute_values_set = set(attribute_values) #去除重复值
    del(attribute[best_attribute_num])
    for values in attribute_values_set:
        sub_data_set = split_data_set(data_set, best_attribute, values)
        tree[best_attribute][values] = create_tree(sub_data_set, attribute)
    return tree


#逐个属性计算信息增益gain，返回使gain最大的属性
def find_split(data_set):
    attribute_count = len(data_set[0]) - 1
    base_entropy = calculate_entropy(data_set)
    best_gain = 0.0
    best_attribute = -1
    for i in range(attribute_count):
        attribute_value = [example[i] for example in data_set]
        attribute_set = set(attribute_value) #每个属性的不同取值分类
        new_entropy = 0.0
        for values in attribute_set:
            sub_data_set = split_data_set(data_set, i, values)
            prob = len(sub_data_set)/float(len(data_set))
            new_entropy += prob * calculate_entropy(sub_data_set)
        if (base_entropy - new_entropy) > best_gain:
            best_gain = base_entropy - new_entropy
            best_attribute = i
    return best_attribute


#分裂数据集
def split_data_set(data_set, attribute, values):
    son_data_set = []
    for data in data_set:
        if data[attribute] == values: #分裂属性等于相应的值则取出连接到son_data_set中
            reduce_attr = data[:attribute]
            reduce_attr.extend(data[attribute+1:])
            son_data_set.append(reduce_attr)
    return son_data_set


#计算信息熵
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


data_set, attribute = create_data_set()
tree = create_tree(data_set, attribute)

