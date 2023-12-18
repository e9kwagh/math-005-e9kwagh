"""no evenly divisible by all of the numbers from 1 to 20?"""
from solver import solver

def answer(limit):
    """Edit the file answer.py and update the function answer() to return the answer."""
    return solver(1, limit)


if __name__ == "__main__":
    print(answer(10))


# import math

# def answer(limit):
#     result =1
#     for i in range(1,limit +1):
#         result = math.lcm(result,i)
#     return result
