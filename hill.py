values = [1, 3, 5, 8, 6, 4, 2]

current = 0

while True:

    print("Current:", values[current])

    if current + 1 < len(values) and values[current + 1] > values[current]:
        current = current + 1

    else:
        break

print("Maximum:", values[current])
