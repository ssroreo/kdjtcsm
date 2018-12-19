import pymysql

str = input("restaurant name: ")
 
# 打开数据库连接
db = pymysql.connect("106.12.95.107","root","123456","kdjtcsm" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

while str != 'exit':
    # SQL 插入语句
    sql = """INSERT INTO restinfo(restaurant) VALUES ('%s')""" % str
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("success!")
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("fail!")
    str = input("restaurant name: ")
# 关闭数据库连接
db.close()