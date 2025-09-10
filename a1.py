# Assignment 1: AI-Generated Python Problems
# Name: [Alexis Pelaez]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I'm learning Python basics in a high school programming class. I have some experience with Java in APCSA.
 Can you create 5-7 practice problems that cover: variables and basic data types, conditionals(if/elif/else), loops (for and while), functions, and basic list operations.]


Problem 1: Ask the user to enter their name and age. Print a message that says how old they’ll be in 5 years.
Example inputs/outputs:

Enter your name: Alex
Enter your age: 16
Hi Alex! In 5 years, you’ll be 21 years old.



Problem 2: Write a program that prints the numbers from 1 to 50. But: 
- For multiples of 3, print "Fizz" instead of the number.
- For multiples of 5, print "Buzz".
- For numbers that are multiples of both 3 and 5, print "FizzBuzz".

Problem 3: Write a function called is_even(num) that:
- Takes a number as input
- Returns True if it’s even, and False if it’s odd
Then test your function on numbers from 1 to 10 using a for loop.

Problem 4: Ask the user for a number, then count down to 0 using a while loop. Print each number as it counts down.
Example inputs/outputs:

Enter a number to start countdown: 5
5
4
3
2
1
0
Blast off!

# Deleted original question 5 because it is already done told in al_practice_problems.py

Problem 6: Write a function grade_converter(score) that takes a numeric test score (0–100) and returns the letter grade:
A: 90–100
B: 80–89
C: 70–79
D: 60–69
F: below 60

Problem 7: Write a function reverse_list(lst) that takes a list and returns a new list with the elements in reverse order.
Try it on: ["apple", "banana", "cherry"]
Expected Output: ["cherry", "banana", "apple"]

"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================


def ageIn5 ():
    """Problem 1"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: ")) + 5
    print("Hi", name + "! In 5 years, you'll be", age)

def oTfifty():
    """Problem 2"""
    for i in range(0,51):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

def is_evenNum(n):
    if n % 2 == 0:
        return True
    else:
        return False

def countdown(n):
    i = n
    while i >= 0:
        print(i)
        i -= 1
    print("Blast off!")

def grade_converter(score):
    if score >= 90 :
        return "A"
    elif score < 90 and score >= 80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    elif score < 70 and score >= 60:
        return "D"
    else:
        return "F"

def reverse_list(lst):
    nList = lst[::-1]
    return nList

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

"""

print("Testing Problem 1:")
ageIn5()

print("\nTesting Problem 2:")
oTfifty()

print("\nTesting Problem 3:")
for i in range(0,11):
    print(is_evenNum(i))

print("\nTesting Problem 4:")
countdown(int(input("Enter a number to start countdown: ")))

#Deleted original question 5 because it is already done told in al_practice_problems.py

print("\nTesting Problem 6:")
score = grade_converter(float(input("What did you score on your test? ")))
print(score)

print("\nTesting Problem 7:")
eList = [5,4,3,2,1]
print(reverse_list(eList))
