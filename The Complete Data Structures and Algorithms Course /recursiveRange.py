# recursiveRange.py

import argparse

def recursiveRange(num):
    assert num >= 0 and int(num) == num, "The number must be positive integer only"
    if num == 0:
        return 0
    else:
        return (num + recursiveRange(num-1))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('num', type=int)
    args = parser.parse_args()
    print("File executed")
    print(recursiveRange(args.num))
