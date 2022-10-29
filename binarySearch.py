### Given an array of size n as input and a number,
### define a method that finds the index at which the number is present in that array. If not
### present return -1;
### solve in log n




def binarySearch(nums, target){
    sort(nums)
    start = 0
    end = len(nums) -1
    while start < end :
        mid = (start + end ) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1
}

