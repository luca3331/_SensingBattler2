import sqlite3


def create_database():
    # データベースに接続（ファイルが存在しない場合は新規作成）
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # テーブルの作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            acceleration_x REAL NOT NULL,
            acceleration_y REAL NOT NULL,
            acceleration_z REAL NOT NULL,
            pulse INT NOT NULL
        );
    ''')

    # 変更をコミットして接続を閉じる
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()