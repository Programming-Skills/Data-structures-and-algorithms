# productOfArray.py

import argparse

def productOfArray(arr):
    n = len(arr)
    if n == 0:
        return 1
    else:
        return (arr[0] * productOfArray(arr[1:]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('arr', nargs='+', type=int)
    args = parser.parse_args()
    print("File executed")
    print(productOfArray(args.arr))
    