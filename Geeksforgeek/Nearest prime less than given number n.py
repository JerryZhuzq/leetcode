def findPrimeNum(n):

    def sieveEratosthenes(n):
        store = [1] * (n+1)
        p = 2
        while (p * p < n+1):
            if store[p]:
                i = p
                while(p * i < n+1):
                    store[p*i] = 0
                    i += 1
            p += 1

        return store
    store = sieveEratosthenes(n)
    k = n - 1
    while(k > 1):
        if store[k]:
            return k
        k -= 1

print(findPrimeNum(5))