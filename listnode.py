class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


list_node = ListNode('A',ListNode('B', ListNode('C', ListNode('D'))))

def ln_append(ln, n):
    a = ln
    while True:
        if a.next is not None:
            a = a.next
        else:
            a.next = n
            break
    return ln

def ln_insert(ln, n, index):
    ret = ln
    while index > 1:
        ln = ln.next
        index -= 1
    n.next = ln.next
    ln.next = n
    return ret

def ln_delete(ln, index):
    p = 0
    ret = ln
    if index == 0:
        ret = ln.next
    else:
        while p != index - 1:
            ln = ln.next
            p += 1
        ln.next = ln.next.next

    return ret

def ln_find(ln, n):
    ret = 0
    while not ln.val == n:
        ln = ln.next
        ret += 1
    return ret

def ln_change(ln, val, index):
    p = 0
    ret = ln
    while p != index:
        ln = ln.next
        p += 1
    else:
        ln.val = val
    return ret

def ln_reverse(ln):
    # !!! 传入的list_node被修改
    ret = ListNode()

    while ln is not None:
        # 拿出一个节点
        tmp = ln
        ln = ln.next

        # 将节点插入到新链表中
        tmp.next = ret.next
        ret.next = tmp
    
    return ret.next

def ln_traserse(ln):
    ret = [] 
    while ln is not None:
        ret.append(ln.val)
        ln = ln.next
    print(ret)
    return ret
    
def ln_len(ln):
    len = 1
    while ln.next is not None:
        ln = ln.next
        len += 1
    
    return len


ln_traserse(ln_append(list_node, ListNode('E', ListNode('F'))))
# ln_traserse(ln_insert(list_node, ListNode('12'), 2))
print('"A" index in listnode: ', ln_find(list_node, 'A'))
print('Length of listnode: ', ln_len(list_node))
list_node = ln_reverse(list_node)
ln_traserse(list_node)
print('"A" index in listnode: ', ln_find(list_node, 'A'))
print('Length of listnode: ', ln_len(list_node))
list_node = ln_reverse(list_node)
ln_traserse(ln_change(list_node, 'X', 3))
ln_traserse(ln_delete(list_node, 3))
