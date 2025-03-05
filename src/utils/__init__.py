def process_waveform_data(data):
    # Function to process raw waveform data from the STM32
    processed_data = [float(value) for value in data.split(',')]
    return processed_data

def format_waveform_data(data):
    # Function to format waveform data for display
    return [f"{value:.2f}" for value in data]