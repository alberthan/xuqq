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
        print 'num is even number, exit()'
        return 0
        
    mid_number = num/2 
    print 'mid_number is : ',mid_number
    for item in range(1,num*num+1):
        if item == 1:
            row_pos = 0
            colomn_pos = mid_number
            print 'current num to be filled is: ', item
            print 'before fill 1, list is: ', list
            #list[0][mid_number] = 1
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

        '''
        elif item == num * num:
            list[row_pos][colomn_pos] = item
            print 'all numbers are filled'
        '''    
    print 'list is: \n', list

if __name__ == '__main__':
    change(raw_input('please input the number of rows for jiugongge: '))            
                    
            
        
        
