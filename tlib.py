'''
統計ライブラリtlib
作成者: K.Hayashi
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import math
import random as rd
from collections import Counter
from fractions import Fraction


# helps
def help_tlib():
    list_function = ["prime_num(num)",
                     "sort(list)",
                     "un_sort(list)",
                     "single_hist(list)",
                     "double_hist(list_1, list_2)",
                     "plot(list_1, list_2)",
                     "single_stat(list)",
                     "double_stat(list_1, list_2)",
                     "des_data(list)",
                     "table(list)",
                     "dice_all_pat()",
                     "double_dice_sum()",
                     "double_dice_mult()",
                     "fraction(num_1, num_2)",
                     "leven(str_1, str_2)",
                     "collatz(num)",
                     "monte_pi(num)",
                     "zeller(year, month, day)"]

    list_info = ["numまでのすべての素数を表示し、素数の数を表示。",
                 "listを昇順に並べ替え。",
                 "listを降順に並べ替え。",
                 "listのヒストグラムを表示。",
                 "list_1とlist_2のヒストグラムを表示。",
                 "list_1とlist_2の散布図をプロット。",
                 "listの要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示。",
                 "list_1とlist_2の要素数、平均、中央値、最頻値、最大値、最小値、範囲、二乗平均、平均偏差、分散、標準偏差を表示し、list_1とlist_2の共分散、相関係数、回帰係数を表示。",
                 "listのデータ数(count)、平均(mean)、標準偏差(std)、最小値(min)、第一四分位点(25%)、第二四分位点(50%)、第三四分位点(75%)、最大値(max)、データ型(dtype)を出力。",
                 "listの度数分布表を表示。左側に階級値、右側に頻度。",
                 "二つのさいころの全パターンを表示。",
                 "二つのさいころの目を足したものを度数分布表に表示。左側に階級値、右側に頻度。",
                 "二つのさいころの目を掛けたものを度数分布表に表示。左側に階級値、右側に頻度。",
                 "num_1 / num_2を既約分数で表示。",
                 "str_1とstr_2のレーヴェンシュタイン距離を求める。",
                 "numをコラッツ予想の法則に則って計算する。",
                 "num個の点を用いてモンテカルロ法から円周率の近似値を求める。",
                 "year/month/dayから曜日、閏年、昭和、平成、令和の元号を求める。"]

    if len(list_function) != len(list_info):
        raise Exception("\nError: 開発者はバカ")
    list_range = len(list_function)
    print(f"1 から {list_range} の表示したいHelpの番号を挿入してください。")
    for i in range(list_range):
        print(f"{i + 1}: {list_function[i]}")
    list_num = int(input()) - 1
    if type(list_num) != int or list_num > list_range or list_num <= 0:
        raise Exception(f"\nError: 1 から{list_range}までの数字で挿入してください。\n")
    print(
        f"\n{list_num + 1}: {list_function[list_num]}: {list_info[list_num]}\n")


# エラトステネスの篩を用いた素数洗い出し
def prime_num(num):
    # numが2以上の自然数の場合Error
    if type(num) != int or num <= 1:
        raise Exception("\nError: 2以上の自然数を挿入してください")

    list_prime = []  # 素数を格納するためのリスト

    # 2から入力された値までのすべての数を格納
    list_num = [i for i in range(2, num + 1)]

    # list_numの0番目が入力された値の平方根以下になるまでloop
    while list_num[0] <= int(np.sqrt(num)):
        # list_primeにlist_numの0番目を追加
        list_prime.append(list_num[0])

        # headにlist_numの0番目を格納
        list_head = list_num[0]

        # 素数判定
        list_num = [i for i in list_num if i % list_head != 0]

    # list_numに残った数を素数としてlist_primeに格納
    list_prime.extend(list_num)

    # 結果を表示
    list_prime_str = [str(a) for a in list_prime]
    list_prime_str = ' '.join(list_prime_str)
    print(f"{list_prime_str}\n素数の合計: {len(list_prime)}\n")


# リストソート(昇順)
def list_sort(list_1):
    list_srt = copy.copy(list_1)
    print(np.sort(list_srt))


# リストソート(降順)
def list_unsort(list_1):
    list_srt = copy.copy(list_1)
    print(np.sort(list_srt)[::-1])


# データ数が多い場合使用するとよい
def des_data(list_1):
    print(pd.Series(list_1).describe())


# 度数分布表を表示
def table(list_1):
    print(pd.Series(list_1).value_counts())


# ヒストグラムを表示
def single_hist(list_1):
    plt.hist(list_1)
    plt.show()


# ヒストグラムを二つ表示
def double_hist(list_1, list_2):
    plt.subplot(2, 2, 1)
    plt.hist(list_1)
    plt.title("List_1")
    plt.subplot(2, 2, 4)
    plt.hist(list_2)
    plt.title("List_2")
    plt.show()


# 散布図を描画。値渡しは回避済み
def plot(list_1, list_2):
    # list_1とlist_2のサイズが異なる場合Exception
    if len(list_1) != len(list_2):
        raise Exception("\nError: list_1とlist_2のサイズが異なります。等しくしてください")

    plt.scatter(list_1, list_2)
    plt.xlabel("List_1")
    plt.ylabel("List_2")
    plt.show()


# さいころ全パターン
def dice_all_pat():
    for i in range(1, 7):
        for j in range(1, 7):
            print(f"{i} + {j} = {i+j}")
            if j == 6:
                print("")


# 足し算パターン
def double_dice_sum():
    dice = []
    for i in range(1, 7):
        for j in range(1, 7):
            dice.append(i + j)
    print(pd.Series(dice).value_counts(sort=False))


# 掛け算パターン
def double_dice_mult():
    dice = []
    for i in range(1, 7):
        for j in range(1, 7):
            dice.append(i * j)
    print(pd.Series(dice).value_counts(sort=False))


# 既約分数を表示
def fraction(num_1, num_2):
    # 0で割ろうとした場合Exception
    if num_2 == 0:
        raise Exception("\nError: 0で割ることはできません。")

    print(Fraction(num_1, num_2))


# レーヴェンシュタイン距離を求める
def leven(str_1, str_2):
    # str_1かstr_2がstr型以外の場合exit
    if type(str_1) != str or type(str_2) != str:
        raise Exception("\nError: str型の値を挿入してください。")

    list_num = [0]*3
    list_str_1 = list(map(str, str_1))
    list_str_2 = list(map(str, str_2))
    list_str_1.insert(0, "$")
    list_str_2.insert(0, "$")

    # 表で出力するため一文字ずつleven_listに格納
    leven_list = [[i for i in range(len(list_str_1))]
                  for j in range(len(list_str_2))]
    for i in range(len(list_str_2)):
        leven_list[i][0] = i

    # 以下計算するところ。どういう計算するかはWikipediaまで
    for y in range(len(list_str_2) - 1):
        for x in range(len(list_str_1) - 1):
            list_num[0] = leven_list[y + 1][x] + 1
            list_num[1] = leven_list[y][x + 1] + 1
            if str_2[y] == str_1[x]:
                list_num[2] = leven_list[y][x]
            else:
                list_num[2] = leven_list[y][x] + 1
            leven_list[y + 1][x + 1] = min(list_num)

    # 結果を表示
    leven_data = pd.DataFrame(
        data=leven_list, columns=list_str_1, index=list_str_2)
    print(
        f"{leven_data}\n\n距離: {leven_list[len(list_str_2)-1][len(list_str_1) - 1]}")


# コラッツ予想
def collatz(collatz_num):
    # collatz_numが1以上の自然数以外の場合exit
    if type(collatz_num) != int or collatz_num == 0:
        raise Exception("\nError: 1以上の自然数を挿入してください。")

    collatz_counter = 0  # 1になるまでの施行回数を表示
    back_collatz_num = 0  # ひとつ前の数字を格納

    while 1:
        # collatz_numが1になるまで以下の操作を繰り返す。1になった場合breakする
        if collatz_num == 1:
            break

        # 式を表示するためにひとつ前のnumを格納
        back_collatz_num = collatz_num

        # numが奇数だった場合
        if collatz_num % 2 == 1:
            # numを3倍し1を足す
            collatz_num = collatz_num * 3 + 1

            # 数式を表示
            print(f"{int(back_collatz_num)} ｘ 3 + 1 = {int(collatz_num)}")

        # numが偶数だった場合
        if collatz_num % 2 == 0:
            # numを2で割る
            collatz_num = collatz_num / 2

            # 数式を表示
            print(f"{int(back_collatz_num)} ÷ 2 = {int(collatz_num)}")

        # 試行回数カウント
        collatz_counter += 1

    # 試行回数を表示
    print(f"\n試行回数: {collatz_counter}")


# モンテカルロ法を用いて円周率の近似値を求める
def monte_pi(all_point):
    # all_pointが1以上の自然数以外の場合exit
    if type(all_point) != int or all_point <= 0:
        raise Exception("\nError: 1以上の自然数を挿入してください")

    x = 0  # x軸
    y = 0  # y軸
    pai = 0  # 実際に求めた円周率の近似値を格納
    in_circle_point = 0  # 円の中に描画された点
    point_counter = 0  # カウンター

    # point_counterがall_pointを超えたら終了
    while point_counter < all_point:
        # xとyに-1から1までの小数点乱数を生成し、格納
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)

        # 円の公式より中心点から1以下の場合以下の処理を行う
        if x**2 + y**2 <= 1:
            in_circle_point += 1

            # 1以下だった場合、円の中と判定し青点を打つ
            plt.scatter(x, y, color="blue")
        else:
            # 1以上だった場合、円の外と判定し赤点を打つ
            plt.scatter(x, y, color="red")

        # カウンターにプラス1
        point_counter += 1

    # 円周率を円の中に入った点と全ての点を用いて計算
    pai = 4 * in_circle_point / all_point

    # 実際に求めた円周率を表示
    print(f"点の合計数: {all_point}\n実際に求めた円周率: {pai}")

    # 綺麗な円を描くためにグラフの表示範囲を変更
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # グラフの形を正方形に変更
    plt.axis('square')
    plt.show()


# ツェラーの公式を用いて西暦何月何日から曜日を求め、閏年か否かを表示する。
def zeller(year, month, day):
    # 返り値に対応した曜日を格納したリスト
    week = ["土", "日", "月",
            "火", "水", "木", "金"]

    # 閏年判定
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = "閏年です。"
        flag = 1
    else:
        leap_year = "閏年ではありません。"
        flag = 0

    # グレゴリオ暦が始まった1582年10月14以前の場合、日にちが正しくない場合Error
    if year * 10000 + month * 100 + day * 1 < 15821015:
        raise Exception("\nError: 1582年10月15日以降の日にちを挿入してください。")
    elif (month > 12 or month < 1 or day > 31 or day < 1) or \
            ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30) or \
            ((month == 2) and ((flag == 1 and day > 29) or (flag == 0 and day > 28))):
        raise Exception("\nError: 正しく日にちを挿入してください。")

    # ツェラーの公式を用いる際、1月と2月は前年の13月、14月として扱う
    year_j_f = year
    month_j_f = month

    if month < 3:
        year_j_f -= 1
        month_j_f += 12

    # big_c: 西暦上2桁, big_y: 西暦下2桁
    big_c = int(year_j_f / 100)
    big_y = year_j_f % 100

    # ツェラーの公式
    day_week = (day + int(26 * (month_j_f + 1) / 10) + big_y +
                int(big_y / 4) - 2 * big_c + int(big_c / 4)) % 7

    print(
        f"{year}年{month:02}月{day:02}日は{week[day_week]}曜日です。{leap_year}\n昭和{year - 1925}年, 平成{year - 1988}年, 令和{year - 2018}年")


# single_statとdouble_statで使用するリスト
LIST_NAME = ["データ数:　",
             "平均:　　　",
             "中央値:　　",
             "最頻値:　　",
             "最大値:　　",
             "最小値:　　",
             "範囲:　　　",
             "二乗平均:　",
             "平均偏差:　",
             "分散:　　　",
             "標準偏差:　"]


# 関数をたたきまくった代物
def single_stat(list_1):
    # 値渡し回避
    list_copy = copy.copy(list_1)
    list_data = []

    # リストをソート
    list_copy.sort

    # リストのサイズを格納
    list_range = len(list_copy)

    # 二乗平均を計算する際に使用
    double_average = 0
    absolute = 0

    # 格納作業
    for i in range(list_range):
        double_average += list_copy[i] ** 2
        absolute += abs(list_copy[i] - np.mean(list_copy))

    # 最頻値を計算
    mode = Counter(list_copy).most_common(1)

    # 結果をlist_dataに格納
    list_data.extend([list_range,
                      round(np.mean(list_copy), 4),
                      np.median(list_copy),
                      mode[0][0],
                      max(list_copy),
                      min(list_copy),
                      max(list_copy) - min(list_copy),
                      round(double_average / list_range, 4),
                      round(absolute / list_range, 4),
                      round(np.var(list_copy), 4),
                      round(np.std(list_copy), 4)])

    # 結果を表示
    print("")
    for i in range(len(LIST_NAME)):
        print(f"{LIST_NAME[i]}{list_data[i]}")
    print("")


# こっちは統計の勉強用に作成したもので、numpyの関数は使っていません。ほんとは少しだけ使いました
def double_stat(list_1, list_2):
    # flag
    flag = 0

    # 値渡し回避
    list_copy_1 = copy.copy(list_1)
    list_copy_2 = copy.copy(list_2)

    # list_1とlist_2のサイズが異なった場合exit
    if len(list_copy_1) != len(list_copy_2):
        print("\nError: list_1とlist_2のサイズが異なります。等しくしてください")

    # listのサイズを格納
    list_range = len(list_copy_1)

    # 必要なものを宣言
    list_multiplied = 0
    absolute_1 = 0
    absolute_2 = 0
    double_1 = 0
    double_2 = 0
    list_data_1 = []
    list_data_2 = []

    # 共分散を計算するために使用。リストソート前に計算する必要あり。
    for i in range(list_range):
        list_multiplied += list_copy_1[i] * list_copy_2[i]

    # 二つのデータを昇順ソート。
    list_copy_1.sort()
    list_copy_2.sort()

    # 平均を計算
    average_1 = sum(list_copy_1) / list_range
    average_2 = sum(list_copy_2) / list_range

    # 最大値を計算
    max_1 = list_copy_1[list_range - 1]
    max_2 = list_copy_2[list_range - 1]

    # 最小値を計算
    min_1 = list_copy_1[0]
    min_2 = list_copy_2[0]

    # 範囲（レンジ）を計算
    renge_1 = max_1 - min_1
    renge_2 = max_2 - min_2

    for i in range(list_range):
        # 平均偏差を計算するためにi番目の要素から要素の平均を減算し、その絶対値を取り、すべてを加算する
        absolute_1 += abs(list_copy_1[i] - average_1)
        absolute_2 += abs(list_copy_2[i] - average_2)

    # 二乗平均を計算するためにi番目の要素を二乗し、すべてを加算する
        double_1 += list_copy_1[i] ** 2
        double_2 += list_copy_2[i] ** 2

    # 平均偏差を計算
    average_deviation_1 = absolute_1 / list_range
    average_deviation_2 = absolute_2 / list_range

    # 二乗平均を計算
    double_average_1 = double_1 / list_range
    double_average_2 = double_2 / list_range

    # 中央値を計算
    if list_range % 2 == 0:
        median_1 = (list_copy_1[int(np.floor(list_range / 2))] +
                    list_copy_1[int(np.floor(list_range / 2 - 1))]) / 2
        median_2 = (list_copy_2[int(np.floor(list_range) / 2)] +
                    list_copy_2[int(np.floor(list_range) / 2 - 1)]) / 2
    elif list_range % 2 == 1:
        median_1 = list_copy_1[int(np.floor(list_range / 2))]
        median_2 = list_copy_2[int(np.floor(list_range) / 2)]

    # 最頻値を計算。
    mode_1 = Counter(list_copy_1).most_common(1)
    mode_2 = Counter(list_copy_2).most_common(1)

    # 分散を計算　二乗平均 - 平均**2
    variance_1 = double_average_1 - (average_1 ** 2)
    variance_2 = double_average_2 - (average_2 ** 2)

    # 標準偏差を計算
    standard_deviation_1 = np.sqrt(variance_1)
    standard_deviation_2 = np.sqrt(variance_2)

    # 共分散を計算 積のデータ/データ数 - xの平均 * yの平均
    covariance = (list_multiplied / list_range) - (average_1 * average_2)

    # 相関係数を計算。0だった場合、Error出力
    if standard_deviation_1 == 0 or standard_deviation_2 == 0:
        err = "ERROR: 0のため相関係数を計算できません。"
        flag = 1
    else:
        # 相関係数を計算
        correlation_coefficient = \
            covariance / standard_deviation_1 / standard_deviation_2

        # 回帰係数を計算
        a = covariance / variance_1
        b = average_2 - (a * average_1)

    # すべての結果をリストに追加
    list_data_1.extend([list_range,
                        round(average_1, 4),
                        median_1,
                        mode_1[0][0],
                        max_1,
                        min_1,
                        renge_1,
                        round(double_average_1, 4),
                        round(average_deviation_1, 4),
                        round(variance_1, 4),
                        round(standard_deviation_1, 4)])

    list_data_2.extend([list_range,
                        round(average_2, 4),
                        median_2,
                        mode_2[0][0],
                        max_2,
                        min_2,
                        renge_2,
                        round(double_average_2, 4),
                        round(average_deviation_2, 4),
                        round(variance_2, 4),
                        round(standard_deviation_2, 4)])

    # 結果を出力。
    print("\ndate_1\n")
    for i in range(len(list_data_1)):
        print(f"{LIST_NAME[i]}{list_data_1[i]}")

    print("\ndate_2\n")
    for i in range(len(list_data_2)):
        print(f"{LIST_NAME[i]}{list_data_2[i]}")

    print(f"\n\n共分散:    {covariance:.4f}")

    if flag != 0:
        print(err)
    else:
        print(f"相関係数:  {correlation_coefficient:.4f}")
        print(f"回帰係数: y = ax + bとするとき、\na = {a:.4f}, b = {b:.4f}")


# Osananajimi is god
def osananajimi(osananajimi_is_the_best_heroine_in_every_story, fxxk_pottode_heroine):
    '''
    try:
        all_heroine == osananajimi
    except AllHeroineAreOsananajimiException:
        Me = happy
        all_heroine = win
    '''
    pass


# main tlibについての説明
if __name__ == '__main__':
    print("tlibへようこそ。\n適当に遊んでください。")
