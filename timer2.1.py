#import functions
import pygame
import time
import math
#sets up sounds
pygame.mixer.init()
pygame.mixer.music.load('~/Downloads/Sound.wav')
#timer function
def timer():
    #sets variables
    timer = 'y'
    now = 'n'
    while now == 'n':
        timertimeh = (int(input('''How many hours do you need? (we'll do minutes and seconds next) ''')))
        timertimem = (int(input('How many minutes do you need? (seconds next) ')))
        timertimes = (int(input('How many seconds do you need? ')))
        timertimew = ((timertimeh * 3600) + (timertimem * 60) + timertimes)
        print('Are you happy to start',  timertimeh,  'hours,', timertimem, 'minutes and',  timertimes,  'seconds on the timer? ')
        now = input('Please Type y/n ')
    while timertimew > 0:
        print(  (timertimew // 3600), 'hours,', ((timertimew // 60) % 60),  'mins,', (timertimew % 60), 'secs.')
        time.sleep(1)
        timertimew = timertimew - 1
    print('0 hours, 0 mins, 0 secs.')
    print('Your time is up!')
    pygame.mixer.music.play(-1)
    time.sleep(1)
    timers = (input('Would you like to start another timer? (y/n) '))
    if timers == 'y':
        timers = 1
    if timers == 'n':
        timers = 0
    pygame.mixer.music.stop()
    return timers
print('''







                  I========================I
                  I Ted's Timely Timer 2.1 I
                  I========================I
                    ----------------------
                    Please use responsibly
                    ----------------------








''')                    
while True:        
    timers = timer()
    if timers == 1:
        continue
    if timers == 0:
        break
print ('''Thank you for using Ted's Timely Timer! Have a nice day.''')
time.sleep(1.5)
print('Quitting...')
time.sleep(1.5)
print('Quitted!')
#Thanks for reading this code! thanks to Carol Vorrderman computer coding book, reccommendations from parents John and Keren Lloyd. Thanks to the internet, and all the people who tested this timer.
