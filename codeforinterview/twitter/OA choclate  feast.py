import sys


def choc_eat(n,p,h):
    wrap = res = n / p

    while wrap >= h:
        div, mod = divmod(wrap, h)
        res += div
        wrap = mod

    return res


input = sys.stdin.readline()
while input:
    input=input.split(' ')
    n,p,h = input
    print choc_eat(int(n), int(p), int(h))
    input = sys.stdin.readline()


