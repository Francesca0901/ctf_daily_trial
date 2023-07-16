def find1():
    num = 0
    a = {}
    i = 0
    while True:
        if (num & 1) == 0 and num % 3 == 2 and num % 5 == 1 and \
           (num + ((num - num // 7 >> 1) + num // 7 >> 2) * -7) == 3 and \
           num % 109 == 55 and num > 100000:
            a[i] = num
            i += 1
            if num > 1000000:
                break
        num += 1
    return a

res1 = find1()
# print(f"The first 10 numbers that meet all conditions are: {res1}")

def find2():
    num = 0
    b = {}
    j = 0
    while True:
        local_18 = 0
        i = num
        while i != 0:
            local_18 = local_18 + (i & 1)
            i = i >> 1
        if 17 <= local_18 < 27:
            b[j] = num
            j += 1
            if num > 1000000:
                break
        num += 1
    return b

res2 = find2()
# print(f"\nThe first number that meets all conditions is: {res2}")






def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# Lists for digit sums
digit_sums1 = [(digit_sum(n), n) for n in res1.values()]
digit_sums2 = [(digit_sum(n), n) for n in res2.values()]

# Find common digit sums
common_digit_sums = set([ds for ds, _ in digit_sums1]) & set([ds for ds, _ in digit_sums2])

# Result pairs
result = [((ds1, n1), (ds2, n2)) for (ds1, n1) in digit_sums1 for (ds2, n2) in digit_sums2 if ds1 == ds2]


def test(param_2, param_3=7):
    res = 1
    local_20 = 4919 % param_3

    local_28 = param_2
    while local_28 != 0:
        if (local_28 & 1) != 0:
            res = (res * local_20) % param_3
        local_20 = (local_20 * local_20) % param_3
        local_28 = local_28 >> 1

    return res

# Filter result pairs for those that satisfy test(a) == test(b)
result = [pair for pair in result if test(pair[0][1]) == test(pair[1][1])]

print(result)



