'''
統計ライブラリtlib
作成者：K.Hayashi
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
from collections import Counter

def first():
	print("help()でヘルプを表示。コマンドラインで利用する際に参照。\nすべてをインポートする際に時間がかかる可能性あり\n\nインポート方法\nimport tlib as t\n\n関数使用方法\nt.関数名\n")

#helps
def help():
	com = ["1: primeNum(num)",
		"2: sort(list)",
		"3: reverseSort(list)",
		"4: singleHist(list)",
		"5: doubleHist(list1,list2)",
		"6: plot(list1, list2)",
		"7: singleStatus(list)",
		"8: doubleStatus(list1,list2)",
		"9: describeData(list)",
		"10: table(list)",
		"11: diceAllPattern()",
		"12: doubleDiceSum()",
		"13: doubleDiceMult()"]

	th = {1:"primeNum(整数): 指定された整数までのすべての素数を表示し、素数の数を表示。", 
		2:"sort(リスト): 指定されたリストを昇順に並べ替え。", 
		3:"reverseSort(リスト): 指定されたリストを降順に並べ替え。", 
		4:"singleHist(リスト): 指定されたリストのヒストグラムを表示。",
		5:"doubleHist(リスト1,リスト2): 指定された二つのリストのヒストグラムを表示。",
		6:"plot(リスト1, リスト2): 指定された二つのリストの散布図をプロット。", 
		7:"singleStatus(リスト): 指定されたリストの要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示。",
		8:"doubleStatus(リスト1, リスト2): 指定された二つのリストの要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示し、二つのリストの共分散、相関係数、回帰係数を表示。",
		9:"describeData(リスト): 指定されたリストのデータ数(count)、平均(mean)、標準偏差(std)、最小値(min)、第一四分位点(25%)、第二四分位点(50%)、第三四分位点(75%)、最大値(max)、データ型(dtype)を出力。",
		10:"table(リスト): 指定されたリストの度数分布表を表示。左側に階級値、右側に頻度。",
		11:"diceAllPattern(): 二つのさいころの全パターンを表示。",
		12:"doubleDiceSum(): 二つのさいころの目を足したものを度数分布表に表示。左側に階級値、右側に頻度。",
		13:"doubleDiceMult(): 二つのさいころの目を掛けたものを度数分布表に表示。左側に階級値、右側に頻度。"}
	while 1:
		print("表示したいHelpの番号を選択してください。0を入力で終了")
		for i in range(len(com)):
			print(com[i])
		h = int(input())
		if h == 0: break
		print("\n",th[h], "\n")

#素数関連　ふるいを用いた素数洗い出し
def primeNum(num):
	n = [] #素数を格納するためのリスト
	li = [] #2から入力された値までのすべての数を格納するリスト

	#2から入力された値までのすべての数を格納
	li = [i for i in range(2,num+1)]

	#liリストの0番目が入力された値の平方根以下になるまでloop
	while li[0] <= int(np.sqrt(num)):
		n.append(li[0]) #nリストにliリストの0番目を追加
		sss = li[0] #sssにliリストの0番目を格納
		li = [i for i in li if i % sss != 0] #素数判定
	n.extend(li) #liリストに残った数を素数としてnリストに格納

	#素数をプリント
	print(n,"\n")

	#素数の数をプリント
	print("素数の合計: ", len(n), "\n")


#リストソート(昇順)
def sort(x):
	srt = copy.copy(x)
	print(np.sort(srt))

#リストソート(降順)
def reverseSort(x):
	unsrt = copy.copy(x)
	print(np.sort(unsrt)[::-1])

#データ数が多い場合使用すればいいと思うの。
def describeData(x):
	print(pd.Series(x).describe())

#度数分布表を表示
def table(x):
	print(pd.Series(x).value_counts())

#ヒストグラムを表示
def singleHist(x):
	plt.hist(x)
	plt.show()

#ヒストグラムを二つ表示
def doubleHist(x,y):	
	plt.subplot(2,2,1)
	plt.hist(x)
	plt.title("hist x")
	plt.subplot(2,2,4)
	plt.hist(y)
	plt.title("hist y")
	plt.show()

#散布図を描画。値渡しは回避済み
def plot(x, y):	
	plt.scatter(x,y)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show()

#さいころ全パターン
def diceAllPattern():
	x = 1
	for i in range(1,7):
		for j in range(1,7):
			print(i, "+", j, "= ", i+j)
			x += 1
			if j == 6: print("")

#足し算パターン
def doubleDiceSum():
	diceT = []
	for i in range(1,7):
		for j in range(1,7):
			diceT.append(i+j)
	print(pd.Series(diceT).value_counts(sort=False))

def doubleDiceMult():
	diceK = []
	for i in range(1,7):
		for j in range(1,7):
			diceK.append(i*j)
	print(pd.Series(diceK).value_counts(sort=False))

#関数をたたきまくった代物
def singleStatus(x):
	#値渡し回避
	li = copy.copy(x)

	#リストをソート
	li.sort

	#二乗平均を計算する際に使用
	lii = []
	ii = ll = 0
	l = ["要素数:   ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ", "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]

	#格納作業
	for i in range(len(li)): ll += li[i] ** 2 
	for i in range(len(li)): ii += abs(li[i] - np.mean(li))
	mode = Counter(li).most_common(1)
	lii.extend([len(li), round(np.mean(li), 4), np.median(li), mode[0][0], max(li), min(li), max(li) - min(li), round(ll / len(li), 4), round(ii / len(li), 4), round(np.var(li), 4), round(np.std(li), 4)])

	#print作業
	print("")
	for i in range(10):
		print(l[i], lii[i])
	print("")

#こっちは統計の勉強用に作成したもので、numpyの関数は使っていません。ほんとは少しだけ使いました
def doubleStatus(x, y):
	#flag
	flag = 0
	#値渡し回避
	li1 = copy.copy(x)
	li2 = copy.copy(y)

	#二つのリストの長さが異なった場合、ERROR文
	if len(li1) != len(li2):
		print("ERROR: リストの長さが異なります。")

	#必要なものを宣言。
	l = ["要素数:   ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ", "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]
	aa = ll1 = ii1 = ll2 = ii2 = 0 
	xx = []
	yy = []

	#共分散を計算するために使用。リストソート前に計算する必要あり。
	for i in range(len(li1)):
		aa += li1[i] * li2[i]

	#二つのデータを昇順ソート。
	li1.sort()
	li2.sort()

	#平均を計算
	ave1 = sum(li1) / len(li1)
	ave2 = sum(li2) / len(li2)

	#最大値を計算
	ma1 = li1[len(li1) - 1]
	ma2 = li2[len(li2) - 1]

	#最小値を計算
	mi1 = li1[0]
	mi2 = li2[0]

	#範囲（レンジ）を計算		
	ren1 = ma1 - mi1
	ren2 = ma2 - mi2

	for i in range(len(li1)):
	#平均偏差を計算するためにi番目の要素から要素の平均を減算し、その絶対値を取り、すべてを加算する
		ii1 += abs(li1[i] - ave1)
		ii2 += abs(li2[i] - ave2)

	#二乗平均を計算するためにi番目の要素を二乗し、すべてを加算する
		ll1 += li1[i] ** 2	
		ll2 += li2[i] ** 2	

	#平均偏差を計算
	hehe1 = ii1 / len(li1)
	hehe2 = ii2 / len(li2)

	#二条平均を計算
	double1 = ll1 / len(li1)
	double2 = ll2 / len(li2)

	#中央値を計算
	if len(li1) % 2 == 0:
		mid1 = (li1[int(np.floor(len(li1) / 2))] + li1[int(np.floor(len(li1) / 2 -1))]) / 2
		mid2 = (li2[int(np.floor(len(li2) / 2))] + li2[int(np.floor(len(li2) / 2 -1))]) / 2
	elif len(li1) % 2 == 1:
		mid1 = li1[int(np.floor(len(li1) / 2))]
		mid2 = li2[int(np.floor(len(li2) / 2))]

	#最頻値を計算。分からなかったのではなく人力でやろうとするとめんどくさかったからやってない。
	mode1 = Counter(li1).most_common(1)
	mode2 = Counter(li2).most_common(1)

	#分散を計算
	bun1 = double1 - (ave1 ** 2)
	bun2 = double2 - (ave2 ** 2)

	#標準偏差を計算
	hyo1 = np.sqrt(bun1)
	hyo2 = np.sqrt(bun2)

	#共分散を計算
	kyoubun = (aa / len(li1)) - (ave1 * ave2) 

	#相関係数を計算。0だった場合、強制的に0を表示する。
	if hyo1 == 0 or hyo2 == 0:
		err = "ERROR: 0のため相関係数を計算できません。"
		flag = 1
	else:
		r = kyoubun / hyo1 / hyo2
		
		#回帰係数を計算
		a = kyoubun / bun1
		b = ave2 - (a * ave1)


	#すべての結果をリストに追加
	xx.extend([len(li1), round(ave1, 4), mid1, mode1[0][0], ma1, mi1, ren1, round(double1, 4), round(hehe1, 4), round(bun1, 4), round(hyo1, 4)])
	yy.extend([len(li2), round(ave2, 4), mid2, mode2[0][0], ma2, mi2, ren2, round(double2, 4), round(hehe2, 4), round(bun2, 4), round(hyo2, 4)])

	#結果を出力。
	print("\nx date\n")
	for i in range(len(xx)):
		print(l[i], xx[i])

	print("\ny date\n")
	for i in range(len(yy)):
		print(l[i], yy[i])

	print("\n共分散:   ", round(kyoubun, 4))
	if flag != 0:
		print(err)
	else:
		print("相関係数: ", round(r, 4))
		print("回帰係数: y = ax + bとするとき、\n a = ", round(a, 4), ", b = ", round(b, 4),"\n")

#main
if __name__ == '__main__':
	first()