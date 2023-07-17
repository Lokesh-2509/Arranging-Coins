def arranging_coins(n_value):
    left, right = 0, n_value
    while left <= right:
        mid = left + (right - left) // 2
        total = (mid * (mid + 1)) // 2
        if total == n_value:
            return mid
        if total > n_value:
            right = mid - 1
        else:
            left = mid + 1
    return right
print(arranging_coins(5))
print(arranging_coins(8))

