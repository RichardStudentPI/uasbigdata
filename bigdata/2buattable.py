# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_richard_2055202017"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE anggaran (

    id INT PRIMARY KEY,

    anggaran_belanja VARCHAR(255),

    jenis_anggaran VARCHAR(255),

    jumlah_anggaran VARCHAR(255),

    satuan VARCHAR(255),
    
    tahun VARCHAR(13)

)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()