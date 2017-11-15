#!/usr/bin/env python3
# -*- coding: utf-8 -*-

___author__ = '3115005056'


import math
import operator


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
    if label_list.count(label_list[0]) == len(label_list): #如果所以标签都一样，则无需再分类
        return label_list[0]

    if len(data_set[0]) == 1: #没有可分类的属性
        return no_more_attribute(label_list)

    best_attribute_num = find_split(data_set)
    best_attribute = attribute[best_attribute_num]
    tree = {best_attribute: {}}
    attribute_values = [data[best_attribute_num] for data in data_set]
    attribute_values_set = set(attribute_values) #去除重复值
    del(attribute[best_attribute_num])
    for values in attribute_values_set:
        sub_data_set = split_data_set(data_set, best_attribute_num, values)
        tree[best_attribute][values] = create_tree(sub_data_set, attribute)
    return tree


#没有可分类属性则选择标签数最多的值返回
def no_more_attribute(data_set):
    label_count = {}
    for label in data_set:
        if label not in label_count.keys():
            label_count[label] = 0
        label_count[label] += 1
    sort_label_count = sorted(label_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sort_label_count[0][0]


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


#预测Label
def fore_see_label(tree, attribute, data):
    tree_key = list(tree.keys())[0]
    attribute_num = -1
    for index in range(len(attribute)):
        if attribute[index] == tree_key:
            attribute_num = index
    data_split = data[attribute_num]
    tree_value = tree[tree_key][data_split]
    if isinstance(tree_value, str):
        return tree_value
    else:
        return fore_see_label(tree_value,attribute,data)


data_set, attribute = create_data_set()
attribute_back_up = []
for item in attribute:
    attribute_back_up.append(item)
tree = create_tree(data_set, attribute)
print(tree)
test_data = ['RAIN', 'MILD', 'HIGH', 'STRONG']
print(fore_see_label(tree, attribute_back_up, test_data))