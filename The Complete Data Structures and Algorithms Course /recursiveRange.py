# recursiveRange.py

import argparse

def recursiveRange(num):
    container = []
    if num == 0:
        return 1
    else:
        for i in list(range(num)):
            container.append(i)
        return (container[0] + recursiveRange(container[1:]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('num', type=int)
    args = parser.parse_args()
    print("File executed")
    print(recursiveRange(args.num))
