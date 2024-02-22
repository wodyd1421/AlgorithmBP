n = int(input())
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    good = a + 2*b + 3*c + 3*d + 4*e + 10*f
    a, b, c, d, e, f, g = map(int, input().split())
    evil = a + 2*b + 2*c + 2*d + 3*e + 5*f + 10*g
    if good > evil:
        print(f"Battle {i+1}: Good triumphs over Evil")
    elif good < evil:
        print(f"Battle {i+1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i+1}: No victor on this battle field")