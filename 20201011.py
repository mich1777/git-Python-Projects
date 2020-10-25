'''class listnode(object):
    def _init_(self, value=None, next=None):
        self.val = value
        delf.next = next 
testlist = list('Apple')
print(testlist)
list ='I love you DD!!'
a = list.split(' ')
print(list)
print(a)'''

'''
year_list = [1989, 1990, 1991, 1992, 1993, 1994]
print(year_list[3])
print(year_list[5])

things = ['moz', 'cin', 'sal']
'''

array = ['none']*11
i = 'keep'
top = 0

while i != '4':
    print('------------------------------------')
    print('Stack test program')
    print(array)
    print(top, array[top])
    print('1.push')
    print('2.pop')
    print('3.peak')
    print('4.get out')
    i = input('Please enter the options number:')
    if i == '1':
        if top != 10:
            top = top+1
            put = input('Input a int  number:')
            try:
                put = int(put)
                print(put)
                array[top] = put
            except ValueError:
                print(123)
                top = top-1
        else:
            print('Please pop at least one number')
    elif i == '2':
        if top >= 1:
            array[top] = 'none'
            top = top-1
        else: print('Please push at least one number')
    elif i == '3':
        print(array[top])
    elif i == '4':
        array = ['none']*10
    else:
        print('Error')


