##
# @file stack.py
# @author xsedla1h
# @brief Module containing a stack implementaion necessary
# for some of the input evaluation functions

class EvalStack:
    def __init__(self):
        self.content = []

    ##
    # @brief Pushes an item onto the stack
    #
    def push(self, item):
        self.content.append(item)

    ##
    # @brief Pops an item from the stack
    #
    def pop(self):
        return self.content.pop()

    ##
    # @brief Checks if the stack is empty
    #
    def empty(self):
        return self.content == []

    ##
    # @brief Returns the last added item
    #
    def peek(self):
        return self.content[len(self.content) - 1]

    ##
    # @brief Returns the momentary size of the stack
    #
    def size(self):
        return len(self.content)
