import math
import sys
from rich.console import Console
#BLBALBALBLABLA
console = Console()

print("")
console.print("="*50,style="red")
teks = "Program Diamond"
console.print(teks.center(50),style="bold red")
console.print("="*50,style="red")
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
                console.print(" "*(int(n)-i),"*"*(y+x),style="cyan")
                y += 1
                x += 1
            else:
                console.print(" "*(x+1),"*"*(y+x-c),style="cyan")
                c += 4
                x += 1
                y += 1
    else:
        print("")
        console.print("="*50,style="red")
        teks = "Program Selesai"
        console.print(teks.center(50),style="bold red")
        console.print("="*50,style="red")
        print("")
        sys.exit()

