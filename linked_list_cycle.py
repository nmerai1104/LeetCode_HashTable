class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False
        return True
