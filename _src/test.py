import pygame
import sys
import random
import time
import sqlite3



# Pygameの初期化
pygame.init()

# ウィンドウのサイズ
WINDOW_SIZE = (1080, 720)
FRAME_WIDTH = 1


# 色の定義 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# タイトルロゴ表示フレーム
TITLE_LOGO_POS_X = 440
TITLE_LOGO_POS_Y = 40
TITLE_LOGO_POS_WIDTH = 200
TITLE_LOGO_POS_HEIGHT = 200

# グラフ表示フレーム
HEARTRATE_GRAPH_P1_POS_X = 78
HEARTRATE_GRAPH_P1_POS_Y = 523
HEARTRATE_GRAPH_P2_POS_X = 603
HEARTRATE_GRAPH_P2_POS_Y = 523
HEARTRATE_GRAPH_WIDTH = 400
HEARTRATE_GRAPH_HEIGHT = 150

# プレイヤー表示フレーム
PLAYER_IMG_P1_POS_X = 170
PLAYER_IMG_P1_POS_Y = 40
PLAYER_IMG_P2_POS_X = 700
PLAYER_IMG_P2_POS_Y = 40
PLAYER_IMG_WIDTH = 200
PLAYER_IMG_HEIGHT = 200

# 色の定義 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# グラフの初期データ
graph_data = [random.randint(50, 60) for _ in range(HEARTRATE_GRAPH_WIDTH)]

# データベースに接続
conn_p1 = sqlite3.connect('sensor_data_p1.db')
conn_p2 = sqlite3.connect('sensor_data_p2.db')


# カーソルを作成
cur_p1 = conn_p1.cursor()
cur_p2 = conn_p2.cursor()


def update_graph_data():
    # グラフのデータを更新する（ランダムな値を追加）
    new_data_point = random.randint(50, 100)
    graph_data.append(new_data_point)
    graph_data.pop(0)

# フォントとフォントサイズの設定
font = pygame.font.SysFont(None, 48)

# ウィンドウの設定
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Sensing Battler 2')


def img_load():
    p1_img = pygame.image.load('../_img/IMG_0145.PNG')
    p2_img = pygame.image.load('../_img/IMG_0147.PNG')
    logo_img = pygame.image.load('../_img/IMG_0170.PNG')
    p1_resized_img = pygame.transform.scale(p1_img, (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))
    p2_resized_img = pygame.transform.scale(p2_img, (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))
    logo_resized_img = pygame.transform.scale(logo_img, (TITLE_LOGO_POS_WIDTH, TITLE_LOGO_POS_HEIGHT))
    return p1_resized_img, p2_resized_img, logo_resized_img

def draw_player_img(p1_img, p2_img):
    screen.blit(p1_img, (PLAYER_IMG_P1_POS_X, PLAYER_IMG_P1_POS_Y))
    screen.blit(p2_img, (PLAYER_IMG_P2_POS_X, PLAYER_IMG_P2_POS_Y))

def draw_logo_img(logo_img):
    screen.blit(logo_img, (TITLE_LOGO_POS_X, TITLE_LOGO_POS_Y))


def draw_graph():
    # グラフの描画
    for i in range(1, len(graph_data)):
        pygame.draw.line(screen, BLUE, (HEARTRATE_GRAPH_P1_POS_X + i - 1, HEARTRATE_GRAPH_P1_POS_Y + HEARTRATE_GRAPH_HEIGHT - graph_data[i - 1]),
                         (HEARTRATE_GRAPH_P1_POS_X + i, HEARTRATE_GRAPH_P1_POS_Y + HEARTRATE_GRAPH_HEIGHT - graph_data[i]), 2)
        
    for i in range(1, len(graph_data)):
        pygame.draw.line(screen, RED, (HEARTRATE_GRAPH_P2_POS_X + i - 1, HEARTRATE_GRAPH_P2_POS_Y + HEARTRATE_GRAPH_HEIGHT - graph_data[i - 1]),
                         (HEARTRATE_GRAPH_P2_POS_X + i, HEARTRATE_GRAPH_P2_POS_Y + HEARTRATE_GRAPH_HEIGHT - graph_data[i]), 2)
        
def draw_frame():
    # 枠の描画
    pygame.draw.rect(screen, BLACK, (HEARTRATE_GRAPH_P1_POS_X, HEARTRATE_GRAPH_P1_POS_Y, HEARTRATE_GRAPH_WIDTH, HEARTRATE_GRAPH_HEIGHT), FRAME_WIDTH)
    pygame.draw.rect(screen, BLACK, (HEARTRATE_GRAPH_P2_POS_X, HEARTRATE_GRAPH_P2_POS_Y, HEARTRATE_GRAPH_WIDTH, HEARTRATE_GRAPH_HEIGHT), FRAME_WIDTH)

def get_latest_record(cur):
    # 最新のレコードを取得するクエリ
    cur.execute('''SELECT * FROM sensor_data
                ORDER BY id DESC
                LIMIT 1''')

    # 最新のレコードを取得
    latest_record = cur.fetchone()

    return latest_record

# def init():
#     p1_img, p2_img = img_load()
#     return p1_img, p2_img

def main():
    running = True
    p1_img, p2_img, logo_img = img_load()
    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # グラフデータの更新
        update_graph_data()

        # 画面の背景を塗りつぶす
        screen.fill(WHITE)

        # プレイヤー画像の表示
        draw_player_img(p1_img, p2_img)

        # タイトルロゴの表示
        draw_logo_img(logo_img)

        # 枠の描画
        draw_frame()

        # グラフの描画
        draw_graph()

        # テキストを描画
        text = font.render('Sensing Battler 2', True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
        screen.blit(text, text_rect)

        # 画面更新
        pygame.display.flip()

        time.sleep(0.2)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
