import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")  # Assuming CSV format

    if len(parts) > 2:  # Ensure valid data
        date, temp, humidity, label = parts[0], parts[1], parts[2], parts[3]
        
        try:
            temp = float(temp)
            if temp > 40:  # Example threshold for anomaly
                print(f"{date}\tAnomaly")
            else:
                print(f"{date}\tNormal")
        except ValueError:
            continue