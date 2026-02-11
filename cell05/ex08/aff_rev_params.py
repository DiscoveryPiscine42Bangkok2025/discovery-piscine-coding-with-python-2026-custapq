import sys

params = sys.argv[1:]

if not params:
    print("none")
elif len(params) < 2:
    print("none")
else:
    params.reverse()
    for param in params:
        print(param)
            