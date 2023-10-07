from Crypto.Util.number import long_to_bytes, bytes_to_long
import random

#use the miller-rabin primality test to generate 2 random large primes
def miller_rabin(n, k=40):
    if n in [2, 3]: return True
    if n < 2 or n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0: r, d = r + 1, d // 2
    def witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1: return True
        return any(pow(x, 2**i, n) == n - 1 for i in range(r-1))
    return all(witness(random.randint(2, n - 2)) for _ in range(k))
def generate_large_prime(bits):
    gen_candidate = lambda : random.getrandbits(bits) | 1 | (1 << bits - 1)
    return next(filter(miller_rabin, iter(lambda: gen_candidate(), None)))

# Generate two 1024-bit primes for RSA
prime1 = generate_large_prime(1024)
prime2 = generate_large_prime(1024)
n = prime1 * prime2

# beeeeeeeg e for more security ofc
e = 16268248251261543428672446643993508613549377734373688153635605143578577920541239669488314799794730117648400536998010999213258901686045742405653673445268713484715887749733821562075691956161547101425438169229208898594426272486629011816262903344549025430296071173363397287808218170266841717979348351415283040240491291572354042381477562655954789464653601383487352378233341384339965853805133514236252285117399599776638760251491670260415445785726209766243272961819015507909768959864854038131416134023991700528904116837898489410891406487021756009863296691909861305511525242371428088148046222298947850331622964176766063919435


m = bytes_to_long(b"sigpwny{FAKEFLAG}")
c = pow(m, e, n)
print(f"n = {n}")
print(f"c = {c}")

#Relevant chal data in RSA.txt
