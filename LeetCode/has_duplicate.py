def hasDuplicate(nums: list[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(hasDuplicate(nums))  # Output: True
    nums = [1, 2, 3, 4]
    print(hasDuplicate(nums))  # Output: False
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(hasDuplicate(nums))  # Output: True