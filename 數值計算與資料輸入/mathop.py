#!usr/bin/python3
'''
讓使用者輸入被除數(整數)及除數(整數，不可以是零)
程式會顯示兩數相除的商及餘數
'''

n = int(input('請輸入被除數(整數):'))
m = int(input('請輸入除數(整數,不可以為0):'))
print('商',n//m,'餘數:',n%m)
