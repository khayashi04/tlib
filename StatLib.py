import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import math
import random as rd
from collections import Counter
from fractions import Fraction

class StatLib:

    #コンストラクター
    def __init__(self): 
        self.num_1 = 0
        self.num_2 = 0
    
    #値一つ用のset関数
    def setSingle(self, num_1):
        self.num_1 = num_1
    
    #値二つ用のset関数
    def setDouble(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    
    #エラトステネスの篩を用いた素数洗い出し
    def primeNum(self) -> list:
        if type(self.num_1) is not int: return "ERROR" #値が整数以外ならERRORを返す
        else:
            list_prime = [] #素数を格納するためのリスト
            list_num = [i for i in range(2, self.num_1 + 1)] #2から入力らされた値までの全ての数を格納
            
            #list_numの0番目が入力された値の平方根以下になるまでloop
            while list_num[0] <= int(np.sqrt(self.num_1)):
                list_prime.append(list_num[0]) #list_primeにlist_numの0番目を追加
                head = list_num[0] #headにlist_numの0番目を追加
                list_num = [i for i in list_num if i % head != 0] #素数判定
            
            list_prime.extend(list_num) #list_numに残った数を素数としてlist_primeに格納
            #list_prime_strに導かれた素数すべてを格納
            list_prime_str = [str(a) for a in list_prime] 
            list_prime_str = ', '.join(list_prime_str) 
            #素数の数とlist_prime_strをreturn
            return len(list_prime), list_prime_str

    #昇順リストソート
    def sort(self) -> list:
        list_str = copy.copy(self.num_1)
        return np.sort(list_str)
    
    #降順リストソート
    def unSort(self) -> list:
        list_str = copy.copy(self.num_1)
        return np.sort(list_str)[::-1]
    
    #与えられたデータを分析する。データ数が多い場合に使用するとよい
    def desData(self) -> list:
        #return [count, mean, std, min, 25%, 50%, 75%, max]
        return pd.Series(self.num_1).describe()

    #度数分布表を表示
    def table(self) -> list:
        return pd.Series(self.num_1).value_counts()

    #ヒストグラムを表示
    def singleHist(self):
        plt.hist(self.num_1)
        plt.show()
    
    #ヒストグラムを二つ表示
    def doubleHist(self):
        plt.subplot(2, 2, 1)
        plt.hist(self.num_1)
        plt.title("Data_1")
        plt.subplot(2, 2, 4)
        plt.hist(self.num_2)
        plt.title("Data_2")
        plt.show()
    
    #散布図を表示
    def scat(self):
        plt.scatter(self.num_1, self.num_2)
        plt.xlabel("Data_1")
        plt.ylabel("Data_2")
        plt.show()
    
    #既約分数を表示
    def fraction(self):
        if(type(self.num_1) is not int) or (type(self.num_2) is not int): return 0 #num_1かnum_2が整数ではない場合0をreturn
        else:
            return Fraction(self.num_1, self.num_2)

    #編集距離を求める
    def leven(self) -> list:
        str_1 = self.num_1
        str_2 = self.num_2
        if(type(str_1) is not str) or (type(str_2) is not str): 
            return 0
        list_num = [0] * 3
        list_str_1 = list(map(str, str_1))
        list_str_2 = list(map(str, str_2))
        list_str_1.insert(0, "$")
        list_str_2.insert(0, "$")

        #表を出力するためにlist_levenに格納
        list_leven = [[i for i in range(len(list_str_1))] for j in range(len(list_str_2))]
        for i in range(len(list_str_2)):
            list_leven[i][0] = i
        
        #以下計算。詳しくはWikipedia
        for y in range(len(list_str_2) - 1):
            for x in range(len(list_str_1) - 1):
                list_num[0] = list_leven[y + 1][x] + 1
                list_num[1] = list_leven[y][x + 1] + 1
                if str_2[y] == str_1[x]: list_num[2] = list_leven[y][x]
                else: list_num[2] = list_leven[y][x] + 1
                list_leven[y + 1][x + 1] = min(list_num)
        
        leven_data = pd.DataFrame(data = list_leven, columns = list_str_1, index = list_str_2)
        #結果をreturn 距離、表
        return list_leven[len(list_str_2)-1][len(list_str_1) - 1], leven_data

        #コラッツ予想
    def collatz(self) -> int:
        counter = 0 #1になるまでの試行回数
        num = self.num_1
        if type(num) is not int: return 0 #入力された値が整数ではなかった場合0をreturn
        else:
                #numが1になるまで以下の操作を繰り返す
            while 1 < num:
                if num % 2 == 1:
                    num = num * 3 + 1 #numが奇数の場合、numを3倍し1を足す
                if num % 2 == 0:
                    num = num / 2 #numが偶数の場合、numを2で割る
                counter += 1 #試行回数カウント
        #試行回数をreturn
        return counter

    def monte(self) -> tuple:
        x = 0 #x軸
        y = 0 #y軸
        pai = 0.0 #実際に求めた円周率の近似値を格納するための変数
        a = 0 #円の中に点が描画されたときにカウントを1する
        i = 0 #num回繰り返すための変数
        num = self.num_1
        if type(num) is not int: return 0
        else:
            while i < num:
                x = rd.uniform(-1, 1) #-1から1までのdouble型乱数を生成
                y = rd.uniform(-1, 1) #xと同じ操作
                if x**2 + y**2 <= 1:
                    a += 1
                    plt.scatter(x, y, color = "blue") #1以下だった場合、円の中と判定し青点を描画
                else:
                    plt.scatter(x, y, color = "red") #1以上だった場合、円の外と判定し赤点を描画
                i += 1 #num回繰り返す
            pai = 4 * a / num #円周率近似値を求めるための公式
            #点の合計と実際に求めた円周率の近似値をreturn
            return num, pai

