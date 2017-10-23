import MySQLdb

try:
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='109427',
        db='news',
        port=3306,
        charset='utf8'
        )
    cursor = conn.cursor()
    sql = (
            "insert into testformysql (name,type)"
            " values (%s,%s)")
    print (sql)
    cursor.execute(sql,('xiao3','xiao3'))
    conn.commit()
    cursor.close()
    conn.close()
except MySQLdb.Error as error:
    print ('Error: %s' % error)