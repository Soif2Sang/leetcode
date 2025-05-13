# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list2 is None:
            return list1
        
        if list1 is None:
            return list2
        
        if list1 is None and list2 is None:
            return None

        current_node = list2
        # We go through each node of list2 and add it to the list1
        while current_node != None:
            #print("addNumberToList", current_node.val)
            #print("before", list1)
            list1 = self.addNumberToList(list1, current_node.val)
            #print("after", list1)
            current_node = current_node.next

        return list1
    
    def addNumberToList(self, list1, number):
        """
        This function aims to add a number to a sorted linked list
        """
        current_node = list1
        if (number <= current_node.val):
            #print("Shortcut")
            return ListNode(number, list1)
        
        if (number > current_node.val and current_node.next is None):
            current_node.next = ListNode(number, None)
            return list1
        prev = current_node
        current_node = current_node.next

        while current_node != None:
            #print("current_node.val", current_node.val, '\n')
            if current_node.val >= number:
                #print("number added")
                prev.next = ListNode(number, prev.next)
                break
            if current_node.next is None:
                current_node.next = ListNode(number, None)
                break
            prev = current_node
            current_node = current_node.next
        return list1