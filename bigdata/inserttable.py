import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'uas_richard_2055202017'
}
 
# Alamat URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/bpkad/od_15840_jumlah_anggaran_belanja_tidak_langsung"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        user_data = response.json().get("data")
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for user in user_data:
            cursor.execute('''
                INSERT INTO anggaran (id, anggaran_belanja, jenis_anggaran, jumlah_anggaran, satuan, tahun)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (user['id'], user['anggaran_belanja'], user['jenis_anggaran'], user['jumlah_anggaran'], user['satuan'], user['tahun']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 