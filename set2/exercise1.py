"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this creates a list, and nests the words into a collection which is declared in some_words
some_words = ["what", "does", "this", "line", "do", "?"]

# I think this creates a loop for the words in the list which can all be called in the print function
for word in some_words:
    print(word) # it prints "what, does, this, line, do, ?" 

# I think this is repeition, similiar to above, the only difference is that it is just declared as x now 
for x in some_words:
    print(x)

print(some_words) # this will print out everything which is ["what", "does", "this", "line", "do", "?"]

# I think that if the list contains more than 3 words it will print the string below if the case was unsucessful it will
# do nothing
if len(some_words) > 3: 
    print("some_words contains more than 3 words") # in this case it will print what was written 

# defines a function as usefulFunction
def usefulFunction(): 
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # prints out the user's specification about their system


usefulFunction() # calls in the function, which allows the code above to run.
