import unittest

# Define Stack Class
#  LIFO, last-in first-out
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


#1 Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
def revstring(mystr):
    rev_s = Stack()
    for i in mystr:
        rev_s.push(i)
    rev_string = ""
    while not rev_s.isEmpty():
        new_letter = rev_s.pop()
        rev_string += new_letter
    return rev_string


#2 Write a function rev_string_2(mystr) that list slicing to reverse the characters in a string.
def rev_string_2(string1):
    return  string1[::-1]

#3 Solve the General Balanced Symbol Problem
def parChecker(symbolString):
    par_s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            par_s.push(symbol)
        else:
            if par_s.isEmpty():
                balanced = False
            else:
                top = par_s.pop()
                if not helper_matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and par_s.isEmpty():
        return True
    else:
        return False

def helper_matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


#4 Given an integer find a binary sequence
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

#5 Extend the above algorithm to extend the problem to solve any base
def baseConverter(decNum,base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decNum > 0:
        remainder = decNum % base
        rem_stack.push(remainder)
        decNum = decNum // base

    new_string = ""
    while not rem_stack.isEmpty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


def infixToPosefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    # (A+B)*C .=> ['(', 'A', '+', 'B', ')', '*', 'C']
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] )




class TestRevString(unittest.TestCase):
    def test1(self):
        self.assertEqual(revstring('apple'),'elppa')
    def test2(self):
        self.assertEqual(revstring('x'),'x')
    def test3(self):
        self.assertEqual(revstring('1234567890'),'0987654321')
    def test4(self):
        self.assertEqual(rev_string_2('ammaannao'), 'oannaamma')
    def test5(self):
        self.assertEqual(divideBy2(42),'101010')
    def test6(self):
        self.assertEqual(parChecker('{{([][])}()}'), True)
    def test7(self):
        self.assertEqual(parChecker('{[()}'), False)
    def test8(self):
        self.assertEqual(baseConverter(42,2), '101010')
    def test9(self):
        self.assertEqual(baseConverter(25,16), '19')
    def test10(self):
        self.assertEqual(baseConverter(25,8), '31')
    def test11(self):
        self.assertEqual(baseConverter(256,16), '100')
    def test12(self):
        self.assertEqual(baseConverter(26,26), '10')





if __name__ == '__main__':
    unittest.main()
