#Here is given script to upload given data to our DataBase

import pandas as pd
import mysql.connector as msql

#Directories depend on whether your data is located
data = pd.read_csv("/Users/Adlet/Downloads/indexData/Data.csv")
info = pd.read_csv("/Users/Adlet/Downloads/indexData/Info.csv")
processed = pd.read_csv("/Users/Adlet/Downloads/indexData/Processed.csv")

data.dropna(axis = 0, inplace = True)


from mysql.connector import Error
try:
    conn = msql.connect(host='localhost',
                        user='root',
                        password='password') #give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        for i, row in info.iterrows():
            #here %S means string values
            sql = "INSERT INTO stock.info_csv VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()

        for i, row in data.iterrows():
            #here %S means string values
            sql = "INSERT INTO stock.data_csv VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            if (i%100 == 0):
                print("Record inserted", i)
                # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()

        for i, row in processed.iterrows():
            #here %S means string values
            sql = "INSERT INTO stock.processed_csv VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            if (i%100 == 0):
                print("Record inserted", i)
                # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
