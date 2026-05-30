def jumlah_digit(n):
    sn = abs(n)
    
    if n < 10:
        return n
    
    return (n % 10) + jumlah_digit(n // 10)

print("=== Program Hitung Jumlah Digit ===")
try:
    angka = int(input("Masukkan bilangan bulat: "))
    hasil = jumlah_digit(angka)
    print(f"Jumlah digit dari {angka} adalah: {hasil}")
except ValueError:
    print("Mohon masukkan bilangan bulat yang valid.")