import serial
import csv
import time
import pynmea2

# Configure serial port (adjust as needed)
ser = serial.Serial("/dev/ttyUSB0", baudrate=4800, timeout=1)  # Replace /dev/ttyS0 with your GPS device's serial port
# Open the CSV file
with open("gps_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=",")
    # Write the header row
    csv_writer.writerow(["Timestamp", "Latitude", "Longitude", "Altitude", "Speed", "Course"])
    # Start reading GPS data
    while True:
        try:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            # Parse the NMEA sentence
            msg = pynmea2.parse(line)
            # Extract relevant data
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            latitude = msg.latitude
            longitude = msg.longitude
            altitude = msg.altitude
            speed = msg.speed
            course = msg.course
            # Write the data to the CSV file
            csv_writer.writerow([timestamp, latitude, longitude, altitude, speed, course])
            print(f"Data saved: {timestamp}, {latitude}, {longitude}, {altitude}, {speed}, {course}")
        except pynmea2.ParseError:
            print("Error parsing NMEA sentence")
        except KeyboardInterrupt:
            print("Exiting program")
            break
