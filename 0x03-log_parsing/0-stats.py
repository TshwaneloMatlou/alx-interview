#!/usr/bin/python3
import sys

lines = []
total_size = 0
status_counts = {}

try:
    for line in sys.stdin:
        line = line.strip()
        if line.startswith('"GET /projects/260 HTTP/1.1"'):
            parts = line.split()
            if len(parts) == 7:
                status_code = parts[5]
                file_size = int(parts[6])
                lines.append(line)
                total_size += file_size
                if status_code.isdigit():
                    status_code = int(status_code)
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1
        if len(lines) == 10:
            print(f"Total file size: {total_size}")
            for status_code in sorted(status_counts.keys()):
                print(f"{status_code}: {status_counts[status_code]}")
            print()
            lines = []
            status_counts = {}
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")
