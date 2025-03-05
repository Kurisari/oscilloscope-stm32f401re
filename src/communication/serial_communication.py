import serial
import threading

class SerialCommunication:
    def __init__(self, port, baudrate):
        self.ser = self.open_serial_port(port, baudrate)
        self.running = False

    def open_serial_port(self, port, baudrate):
        try:
            ser = serial.Serial(port, baudrate, timeout=1)
            return ser
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return None

    def read_data(self, callback):
        if self.ser and self.ser.is_open:
            self.running = True
            def run():
                while self.running:
                    try:
                        data = self.ser.readline().decode('utf-8').strip()
                        if data:
                            callback(float(data.split(":")[1].strip().split(" ")[0]))
                    except Exception as e:
                        print(f"Error reading data: {e}")
            thread = threading.Thread(target=run, daemon=True)
            thread.start()

    def stop_reading(self):
        self.running = False

    def send_command(self, command):
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(command.encode('utf-8'))
            except Exception as e:
                print(f"Error sending command: {e}")
