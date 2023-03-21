
def findFrequencies(arr):
    n = len(arr)
    fq = dict()
    for ele in arr:
        fq[ele] = fq.get(ele, 0) + 1
        
    for key in fq:
        print(f"{key}: {fq[key]}")
        
if __name__ == "__main__":
    
    arr = [int(x) for x in input().split()]
    findFrequencies(arr)
        