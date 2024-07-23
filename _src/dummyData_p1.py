import sqlite3
import time
import random

# ct: for timestamp
ct = 0

# データベースに接続（存在しない場合は作成）
conn = sqlite3.connect('../_db/sensor_data_p1.db')

# カーソルを作成
cur = conn.cursor()

# テーブルを作成
cur.execute('''CREATE TABLE IF NOT EXISTS sensor_data
               (id INTEGER PRIMARY KEY, timestamp INTEGER, acceleration_x REAL, acceleration_y REAL, acceleration_z REAL, pulse INTEGER)''')

# データを挿入する関数
def insert_record(timestamp, acceleration_x, acceleration_y, acceleration_z, pulse):
    cur.execute("INSERT INTO sensor_data (timestamp, acceleration_x, acceleration_y, acceleration_z, pulse) VALUES (?, ?, ?, ?, ?)", (timestamp, acceleration_x, acceleration_y, acceleration_z, pulse))
    conn.commit()

# レコードを定期的に挿入
try:
    while True:
        ct += 1
        random_pulse = random.randint(50, 70)
        random_accel_x = random.uniform(-2.0, 2.0)
        random_accel_y = random.uniform(-2.0, 2.0)
        random_accel_z = random.uniform(-2.0, 2.0)

        # データを挿入（ここでは例として固定データを使用）
        insert_record(ct, random_accel_x, random_accel_y, random_accel_z, random_pulse)
        print(ct, random_accel_x, random_accel_y, random_accel_z, random_pulse)
        
        # 0.2秒待機
        time.sleep(0.2)
except KeyboardInterrupt:
    # ループを停止するためのキー割り込みを処理
    print("停止しました")
finally:
    # 接続を閉じる
    conn.close()
