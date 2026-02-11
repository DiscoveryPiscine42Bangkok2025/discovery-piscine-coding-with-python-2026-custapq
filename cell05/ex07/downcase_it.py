import sys

params = sys.argv[1:]

if not params:
    print("none")
elif len(params) == 1:
    print(params[0].lower())
else:
    print("none")