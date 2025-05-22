'''
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.


'''

def distinctCompanyNamesBF(ideas):
    ideaSet =set(ideas)
    newCompanynames=[]

    for i in range(len(ideas)):
        for j in range(i+1,len(ideas)):
            stringA = ideas[i][0]
            stringB = ideas[j][0]
            suffixA = ideas[i][1:]
            suffixB = ideas[j][1:]
            newStringA = stringA+suffixB
            newStringB = stringB+suffixA
            if newStringA not in ideaSet and newStringB not in ideaSet:
                newCompanynames.append(newStringA+" "+newStringB)
                newCompanynames.append(newStringB+" "+newStringA)
            
    return newCompanynames

print(distinctCompanyNamesBF(["coffee","donuts","time","toffee"]))