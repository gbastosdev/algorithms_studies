def smallestRepunitDivByK(k: int) -> int:
        cur = 1
        for i in range(1,k +1):
            if cur % k == 0:
                return i
            cur = 10 * (cur % k) + 1
        return -1


if __name__ == "__main__":
    k = 3
    print(smallestRepunitDivByK(k))  # Example usage