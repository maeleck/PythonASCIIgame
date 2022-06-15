from time import sleep

import Environment 


# Printing Some Text

time = 0
Env = Environment.Env()

# Waiting for 1 second to clear the screen

def gameloop():
    global time
    if time % 2 == 0:
        Env.paintScene1()
    else:
        Env.paintScene2()
    sleep(1)
    print("\033[H\033[J")
    time = time + 1
    
while True:
    gameloop()
    
# Clearing the Screen
#print("\033[H\033[J") 