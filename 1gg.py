l = int(input())
g = list(map(int,input().split()))
r = []
for i in range(len(g)):
    if g.count(g[i]) > 1:
        if g[i] not in r:
            r.append(g[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
