from flask import Blueprint

login=Blueprint('login',__name__)

@login.route('/login')
def login1():
    return 'login'

@login.route('/logout')
def logout1():
    return '退出'