import sys
import pygame
import random

pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ваша мокрая сова")

# Цвета
WHITE = (255, 255, 255)


# Функция для загрузки изображений с обработкой ошибок
def load_image(path):
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error as e:
        print(f"Ошибка загрузки изображения: {path} - {e}")
        return None


# Загрузка изображений
owl_image = load_image("images/owl.png")
background_image = load_image("images/background.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) if background_image else None

owl_rect = owl_image.get_rect() if owl_image else None

food_icon = load_image("images/Food_icon.png")  # Иконка еды
bath_icon = load_image("images/Душ.png")  # Иконка ванной
food_background = load_image("images/kitchen.jpg")
food_background = pygame.transform.scale(food_background, (screen_width, screen_height)) if food_background else None
bath_background = load_image("images/bath.jpg")

food_icon = pygame.transform.scale(food_icon, (50, 50)) if food_icon else None  # Масштабируем иконку
bath_icon = pygame.transform.scale(bath_icon, (50, 50)) if bath_icon else None  # Масштабируем иконку

# Позиции иконок
food_icon_pos = (20, 50)  # Положение иконки еды
bath_icon_pos = (20, 150)  # Положение иконки душа


# Звук
def load_sound(path):
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error as e:
        print(f"Ошибка загрузки звука: {path} - {e}")
        return None


ugu_sound = load_sound("owl_sounds.wav")

current_location = "living_room"
current_background = background_image

owl_pos_living_room = (185, 80)
owl_pos_kitchen = (100, 300)
owl_pos_bath = (200, 300)


def draw_icons():
    if food_icon:
        screen.blit(food_icon, food_icon_pos)  # Отрисовываем иконку еды
    if bath_icon:
        screen.blit(bath_icon, bath_icon_pos)  # Отрисовываем иконку душа


def main():
    global current_background, current_location
    running = True
    while running:
        # Отрисовка фона
        screen.fill(WHITE)  # Очищаем экран перед отрисовкой
        if current_background:
            screen.blit(current_background, (0, 0))

        if current_location == "living_room":
            owl_rect.topleft = owl_pos_living_room  # Положение совы в гостиной
        elif current_location == "kitchen":
            owl_rect.topleft = owl_pos_kitchen  # Положение совы на кухне
        elif current_location == "bath":
            owl_rect.topleft = owl_pos_bath

        draw_icons()  # Отрисовываем иконки
        if owl_image:
            screen.blit(owl_image, owl_rect.topleft)  # Отрисовка совы

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if ugu_sound:
                        ugu_sound.play()  # Проигрываем звук
                    mouse_x, mouse_y = event.pos

                    if current_location == "living_room":
                        if food_icon and food_icon_pos[0] < mouse_x < food_icon_pos[0] + 50 and food_icon_pos[
                            1] < mouse_y < food_icon_pos[1] + 50:
                            print("Пойдём на кухню.")
                            current_background = food_background
                            current_location = "kitchen"
                        elif bath_icon and bath_icon_pos[0] < mouse_x < bath_icon_pos[0] + 50 and bath_icon_pos[
                            1] < mouse_y < bath_icon_pos[1] + 50:
                            print("Пойдём в ванную.")
                            current_background = bath_background
                            current_location = "bath"
                    else:  # Возврат в гостиную
                        print("Вернёмся в гостиную.")
                        current_background = background_image
                        current_location = "living_room"

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()