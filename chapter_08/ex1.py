'''
Write a function called chop that takes a list and modifies it,
removing the 1st and last elements, and returns None.

Then, write a function named middle that takes a list and returns
a new list that contains all but the first and last elements
'''

# recall the function that will modify the original list
# 1. t.pop(index)
# 2. del t[index]

def chop(t):
    if len(t) <= 2:
        print('The given list is less than or equal to 2 elements')
        return None
    t.pop(0)
    t.pop(len(t) - 1)

def chop2(t):
    if len(t) <= 2:
        print('The given list is less than or equal to 2 elements')
        return None
    del t[0]
    del t[len(t) - 1]

# If we're ok the original list to be middled, do the following
def middle(t):
    chop(t)
    return t

# If we want to preserve the original list, and only make a new list which is middled from the original list
def middle2(t):
    return t[1: len(t) - 1]

'''
Testing section
'''
orig_list = [1, 2, 3, 4]
print(chop(orig_list))
# after chop, the original list is:
print(orig_list)

orig_list = ['a', 'b', 'c', 'd']
print(chop2(orig_list))
# after chop, the original list is:
print(orig_list)

orig_list = ['k', 'e', 'b', 'e']
middled_list = middle(orig_list)
print('original list is:', orig_list)
print('middled list is:', middled_list)


orig_list2 = ['h', 'a', 'h', 'a']
middled_list2 = middle2(orig_list2)
print('original list is:', orig_list2)
print('middled list is:', middled_list2)
