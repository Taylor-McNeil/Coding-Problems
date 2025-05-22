def firstUniqueCharInString(string):

    if len(string) <= 0:
        return -1

    table = {}

    for index,char in enumerate(string):
        if char in table:
            table[char]['count'] += 1
        else:
            table[char] = {'count': 1, 'index': index}

    for char in string:
        if table[char]['count'] == 1:
            return table[char]['index']         
                    


print(firstUniqueCharInString("leetcode"))