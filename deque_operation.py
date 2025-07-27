from collections import deque

history=deque(maxlen=5)
forward_stack = deque(maxlen=5)

def add_page(str):
    history.append(str) 


def go_back():
    if len(history)>0:
        x=history.pop()
        forward_stack.append(x)

def go_forward():
    if len(forward_stack)>0:
        x=forward_stack.pop()
        history.append(x)
 


def main():
    add_page(1)
    add_page(2)
    add_page(3)
    add_page(4)
    add_page(5)
    add_page(6)

    print(history)
    print(forward_stack)
    go_back()
    print(history)
    print(forward_stack)
    go_forward()
    print(history)
    print(forward_stack)
    

if __name__=="__main__":
    main()