def sumnature(n):
    if n <= 1:
        return n
    else:
        return  (n) + sumnature(n-1)
n = 3
print(sumnature(n))
