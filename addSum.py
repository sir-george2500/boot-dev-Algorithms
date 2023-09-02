"""
Start with input variables "a" and "b"
Add "a" and "b" using the + operator, and assign the result to a new variable, "sum"
Return the "sum" variable
ASSIGNMENT
In Socialytics, we need to calculate the total reach of a group of influencers so we can estimate how many views a post will get if we have them all share it.

Complete the sum function. Write it as a modified version of the sum algorithm that accepts a list of numbers and returns the sum of all of them.

"""
def sum(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


# don't touch below this line


def test(nums):
    res = sum(nums)
    print(f"Follower counts: {nums}")
    print(f"Total follower count: {res}")
    print("----")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])


main()
