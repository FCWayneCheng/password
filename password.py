#!/usr/bin/python3

password = '12334'
i=3

while True:
    pwd = input('請輸入密碼:')
    if pwd == password:
        print('恭喜登入成功')
        break
    else:
        i=i-1
        print('密碼錯誤！你還有',i,'次機會')
        if i == 0:
            print('密碼被鎖，請洽客服')