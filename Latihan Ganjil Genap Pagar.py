n = int(input("Masukkan nilai dari n = "))

# variabel cekBaris = 1 menandakan baris adalah ganjil
# variabel cekBaris = 0 menandakan baris adalah genap
cekBaris = 1

if(n%2==0):
    for i in range(1,n*n+1):
        if(cekBaris == 1):
            if(i%2 == 0):
                print("#",end="")
            else:
                print(i, end="")
        else:
            if(i%2 != 0):
                print("#",end="")
            else:
                print(i, end="")

        if(i%n == 0):
            print()
            if(cekBaris == 1):
                cekBaris = 0
            else:
                cekBaris = 1
else:
    for i in range(1,n*n+1):
        if(i%2 == 0):
            print("#",end="")
        else:
            print(i,end="")

        if(i%n == 0):
            print()
