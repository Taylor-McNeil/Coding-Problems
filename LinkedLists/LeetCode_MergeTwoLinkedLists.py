from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
        self.val = val
        self.next = next   



def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    if not list1:
        return list2
    
    
    mergedList = []
    current = list1

    while current:
        mergedList.append(current.val)
        current = current.next
        

    current = list2
    while current:
        mergedList.append(current.val)
        current = current.next
        
    mergedList.sort()
    

    finalList = ListNode(mergedList[0])      
    current = finalList
    
    for val in mergedList[1:]:
        current.next = ListNode(val)
        current = current.next


        '''finalList.next = ListNode(mergedList[counter])

        print('f counter is {counter} \n current is {current}')
        counter += 1
        current = current.next'''



        
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


mergeTwoLists(list1,list2)