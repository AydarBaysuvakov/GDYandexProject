import pygame
from .LoadComponents import load_image

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

class Object(pygame.sprite.Sprite):
    def __init__(self, group, image_name=None, size=[10, 10], take_size=False, colorkey=None):
        super().__init__(group)
        if image_name is None:
            self.image = pygame.Surface(size)
            self.image.fill(pygame.color.Color('white'))
        elif image_name[0] == 'Image':
            self.image = load_image(image_name[1], colorkey=colorkey)
            if take_size:
                self.image = pygame.transform.scale(self.image, size)
        elif image_name[0] == 'Color':
            self.image = pygame.Surface(size)
            self.image.fill(pygame.color.Color(image_name[1]))
        self.rect = self.image.get_rect()
        if take_size:
            self.rect.w = size[0]
            self.rect.h = size[1]

    def update(self):
        pass

class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self, group, sheet_name, columns, rows, x, y):
        super().__init__(group)
        self.frames = []
        self.sheet = load_image(sheet_name, colorkey=-1)
        self.cut_sheet(columns, rows)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (38, 68))
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 38
        self.rect.h = 68

    def cut_sheet(self, columns, rows):
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // columns,
                                self.sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(self.sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def change_frame(self, run_dir):
        self.cur_frame = (self.cur_frame + 1) % 64
        self.image = pygame.transform.scale(self.frames[self.cur_frame * sign(run_dir) // 8], (38, 68))