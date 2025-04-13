import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    date, status = line.split("\t")
    counts[status] += 1  # Count anomalies and normal readings

# Output the final counts
for status, count in counts.items():
    print(f"{status}\t{count}")