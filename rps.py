# File created by Ryan McDonald 

# Import libraries- 
# need for time
from time import sleep 
# need so that computer can choose random item from list
from random import randint
# comprehensive game library for use of python
import pygame as pg
# allows use to manage files and folders
import os 

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors 
# tuples are immutable - cannot change one created 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 255)

choices0 = ["rock", "paper", "scissors"]

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def cpu_randomchoice():
    print("computer randomly decides ")
    global cpu_choice
    cpu_choice = choices0[randint(0,2)]
    return cpu_choice


pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("rock, paper, scissors...")
clock = pg.time.Clock()

rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()

scissor_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissor_image_rect = scissor_image.get_rect()
cpu_scissor_image_rect = scissor_image.get_rect()


paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = rock_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()

start_screen = True

player_choice = ""
cpu_choice = ""
running = True


while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("Let the game begin!")
                start_screen = False
        if event.type == pg.MOUSEBUTTONUP:
            # 
            print(pg.mouse.get_pos()[0])
            # 
            print(pg.mouse.get_pos()[1])
            # 
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else: 
            #     print("no rock lol")
            if rock_image_rect.collidepoint(mouse_coords):
                print("rock")
                player_choice = "rock"
                cpu_choice = cpu_randomchoice()
                # call a function that gets the cpu choice
            elif scissor_image_rect.collidepoint(mouse_coords):
                print("scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randomchoice()

            elif paper_image_rect.collidepoint(mouse_coords):
                print("paper")
                player_choice = "paper"
                cpu_choice = cpu_randomchoice()
            else:
                print("you didn't click anything")
         

    ########## update ############
    screen.fill(BLACK)

    if start_screen:
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.x = 2000
        paper_image_rect.x = 2000
        scissor_image_rect.x = 2000

    if not start_screen and player_choice == "":
        rock_image_rect.x = 50
        paper_image_rect.x = 350
        scissor_image_rect.x = 550
        screen.blit(scissor_image, scissor_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)

    if not start_screen and player_choice == "":
        rock_image_rect.x = 50
        paper_image_rect.x = 350
        scissor_image_rect.x = 550
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect) 
        screen.blit(scissor_image, scissor_image_rect)

    if player_choice == "rock" and cpu_choice == "rock":
        cpu_rock_image_rect.x = 500
        screen.blit(rock_image, rock_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)

    
    if player_choice == "rock" and cpu_choice == "scissors":
        screen.blit(rock_image, rock_image_rect)
        screen.blit(scissor_image, scissor_image_rect)

    if player_choice == "paper":
        screen.blit(paper_image, paper_image_rect)

    if player_choice == "scissors":
        screen.blit(scissor_image, scissor_image_rect)

    if player_choice == "rock":
        screen.blit(rock_image, rock_image_rect)


    # get user input


    # update   
    
    pg.display.flip()

pg.quit()