def is_palindrom_rekursif(teks):
    if len(teks) <= 1:
        return True
    
    if teks[0] != teks[-1]:
        return False
    
    return is_palindrom_rekursif(teks[1:-1])


print("=== Program Pengecek Palindrom ===")
kalimat_input = input("Masukkan kata atau kalimat: ")

teks_bersih = "".join(kalimat_input.lower().split())

if is_palindrom_rekursif(teks_bersih):
    print(f'Hasil: "{kalimat_input}" adalah PALINDROM! 🎉')
else:
    print(f'Hasil: "{kalimat_input}" BUKAN palindrom. ❌')