from collections import Counter

if __name__ == "__main__":
    result = 0
    number_of_shoes = int(input())
    shoes_sizes = Counter(list(map(int, input().split())))
    number_of_customers = int(input())
    sizes_desired = []
    for i in range(0, number_of_customers):
        size, money = list(map(int, input().split()))
        sizes_desired.append(size)
        sizes_desired_count = Counter(sizes_desired)
        if size in shoes_sizes.keys() and sizes_desired_count.get(
            size
        ) <= shoes_sizes.get(size):
            result = result + money

    print(result)
