"""print("Welcome to List")

marks = [90,20,45,67,89]
name = ["Suraj", "Putta", "Balu"]
mix = [30,"Suraj",3.14,True]
empty = []
print(len(marks))
print(mix)
print(type(name))"""


"""marks = [90,20,45,67,89]
#         0, 1, 2, 3, 4  index value 
print(marks[0])
print(marks[3])   
print(marks[-3])   
print(marks[-1])"""


#slicing — get a portion of list
"""marks = [85, 90, 78, 92, 88]

print(marks[1:4])
print(marks[0:],"Seeda")
print(marks[::-1],"Ulta")
print(marks[:2])"""


"""marks = [85, 90, 78, 92, 88]

marks.append(100)
print(marks)
marks.insert(3,50)   # insert at index
print(marks)
marks.remove(100)
print(marks)
marks.pop()
print(marks)
marks.pop(0)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks.index(50))
print(marks.count(78))
print(marks)"""


"""marks = [85, 90, 78]

marks.append(92)        # add to end     → [85,90,78,92]
marks.insert(1, 100)    # insert at index → [85,100,90,78,92]
marks.remove(78)        # remove by value → [85,100,90,92]
marks.pop()              # remove last     → [85,100,90]
marks.pop(0)            # remove at index → [100,90]
marks.sort()             # sort ascending  → [90,100]
marks.reverse()          # reverse         → [100,90]
print(marks)

print(marks.index(90))  # find index of 90
print(marks.count(90))  # count occurrences"""

"""names = ["Suraj", "Putta", "Ravi"]
for name in names:
    print(name)

for i, name in enumerate(names): # With index using enumerate
    print(f"{i+1}. {name}")"""