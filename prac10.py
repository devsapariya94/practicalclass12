stack=["dev","khush", "ronak"]
stack.append("ashish")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)


from collections import deque

queue= deque(["pankaj","ankit", "abhay"])
print(queue)
queue.append('sagar')
print(queue)
queue.append('deep')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
