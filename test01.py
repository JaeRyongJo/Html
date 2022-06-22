#세로 h 가로 w 막대 개수 n 길이 l 방향 d 좌표 xy
arr = []
h, w = input().split()
h = int(h)
w = int(w)
n = int(input())

for i in range (h):
    arr.append([])
    for j in range(w):
        arr[i].append(0)
for i in range(n):
    l, d, x, y = input().split()
    x = int(x)
    y = int(y)
    d = int(d)
    l = int(l)
    for j in range(l):
        if d==0:
            arr[x-1][y+j-1] =1
        else:
            arr[x+j-1][y-1]=1

for i in range(h):
    for j in range(w):
        print(arr[i][j],end=' ')
    print()


