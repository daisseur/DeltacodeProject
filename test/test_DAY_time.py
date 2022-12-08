from DeltacodeProject.DeltacodeProject import DayEncoding as coding
from time import perf_counter as tc
from string import ascii_lowercase

min = 1
max = 0.000000000000000000000001

for character in range(0x110000):
    for p in range(0x110000):
        for f in range(0x110000):
            s = tc()
            coding(password=chr(p), string=character, shift=f).encode()
            e = tc()
            t = e - s
            if t < min:
                min = t
            elif t > max:
                max = t
        print(f"{min:.7f}", max)
