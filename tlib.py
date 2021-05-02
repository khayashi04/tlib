'''
統計ライブラリtlib
作成者：K.Hayashi
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import math
from collections import Counter
from fractions import Fraction

def first():
	print("tlibへようこそ。\nライブラリをインポートする際に時間がかかります。\n\nインポート方法\nimport tlib as t\n\n関数使用方法\nt.関数名\n")

#helps
def help():
	list_name = ["1: primeNum()",
		"2: sort()",
		"3: reverseSort()",
		"4: singleHist()",
		"5: doubleHist()",
		"6: plot()",
		"7: singleStatus()",
		"8: doubleStatus()",
		"9: describeData()",
		"10: table()",
		"11: diceAllPattern()",
		"12: doubleDiceSum()",
		"13: doubleDiceMult()",
		"14: fraction()",
		"15: levenshtein()"]

	list_info = {1:"primeNum(整数): 指定された整数までのすべての素数を表示し、素数の数を表示。", 
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
		13:"doubleDiceMult(): 二つのさいころの目を掛けたものを度数分布表に表示。左側に階級値、右側に頻度。",
		14:"fraction(整数1,整数2): 整数1/整数2を既約分数で表示。",
		15:"levenshtein(文字列1,文字列2): 文字列1と文字列2のレーヴェンシュタイン距離を求める。"}
	
	while 1:
		print("表示したいHelpの番号を選択してください。0を入力で終了")
		for i in range(len(list_name)):
			print(list_name[i])
		is_number_correct = int(input())
		if is_number_correct > 15 or is_number_correct < 0: 
			print("\nError 1から14までの数字で入力してください。\n")
			continue
		if is_number_correct == 0: break
		print("\n",list_info[h], "\n")
		break

#素数関連　ふるいを用いた素数洗い出し
def primeNum(num):
	if type(num) is not int:
		print("ERROR 整数を入力してください。")
	else:
		#素数を格納するためのリスト	
		list_prime = []
		#2から入力された値までのすべての数を格納
		list_num = [i for i in range(2,num+1)]

		#list_numの0番目が入力された値の平方根以下になるまでloop
		while list_num[0] <= int(np.sqrt(num)):
			#list_primeにnumer_listの0番目を追加
			list_prime.append(list_num[0]) 
			#headにliリストの0番目を格納
			head = list_num[0] 
			#素数判定
			list_num = [i for i in list_num if i % head != 0]

		#list_numに残った数を素数としてlist_primeリストに格納
		list_prime.extend(list_num) 
		#素数をプリント
		list_prime_str = [str(a) for a in list_prime]
		list_prime_str = ' '.join(list_prime_str)
		print(list_prime_str,"\n")
		#素数の数をプリント
		print("素数の合計: ", len(list_prime), "\n")

#リストソート(昇順)
def sort(list):
	list_srt = copy.copy(list)
	print(np.sort(list_srt))

#リストソート(降順)
def reverseSort(list):
	list_srt = copy.copy(list)
	print(np.sort(list_srt)[::-1])

#データ数が多い場合使用するとよい
def describeData(list):
	print(pd.Series(list).describe())

#度数分布表を表示
def table(list):
	print(pd.Series(list).value_counts())

#ヒストグラムを表示
def singleHist(list):
	plt.hist(list)
	plt.show()

#ヒストグラムを二つ表示
def doubleHist(list1,list2):	
	plt.subplot(2,2,1)
	plt.hist(list1)
	plt.title("List1")
	plt.subplot(2,2,4)
	plt.hist(list2)
	plt.title("List2")
	plt.show()

#散布図を描画。値渡しは回避済み
def plot(list1, list2):	
	plt.scatter(list1,list2)
	plt.xlabel("List1")
	plt.ylabel("List2")
	plt.show()

#さいころ全パターン
def diceAllPattern():
	for i in range(1,7):
		for j in range(1,7):
			print(i, "+", j, "= ", i+j)
			if j == 6: print("")

#足し算パターン
def doubleDiceSum():
	dice = []
	for i in range(1,7):
		for j in range(1,7):
			dice.append(i+j)
	print(pd.Series(dice).value_counts(sort=False))

#掛け算パターン
def doubleDiceMult():
	dice = []
	for i in range(1,7):
		for j in range(1,7):
			dice.append(i*j)
	print(pd.Series(dice).value_counts(sort=False))

#既約分数を表示
def fraction(num1,num2):
	if (type(num1) is not int) or (type(numb2) is not int):
		print("ERROR 整数を入力してください。")
	else:
		print(Fraction(num1,num2))

#レーヴェンシュタイン距離を求める
def levenshtein(str1,str2):
	list_num = [0]*3
	list_str1 = list(map(str,str1))
	list_str2 = list(map(str,str2))
	list_str1.insert(0,"$")
	list_str2.insert(0,"$")

	leven_list =[[i for i in range(len(list_str1))] for j in range(len(list_str2))]
	for i in range(len(list_str2)): 
		leven_list[i][0] = i

	for y in range(len(list_str2) - 1):
		for x in range(len(list_str1) - 1):
			list_num[0] = leven_list[y+1][x] + 1
			list_num[1] = leven_list[y][x+1] + 1
			if str2[y] == str1[x]: 
				list_num[2] = leven_list[y][x]
			else: 
				list_num[2] = leven_list[y][x] + 1
			leven_list[y+1][x+1] = min(list_num)

	leven = pd.DataFrame(data=leven_list,columns=list_str1,index=list_str2)
	print(leven,"\n\n","距離: ",leven_list[len(list_str2)-1][len(list_str1)-1])

#関数をたたきまくった代物
def singleStatus(list):
	#値渡し回避
	list_copy = copy.copy(list)
	data = []
	
	#リストをソート
	list_copy.sort
	
	#二乗平均を計算する際に使用
	double_average = absolute = 0
	
	#各データに対応する名前
	list_name = ["データ数: ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ",
	 "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]
	
	#格納作業
	for i in range(len(list_copy)): 
		double_average += list_copy[i] ** 2
		absolute += abs(list_copy[i] - np.mean(list_copy))

	#最頻値を計算
	mode = Counter(list_copy).most_common(1)
	data.extend([len(list_copy), round(np.mean(list_copy), 4), np.median(list_copy), 
		mode[0][0], max(list_copy), min(list_copy), max(list_copy) - min(list_copy), 
		round(double_average / len(list_copy), 4), round(absolute / len(list_copy), 4), round(np.var(list_copy), 4), 
		round(np.std(list_copy), 4)])

	#print作業
	print("")
	for i in range(len(list_name)):
		print(list_name[i], data[i])
	print("")


#こっちは統計の勉強用に作成したもので、numpyの関数は使っていません。ほんとは少しだけ使いました
def doubleStatus(x, y):
	#flag
	flag = 0
	#値渡し回避
	list_copy1 = copy.copy(x)
	list_copy2 = copy.copy(y)

	#二つのリストの長さが異なった場合、ERROR文
	if len(list_copy1) != len(list_copy2):
		print("ERROR: リストの長さが異なります。")

	#必要なものを宣言。
	list_name = ["データ数: ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ", "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]
	list_multiplied = absolute1 = absolute2 = list_double1 = list_double2 = 0
	data1 = []
	data2 = []

	#共分散を計算するために使用。リストソート前に計算する必要あり。
	for i in range(len(list_copy1)):
		list_multiplied += list_copy1[i] * list_copy2[i]

	#二つのデータを昇順ソート。
	list_copy1.sort()
	list_copy2.sort()

	#平均を計算
	average1 = sum(list_copy1) / len(list_copy1)
	average2 = sum(list_copy2) / len(list_copy2)

	#最大値を計算
	max1 = list_copy1[len(list_copy1) - 1]
	max2 = list_copy2[len(list_copy2) - 1]

	#最小値を計算
	min1 = list_copy1[0]
	min2 = list_copy2[0]

	#範囲（レンジ）を計算		
	renge1 = max1 - min1
	renge2 = max2 - min2

	for i in range(len(list_copy1)):
	#平均偏差を計算するためにi番目の要素から要素の平均を減算し、その絶対値を取り、すべてを加算する
		absolute1 += abs(list_copy1[i] - average1)
		absolute2 += abs(list_copy2[i] - average2)

	#二乗平均を計算するためにi番目の要素を二乗し、すべてを加算する
		list_double1 += list_copy1[i] ** 2	
		list_double2 += list_copy2[i] ** 2	

	#平均偏差を計算
	average_deviation1 = absolute1 / len(list_copy1)
	average_deviation2 = absolute2 / len(list_copy2)

	#二乗平均を計算
	double_average1 = list_double1 / len(list_copy1)
	double_average2 = list_double2 / len(list_copy2)

	#中央値を計算
	if len(list_copy1) % 2 == 0:
		median1 = (list_copy1[int(np.floor(len(list_copy1) / 2))] + list_copy1[int(np.floor(len(list_copy1) / 2 -1))]) / 2
		median2 = (list_copy2[int(np.floor(len(list_copy2) / 2))] + list_copy2[int(np.floor(len(list_copy2) / 2 -1))]) / 2
	elif len(list_copy1) % 2 == 1:
		median1 = list_copy1[int(np.floor(len(list_copy1) / 2))]
		median2 = list_copy2[int(np.floor(len(list_copy2) / 2))]

	#最頻値を計算。
	mode1 = Counter(list_copy1).most_common(1)
	mode2 = Counter(list_copy2).most_common(1)

	#分散を計算　二乗平均 - 平均**2
	variance1 = double_average1 - (average1 ** 2)
	variance2 = double_average2 - (average2 ** 2)

	#標準偏差を計算
	standard_deviation1 = np.sqrt(variance1)
	standard_deviation2 = np.sqrt(variance2)

	#共分散を計算 積のデータ/データ数 - xの平均 * yの平均
	covariance = (list_multiplied / len(list_copy1)) - (average1 * average2) 

	#相関係数を計算。0だった場合、Error出力
	if standard_deviation1 == 0 or standard_deviation2 == 0:
		err = "ERROR: 0のため相関係数を計算できません。"
		flag = 1
	else:
		#相関係数を計算
		correlation_coefficient = covariance / standard_deviation1 / standard_deviation2
		
		#回帰係数を計算
		a = covariance / variance1
		b = average2 - (a * average1)


	#すべての結果をリストに追加
	data1.extend([len(list_copy1), round(average1, 4), median1, mode1[0][0], 
		max1, min1, renge1, round(double_average1, 4), round(average_deviation1, 4), round(variance1, 4), round(standard_deviation1, 4)])

	data2.extend([len(list_copy2), round(average2, 4), median2, mode2[0][0], 
		max2, min2, renge2, round(double_average2, 4), round(average_deviation2, 4), round(variance2, 4), round(standard_deviation2, 4)])

	#結果を出力。
	print("\ndate 1\n")
	for i in range(len(data1)):
		print(list_name[i], data1[i])

	print("\ndate 2\n")
	for i in range(len(data2)):
		print(list_name[i], data2[i])

	print("\n\n共分散:   ", round(covariance, 4))
	if flag != 0:
		print(err)
	else:
		print("相関係数: ", round(correlation_coefficient, 4))
		print("回帰係数: y = ax + bとするとき、\n a = ", round(a, 4), ", b = ", round(b, 4),"\n")


#main tlibについての説明
if __name__ == '__main__':
	first()