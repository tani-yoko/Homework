#合計金額が与えられたとき、必要な硬貨の枚数を表示するプログラムを作成してください(money.py)
#硬貨は500円、100円、50円、10円、５円、１円です。
#入力される金額は1000円以下です。
#使用する硬貨の枚数を最低限の枚数にしてください

#金額の入力
yen = int(input("合計金額は?"))

#集計

count_500 =0
count_100 =0
count_50 =0
count_10 =0
count_5 =0
count_1 =0

#条件
while yen/500 >= 1:
    count_500 += 1
    yen = yen - 500

while yen / 100 >= 1:
    count_100 += 1
    yen = yen - 100

while yen / 50 >= 1:
    count_50 += 1
    yen = yen - 50

while yen / 10 >= 1:
    count_10 += 1
    yen = yen - 10

while yen / 5 >= 1:
    count_5 += 1
    yen = yen - 5

while yen / 1 >= 1:
    count_1 += 1
    yen = yen - 1


print(count_500)
print(count_100)
print(count_50)
print(count_10)
print(count_5)
print(count_1)
