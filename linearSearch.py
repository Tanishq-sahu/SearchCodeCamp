### Given an array of size n as input and a number, 
### define a method that finds the index at which the number is present in that array. If not ### present return -1;


def linearSearch(nums, target){
    index = 0
    for num in nums :
        if num == target:
            return index
        index += 1
    return -1
}
