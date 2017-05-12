#!/usr/bin/python
#coding:utf-8


#list = [[0,0,0],[0,0,0],[0,0,0]]
#num为奇数时的算法
def change(num):
    num = int(num)
    list = [[0 for i in range(num)] for i in range(num)] 
    print 'before filling, list is: ', list
    print '\n'

    
    if num % 2 == 1:
        print 'num is odd number'

    elif num % 2 == 0:
        print 'num is even number, goto another function'
        change_even(num)
        exit(0)
        
    mid_number = num/2 
    print 'mid_number is : ',mid_number
    for item in range(1,num*num+1):
        if item == 1:
            row_pos = 0
            colomn_pos = mid_number
            print 'current num to be filled is: ', item
            print 'before fill 1, list is: ', list
            
            list[0][mid_number] = 1
            print 'After fill 1, list is :', list
            print '1 has been filled , now num to be filled is: ', item
            item = item + 1
            
            row_pos = row_pos - 1
            colomn_pos = colomn_pos + 1
            
        elif item > 1 and item < num*num+1:
            print 'current item is: ', item
            print 'current list is: ', list
            if row_pos < 0 and colomn_pos < num:
                row_pos = num - 1
                colomn_pos = colomn_pos

            elif colomn_pos > num - 1 and row_pos < num and row_pos > -1:
                colomn_pos = 0
                row_pos = row_pos

            elif (row_pos < 0) and (colomn_pos > num - 1):
                row_pos = row_pos + 2
                colomn_pos = colomn_pos -1 
                
            elif list[row_pos][colomn_pos] != 0:
                row_pos = row_pos + 2
                colomn_pos = colomn_pos -1                 
            
            print 'current row_pos is for current item, it is now: ', row_pos
            print 'current colomn_pos is for current item, it is now: ',  colomn_pos            
            list[row_pos][colomn_pos] = item
            row_pos = row_pos - 1
            colomn_pos = colomn_pos + 1 
            print '\nnext, row_pos for next item to be filled, it is: ', row_pos
            print 'next, colomn_pos for next item to be filled, it is: ', colomn_pos
            
            item = item + 1
            print 'next item is: ', item
            print '*****************'
            continue
            
    print 'list is: \n', list

#以下num是几维数组的维度，偶数阶的处理方法    
def change_even(num):
    num = int(num)
    sum = num*num + 1
    #初始化list，告诉程序这是一个二维数组，防止不初始化直接填充的话会报错
    list = [[0 for i in range(num)] for i in range(num)] 
    
    #首先把数字按顺序填进去
    for i in range(0,num):
        for j in range(0,num):
            item = i * num + j + 1
            list[i][j] = item
    print 'before sorting, list is : ', list
    
    #开始交换顺序
    for i in range(0,num):
        for j in range(0,num):
            if i == j :
                list[i][j] = sum - list[i][j]
            elif i + j == num -1:
                list[i][j] = sum - list[i][j]
  
    print '\nafter sorting, list is : ', list
    
if __name__ == '__main__':
    change(raw_input('please input the number of rows for jiugongge: '))            
                    
            
        
        
