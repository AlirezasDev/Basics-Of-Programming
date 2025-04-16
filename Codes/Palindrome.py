def palindromic_substrings(s):
    n = len(s)
    palindromes = []

    for start in range(n):
        for end in range(start, n):
            substring = s[start:end + 1]
            if substring == substring[::-1]: 
                palindromes.append(substring)

    palindromes.sort(key=lambda x: (len(x), x))
    
    return palindromes

for substring in palindromic_substrings(input()):
    print(substring)
