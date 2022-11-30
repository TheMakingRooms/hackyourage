import picamera
import pygame
import io

# Init pygame 
pygame.init()
screen = pygame.display.set_mode((0,0))
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)

scale_ratio =  screen.get_width() /1920

# Init camera
camera = picamera.PiCamera()
camera.resolution = (int(640*scale_ratio), int(360*scale_ratio))
camera.crop = (0.0, 0.0, 1.0, 1.0)

BLACK = (0, 0, 0)
GREY = (100,100,100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255,255,0)

BAR_COLOURS = [GREEN,YELLOW,ORANGE,RED]

BAR_WIDTH = int(50* scale_ratio)
BAR_HEIGHT = int(30* scale_ratio)

specs = [[2,1,1,4,3],
        [1,3,4,4,2],
        [1,3,4,4,2]]


x = (screen.get_width() - camera.resolution[0]) / 4
y = (screen.get_height() - camera.resolution[1]) / 4

# Init buffer
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

# Main loop
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False

    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb)
    stream.close()
    img = pygame.image.frombuffer(rgb[0:
          (camera.resolution[0] * camera.resolution[1] * 3)],
           camera.resolution, 'RGB')

    screen.fill(GREY)
    if img:
        screen.blit(img, (x,y))

    for index, item in enumerate(specs[0]):
        for i in range(item):
            pygame.draw.rect(screen, BAR_COLOURS[item-1], pygame.Rect(1200 + (i*BAR_WIDTH*1.3), 500+(BAR_HEIGHT*1.3*index), BAR_WIDTH, BAR_HEIGHT))
    price = my_font.render('Price:', False, (0, 0, 0))
    quality = my_font.render('Quality:', False, (0, 0, 0))
    ethical = my_font.render('Ethical:', False, (0, 0, 0))
    sustainability =  my_font.render('Sustainability:', False, (0, 0, 0))
    statsX = int(1000*scale_ratio)
    statsY = int(500*scale_ratio)
    statsYChange = int(50*scale_ratio)

    screen.blit(price, (statsX,statsY))
    screen.blit(quality, (statsX,statsY+ statsYChange))
    screen.blit(ethical, (statsX,statsY+(statsYChange*2)))
    screen.blit(sustainability, (statsX,statsY+(statsYChange*2)))

    pygame.display.update()

camera.close()
pygame.display.quit()