import os

class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None

class ListOperation:
    """
    use all operation related to linked list..
    """
    def print_list(self, head) -> None:
        print("\n print list is : ")
        while head:
            print(head.data)
            head = head.next


    def create_list(self, data, head) -> Node:
        if not head:
            head = Node(data)
        else:
            self.temp = Node(data)
            self.temp.next = head
            head = self.temp
        return head
    

    def get_mediam_using_slow_and_mediam(self, head):
        self.temp1 = head
        self.temp2 = head
        while self.temp2!=None and self.temp2.next!=None:
            self.temp1 = self.temp1.next
            self.temp2 = self.temp2.next.next
        return self.temp1.data


    def detected_loop_using_slow_and_fast_pointer(self, head):
        self.slow = head
        self.fast = head
        while self.slow and self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next
            if self.slow == self.fast:
                return True
        return False


    def detected_list_loop_size(self, head):
        self.slow = head
        self.fast = head
        loop_exist = False
        while self.slow and self.fast and self.fast.next:
            self.slow = self.slow.next
            self.fast = self.fast.next.next
            if self.slow == self.fast:
                loop_exist = True
                break
            
        if loop_exist:
            self.slow = self.slow.next
            list_size = 1
            while self.slow != self.fast:
                self.slow = self.slow.next
                list_size += 1
            return list_size
        return 0



# 2 4 5 7 8 9

if __name__ == "__main__":
    obj = ListOperation()

    list_size = int(input("Give list size : "))
    list_data = list(map(int, input("Give the list data item : ").split(' ')))

    # create an linked list to make some operations..
    head = None
    for i in list_data[::-1]:
        head = obj.create_list(i, head)

    # print the list object..
    obj.print_list(head)
    print("\n")
    median_item = obj.get_mediam_using_slow_and_mediam(head)
    print("median of item : ", median_item)

    # make loopnig in the list..
    loop_temp = head
    while loop_temp.next != None:
        loop_temp = loop_temp.next
    loop_temp.next  = head.next.next


    loop_res = obj.detected_loop_using_slow_and_fast_pointer(head)
    print("\n loop exist in the list is :", loop_res)

    loop_size = obj.detected_list_loop_size(head)
    print("\n list loop size is :", loop_size)

