import sys

a = int(sys.argv[1])

i = 0
while i < 999999999: # pragma: no branch
    if i == a:
        print("a == " + str(i))
        break
    print("a != " + str(i))
    i = i + 1
