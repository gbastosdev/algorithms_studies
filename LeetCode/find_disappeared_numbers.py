def findDisappearedNumbers(nums: list[int]) -> list[int]:
    viewed = set(nums)
    ans = []
    for n in range(1,len(nums)+1):
        if n not in viewed:
            ans.append(n)
    return ans

# Example usage:
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))  # Output: [5,6]
    nums = [1,1]
    print(findDisappearedNumbers(nums))  # Output: [2]