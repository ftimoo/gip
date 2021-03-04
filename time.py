from pynput.keyboard import Key, Listener
from time import perf_counter
bool = 0
sttime = 0
stime = 0




def on_press(key):
    print('{0} pressed'.format(
        key))
def time():
    global bool
    global sttime
    global stime
    if bool:
        stime = perf_counter()
        print(stime - sttime)
        bool = 0
    else:
        sttime = perf_counter()
        bool = 1


def on_release(key):
    print('{0} release'.format(
        key))
    time()
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()