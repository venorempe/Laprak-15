def is_prima(n, i=2):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % i == 0:
        return False
    
    if i * i > n:
        return True
    
    return is_prima(n, i + 1)

print("=== Program Pengecek Bilangan Prima ===")
try:
    angka = int(input("Masukkan sebuah bilangan bulat: "))
    
    if is_prima(angka):
        print(f"Hasil: {angka} adalah BILANGAN PRIMA! 🎉")
    else:
        print(f"Hasil: {angka} BUKAN bilangan prima. ❌")
except ValueError:
    print("Mohon masukkan bilangan bulat yang valid.")