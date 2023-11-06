import mysql.connector

try:
    my_conn = mysql.connector.connect(host="roundhouse.proxy.rlwy.net",
                                      port="47637",
                                      database="railway",
                                      user="root",
                                      password="AhcdF-Ch6BGh21Af6hAc2-FD51Hbca2d")
    my_cursor = my_conn.cursor()
    print("You are connected!")

except Exception as e:
    print("Error",e)