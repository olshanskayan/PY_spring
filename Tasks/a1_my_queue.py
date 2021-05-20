"""
My little Queue
"""
from typing import Any

my_queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    my_queue.insert(0, elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    if my_queue:
        return(my_queue.pop())
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if my_queue:
        return(my_queue[len - ind])

def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    my_queue.clear()
    return None


if __name__ == '__main__':
    enqueue(1)
    enqueue(12)
    enqueue(3)
    enqueue(5)
    print(my_queue)

    # clear()
    #
    # print(dequeue())
    #
    # print(peek(2))


# my_stack = []
#
#
# def push(elem: Any) -> None:
#     """
#     Operation that add element to stack
#
#     :param elem: element to be pushed
#     :return: Nothing
#     """
#
#     my_stack.append(elem)
#     print(elem)
#     return None
#
#
# def pop() -> Any:
#     """
#     Pop element from the top of the stack. If not elements - should return None.
#
#     :return: popped element
#     """
#     if my_stack:
#         my_stack.pop()
#         return None
#
#
# def peek(ind: int = 0) -> Any:
#     """
#     Allow you to see at the element in the stack without popping it.
#
#     :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
#     :return: peeked element or None if no element in this place
#     """
#     # print(ind)
#     if 0 <= ind < len(my_stack):
#         return(my_stack[-1 -ind])
#
#
# def clear() -> None:
#     """
#     Clear my stack
#
#     :return: None    """
#     my_stack.clear()
#
# if __name__ == '__main__':
#     push(1)
#     push(2)
#     push(3)
#     push(4)
#     print(my_stack)
#
#     peek(my_stack[0])
#     print(my_stack)
#
#     # pop()
#     # print(my_stack)
#     # pop()
#     # print(my_stack)
#     # pop()
#     # print(my_stack)
#     # pop()
#     # print(my_stack)
#
#     clear()
#     print('My result: ',my_stack)
