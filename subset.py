def subset_sum_dc(arr, target):
    if len(arr) == 0:
        # Caso base: Si la lista está vacía, devuelve True si el target también es cero, y una lista vacía para el subconjunto vacío
        return target == 0, []
    elif arr[0] > target:
        # Si el primer elemento de la lista es mayor que el target, se llama recursivamente con el resto de la lista y el mismo target
        return subset_sum_dc(arr[1:], target)
    else:
        # Se llama recursivamente sin el primer elemento, este se resta al target
        found, subset = subset_sum_dc(arr[1:], target - arr[0])
        if found:
            # Si se encontró un subconjunto que suma el target, se agrega el primer elemento a la lista de subset
            subset.append(arr[0])
            return True, subset
        else:
            # Si no se encontró un subconjunto que suma el target, se llama recursivamente con el resto de la lista y el mismo target
            return subset_sum_dc(arr[1:], target)



def subset_sum_dp(arr, target):
    n = len(arr)
    # Se crea una tabla de verdad de tamaño (n+1) x (target+1), inicializada con valores False
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        # Todos los elementos en la primera columna de la tabla son True, ya que cualquier subconjunto puede sumar cero (target = 0)
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < arr[i - 1]:
                # Si el elemento actual es mayor que el target actual, se copia el valor de la celda superior
                dp[i][j] = dp[i - 1][j]
            else:
                # Se toma el valor lógico OR entre la celda superior y la celda que está hacia arriba y hacia la izquierda,
                # desplazada por el valor del elemento actual. Esto representa si se puede incluir o excluir el elemento actual
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                
    if not dp[n][target]:
        # Si la última celda en la tabla es False, significa que no se puede obtener el target con los elementos del arreglo
        return False, []
    
    # Se reconstruye el subconjunto que suma el target a partir de la tabla de verdad
    subset = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            # Si la celda superior es True, significa que el elemento actual no está incluido en el subconjunto
            i -= 1
        else:
            # Si la celda superior es False, significa que el elemento actual está incluido en el subconjunto
            subset.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1
            
    # Se devuelve True, y la lista de subset que suma el target
    return True, subset
