text = input()
n, m, t = map(int, text.split(' '))
cannons = []
for _ in range(n):
    text = input()
    d, g, c = map(int, text.split(' '))
    cannons.append((d, g, c))
cannons.sort(key=lambda x: x[0] / x[1], reverse=True)
result = 0
for d, g, c in cannons:
    if m > g:
        fire_times = min(m // g, t // c)
        m -= fire_times * g
        result += fire_times * d
    else:
        continue
print(result)



