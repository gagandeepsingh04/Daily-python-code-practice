def checkingTarget(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                if i != j:
                    return i, j
    return None


def main():
    nums = list(map(int, input().split()))
    target = int(input())
    nums_target = checkingTarget(nums, target)
    print(nums_target)


if __name__ == '__main__':
    main()
  
