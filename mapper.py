import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")

    if len(parts) > 2 and parts[0] != "Date":
        try:
            temp = float(parts[1])
            if temp > 40:
                print("%s\t%s" % (parts[0], "Anomaly"))
            else:
                print("%s\t%s" % (parts[0], "Normal"))
        except ValueError:
            continue
