n = int(input())
con = -1
denomi = 2

for x in range(n - 1):
    if denomi % 2 ==0:
        con = con + 1 / denomi
    else:
        con = con + 1 / denomi
    denomi = con + 1
print("{:.6f}".format(con))