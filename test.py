import pandas as pd
def levenshtein(x,y):
	num = [0,0,0]
	xli = ["$"]
	yli = ["$"]

	for i in x:
		xli.append(i)
	for j in y:
		yli.append(j)

	li = [[0 for i in range(len(xli))] for j in range(len(yli))]

	for i in range(len(xli)):
		li[0][i] = i
	for j in range(len(yli)):
		li[j][0] = j

	for i in range(len(xli) - 1):
		for j in range(len(yli) - 1):
			num[0] = li[i+1][j] + 1
			num[1] = li[i][j+1] + 1
			if xli[i+1] == xli[j+1]:
				num[2] = li[i][j]
			else:
				num[2] = li[i][j] + 1
			li[i+1][y+1] = min(num)
			num = [0,0,0]



	unchi = pd.DataFrame(li)
	unchi.columns = xli
	unchi.index = yli
	print(unchi)

if __name__ == '__main__':
	levenshtein("ApexLegends","LeagueOfLegends")