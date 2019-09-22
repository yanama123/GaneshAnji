# import os
#
# for (root,dirs,files) in os.walk(r'C:\Users\yanama\PycharmProjects\untitled\middlewareservice\daya'):
#     print(files)
import time
import signal

# determines if the loop is running
running = True

def cleanup():
  print("Cleaning up ...")

def main():
  global running

  # add a hook for TERM (15) and INT (2)
  signal.signal(signal.SIGTERM, _handle_signal)
  signal.signal(signal.SIGINT, _handle_signal)

  # is True by default - will be set False on signal
  while running:
    time.sleep(1)

# when receiving a signal ...
def _handle_signal(signal, frame):
  global running

  # mark the loop stopped
  running = False
  # cleanup
  cleanup()

if __name__ == '__main__':
  main()