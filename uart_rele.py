import serial
import struct
import time

    
def send_comand(state, number):
    try:
        ser = serial.Serial('/dev/ttyUSB0', 115200)
        time.sleep(2)  # Ожидание инициализации соединения
    except:
        return None
    
    packet = struct.pack('>BBH',0xFF,state,number)
    ser.write(packet)
    print(f'Команда: {state,number}')
    response = ser.readline().decode()
    return response


if __name__ == "__main__":
    while True:
        state,number = input().split()
        response = send_comand(int(state),int(number))
        print(f"Ответ: {response}")