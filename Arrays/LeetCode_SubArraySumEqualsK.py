def subArraySumEqualsK(nums,target):
   matches = 0
   currentSum = 0
   hashmap = {0:1}
   
   for index,value in enumerate(nums):
      currentSum += value
      compliment = currentSum - target

      if compliment in hashmap:
         matches += hashmap[compliment]

      if currentSum in hashmap:
         hashmap[currentSum] += 1
      else:
         hashmap[currentSum] = 1   
   return matches

nums = [1, -1, 5, -2, 3]
k = 3