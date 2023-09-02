"""
ALGORITHM - FIND MIN

Set min to positive infinity: float("inf").
For each number in the list nums, compare it to min. If num is smaller, set min to num.

min is now set to the smallest number in the list.

ASSIGNMENT

In each assignment in this course we'll be building out pieces of a pretend product: Socialytics - The tool you need to track your growth as an Instagram influencer. We need to display to our influencers the people they follow who have the lowest follower count. This will help them know which of the people they follow aren't popular enough to be worth following anymore.

Implement the "find min" algorithm in Python by completing the find_min() function.
"""

#Sountion 

def find_min(nums):
    min = float("inf")
    for i in nums :
          if i< min:
              min = i
    return min

# don't touch below this line


def test(nums):
    res = find_min(nums)
    print(f"Follower counts: {nums}")
    print(f"Lowest follower count: {res}")
    print("----")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])


main()
