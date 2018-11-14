manatis = dict(lam={'name': 'a', 'age': 1},
               lam1={'name': 'b', 'age': 2},
               lam2={'name': 'c', 'age': 3},
               lam3={'name': 'd', 'age': 4},
               lam4={'name': 'e', 'age': 5},
               lam5={'name': 'f', 'age': 6},
               lam6={'name': 'j', 'age': 7},
               )

print(manatis['lam']['name'])
print(manatis)


def example1(manatees):
    for k, v in manatees:
        print([k][v])


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


l = LinkedList()
print(l)
l.append(1)
print(l)