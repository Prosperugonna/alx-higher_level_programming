#!/usr/bin/python3
import sys

count = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
size = 0

try:
    for line in sys.stdin:
        count += 1
        data = line.split()

        try:
            size += int(data[-1])
        except:
            pass

        try:
            code = data[-2]
            if code in codes:
                codes[code] += 1
        except:
            pass

        if count % 10 == 0:
            print("File size: {}".format(size))
            for code in sorted(codes.keys()):
                if codes[code] != 0:
                    print("{}: {}".format(code, codes[code]))
except KeyboardInterrupt:
    print("File size: {}".format(size))
    for code in sorted(codes.keys()):
        if codes[code] != 0:
            print("{}: {}".format(code, codes[code]))
    raise
