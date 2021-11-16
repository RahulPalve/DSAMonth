
s = []

arr=[1,2,1,5,6,9,8,10]
next_no = [0]*len(arr)

for i,e in enumerate(arr):
    if len(s):
        if arr[s[-1]] < e:
            while len(s) and arr[s[-1]] < e:
                next_no[s[-1]] = e
                s.pop()
    s.append(i)

print(next_no)