n = int(input("Berapa variabel? "))
iterasi = int(input("Berapa iterasi? "))
mtx = [[float(input("Nilai untuk [{}][{}]=".format(i,j))) for j in range(n+1)] for i in range(n)]
starter = [float(input("Nilai awal X{}=".format(i+1))) for i in range(n)]
res = [0 for i in mtx]
for h in range(iterasi):
    for i in range(len(mtx)):
        holder = mtx[i][-1]
        for j in range(len(mtx[i])-1):
            if i == j:
                continue
            holder -= mtx[i][j]*res[j]
        res[i] = holder/mtx[i][i]
        [print("X{}={}".format(k, res[k]), end='\t') for k in range(len(res))]
        print("")