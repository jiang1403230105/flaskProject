#偏函数
import functools

def index(a1,a2):
    return a1*a2

new_function=functools.partial(index,4)

ret=new_function(2)

print(ret)

class foo(object):
    def __init__(self):
        print("执行了")
    def __setattr__(self, key, value):
        print(key,value)
obj=foo()
obj.xx=123

import pymysql

con=pymysql.Connect(host='127.0.0.1',user='root',password='641641',database='nrm',charset='utf8')
cursor=con.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from user where username =%s and userpassword=%s",('root','123456'))
data=cursor.fetchall()
print(data[0]['userrank'])
cursor.close()
con.close()

db = pymysql.connect(host='127.0.0.1',user='root',password='641641',database='nrm',charset='utf8')
in_cursor=db.cursor(cursor=pymysql.cursors.DictCursor)
insertsql="insert into user(username,userpassword,userrank,state)values(%s,%s,%s,%s)"
try:
    in_re=in_cursor.execute(insertsql,('jiangyoujia1','33333',2,0))
    print(in_re)
    db.commit()
except:
    db.rollback()

in_cursor.close()
db.close()

# ret=bin(0x5)[2:].zfill(64)
# print(ret)
# print(ret[0:60]+"\033[0;33;40m"+ret[60:64]+"\033[0m")
#
# print("\033[0;35;40m方倍实验室\033[0m")
