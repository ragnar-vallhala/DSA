def generate_sequence(n):
    sequence = [n]
    current = n
    for i in range(60, -1, -1):
        if (current & (1 << i)) != 0:
            next_num = current & ~(1 << i)
            sequence.append(next_num)
            current = next_num
    sequence.sort()
    return sequence

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sequence = generate_sequence(n)
        print(len(sequence))
        print(' '.join(map(str, sequence)))

if __name__ == "__main__":
    solve()
