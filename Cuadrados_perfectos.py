def lista_cuadrados(N):
    cua_perf = []
    for n in range(1, N+1):
        raiz = n ** (0.5)
        if n % raiz == 0:
            cua_perf.append(int(raiz*raiz))
    return cua_perf

N = int(input("Numero: "))
print(lista_cuadrados(N))