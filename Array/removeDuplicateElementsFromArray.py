# Problem link: https://practice.geeksforgeeks.org/batch/Amazon-Test-Series/track/amazon-arrays/problem/max-sum-path-in-two-arrays

def removeDuplicates(arr):
    # code here
    ans = []
    # Used a set dataStructure
    s = set()

    for ele in arr:
        if ele not in s:
            ans.append(ele)
            s.add(ele)
    return ans


if __name__ == "__main__":

    arr = [int(x) for x in input().split(" ")]
    print(removeDuplicates(arr))
