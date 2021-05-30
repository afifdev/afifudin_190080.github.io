def fx(x):
    return float(2*x*x*x)
def fx_exact(y):
    return float((y*y*y*y)/2)

bb = float(input("Masukkan batas bawah: "))
ba = float(input("Masukkan batas atas: "))
dvder = float(input("Tentukan jumlah pembagi: "))

h = float((ba-bb)/dvder)
x = bb

print("x\t\tf(x)")

while(x<(ba+h)):
    print("{}\t{}".format(x, fx(x)))
    x += h

x = bb+h
res_luas = 0
l0 = fx(bb)
l1 = fx(ba)

while(x<ba):
    l2 = fx(x)
    res_luas += l2
    x += h

trape = (h*(l0+l1+(2*res_luas)))/2
res_exact = fx_exact(ba) - fx_exact(bb)
error = float(trape-res_exact)

print("Hasil Integral Eksak = {}".format(res_exact))
print("Hasil Integral Trapezoid = {}".format(trape))
print("Error = {}".format(error))