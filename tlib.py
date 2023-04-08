'''
統計ライブラリtlib
作成者：K.Hayashi
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import math
import random as rd
from collections import Counter
from fractions import Fraction

def first():
	print("tlibへようこそ。\nインポートする際に時間がかかります。\n\nインポート方法\nimport tlib\n\n関数使用方法\ntlib.関数名\n")

#helps
def help():
	list_function = ["1: primeNum()",
		"2: sort()",
		"3: unSort()",
		"4: singleHist()",
		"5: doubleHist()",
		"6: plot()",
		"7: singleSt()",
		"8: doubleSt()",
		"9: desData()",
		"10: table()",
		"11: diceAllPat()",
		"12: doubleDiceSum()",
		"13: doubleDiceMult()",
		"14: fraction()",
		"15: leven()",
		"16: collatz()",
		"17: monte()"]

	list_info = {1:"primeNum(整数): 指定された整数までのすべての素数を表示し、素数の数を表示。", 
		2:"sort(リスト): 指定されたリストを昇順に並べ替え。", 
		3:"unSort(リスト): 指定されたリストを降順に並べ替え。", 
		4:"singleHist(リスト): 指定されたリストのヒストグラムを表示。",
		5:"doubleHist(リスト1,リスト2): 指定された二つのリストのヒストグラムを表示。",
		6:"plot(リスト1, リスト2): 指定された二つのリストの散布図をプロット。", 
		7:"singleSt(リスト): 指定されたリストの要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示。",
		8:"doubleSt(リスト1, リスト2): 指定された二つのリストの要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示し、二つのリストの共分散、相関係数、回帰係数を表示。",
		9:"desData(リスト): 指定されたリストのデータ数(count)、平均(mean)、標準偏差(std)、最小値(min)、第一四分位点(25%)、第二四分位点(50%)、第三四分位点(75%)、最大値(max)、データ型(dtype)を出力。",
		10:"table(リスト): 指定されたリストの度数分布表を表示。左側に階級値、右側に頻度。",
		11:"diceAllPat(): 二つのさいころの全パターンを表示。",
		12:"doubleDiceSum(): 二つのさいころの目を足したものを度数分布表に表示。左側に階級値、右側に頻度。",
		13:"doubleDiceMult(): 二つのさいころの目を掛けたものを度数分布表に表示。左側に階級値、右側に頻度。",
		14:"fraction(整数1,整数2): 整数1/整数2を既約分数で表示。",
		15:"leven(文字列1,文字列2): 文字列1と文字列2のレーヴェンシュタイン距離を求める。",
		16:"collatz(整数): 指定された整数をコラッツ予想の法則に則って計算する。",
		17:"monte(整数): 指定された整数個の点を用いてモンテカルロ法から円周率の近似値を求める。"}
	
	while 1:
		print("表示したいHelpの番号を選択してください。0を入力で終了")
		for i in range(len(list_function)):
			print(list_function[i])
		listNum = int(input())
		if listNum > len(list_function) or listNum < 0: 
			print("\nError: 1 から", len(list_function), "までの数字で入力してください。\n")
			break
		if listNum == 0: break
		print("\n",list_info[listNum], "\n")
		break

#素数関連　エラトステネスの篩を用いた素数洗い出し
def primeNum(num):
	if type(num) is not int:
		print("ERROR 整数を入力してください。")
	else:
		#素数を格納するためのリスト	
		list_prime = []
		#2から入力された値までのすべての数を格納
		list_num = [i for i in range(2,num + 1)]

		#list_numの0番目が入力された値の平方根以下になるまでloop
		while list_num[0] <= int(np.sqrt(num)):
			#list_primeにlist_numの0番目を追加
			list_prime.append(list_num[0]) 
			#headにlist_numの0番目を格納
			head = list_num[0] 
			#素数判定
			list_num = [i for i in list_num if i % head != 0]

		#list_numに残った数を素数としてlist_primeに格納
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
def unSort(list):
	list_srt = copy.copy(list)
	print(np.sort(list_srt)[::-1])

#データ数が多い場合使用するとよい
def desData(list):
	print(pd.Series(list).describe())

#度数分布表を表示
def table(list):
	print(pd.Series(list).value_counts())

#ヒストグラムを表示
def singleHist(list):
	plt.hist(list)
	plt.show()

#ヒストグラムを二つ表示
def doubleHist(list_1,list_2):	
	plt.subplot(2, 2, 1)
	plt.hist(list_1)
	plt.title("List_1")
	plt.subplot(2, 2, 4)
	plt.hist(list_2)
	plt.title("List_2")
	plt.show()

#散布図を描画。値渡しは回避済み
def plot(list_1, list_2):	
	plt.scatter(list_1, list_2)
	plt.xlabel("List_1")
	plt.ylabel("List_2")
	plt.show()

#さいころ全パターン
def diceAllPat():
	for i in range(1, 7):
		for j in range(1, 7):
			print(i, "+", j, "= ", i+j)
			if j == 6: print("")

#足し算パターン
def doubleDiceSum():
	dice = []
	for i in range(1, 7):
		for j in range(1, 7):
			dice.append(i + j)
	print(pd.Series(dice).value_counts(sort=False))

#掛け算パターン
def doubleDiceMult():
	dice = []
	for i in range(1, 7):
		for j in range(1, 7):
			dice.append(i * j)
	print(pd.Series(dice).value_counts(sort=False))

#既約分数を表示
def fraction(num_1, num_2):
	if (type(num_1) is not int) or (type(num_2) is not int):
		print("ERROR 整数を入力してください。")
	else:
		print(Fraction(num_1, num_2))


#レーヴェンシュタイン距離を求める
def leven(str_1,str_2):
	list_num = [0]*3
	list_str_1 = list(map(str, str_1))
	list_str_2 = list(map(str, str_2))
	list_str_1.insert(0, "$")
	list_str_2.insert(0, "$")

	#表で出力するため一文字ずつleven_listに格納
	leven_list =[[i for i in range(len(list_str_1))] for j in range(len(list_str_2))]
	for i in range(len(list_str_2)): 
		leven_list[i][0] = i

	#以下計算するところ。どういう計算するかはWikipediaまで
	for y in range(len(list_str_2) - 1):
		for x in range(len(list_str_1) - 1):
			list_num[0] = leven_list[y + 1][x] + 1
			list_num[1] = leven_list[y][x + 1] + 1
			if str_2[y] == str_1[x]: 
				list_num[2] = leven_list[y][x]
			else: 
				list_num[2] = leven_list[y][x] + 1
			leven_list[y + 1][x + 1] = min(list_num)

	leven_data = pd.DataFrame(data=leven_list,columns=list_str_1,index=list_str_2)
	print(leven_data,"\n\n","距離: ",leven_list[len(list_str_2)-1][len(list_str_1) - 1])

#各データに対応する名前
LIST_NAME = ["データ数: ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ",
 "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]

#コラッツ予想
def collatz(num):
	#1になるまでの施行回数を表示
	flag = 0
	#数式用
	backNumber = 0
	if type(num) is not int:
		print("ERROR 整数を入力してください。")
	else:
		while 1:
			#numが1になるまで以下の操作を繰り返す。1になった場合breakする
			if num == 1: 
				break
			#式を表示するためにひとつ前のnumを格納
			backNumber = num
			#numが奇数だった場合
			if num % 2 == 1:
				#numを3倍し1を足す
				num = num * 3 + 1
				#数式を表示			
				print(int(backNumber), "× 3 + 1 =",int(num))

			#numが偶数だった場合
			if num % 2 == 0:	
				#numを2で割る
				num = num / 2
				#数式を表示			
				print(int(backNumber), "÷ 2 =",int(num))
			#試行回数カウント
			flag += 1

		#試行回数を表示
		print("\n試行回数: ", flag)

def monte(num):
	x = 0 #x軸
	y = 0 #y軸
	pai = 0 #実際に求めた円周率を格納
	a = 0 #
	i = 0
	if type(num) is not int:
		print("ERROR 整数を入力してください。")
	else:
		while i < num:
			x = rd.uniform(-1, 1) #-1から1までの小数点乱数を生成
			y = rd.uniform(-1, 1) #xと同じ操作
			if x**2 + y**2 <= 1: #円の公式より中心点から1以下の場合以下の処理を行う
				a += 1
				plt.scatter(x, y, color = "blue") #1以下だった場合、円の中と判定し青点を打つ
			else:
				plt.scatter(x, y, color = "red") #1以上だった場合、円の外と判定し赤点を打つ
			i += 1 #num回繰り返す
		pai = 4 * a / num #PI = 4 * a / (a + b)より
		print("点の合計数: ", num, "\n実際に求めた円周率: ", pai) #実際に求めた円周率を表示
		plt.xlim(-1, 1) #綺麗な円を描くためにグラフの表示範囲を変更
		plt.ylim(-1, 1)
		plt.axis('square') #グラフの形を正方形に変更
		plt.show() #グラフ表示
		
#関数をたたきまくった代物
def singleSt(list):
	#値渡し回避
	list_copy = copy.copy(list)
	data = []
	
	#リストをソート
	list_copy.sort
	
	#二乗平均を計算する際に使用
	double_average = absolute = 0
	
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
	for i in range(len(LIST_NAME)):
		print(LIST_NAME[i], data[i])
	print("")


#こっちは統計の勉強用に作成したもので、numpyの関数は使っていません。ほんとは少しだけ使いました
def doubleSt(x, y):
	#flag
	flag = 0
	#値渡し回避
	list_copy_1 = copy.copy(x)
	list_copy_2 = copy.copy(y)

	#二つのリストの長さが異なった場合、ERROR文
	if len(list_copy_1) != len(list_copy_2):
		print("ERROR: リストの長さが異なります。")

	#必要なものを宣言
	list_multiplied = absolute_1 = absolute_2 = list_double_1 = list_double_2 = 0
	data_1 = []
	data_2 = []

	#共分散を計算するために使用。リストソート前に計算する必要あり。
	for i in range(len(list_copy_1)):
		list_multiplied += list_copy_1[i] * list_copy_2[i]

	#二つのデータを昇順ソート。
	list_copy_1.sort()
	list_copy_2.sort()

	#平均を計算
	average_1 = sum(list_copy_1) / len(list_copy_1)
	average_2 = sum(list_copy_2) / len(list_copy_2)

	#最大値を計算
	max_1 = list_copy_1[len(list_copy_1) - 1]
	max_2 = list_copy_2[len(list_copy_2) - 1]

	#最小値を計算
	min_1 = list_copy_1[0]
	min_2 = list_copy_2[0]

	#範囲（レンジ）を計算		
	renge_1 = max_1 - min_1
	renge_2 = max_2 - min_2

	for i in range(len(list_copy_1)):
	#平均偏差を計算するためにi番目の要素から要素の平均を減算し、その絶対値を取り、すべてを加算する
		absolute_1 += abs(list_copy_1[i] - average_1)
		absolute_2 += abs(list_copy_2[i] - average_2)

	#二乗平均を計算するためにi番目の要素を二乗し、すべてを加算する
		list_double_1 += list_copy_1[i] ** 2	
		list_double_2 += list_copy_2[i] ** 2	

	#平均偏差を計算
	average_deviation_1 = absolute_1 / len(list_copy_1)
	average_deviation_2 = absolute_2 / len(list_copy_2)

	#二乗平均を計算
	double_average_1 = list_double_1 / len(list_copy_1)
	double_average_2 = list_double_2 / len(list_copy_2)

	#中央値を計算
	if len(list_copy_1) % 2 == 0:
		median_1 = (list_copy_1[int(np.floor(len(list_copy_1) / 2))] + list_copy_1[int(np.floor(len(list_copy_1) / 2 -1))]) / 2
		median_2 = (list_copy_2[int(np.floor(len(list_copy_2) / 2))] + list_copy_2[int(np.floor(len(list_copy_2) / 2 -1))]) / 2
	elif len(list_copy_1) % 2 == 1:
		median_1 = list_copy_1[int(np.floor(len(list_copy_1) / 2))]
		median_2 = list_copy_2[int(np.floor(len(list_copy_2) / 2))]

	#最頻値を計算。
	mode_1 = Counter(list_copy_1).most_common(1)
	mode_2 = Counter(list_copy_2).most_common(1)

	#分散を計算　二乗平均 - 平均**2
	variance_1 = double_average_1 - (average_1 ** 2)
	variance_2 = double_average_2 - (average_2 ** 2)

	#標準偏差を計算
	standard_deviation_1 = np.sqrt(variance_1)
	standard_deviation_2 = np.sqrt(variance_2)

	#共分散を計算 積のデータ/データ数 - xの平均 * yの平均
	covariance = (list_multiplied / len(list_copy_1)) - (average_1 * average_2) 

	#相関係数を計算。0だった場合、Error出力
	if standard_deviation_1 == 0 or standard_deviation_2 == 0:
		err = "ERROR: 0のため相関係数を計算できません。"
		flag = 1
	else:
		#相関係数を計算
		correlation_coefficient = covariance / standard_deviation_1 / standard_deviation_2
		
		#回帰係数を計算
		a = covariance / variance_1
		b = average_2 - (a * average_1)


	#すべての結果をリストに追加
	data_1.extend([len(list_copy_1), round(average_1, 4), median_1, mode_1[0][0], 
		max_1, min_1, renge_1, round(double_average_1, 4), round(average_deviation_1, 4), round(variance_1, 4), round(standard_deviation_1, 4)])

	data_2.extend([len(list_copy_2), round(average_2, 4), median_2, mode_2[0][0], 
		max_2, min_2, renge_2, round(double_average_2, 4), round(average_deviation_2, 4), round(variance_2, 4), round(standard_deviation_2, 4)])

	#結果を出力。
	print("\ndate_1\n")
	for i in range(len(data_1)):
		print(LIST_NAME[i], data_1[i])

	print("\ndate_2\n")
	for i in range(len(data_2)):
		print(LIST_NAME[i], data_2[i])

	print("\n\n共分散:   ", round(covariance, 4))
	if flag != 0:
		print(err)
	else:
		print("相関係数: ", round(correlation_coefficient, 4))
		print("回帰係数: y = ax + bとするとき、\n a = ", round(a, 4), ", b = ", round(b, 4))


#main tlibについての説明
if __name__ == '__main__':
	first()