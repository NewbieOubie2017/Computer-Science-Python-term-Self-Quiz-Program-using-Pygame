#!/usr/bin/env python3

'''
CSPythonTermIntroduction.py
'''



import sys
import random
import pygame
import textwrap 
from time import sleep

#CONSTANTS
MIN_ASCII_VALUE = 97 
MAX_ASCII_VALUE = 122
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800

BACKGROUND_COLOR=(90,90,30)
FOREGROUND_COLOR=(100,200,255)

gameDisplay = pygame.display.set_mode((0, 0))
pygame.font.init()               
myfont = pygame.font.SysFont('arial', 36, 'Comic Sans MS', 40)
myfont_big = pygame.font.SysFont('arial', 40, 'Comic Sans', 54)

line1 = "Press any letter to get "
line2 = 'a definition for a randomly selected bingo card term to call.'
line3 = 'press the letter y to start a new game press q to close the game'

# this list keeps track of what was called

definitionsDone = []

definitionA = ''
# This is the Original Dictionary of terms and definitions 
termDictionary = {'Expression': 'Numbers, symbols and operators (such as + and times (*)) grouped together that show the value of something \n \n an act, process, or instance of representing in a medium', 'types of loops': 'for; while.', 'loop also methods also functions': 'a powerful tool to do something to each object in a group of objects', 'string': 'the most popular type of object in Python. Creating them is as simple as assigning a value to a variable This object must be enclosed in single or double quotes.', 'float': 'a decimal number or floating point number such as 1.1 ', 'Integer, in python int() can convert a string or floating point number into an integer': 'a whole number', 'Dictionary \t \t example: print(DictQ[WA])  prints "Olympia" \n \n when the dictionary contains states and their capitals': 'this data group has two elements: keys and values. To access the value elements, you can use the familiar square brackets, [ ], along with the key. Keys are unique within this group while values may not be. The values can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.', 'Variable': 'is assigned space in memory and is created when defined', 'tuple': 'is a sequence of immutable Python objects. They are sequences, just like lists. The main difference between the these object groups and lists is that they cannot be changed unlike lists, which can be changed. They use parentheses, ( ), whereas lists use square brackets.', 'list': 'is the most versatile data type available in Python, which can be written as a group of comma-separated values (items) between square brackets, [ ]. Important thing about a this object is that the items in it need not be of the same type.', 'object': 'Any data with state (that is attributes or value) and defined behavior (also called methods). Also the ultimate base class of any new-style class.', 'IDE': 'An Integrated Development Environment, software to help write software', 'attribute': 'A value associated with an object which is referenced by name using dotted expressions. \n \n An example is \t object.expression \n \n \t \t or a.append \t when a is a list', 'class': 'A template for creating user-defined objects.', 'Boolean \n \n Python reserved keys words are "True" and "False"': 'is a subset of algebra used for creating true/false statements.', 'bit': 'the smallest unit of computer information', 'byte': 'a unit of eight bits'
}

def main():
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Bingo Selector for Computer Science and Python Programming')
    screen.fill(BACKGROUND_COLOR)
    display_message(screen, line1, FOREGROUND_COLOR, (10, 10))
    display_message(screen, line2, FOREGROUND_COLOR, (10, 50))
    display_message(screen, line3, FOREGROUND_COLOR, (10, 90))
    pygame.display.flip()
    global termListKeys
    termListKeys = list(termDictionary.keys())
    playGame = True
    while playGame == True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            else:
                letter = askLetter(screen, 80, 350)
                if letter == "":
                    playGame = False
                    main()
                # starts new game and resets
                elif letter.lower() == 'y':
                    playGame = False
                    # resets to empty
                    definitionsDone[:] = []
                    main()
                elif letter.lower() == 'q':
                    line25 = "Thank you so very much for playing!" 
                    screen.fill(BACKGROUND_COLOR)
                    display_message(screen, line25, FOREGROUND_COLOR, (180, 230))
                    sleep(1)
                    line27 = "Good Bye!" 
                    screen.fill(BACKGROUND_COLOR)
                    display_message(screen, line27, FOREGROUND_COLOR, (180, 230))
                    sleep(1)
                    sys.exit()
                else:
                    definitionA = generate_choice()
                    termListKeys = updateTerms(definitionA)
                    
            screen.fill(BACKGROUND_COLOR)
            line5 = "The Next definition to call is: " 
            display_message(screen, line5, FOREGROUND_COLOR, (10, 10))
            message_display(definitionA, screen)
            if len(definitionsDone) == len(termDictionary):
               lineEnd = 'You have called all the terms in this program'
               display_message(screen, lineEnd, FOREGROUND_COLOR, (10, 720))
               lineEnded = 'Press y to start a New Game, q to quit'
               display_message(screen, lineEnded, FOREGROUND_COLOR, (10, 760))
               pygame.display.flip()
            else:
                pass
            letter = askLetter(screen, 80, 350)
            if letter == "":
                playGame = False
                main()
            # starts new game and resets
            elif letter.lower() == 'y':
                playGame = False
                # resets to empty
                definitionsDone[:] = []
                main()
            elif letter.lower() == 'q':
                line25 = "Thank you so very much for playing!" 
                screen.fill(BACKGROUND_COLOR)
                display_message(screen, line25, FOREGROUND_COLOR, (180, 230))
                sleep(1)
                line27 = "Good Bye!" 
                screen.fill(BACKGROUND_COLOR)
                display_message(screen, line27, FOREGROUND_COLOR, (180, 580))
                sleep(1)
                sys.exit()
            else:
                message_displayB(termNow, screen)
                #display_message(screen, termNow, FOREGROUND_COLOR, (180, 530))
                pygame.display.flip() 
            pygame.display.flip()

def detect_pressed_key(screen, key_pressed_ascii):
    key_pressed = ""
    if key_pressed_ascii >= MIN_ASCII_VALUE and key_pressed_ascii <= MAX_ASCII_VALUE: 
        key_pressed = chr(key_pressed_ascii)
        if key_pressed == "":
            pass
        else:
            return key_pressed
    else:
        
        return key_pressed   

def askLetter(screen, cord_x = 50, cord_y = 50):
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
            if events.type == pygame.KEYDOWN:
                letter = detect_pressed_key(screen, events.key)
                running = False
    return letter

           
def display_message(screen, message, color, pos = (50, 30)):
    text = myfont.render(message, False, color)
    screen.blit(text, pos)
    pygame.display.flip()

def updateTerms(word):
    New = []
    New = sorted(termListKeys)
    return New

               
def generate_choice():
    # global needed here because this is used else where and assigned here
    global termNow
    if len(termListKeys) > 0:
        numberBig = random.randint(0, 12345)
        numberW = numberBig % len(termListKeys)
        termNow = termListKeys.pop(numberW)
        definitionsDone.append(termDictionary.get(termNow))
        return termDictionary.get(termNow)
    else:
        definitionsDone[:] = []

def wrap_text(message, limit):
    wraplimit = limit
    return textwrap.fill(message, wraplimit)        
      
def message_display(message, screen):
    message = wrap_text(message, 50)
    down = 70
    for part in message.split('\n'):
        display_message(screen, part, FOREGROUND_COLOR, (30, down))
        down +=40      
        pygame.display.update()
    pygame.display.flip()

def message_displayB(message, screen):
    message = wrap_text(message, 50)
    down = 530
    for part in message.split('\n'):
        display_message(screen, part, FOREGROUND_COLOR, (30, down))
        down +=40      
        pygame.display.update()
    pygame.display.flip()

if __name__=="__main__":
  main()


