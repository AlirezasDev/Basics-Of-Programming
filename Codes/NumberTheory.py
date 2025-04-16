def is_harshad(num: str):
    sum_digits = 0
    for i in num:
        sum_digits += int(i)
    if int(num) % sum_digits == 0:
        print("YES")
    else:
        print("NO")

def total_primes(num: int):
    sum_primes = 0
    for i in range(2, num):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            sum_primes += i
    print(sum_primes)

def is_disarium(num: str):
    sum_disarium = 0
    for i in num:
        sum_disarium += int(i) ** (num.index(i) + 1)
    if sum_disarium == int(num):
        print("YES")
    else:
        print("NO")

def sequence_palindrome(num: str):
    counter = 0
    number = int(num)
    reversednumber = ""
    
    while True:
        reversednumber = str(number)[::-1]
        if number == int(reversednumber):
            break
        number += int(reversednumber)
        counter += 1
    print(f"({number},{counter})")

def amicable_numbers(n: int):
    pairs = []

    def sum_of_divisors(num):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total

    for i in range(1, n + 1):
        sum_i = sum_of_divisors(i)
        if sum_i > i and sum_i <= n:
            sum_j = sum_of_divisors(sum_i)
            if sum_j == i:
                pairs.append((i, sum_i))

    if pairs:
        print(pairs)
    else:
        print("No number pairs found")

def Incremental_figures(num: str):
    is_increase = True
    for j in range(int(num), 0, -1):
        str_num = str(j)
        for i in range(len(str_num) - 1):
            if str_num[i] > str_num[i + 1]:
                is_increase = False
                break
        if is_increase:
            print(j)
            break
        is_increase = True

b = []
while True:
    a = input().strip().split()
    if a[0] == "end":
        break
    b.append(a)

for k in b:
    if k[0] == "is_disarium":
        is_disarium(k[1])
    elif k[0] == "is_harshad":
        is_harshad(k[1])
    elif k[0] == "sequence_palindrome":
        sequence_palindrome(k[1])
    elif k[0] == "amicable_numbers":
        amicable_numbers(int(k[1]))
    elif k[0] == "total_primes":
        total_primes(int(k[1]))
    elif k[0] == "Incremental_figures":
        Incremental_figures(k[1])
