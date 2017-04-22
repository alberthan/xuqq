#!/bin/env python
# -*- coding: utf-8 -*-
import random

'''
【问题描述】

在微信发群红包，设定了总金额和总人数之后，每个人能抢到多少红包是随机的。
要求：使用函数模拟一个随机分配红包的方法


参考文章：用 Python 实现一个简单的微信红包算法（http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=402183699&idx=1&sn=f5c12abeec90d32eca177dce2b1ca467）
 
主要涉及内容：随机数
'''

#这里我们把最小单位换算成分，所以最少拿到一分钱，money的单位是分
def package(total_money, total_person):
    average_money = float(total_money / total_person)*2
    money_list = []
    for i in range (total_person):
        
        tmp_money = int(random.uniform(1,min(average_money,total_money)))
        total_money = total_money - tmp_money
        money_list.append(tmp_money)
        if i < total_person - 1:
            continue
        elif i == total_person - 1:
            money_list.append(total_money)
            
    print"ramdom assigned package is :" , money_list
    
if __name__ == '__main__':
    total_money_input = float(raw_input('Please enter total money you want to split: '))
    total_person_input = int(raw_input('Please input the person number you want to give: '))
    package(total_money_input, total_person_input)
    