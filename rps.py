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
# makes width og game 1000
WIDTH = 1000
# makes height off game 600
HEIGHT = 600
# will be 30 frames per second
FPS = 30

# define colors 
# tuples are immutable - cannot change one created 
# creates color white
WHITE = (255, 255, 255)
# creates color black
BLACK = (0, 0, 0)
# creates color red
RED = (255, 0, 0)
# creates color green
GREEN = (0, 225, 0)
# creates color blue
BLUE = (0, 0, 255)

# creates the choices rock, paper or scissors
choices0 = ["rock", "paper", "scissors"]

# Makes the text shown on the screen
def draw_text(text, size, color, x, y):
    # calls the font of what is shown when writing 
    font_name = pg.font.match_font('arial')
    # initializes a font object using the Pygame library
    font = pg.font.Font(font_name, size)
    # creates a new surface containing a rendered text string
    text_surface = font.render(text, True, color)
    # creates a new Rect object that is sized and positioned to fit the text_surface created in the previous line of code
    text_rect = text_surface.get_rect()
    # where line of text is positioned 
    text_rect.midtop = (x,y)
    # copies the contents of the text_surface to the screen surface at the position specified by the text_rect.
    screen.blit(text_surface, text_rect)

# defines a function named cpu_randomchoice.
def cpu_randomchoice():
    # prints "computer randomly decides"
    print("computer randomly decides ")
    # globalizes cpu_choice so it can be used throughout the code
    global cpu_choice
    # allows cpu to choice rock paper or sissors
    cpu_choice = choices0[randint(0,2)]
    # returms cpu_choice 
    return cpu_choice

# code initializes the Pygame library.
pg.init()
# initializes the Pygame mixer module, which is used for handling sound in Pygame.
pg.mixer.init()

# creates a new Pygame display surface
screen = pg.display.set_mode((WIDTH, HEIGHT))
# sets the title of the Pygame window.
pg.display.set_caption("rock, paper, scissors...")
# used to regulate the frame rate of a game
clock = pg.time.Clock()

# ads an image file and converts it to a Pygame surface.
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# creates a new rectangle object that surrounds the loaded image
rock_image_rect = rock_image.get_rect()
# creates a new rectangle object that matches the size and position as rock_image
cpu_rock_image_rect = rock_image.get_rect()


# ads an image file and converts it to a Pygame surface.
scissor_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
# creates a new rectangle object that surrounds the loaded image
scissor_image_rect = scissor_image.get_rect()
# creates a new rectangle object that matches the size and position as scissor_image
cpu_scissor_image_rect = scissor_image.get_rect()


# ads an image file and converts it to a Pygame surface.
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
# creates a new rectangle object that surrounds the loaded image
paper_image_rect = paper_image.get_rect()
# creates a new rectangle object that matches the size and position as paper _image
cpu_paper_image_rect = paper_image.get_rect()

# determines which screen should be displayed to the user
start_screen = True
# connects variable to an empty string.
player_choice = ""
# connects variable to an empty string.
cpu_choice = ""
# game loop is currently running and should continue to execute.
running = True

# Loop continues to run until the value of running is set to False
while running:
    # limits the frame rate
    clock.tick(FPS)
    # a loop that retrieves and processes all of the events
    for event in pg.event.get():
        # occurs when the user closes the Pygame window or otherwise signals that the program should exit.
        if event.type == pg.QUIT:
            # loop ends
            running = False
        # checks whether a Pygame event represents a key press event.
        if event.type == pg.KEYDOWN:
            # checks whether a Pygame key press event corresponds to the spacebar key on the keyboard.
            if event.key == pg.K_SPACE:
                # prints "let the game begin"
                print("Let the game begin!")
                # end the loop
                start_screen = False
        # checks whether a Pygame event represents a mouse button release event.
        if event.type == pg.MOUSEBUTTONUP:
            # a statement that prints the x-coordinate of the current mouse position to the console.
            print(pg.mouse.get_pos()[0])
            # a statement that prints the y-coordinate of the current mouse position to the console.
            print(pg.mouse.get_pos()[1])
            # a statement that retrieves the current position of the mouse on the screen
            mouse_coords = pg.mouse.get_pos()
            #  a conditional statement that checks whether the current position of the mouse is within the area of image
            if rock_image_rect.collidepoint(mouse_coords):
                # prints rock when clicked on rock
                print("rock")
                # a statement that sets the value of the player_choice variable to the string "rock".
                player_choice = "rock"
                # calls a function that gets the cpu choice
                cpu_choice = cpu_randomchoice()
            # checks if the mouse coordinates are within the bounding rectangle of the scissor image
            elif scissor_image_rect.collidepoint(mouse_coords):
                # prints scissors
                print("scissors")
                # a statement that sets the value of the player_choice variable to the string "scissors".
                player_choice = "scissors"
                # calls a function that gets the cpu choice
                cpu_choice = cpu_randomchoice()
            # checks if the mouse coordinates are within the bounding rectangle of the paper image
            elif paper_image_rect.collidepoint(mouse_coords):
                # prints paper 
                print("paper")
                # a statement that sets the value of the player_choice variable to the string "paper".
                player_choice = "paper"
                # calls a function that gets the cpu choice
                cpu_choice = cpu_randomchoice()
            else:
                # prints you didn's click anyhting if not clicked on image
                print("you didn't click anything")
         

    ########## update ############
    # screen goes black
    screen.fill(BLACK)

    #  boolean variable that represents if the game should display an initial screen when it starts runnin
    if start_screen:
        #  function that is being called to display text on the screen.
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        # where the rock image is
        rock_image_rect.x = 2000
        # where paper image is
        paper_image_rect.x = 2000
        # where sissor image is
        scissor_image_rect.x = 2000

    # checking if the variable "player_choice" is an empty string
    if not start_screen and player_choice == "":
        # rock image is placed at 50 pixels 
        rock_image_rect.x = 50
        # paper image appears on screen and it places at 500 pixels 
        paper_image_rect.x = 500
        # paper is move down 300 pixels 
        paper_image_rect.y = 300
        # scissor image appears at 800 pixels
        scissor_image_rect.x = 800
        # draws an image onto the screen at a specified position
        screen.blit(scissor_image, scissor_image_rect)
        # draws an image onto the screen at a specified position
        screen.blit(paper_image, paper_image_rect)
        # draws an image onto the screen at a specified position
        screen.blit(rock_image, rock_image_rect)

    # The code is checking if the player's choice is "rock" and the CPU's choice is also "rock"
    if player_choice == "rock" and cpu_choice == "rock":
        cpu_rock_image_rect.x = 700
        screen.blit(rock_image, rock_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        # being called to display text on the screen.
        draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)

    if player_choice == "rock" and cpu_choice == "scissors":
        cpu_scissor_image_rect.x = 700
        screen.blit(rock_image, rock_image_rect)
        screen.blit(scissor_image, scissor_image_rect)
        draw_text("You Won!", 22, WHITE, WIDTH/2, HEIGHT/10 )

    if player_choice == "rock" and cpu_choice == "paper":
        cpu_paper_image_rect.x = 700
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, cpu_paper_image_rect)
        draw_text("You lost :(", 22, WHITE, WIDTH/2, HEIGHT/10  )

    if player_choice == "paper" and cpu_choice == "rock":
        cpu_rock_image_rect.x = 50
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        draw_text("You Won!", 22, WHITE, WIDTH/2, HEIGHT/10 )

    if player_choice == "paper" and cpu_choice == "scissors":
        cpu_scissor_image_rect.x = 50
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissor_image, cpu_scissor_image_rect)
        draw_text("You Lost :(", 22, WHITE, WIDTH/2, HEIGHT/10 )

    if player_choice == "paper" and cpu_choice == "paper":
        cpu_paper_image_rect.x = 50
        screen.blit(paper_image, paper_image_rect)
        screen.blit(paper_image, cpu_paper_image_rect)
        draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10 )
    
    if player_choice == "scissors" and cpu_choice == "rock":
        cpu_rock_image_rect.x = 50
        screen.blit(scissor_image, scissor_image_rect)
        screen.blit(rock_image, cpu_rock_image_rect)
        draw_text("You Lose!!!", 22, WHITE, WIDTH/2, HEIGHT/10 )

    if player_choice == "scissors" and cpu_choice == "paper":
        cpu_paper_image_rect.x = 50
        screen.blit(scissor_image, scissor_image_rect)
        screen.blit(paper_image, cpu_paper_image_rect)
        draw_text("You Won!!!", 22, WHITE, WIDTH/2, HEIGHT/10 )

    if player_choice == "scissors" and cpu_choice == "scissors":
        cpu_scissor_image_rect.x = 50
        screen.blit(scissor_image, scissor_image_rect)
        screen.blit(scissor_image, cpu_scissor_image_rect)
        draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10 )

    

 
    # get user input  


    # update   
    #  used to update the contents of the screen
    pg.display.flip()
# The "quit" function is used to shut down Pygame
pg.quit()