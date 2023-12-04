queue = []

def push(value):
    queue.append(value)

def pop():
    if not empty():
        return queue.pop(0)
    else:
        return None
    
def empty():
    return len(queue) == 0

def display():
    for i in range(0, len(queue)):
        print(queue[i])
    print()

# check length of stack
def check_length():
    return len(queue)