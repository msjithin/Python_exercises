# Test cases
nums_list= [[6,7,1,2,3,4,5],
            [1, 2, 3, 4, 5, 6, 7],
            [10, 20, 30, 40, 50, 60],
            [12, 24, 35, 47, 58, 69, 72, 83, 94],
            [5, 13, 28, 41, 56, 63, 77, 82, 99, 105],
            [5, 7, 12, 17, 21, 28, 33, 37, 41, 48, 52, 57, 62, 68, 72]]

targets = [6, 1, 50, 12, 56, 5]
solutions = [0, 0, 4, 0, 4, 0]

def test_cases():
    """
    Test that binary search gave correct result
    """
    n = len(nums_list)
    npassed = 0
    print(f"Number of tests = {n}")
    for i in range(len(nums_list)):
        arr = nums_list[i]
        target = targets[i]
        soln   = solutions[i]
        output = binary_search_rotated(arr, target)
        if output== soln :
            npassed += 1
            print(f"Success: Passed {npassed}/{n}")
        else:
            print(f"FAILED: Incorrect index, Array={arr}, expected index={soln}, Output={output}")
        
    print(f"Passed {npassed}/{n}")
        

def binary_search_rotated(nums, target):
  # Replace this placeholder return statement with your code
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = (left + right)//2
    if nums[left] == target:
      return left 
    if nums[right] == target:
      return right 
    if nums[mid] == target:
      return mid
    
    if nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1


def main():
    test_cases()

if __name__ == '__main__':
    main()