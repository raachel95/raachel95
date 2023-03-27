
import pymysql

def open():
        db = pymysql.connect(host = "localhost", user = "root", password = "Jokerhater95", database="userinfo")
        return db

def check(username, password):
    db = open()
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(username, password) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result

def exec(sql,values):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql,values) # 执行增删改的SQL语句
        db.commit() # 提交数据
        return 1 # 执行成功
    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败
    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接

def query(sql,*keys):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql,keys) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果
