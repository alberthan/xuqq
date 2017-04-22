#!/bin/env python
# -*- coding: utf-8 -*-
import random
'''
【问题描述】

三人斗地主手牌规则：
一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。
 
要求：
将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。
 
可使用 list 和 random 完成。
'''

puke_dic = []
value_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
style_list = ['Flower','Rectancgle','Red_Peach','Black_Peach']
for item_value in value_list:
    for item_style in style_list:
        compoud_item = item_value + '_' + item_style
        puke_dic.append(compoud_item)

#增加大王小王        
puke_dic.append('@small')
puke_dic.append('@@big')  

#这是第几张牌
number = 1
for item in puke_dic:
    print "This is the %s number", number
    print "current puke is now as following:  ",  item
    number = number + 1

#底牌和每个人手上抓的牌都是一个列表
dipai = []
persona = []
personb = []
personc = []

#这是3张底牌
for i in range (1,4):
    a = random.choice(puke_dic)
    dipai.append(a)
    puke_dic.remove(a)
    
#3个人随机摸牌    
for list_item in [persona, personb, personc]:    
    for j in range(1,18):
        a = random.choice(puke_dic)
        list_item.append(a)
        puke_dic.remove(a)
    #把牌洗好，按照顺序排好
    list_item.sort()    
        
print "\ndipai is: ", dipai
print "\n"
print "persona is: \n", persona
print "\n"
print "personb is: \n", personb
print "\n"
print "personc is: ", personc
    
    

   

