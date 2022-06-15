from colorama import Fore, Back, Style

class Env:
     def __init__(self):
          self._state = 0
       
     # using property decorator
     # a getter function
     @property
     def state(self):
         print("getter method called")
         return self.state
       
     # a setter function
     @state.setter
     def state(self, a):
         if(a > 6):
            raise ValueError("Sorry, need to be 1-5 for state")
         print("setter method called")
         self._state = a
         
     def paintScene1(self):
         print(Fore.BLUE + 'oooooooooooooooooooooooooooooo')
         print(Fore.YELLOW + '                              ')
         print(Fore.YELLOW + '                              ')
         print(Fore.YELLOW + '                              ')
         print(Fore.GREEN + '/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/')
        # print(Back.GREEN + 'and with a green background')
        # print(Style.DIM + 'and in dim text')
         print(Style.RESET_ALL)
      
     def paintScene2(self):
         print(Fore.BLUE + 'oo ooooooooooo oooooooooo oooo')
         print(Fore.YELLOW + '                              ')
         print(Fore.YELLOW + '                              ')
         print(Fore.YELLOW + '                              ')
         print(Fore.GREEN + '\ /\/ \/ \/\/\/\/ /\ \/ \/\ / ')
        # print(Back.GREEN + 'and with a green background')
        # print(Style.DIM + 'and in dim text')
         print(Style.RESET_ALL)
   