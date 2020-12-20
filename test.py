import pandas as pd
import numpy as np
def levenshtein(x,y):
	num = [0]*3
	xli = list(map(str,x))
	yli = list(map(str,y))
	xli.insert(0,"$")
	yli.insert(0,"$")
	print(xli,yli)

	#li = [[0]*len(xli)]*len(yli)
	li =[[0 for i in range(len(xli))] for j in range(len(yli))]

	for i in range(len(xli)): 
		li[0][i] = i
		print(li)
	for j in range(len(yli)): 
		li[j][0] = j
		print(li)

	for yy in range(len(yli) - 1):
		for xx in range(len(xli) - 1):
			num[0] = li[yy+1][xx] + 1
			num[1] = li[yy][xx+1] + 1
			if y[yy] == x[xx]:
				num[2] = li[yy][xx]
			else:
				num[2] = li[yy][xx] + 1
			li[yy+1][xx+1] = min(num)
			num = [0,0,0]

	lev = pd.DataFrame(data=li,columns=xli,index=yli)
	print(lev,"\n\n","距離: ",li[len(yli)-1][len(xli)-1])

if __name__ == '__main__':
	levenshtein("takoyaki","tako")