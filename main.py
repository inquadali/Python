import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("宝可梦游戏")

# 加载精灵图片
pikachu_img = pygame.image.load("images/pikachu.png")
# 根据精灵图片创建矩形
pikachu_rect = pikachu_img.get_rect()
# 将精灵矩形放置在屏幕中央
pikachu_rect.center = (WIDTH // 2, HEIGHT // 2)

# 设置移动速度
SPEED = 10

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()
    
    # 根据按键移动精灵
    if keys[pygame.K_LEFT]:
        pikachu_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        pikachu_rect.x += SPEED
    if keys[pygame.K_UP]:
        pikachu_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        pikachu_rect.y += SPEED

    # 确保精灵不会移出屏幕
    pikachu_rect.clamp_ip(screen.get_rect())

    # 绘制背景
    screen.fill("aqua")

    # 绘制精灵
    screen.blit(pikachu_img, pikachu_rect)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出pygame
pygame.quit()
sys.exit()
