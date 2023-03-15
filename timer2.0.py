#import functions
import pygame
import time
import math
#sets up sounds
pygame.mixer.init()
pygame.mixer.music.load('~/Downloads/sound.wav')
#timer function
def timer():
    #sets variables
    timer = 'y'
    now = 'n'
    while now == 'n':
        timertimem = (int(input('''How many minutes do you need? (we'll do seconds next) ''')))
        timertimes = (int(input('How many seconds do you need? ')))
        timertimew = ((timertimem * 60) + timertimes)
        print('Are you happy to start ',  timertimem,  'minutes and ',  timertimes,  'seconds on the timer? ')
        now = input('please type y/n ')
    while timertimew > 0:
        print(  (timertimew // 60), 'mins, ', (timertimew % 60), 'secs.')
        time.sleep(1)
        timertimew = timertimew - 1
    print('0 mins, 0 secs.')
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
                  I Ted's Timely Timer 2.0 I
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
