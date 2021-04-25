import math
import sys

print("")
print("="*50)
teks = "Program Diamond"
print(teks.center(50))
print("="*50)
print("")

n = " "
while n != "":
    n = input("\nmasukkan angka ganjil :")
    print("")
    y = 1
    x = 0
    c = 4

    if n != "":
        for i in range(int(n)):
            if i < math.ceil(int(n)/2):
                print(" "*(int(n)-i),"*"*(y+x))
                y += 1
                x += 1
            else:
                print(" "*(x+1),"*"*(y+x-c))
                c += 4
                x += 1
                y += 1
    else:
        print("")
        print("="*50)
        teks = "Program Selesai"
        print(teks.center(50))
        print("="*50)
        print("")
        sys.exit()

