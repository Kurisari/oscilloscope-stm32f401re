import tkinter as tk
from communication import SerialCommunication
from gui import OscilloscopeGUI

class OscilloscopeApp:
    def __init__(self, port, baudrate):
        self.root = tk.Tk()
        self.root.title("Oscilloscope")
        self.root.iconbitmap("icon.ico")
        self.serial_comm = SerialCommunication(port, baudrate)
        self.gui = OscilloscopeGUI(self.root, self.serial_comm)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.serial_comm.stop_reading()
        if self.serial_comm.ser and self.serial_comm.ser.is_open:
            self.serial_comm.ser.close()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = OscilloscopeApp(port="COM3", baudrate=9600)
    app.run()