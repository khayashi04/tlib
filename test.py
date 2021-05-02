'''import numpy as np
import copy
from collections import Counter
def singleStatus(list):
	single_list = copy.copy(list)
	result = []
	#リストをソート
	single_list.sort
	#二乗平均を計算する際に使用
	doubleAve = doubleSqr = 0

	name = ["要素数:   ","平均:     ", "中央値:   ", "最頻値:   ", "最大値:   ", "最小値:   ",
	 "範囲:     ", "二乗平均: ", "平均偏差: ", "分散:     ", "標準偏差: "]
	#格納作業
	for i in range(len(single_list)): 
		doubleAve += single_list[i] ** 2 
		doubleSqr += abs(single_list[i] - np.mean(single_list))
	#最頻値を計算
	mode = Counter(single_list).most_common(1)
	result.extend([len(single_list), round(np.mean(single_list), 4), np.median(single_list), 
		mode[0][0], max(single_list), min(single_list), max(single_list) - min(single_list), 
		round(doubleAve / len(single_list), 4), round(doubleSqr / len(single_list), 4), round(np.var(single_list), 4), 
		round(np.std(single_list), 4)])

	#print作業
	print("")
	for i in range(len(name)):
		print(name[i], result[i])
	print("")
'''
import tlib as t
if __name__ == '__main__':
	t.singleStatus([1,5,15,12,5,321,4513,532,35,15,51,2,51,5,15,1,5,15,51,2])