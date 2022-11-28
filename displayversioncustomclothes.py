import picamera
import pygame
import io

# Init pygame 
pygame.init()
screen = pygame.display.set_mode((0,0))

# Init camera
camera = picamera.PiCamera()
camera.resolution = (1280/2, 720/2)
camera.crop = (0.0, 0.0, 1.0, 1.0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255,255,0)

BAR_COLOURS = [GREEN,YELLOW,ORANGE,RED]

BAR_WIDTH = 30
BAR_HEIGHT = 10

specs = [2,0,1,3]


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

    screen.fill(WHITE)
    if img:
        screen.blit(img, (x,y))

    for index, item in enumerate(specs):
        for i in range(item):
            pygame.draw.rect(screen, BAR_COLOURS[item], pygame.Rect(40*index, 30 + (i*BAR_HEIGHT*1.2), BAR_WIDTH, BAR_HEIGHT))
   
    pygame.display.update()

camera.close()
pygame.display.quit()