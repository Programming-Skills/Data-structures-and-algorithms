# sumOfPositiveInteger.py

import argparse

def sumOfPositiveInteger(num):

    """Recursively calculates the sum of positive digits

    Parameters
    ----------
    arr : int
        The file location of the spreadsheet

    Returns
    -------
    int
        the sum of the digits
    """

    assert num >= 0 and int(num) == num, "Only positive integers!"
    quotent_remainder = [num // 10, num % 10]
    return (quotent_remainder[0] + quotent_remainder[1])

if __name__ == "main":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('num', nargs="+", type=int)
    args = parser.parse_args()
    print("File executed!")
    print(sumOfPositiveInteger(args.num))
