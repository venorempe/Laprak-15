def jumlah_deret_ganjil(n):
    if n % 2 == 0:
        n = n - 1
        
    if n <= 1:
        return 1
    
    return n + jumlah_deret_ganjil(n - 2)

n_input = 7 
print(f"Jumlah deret ganjil alami hingga {n_input}: {jumlah_deret_ganjil(n_input)}")