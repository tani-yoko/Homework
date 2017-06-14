#4. リストLを昇順(小さい順)にソートした結果を返す関数sorted(L)を定義してください

def sorted(L):
    L.sort()
    return L
print(sorted([3,1,4,6,9]))
