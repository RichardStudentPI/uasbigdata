import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_richard_2055202017"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM anggaran"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["ID", "Anggaran Belanja", "Jenis Anggaran", "Jumlah Anggaran", "Satuan", "Tahun"])

 

# Simpan dataframe sebagai file Excel

df.to_csv("data_Anggaran.csv", index=False)

 

print("Data telah disimpan dalam file CSV 'data_Anggaran.csv'") #csv / xlsx

 