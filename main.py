from subset import subset_sum_dc, subset_sum_dp
arr = [4, 12, 5, 2, 3, 1]
target = 9

# Solución con Divide and Conquer
found_dc, subset_dc = subset_sum_dc(arr, target)
if found_dc:
    print("Solución con Divide and Conquer:", subset_dc)
else:
    print("Solución con Divide and Conquer: No se encontró un subconjunto que sume", target)

# Solución con Programación Dinámica
found_dp, subset_dp = subset_sum_dp(arr, target)
if found_dp:
    print("Solución con Programación Dinámica:", subset_dp)
else:
    print("Solución con Programación Dinámica: no se encontro :(")