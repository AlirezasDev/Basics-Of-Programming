def tower_of_hanoi(n, source, target, auxiliary, moves):
    if n == 0:
        return
    tower_of_hanoi(n - 1, source, auxiliary, target, moves)
    moves.append(f"{source}{target}")
    tower_of_hanoi(n - 1, auxiliary, target, source, moves)

def solve_hanoi(n, m):
    min_moves = (1 << n) - 1
    if m < min_moves:
        return "There is nothing we can do"
    moves = []
    tower_of_hanoi(n, 1, 3, 2, moves)
    return " ".join(moves)

n = int(input())
m = int(input())
print(solve_hanoi(n, m))
