#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    summ = 0

    if count == 1:
        print ("{}".format(summ))
    else:
        for i in range(1, count):
            summ += int(sys.argv[i])

        print("{}".format(summ))
