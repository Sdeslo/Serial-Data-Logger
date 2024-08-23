# Serial-Data-Logger
Python script to save serial data into a CSV file

## Features
- **Serial Communication:** Connects to a specified serial port at a specified baud rate.
- **Data Logging:** Logs received time and voltage data into a CSV file (`voltage_log.csv`).
- **Error Handling:** Gracefully handles common issues like connection errors, permission issues, and unexpected exceptions.
- **User-Friendly:** Allows users to specify the serial port and baud rate via command-line arguments.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x** installed on your machine.
- **pySerial** library installed. You can install it using pip:
  pip install pyserial

## Usage
### Command-Line Arguments
- **--port:** The serial port to connect to (e.g., COM5, /dev/ttyUSB0).
- **--baud_rate:** The baud rate for the serial connection (e.g., 9600, 115200).

### Running the script
To run the script use the following line: python serial_logging.py --port <your-port> --baud_rate <your-baud-rate>

### Stopping the script
The script can be stopped at any time by pressing Ctrl + C. This will safely close the serial port and stop logging.

### Output
The script creates a CSV file named voltage_log.csv in the current working directory.

### Error handling
- **Serial Connection Errors:** If the specified serial port cannot be opened, an error message will be displayed.
- **Permission Errors:** If there is a permission issue accessing the port, an appropriate message will be shown.
- **General Exceptions:** Any other unforeseen errors will be caught and displayed.

### Customization
- **CSV File Name and Headers:** Modify the file name and headers in the open function and csvwriter.writerow line.
- **Data Parsing:** Adjust the data parsing logic in the while loop if your device sends data in a different format.
