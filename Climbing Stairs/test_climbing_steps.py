import pytest
import climbing_stairs_2

# def test_sum_three_numbers():
#   assert main.sum([1, 3, 5]) == 9

# def test_sum_five_numbers():
#   assert main.sum([1, 3, 5, 13, 0]) == 22

# def test_is_palindrome_no_spaces_negative():
#   assert main.is_palindrome("enterprise") == False

# def test_is_palindrome_no_spaces_positive():
#   assert main.is_palindrome("racecar") == True

# def test_is_palindrome_with_spaces_positive():
#   assert main.is_palindrome("never odd or even") == True

# def test_is_palindrome_with_spaces_negative():
#  assert main.is_palindrome("not a palindrome") == False

def test_step_ways_zero():
  assert climbing_stairs_2.step_ways(0) == 0

def test_step_ways_negative():
    assert climbing_stairs_2.step_ways(-1) == 0

# def test_step_ways_zero():
#     assert climbing_stairs_2.step_ways(0) == 1
  
def test_step_ways_four():
  assert climbing_stairs_2.step_ways(4) == 7

def test_step_ways_five():
  assert climbing_stairs_2.step_ways(5) == 13

def test_step_ways_fifteen():
  assert climbing_stairs_2.step_ways(15) == 5768

