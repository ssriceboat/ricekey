## Doxygen header
# @author   Kevin Sacca
# @email    ssriceboat@gmail.com
# @title    Ricekey - A threaded keypress event detector
#
# @brief    Utility for creating thread- or loop-killing keypresses. This works
#           on macOS, Linux, and Windows. Simply start a thread with kbcontrol()
#           as the target, and you'll be able to terminate that thread with a
#           keypress, allowing your main thread to know to stop if the other
#           thread is dead.
#
#           Example unit-test command entry in terminal or CMD:
#           python ricekey.py

## Standard library imports
################################################################################
import atexit
import os
from riceprint import pprint, tprint
from select import select
import sys

# Windows or Unix
if os.name == 'nt':
   import msvcrt
else:
   import termios


## Public class definitions
################################################################################
class KBHit:
   """
   Class object that creates a keyboard keypress monitor to run in parallel to
   another function that could utilize a keypress-controlled stop/exit function.
   This class works on both Windows and Linux operating systems/terminals.
   """
   def __init__(self):
      """
      Initialize KBHit object to do keyboard things.
      """
      if os.name == 'nt':
         pass
      else:
         # Save the terminal settings
         self.fd = sys.stdin.fileno()
         self.new_term = termios.tcgetattr(self.fd)
         self.old_term = termios.tcgetattr(self.fd)

         # New terminal setting unbuffered
         self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
         termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

         # Support normal-terminal reset at exit
         atexit.register(self.set_normal_term)

   def kbhit(self):
      """
      Returns True if keyboard character was hit, False otherwise.
      """
      if os.name == 'nt':
         return msvcrt.kbhit()
      else:
         dr,dw,de = select([sys.stdin], [], [], 0)
         return dr != []

   def getch(self):
      """
      Returns a keyboard character after kbhit() has been called.
      """
      if os.name == 'nt':
         return msvcrt.getch().decode('utf-8')
      else:
         return sys.stdin.read(1)

   def set_normal_term(self):
      """
      Resets to normal terminal.  On Windows this is a no-op.
      """
      if os.name == 'nt':
         pass
      else:
         termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


def kbcontrol():
   """
   Threaded function to enable keyboard events to stop a function. This is an
   example usage of this class that results in the 'q' and 'Esc' keys acting
   as terminating keypresses for a threaded process. This way, when the
   thread running this function returns False, you know outside the thread
   that the user pressed q or Esc and can handle safe shutdown of code
   separately.
   """
   kb = KBHit()
   pprint('Press q or Esc to stop and exit.', 'dy')
   while(True):
      # Check for any keypress
      if kb.kbhit():
         key = kb.getch()
         # If keypress was 'q' or 'Esc', return False to terminate thread
         if ord(key) == 27 or ord(key) == 113:
            pprint('Stopkey pressed. Terminating.')
            tprint('Exiting...')
            kb.set_normal_term()
            return False


if __name__ == '__main__':
   from riceprint import ConsolePrinter, progressbar
   cp = ConsolePrinter()
   import threading
   import time

   # Start the keypress monitoring thread
   thread = threading.Thread(target=kbcontrol, args=())
   thread.start()

   # While the thread is alive, do something.
   i = 0
   while thread.isAlive():
      c = cp.palette.colors[i % 16]
      progressbar(i%100, 100, color=c, char='\u2587', lend='|', rend='|')
      time.sleep(0.01)
      i+=1

   pprint('Done!', 'g')
