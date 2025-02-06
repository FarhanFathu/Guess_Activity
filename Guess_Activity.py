import random

def aktivitas():
        data = ("masak","Makan","Belanja","mancing","berlari","menulis","merawat")
        data_secret = random.choice(data)

        percobaan = 0
        skor = 0

        print(" Selamat Datang di Game Tebak Akitivitas")
        print(f"disini ada beberapa aktivitas : \n 1.masak \n 2.Makan \n 3.Belanja \n 4.mancing \n 5.berlari \n 6.menulis")
        LEVEL = input("Pilih LEVEL (1/2/3) : ")

        if LEVEL == "1":
                max_percobaan =2
               
        elif LEVEL == "2" :
                max_percobaan =3
               
        else  :
                max_percobaan =5
              
        while percobaan < max_percobaan :
            tebak=input(f"Percobaan {percobaan+1} dari {max_percobaan}Tebak Jawaban Data Rahasia :")
            percobaan +=1

            if tebak== data_secret:
                print(f"\nJawaban Anda Benar")
                
                break
            elif tebak in data :
                print(f"\nJawaban Anda Salah")
            else :
                print(f"\nJawaban Anda tidak Ada di Data")
            if percobaan < max_percobaan:
                print(f"Clue nya adalah {data_secret[0]}")

        if tebak == data_secret:
            if percobaan == 1:
                skor =100
            elif percobaan == 2:
                 skor=75
            elif percobaan == 3:
                 skor=50
            elif percobaan == 4:
                 skor=25
            else :
                 skor=10
        
        print(f"Skor yang kamu dapatkan adalah : {skor}")
            
             
        if percobaan==max_percobaan:
            print(f"\nKesempatan Anda Telah Habis, Silahkan coba lagi dan jawaban benarnya adalah {data_secret}.")
        
        
     
    
while True:
    aktivitas()
    restart = input("apakah anda ingin bermain lagi (YES/NO) : ").strip().upper()
    if restart != "YES" :
        print (f"\nTerimakasih Telah Bermain :))")
        break
   
