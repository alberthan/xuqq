#!/bin/env python
# -*- coding: utf-8 -*-
'''
【问题描述】

BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字

BMI < 18.5 体重偏轻
18.5 <= BMI < 24 体重正常
BMI >= 24 体重偏重

设计一个BMI计算器吧，看看自己体重是否正常。
输入：身高、体重值
输出：BMI 指数、是否正常
'''

def BMI(height, weight):
    value_BMI = float(weight / (height * height))
    if value_BMI < 18.5:
        print"you are so light"
    elif value_BMI>= 18.5 and value_BMI < 24:
        print "you are normal"
    elif value_BMI >= 24:
        print "you are a little heavy"
    else:
        print "please input another height and weight"

if __name__ == '__main__':
    height_input = float(raw_input("please input height(meter): "))
    weight_input = float(raw_input("please input weight(KG): "))
    BMI(height_input,weight_input)    
