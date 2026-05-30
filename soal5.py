def kombinasi_rekursif(n, r):
    if r < 0 or r > n:
        return 0
        
    if r == 0 or r == n:
        return 1
        
    return kombinasi_rekursif(n - 1, r - 1) + kombinasi_rekursif(n - 1, r)



print("=== Program Hitung Kombinasi C(n, r) ===")
try:
    n = int(input("Masukkan nilai n (total objek): "))
    r = int(input("Masukkan nilai r (objek yang dipilih): "))
    
    hasil = kombinasi_rekursif(n, r)
    print(f"Hasil dari C({n}, {r}) adalah: {hasil}")
except ValueError:
    print("Mohon masukkan bilangan bulat yang valid.")