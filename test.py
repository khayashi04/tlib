from StatLi import StatLi
li1 = [19,765,76,3,456,7,75,5,465,4,754,754,6,2,523,3,543]
li2 = [19,765,76,3,456,4,75,5,465,4,754,754,6,2,523,3,543]
a = 1234
b = 5678
data1 = StatLi(li1, li2)
data2 = StatLi(a, b)
data3 = StatLi("いいよこいよいくいく", "いいくにつくろうかまくらばくふ")
print(data2.collatz())
print(data2.monte())