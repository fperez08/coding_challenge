from itertools import product

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = list(product(A, B))
    for t in result:
        print("{} ".format(t), end="")
