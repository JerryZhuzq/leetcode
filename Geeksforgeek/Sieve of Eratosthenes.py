# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print
            p,

        # driver program


if __name__ == '__main__':
    n = 30
    print
    "Following are the prime numbers smaller",
    print
    "than or equal to", n
    SieveOfEratosthenes(n)


def SieveOfSundaram(n):
    # In general Sieve of Sundaram,
    # produces primes smaller
    # than (2*x + 2) for a number
    # given number x. Since we want
    # primes smaller than n, we
    # reduce n to half
    nNew = int((n - 2) / 2);

    # This array is used to separate
    # numbers of the form i+j+2ij
    # from others where 1 <= i <= j
    # Initialize all elements as not marked
    marked = [0] * (nNew + 1);

    # Main logic of Sundaram. Mark all
    # numbers of the form i + j + 2ij
    # as true where 1 <= i <= j
    for i in range(1, nNew + 1):
        j = i;
        while ((i + j + 2 * i * j) <= nNew):
            marked[i + j + 2 * i * j] = 1;
            j += 1;

            # Since 2 is a prime number
    if (n > 2):
        print(2, end=" ");

        # Print other primes. Remaining
    # primes are of the form 2*i + 1
    # such that marked[i] is false.
    for i in range(1, nNew + 1):
        if (marked[i] == 0):
            print((2 * i + 1), end=" ");