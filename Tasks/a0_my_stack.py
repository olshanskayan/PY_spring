"""
My little Stack
"""
from typing import Any

my_stack = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """

    my_stack.append(elem)
    print(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """

    my_stack.pop()

    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    # print(ind)
    print(my_stack[-1 -ind])

    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    my_stack.clear()

if __name__ == '__main__':
    push(1)
    push(2)
    push(3)
    push(4)
    print(my_stack)

    peek(my_stack[0])
    print(my_stack)

    # pop()
    # print(my_stack)
    # pop()
    # print(my_stack)
    # pop()
    # print(my_stack)
    # pop()
    # print(my_stack)

    clear(my_stack)
    print('My result: ',my_stack)
