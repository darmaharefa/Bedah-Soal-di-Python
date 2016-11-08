n = int(input("Masukkan panjang angka = "))

for i in range(1,n+1):
    if(i%2 != 0): #Saat i bernilai ganjil
        for j in range(1,n+1):
            print(j,end=" ")
        print()
    else: #Saat i bernilai genap
        for j in range(n,0,-1):
            print(j,end=" ")
        print()
