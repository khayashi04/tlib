import tlib as t
import numpy as np
while True:
	xx = int(input("\nmode select\n入力モード以外を選択するとモードに応じて乱数を生成。0を入力で終了。\n1:整数\n2:正規分布\n3:二項分布\n4:ポワソン分布\n5:小さい値\n6:入力\n7:Helps\n"))
	if xx == 0:
		break
	if xx == 1:
		#-999から999のj範囲の整数を1000個生成
		x = np.random.randint(-999,999,1000)
		y = np.random.randint(-999,999,1000)
	elif xx == 2:
		#正規分布にそった乱数を1000個生成
		x = np.random.randn(1000)
		y = np.random.randn(1000)
	elif xx == 3:
		#試行回数10回、確率0.5の二項分布乱数を1000個生成
		x = np.random.binomial(10,0.5,1000)
		y = np.random.binomial(10,0.5,1000)
	elif xx == 4:
		#ポワソン
		x = np.random.poisson(30,1000)
		y = np.random.poisson(30,1000)
	elif xx == 5:
		#小さい値
		x = [10, 20, 30, 40, 50, 60]
		y = [70, 80, 90, 100, 110, 120]
	elif xx == 6:
		#入力型
		x = list(map(int, input("list1> ").split()))
		y = list(map(int, input("list2> ").split()))
	elif xx == 7:
		#helpを表示
		t.helps()	
	else:
		print("ERROR")
		break
	
	yy = int(input("\n次に使用する関数を選択。0を入力で終了。\n1: primeNum\n2: sort\n3: rsort\n4: dist\n5: ddist\n6: plot\n7: dsta\n8: des\n9: table\n10: diceAll\n11: dicett\n12: dicekt\n"))
	if yy == 0:
		break
	elif yy  == 1:
		primeNum(int(input("整数を入力\n")))
	elif yy== 2:
		print("\ndate1\n")
		t.sort(x)
		print("\ndate2\n")
		t.sort(y)
	elif yy== 3:
		print("\ndate1\n")
		t.reverseSort(x)
		print("\ndate2\n")
		t.reverseSort(y)
	elif yy== 4:
		t.singleHist(x)
		t.singleHist(y)
	elif yy== 5:
		t.doubleHist(x,y)
	elif yy== 6:
		t.plot(x,y)
	elif yy == 7:
		t.doubleStatus(x,y)
	elif yy == 8:
		print("\ndate1\n")
		t.describeData(x)
		print("\ndate2\n")
		t.describeData(y)
	elif yy == 9:
		print("\ndate1\n")
		t.table(x)
		print("\ndate2\n")
		t.table(y)
	elif yy == 10:
		t.print("")
		diceAllPattern()
		print("")
	elif yy == 11:
		print("\n賽目  頻度")
		t.doubleDiceSum()
		print("")
	elif yy == 12:
		print("\n賽目  頻度")
		t.doubleDiceMult()
		print("")
	else:
		print("ERROR")
		break