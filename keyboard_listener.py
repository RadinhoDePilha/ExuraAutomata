from pynput import keyboard
from pynput.keyboard import Listener, GlobalHotKeys
from logs import make_log

# The event listener will be running in this block
def get_key():
    try:
        with keyboard.Events() as events:
            # Block at most one second
            event = events.get(3.0)
            if event is None:
                print('Tecla não capturada')
            else:
                return str(event.key).replace('Key.', '').replace("'", '')
    except Exception as error:
            make_log('ERROR' + str(error))
    
if __name__ == "__main__":
    pass