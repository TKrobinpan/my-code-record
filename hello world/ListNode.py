from operator import ne
from platform import node


class ListNode:
    def __init__(self,val,next=None,random=None) -> None:
        self.val = val
        self.next = next
        self.random = random

# 判断是否为回文链表，快慢指针+链表反转，时间复杂度O(N)，空间复杂度O(1)
class HuiwenListNode:
    def huiWenListNode(self,head):
        if (not head.next) or (not head):
            return True
        slow = head;fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        slow = self.reverseList(slow.next)
        return self.isHuiWen(head,slow)
    
    def isHuiWen(self,l1,l2):
        while l2:
            if l1.val!=l2.val:return False
            l2=l2.next;l1=l1.next
        return True
# 链表反转
    def reverseList(self,l1):
        prev = None
        while l1:
            next=l1.next
            l1.next = prev
            prev = l1
            l1=next
        return prev

# 复制具有随机指针的链表
# 1. 哈希表（字典）,空间复杂度O(n)
class CopyRandomListNode1:
    def copyRandomList(self, head:ListNode):
        mapp={}
        node = head
        while node:
            mapp[node] = ListNode(node.val)
            node = node.next
        mapp[node] = None
        node = head
        copyHead = mapp[node]
        copyNode = copyHead
        while node:
            copyNode.next = mapp[node.next]
            copyNode.random = mapp[node.random]
            copyNode=copyNode.next;node=node.next
        return copyHead

# 2. 克隆节点，和源节点交叉相串，空间复杂度为O(1)
class CopyRandomListNode2:
    def copyRandomList(self, head:ListNode):
        if not head:return None
        node=head
        # 构建一个交叉相串的链表
        while node:
            next=node.next
            node.next=ListNode(node.val,next)
            node=node.next.next
        node=head
        node1=node.next
        while node:
            if node.random:
                node1.random = node.random.next
            else:
                node1.random = node.random
            node=node1.next
            if node: node1=node.next
        node=head;node1=node.next;head1=node1
        while node1.next:
            node1.next = node1.next.next
            node1=node1.next
        return head1
