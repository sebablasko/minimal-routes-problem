import sys

if __name__ == '__main__':
    f1, f2 = str(sys.argv[1]), str(sys.argv[2])
    fo_1 = open(f1, "r")
    fo_2 = open(f2, "r")

    assert fo_1.readline().rstrip("\n\r") == fo_2.readline().rstrip("\n\r")

    for line_1 in fo_1:
        line_2 = fo_2.readline()
        n1, _, w1 = line_1.rstrip("\n\r").split(" ")
        n2, _, w2 = line_2.rstrip("\n\r").split(" ")
        assert n1 == n2
        assert w1 == w2

    fo_1.close()
    fo_2.close()
    print('OK')
