# sumOfDigits.py

import argparse

def sumOfDigits(n: int) -> int:
    """Recursively calculates the sum of positive digits

    Parameters
    ----------
    arr : int
        digit inputted by the user.

    Returns
    -------
    int
        the sum of the digits
    """
    assert n >= 0, "Only positive integers!"
    if n < 10:
        return n
    else:
        return (int(n%10) + sumOfDigits(int(n/10)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    print("File executed")
    print(sumOfDigits(args.n))