import picamera
import pygame
import io

# Init pygame 
pygame.init()
screen = pygame.display.set_mode((0,0))

# Init camera
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.crop = (0.0, 0.0, 1.0, 1.0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)

BAR_WIDTH = 20
BAR_HEIGHT = 10

x = (screen.get_width() - camera.resolution[0]) / 2
y = (screen.get_height() - camera.resolution[1]) / 2

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
          (camera.resolution[0] * camera.resolution[1] * 2)],
           camera.resolution, 'RGB')

    screen.fill(WHITE)
    if img:
        screen.blit(img, (x,y))
    pygame.draw.rect(screen, RED, pygame.Rect(30, 30, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, ORANGE, pygame.Rect(30, 30 + (BAR_HEIGHT*1.5), BAR_WIDTH, BAR_HEIGHT))
   
    pygame.display.update()

camera.close()
pygame.display.quit()