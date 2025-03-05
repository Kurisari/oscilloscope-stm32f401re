from .serial_communication import SerialCommunication

def open_serial_port(port, baudrate):
    import serial
    try:
        ser = serial.Serial(port, baudrate)
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def read_data(ser):
    if ser and ser.is_open:
        try:
            data = ser.readline().decode('utf-8').strip()
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            return None
    return None

def send_command(ser, command):
    if ser and ser.is_open:
        try:
            ser.write(command.encode('utf-8'))
        except Exception as e:
            print(f"Error sending command: {e}")