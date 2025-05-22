def isAnagram(stringOne,stringTwo):
   if len(stringOne) != len(stringTwo):
    return False
   
   h_stringOne = {}
   h_stringTwo ={}

   for i in range(len(stringOne)):
      if stringOne[i] not in h_stringOne:
         h_stringOne[stringOne[i]] = 1
      else:
         h_stringOne[stringOne[i]] += 1   
      if stringTwo[i] not in h_stringTwo:
         h_stringTwo[stringTwo[i]] = 1
      else:
         h_stringTwo [stringTwo[i]] += 1 

   if h_stringOne == h_stringTwo:
      return True
   else:
      return False       
   
