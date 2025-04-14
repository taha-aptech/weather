import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    _, status = line.split("\t")
    counts[status] += 1

for status, count in counts.items():
    print("%s\t%d" % (status, count))
