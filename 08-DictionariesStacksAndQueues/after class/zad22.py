# 22.	Following the example of stack.py, create a queue.py module in which define queue handling. 
# Then write a program that imports the queue.py module. 
# Add and remove values from the queue. Display its content.

import queue_module

def main() -> None:
    queue_module.display()
    queue_module.push(1)
    queue_module.push(2)
    queue_module.push(3)
    queue_module.push(4)
    queue_module.push(5)
    queue_module.display()
    queue_module.pop()
    queue_module.pop()
    queue_module.display()

if __name__ == '__main__':
    main()