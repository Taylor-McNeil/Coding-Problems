

def maxSubArray(nums):

    if len(nums) <= 1:
        return nums[0]

    sum = maxSoFar = nums[0]

    for i in range(len(nums)):
        sum = max(nums[i], sum + nums[i])
        maxSoFar = max(sum,maxSoFar)

    return maxSoFar

tester = [-2,1,-3,4,-1,2,1,-5,4]  
tester2 = [-5, -4, -3]      

print(maxSubArray(tester2))