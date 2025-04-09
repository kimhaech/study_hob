# n마리 중 n/2마리 
# 최대한 다른 종류의 폰켓몬을 골라야함
def solution(nums):
    max_count = len(set(nums))
    half = len(nums)//2
    
    if max_count > half:
        return half
    else:
        return max_count
