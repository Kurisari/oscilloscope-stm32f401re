import tkinter as tk
import random
from communication.serial_communication import SerialCommunication
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OscilloscopeGUI:
    def __init__(self, master, serial_comm):
        self.master = master
        self.serial_comm = serial_comm
        self.master.title("Oscilloscope")

        self.data = []
        self.max_points = 50

        self.create_widgets()

    def create_widgets(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Voltage over Time")
        self.ax.set_ylim(0, 3.3)
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Voltage")
        self.line, = self.ax.plot([], [], 'r-')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_acquisition, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_acquisition, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        self.interval_label = tk.Label(self.master, text="Interval (ms):")
        self.interval_label.pack(side=tk.LEFT)

        self.interval_entry = tk.Entry(self.master)
        self.interval_entry.pack(side=tk.LEFT)
        
        self.apply_button = tk.Button(self.master, text="Apply", command=self.apply_interval)
        self.apply_button.pack(side=tk.LEFT)

    def start_acquisition(self):
        # try:
        #     interval = int(self.interval_entry.get())
        # except ValueError:
        #     interval = 100  # Valor por defecto si la entrada no es válida
        # self.serial_comm.send_command(str(interval))
        self.serial_comm.read_data(self.update_waveform)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
    def apply_interval(self):
        try:
            interval = int(self.interval_entry.get())
        except ValueError:
            interval = 100
        self.serial_comm.send_command(str(interval))
        self.start_button.config(state=tk.NORMAL)

    def stop_acquisition(self):
        self.serial_comm.stop_reading()
        self.serial_comm.send_command("-1")
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def update_waveform(self, new_data):
        self.data.append(new_data)
        if len(self.data) > self.max_points:
            self.data.pop(0)

        self.line.set_xdata(range(len(self.data)))
        self.line.set_ydata(self.data)
        self.ax.set_xlim(0, len(self.data))

        self.canvas.draw()