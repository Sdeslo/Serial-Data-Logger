"""
Serial Data Logger

Author:
    Simon Deslauriers

This script reads data from a serial port and logs it into a CSV file. It allows
users to specify the serial port and baud rate via command-line arguments.

Features:
- Reads data from a specified serial port at a specified baud rate.
- Logs the received data into a CSV file named 'voltage_log.csv' in the current working directory.
- Handles common errors such as port connection issues and permission errors.
- Supports graceful termination of the logging process using Ctrl + C.
- Ensures that the serial port is properly closed after logging is stopped.

Usage:
1. Run the script from the command line, specifying the desired port and baud rate.
2. The CSV file will be created in the current directory with logged data.

Dependencies:
- Python 3.x
- pySerial library (`pip install pyserial`)

Command-line Arguments:
- --port: The serial port to which the device is connected (e.g., 'COM5', '/dev/ttyUSB0').
- --baud_rate: The baud rate for the serial communication (e.g., 9600, 115200).

Example:
    $ cd directory_of_this_file
    $ python serial_logging.py --port COM5 --baud_rate 9600

Note:
    If your data dosent contain time stamps, they can easily be added with the lines start_time = time.time() 
    and time_value = time.time() - start_time as a data value
"""
import os
import serial
import time
import csv
import argparse

def parse_arguments():
    """Parses command-line arguments for serial port and baud rate."""
    parser = argparse.ArgumentParser(description="Serial Data Logger")
    parser.add_argument('--port', type=str, required=True, help="The serial port to connect to (e.g., COM5, /dev/ttyUSB0)")
    parser.add_argument('--baud_rate', type=int, required=True, help="The baud rate for the serial connection (e.g., 9600, 115200)")
    return parser.parse_args()

def main():
    args = parse_arguments()

    print("Current Working Directory:", os.getcwd())

    port = args.port
    baud_rate = args.baud_rate

    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Wait for the serial connection to initialize

        # CSV file voltage_log.csv file be created in working directory
        # Replace to the wanted name of the file
        with open('voltage_log.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Replce with wanted headers
            csvwriter.writerow(["Time(s)", "Voltage(V)"]) 
            print("CSV file opened and headers written.")
            print("Time(s)", "Voltage(V)")
        
            try:
                while True:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        print(line) # not necessary but useful for debug
                        data = line.split(',') # Replace by what seperates values
                        if len(data) == 2:  # Ensure we have exactly 2 columns, replace by the amount of values
                            time_value = data[0].strip()  # First value
                            voltage_value = data[1].strip()  # Second value
                            # Write time and voltage to separate columns
                            csvwriter.writerow([time_value, voltage_value])
                            csvfile.flush()  # Ensure data is written to the file
            except KeyboardInterrupt:
                print("Logging stopped by user.") # ctrl + c to stop logging
    except serial.SerialException as e:
        print(f"Could not open port {port}: {e}") # unable to connect error
    except PermissionError as e:
        print(f"Permission error accessing port {port}: {e}") # Not runned on administrator mode or sanother software uses that port
    except Exception as e:
     print(f"Unexpected error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()
    