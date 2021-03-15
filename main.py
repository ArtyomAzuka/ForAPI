import pygame
import requests


def load_image(name, colorkey=None):
    fullname = (name)
    # если файл не существует, то выходим
    image = pygame.image.load(fullname)
    return image

map_type = 'map'
scale = 90
api_server = "http://static-maps.yandex.ru/1.x/"
longitude = 0
latitude = 0
params = {
    "ll": ",".join([f'{str(longitude)}', f'{latitude}']),
    "spn": ",".join([f'{scale}', f'{scale}']),
    'l': map_type}

response = requests.get(api_server, params=params)
pygame.init()
size = width, height = 1500, 1000
screen = pygame.display.set_mode(size)
running = True
with open("map.png", "wb") as file:
    file.write(response.content)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if scale != 90:
                    scale += 10
            if event.key == pygame.K_PAGEDOWN:
                if scale != 0:
                    scale -= 10
            if event.key == pygame.K_RIGHT:
                if longitude < 179:
                    longitude = longitude + 1
            if event.key == pygame.K_LEFT:
                if longitude > -179:
                    longitude = longitude - 1
            if event.key == pygame.K_DOWN:
                if latitude > -80:
                    latitude -= 1
            if event.key == pygame.K_UP:
                if latitude < 80:
                    latitude += 1
            if event.key == pygame.K_1:
                map_type = 'map'
            if event.key == pygame.K_2:
                map_type = 'sat'
            if event.key == pygame.K_3:
                map_type = 'skl'

            params["spn"] = ",".join([f'{scale}', f'{scale}'])
            params['ll'] = ",".join([f'{str(longitude)}', f'{latitude}'])
            params['l'] = map_type
            response = requests.get(api_server, params=params)
            pygame.init()
            size = width, height = 1500, 1000
            screen = pygame.display.set_mode(size)
            running = True
            with open("map.png", "wb") as file:
                file.write(response.content)
        fon = pygame.transform.scale(load_image('map.png'), (1500, 1000))
        screen.blit(fon, (0, 0))
    pygame.display.flip()
pygame.quit()
