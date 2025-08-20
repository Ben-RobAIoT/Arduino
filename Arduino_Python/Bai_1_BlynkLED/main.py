from pyfirmata2 import Arduino
import time

board = Arduino('COM3')
LED_BUILTIN = 13

while True:
    cmd = input("Nhập 1 để bật, 0 để tắt, q để thoát: ")
    if cmd == '1':
        board.digital[LED_BUILTIN].write(1)
        print("LED sáng")
    elif cmd == '0':
        board.digital[LED_BUILTIN].write(0)
        print("LED tắt")
    elif cmd.lower() == 'q':
        board.digital[LED_BUILTIN].write(0)
        board.exit()
        break
    else:
        print("Lệnh không hợp lệ")
