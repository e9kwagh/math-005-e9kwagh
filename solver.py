"""Write a function in python that returns the smallest positive number 
that is evenly divisible by all of the numbers between the range p and q, inclusive.
"""


def solver(p, q):
    """creating function to return the smallest divisible no """
    if p > q:
        start, end = q, p
    else:
        start, end = p, q
    num = end

    while True:
        flag = True
        for i in range(start, end + 1):
            if num % i != 0:
                flag = False
                break
        if flag:
            return num
        num += 1


if __name__ == "__main__":
    print(solver(1, 10))
