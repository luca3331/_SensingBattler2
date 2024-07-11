import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ウィンドウのサイズと枠の幅
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAME_WIDTH = 10

# 色の定義 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# グラフの設定
GRAPH_POS_X = FRAME_WIDTH
GRAPH_POS_Y = FRAME_WIDTH
GRAPH_WIDTH = WINDOW_WIDTH - 2 * FRAME_WIDTH
GRAPH_HEIGHT = WINDOW_HEIGHT - 2 * FRAME_WIDTH

# ウィンドウの設定
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Real-time Line Graph')

# グラフの初期データ
graph_data = [0] * GRAPH_WIDTH

def update_graph_data():
    # グラフのデータを更新する（ランダムな値を追加）
    new_data_point = random.randint(0, GRAPH_HEIGHT)
    graph_data.append(new_data_point)
    graph_data.pop(0)

def draw_graph():
    # グラフの描画
    pygame.draw.rect(screen, WHITE, (GRAPH_POS_X, GRAPH_POS_Y, GRAPH_WIDTH, GRAPH_HEIGHT))
    for i in range(1, len(graph_data)):
        pygame.draw.line(screen, BLUE, (GRAPH_POS_X + i - 1, GRAPH_POS_Y + GRAPH_HEIGHT - graph_data[i - 1]),
                         (GRAPH_POS_X + i, GRAPH_POS_Y + GRAPH_HEIGHT - graph_data[i]), 2)

def draw_frame():
    # 枠の描画
    pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), FRAME_WIDTH)

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # グラフデータの更新
        update_graph_data()

        # 画面の背景を塗りつぶす
        screen.fill(WHITE)

        # 枠の描画
        draw_frame()

        # グラフの描画
        draw_graph()

        # 画面更新
        pygame.display.flip()

        # フレームレートの調整
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
