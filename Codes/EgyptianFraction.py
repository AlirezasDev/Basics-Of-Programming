k = int(input())

pairs = []
for x in range(1, 1001):
    if x == k:
        continue
    else:

        y = (k * x) / (x - k)
        
        if y.is_integer() and 1 <= y <= 1000:
            pairs.append((x, int(y)))


for x, y in pairs:
    print(f"1/{k} = 1/{x} + 1/{y}")
