#2. リストLと二つの数l,rが与えられて、Lのl番目からr番目までの要素の合計を返す関数cumsum(L, l, r)を定義してください

### 2の入力と出力
#```
#>>> square([1,2,3,4,5,6], 1, 5)
#14
#>>> square([1,2,5,6], 2, 4)
#11
#```

def cumsum(L,l,r):
    sum=0
    for i in range(l,r):
        sum+=L[i]
    return sum

print(cumsum([1,2,5,6],2,4))
