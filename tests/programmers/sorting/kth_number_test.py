from src.programmers.sorting.kth_number import *

# https://programmers.co.kr/learn/courses/30/lessons/42748
def test_kth_number():
    arr = [1, 5, 2, 6, 3, 7, 4]
    cmd = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    assert solution(arr, cmd) == [5, 6, 3]