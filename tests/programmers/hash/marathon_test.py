from src.programmers.hash.marathon import *

# https://programmers.co.kr/learn/courses/30/lessons/42576
def test_marathon():
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    assert solution(participant, completion) == "leo"

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    assert solution(participant, completion) == "vinko"

    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    assert solution(participant, completion) == "mislav"
