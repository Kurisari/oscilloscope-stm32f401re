# Oscilloscope Application

This project is an oscilloscope application that communicates with an STM32F401RE microcontroller using serial communication. The application provides a graphical user interface (GUI) for visualizing waveform data received from the microcontroller.

## Project Structure

``` None
oscilloscope-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── gui
│   │   └── __init__.py        # GUI class for managing layout and user interactions
│   ├── communication
│   │   └── __init__.py        # Handles serial communication with the STM32F401RE
│   └── utils
│       └── __init__.py        # Utility functions for data processing and formatting
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ``` terminal
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Connect the STM32F401RE microcontroller to your computer via USB.
2. Open the application by running the following command:

   ``` terminal
   python src/main.py
   ```

3. The GUI will launch, and you can start interacting with the oscilloscope features.

## STM32F401RE Communication

The application communicates with the STM32F401RE using serial communication. Ensure that the correct COM port is selected in the application settings to establish a successful connection. The application will read waveform data from the microcontroller and display it in real-time on the GUI.
