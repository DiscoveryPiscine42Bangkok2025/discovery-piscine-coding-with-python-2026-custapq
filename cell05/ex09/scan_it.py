import sys

if len(sys.argv) != 3 or sys.argv[1] not in sys.argv[2]:
    print("none")
else:
    count = sys.argv[2].count(sys.argv[1])
    print(count)