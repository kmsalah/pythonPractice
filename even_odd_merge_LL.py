#even odd merge of a linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def even_odd_merge(head):
	if not head:
		return head

	even_head = ListNode(0)
	odd_head = ListNode(0)

	tails = [even_head, odd_head]
	turn = 0

	curr = head

	while curr:
		tails[turn].next = curr
		curr = curr.next
		tails[turn] = tails[turn].next
		turn ^= 1

	tails[1].next = None
	tails[0].next = odd_head.next

	return even_head.next