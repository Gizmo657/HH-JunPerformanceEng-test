import sys

def massive_pass(n, m):
    j = 0
    c = 1
    path = ""
    while j == 0:
        path += str(c)
        for i in range(m):
            if i == m - 1 and c == 1:
                j = 1
            if i != m - 1:
                c += 1
            if c > n:
                c = 1
    return path

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])
output = massive_pass(n1, m1) + massive_pass(n2, m2)
print(output)