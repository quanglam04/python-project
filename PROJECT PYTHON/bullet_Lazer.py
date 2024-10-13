import pygame
import math
from bullet_logic import Laser_logic

class Laser(Laser_logic):        #Buoc 2: Đạn laser
    def __init__(self, x, y, angle):
        self.color = (255, 0, 0)  # Màu của tia laser
        self.width = 2  # Độ dày của tia laser
        self.length = 20  # Chiều dài của tia laser
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.5
        self.creation_time = pygame.time.get_ticks()
        self.bounces = 0  # Số lần có thể phản xạ (nảy) trước khi biến mất
        self.normal = [0, 0]

        #Tính toán vector hướng dựa theo góc
        self.direction_x = math.cos(math.radians(self.angle)) * self.speed
        self.direction_y = -math.sin(math.radians(self.angle)) * self.speed

        #Toa do diem cuoi cua dan laser
        self.end_x = 0
        self.end_y = 0

        self.check = 0    # 0: khong va cham, 1 va cham 1 tuong, 2 va cham 2 tuong (ban vao goc tuong)
    
    def draw(self, window):
        pygame.draw.line(window, self.color, [self.x, self.y], [self.end_x, self.end_y], self.width)
