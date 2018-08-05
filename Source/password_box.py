# P106 6.3口令保管箱项目，并增加了添加账号密码的功能
import sys
import pyperclip

password = {'email': 'XcWa6PwgRbEXFJa',
            'blog': 'VvNuTFBELzZw7fM',
            'web': 'eEGeFPaRDFaBV3j'}


def password_find(account):
    if account in password:
        pyperclip.copy(password[account])
        print('password ' + account + ' is copied')
    else:
        print('account is not in the Database')


# 判断处理用户没有输入账号的情况
if len(sys.argv) < 2:
    print('''Usage : python3 password_box.py [account]-copy account password
        if you want to add the password,please enter "add",if you enter nothing,the system will exit''')
    # 提示是否需要退出或增加新的账号密码

    key_input = input('''what's your command?\n''')
    if key_input == 'add':
        print('''you are adding the account and the password''')
        account_input = input('''what's your account?\n''')
        password_input = input('''what's your password?\n''')
        password[account_input] = password_input
        print('your account and password are memorized\n do you want to find an account? \n "yes"or "no"')
        if input() == 'yes':
            password_find(input('''which account?\n'''))
        else:
            sys.exit()

    else:
        sys.exit()
else:
    account = sys.argv[1]
    password_find(account)
