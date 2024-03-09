
print("\n<<-- Initial -->>")

list = [7,4,2,6,4,3]
print(list)

#1 sorting
print("\n1 After Sorting:")
list.sort()
print(list)

#2 add 100 in last
print("\n2 After Append 100:")
list.append(100)
print(list)

#3 insert before a number
print("\n3 After Insert value in index:")
list.insert(2,200)
print(list)

#4 remove any number
print("\n4 After remove value")

list.remove(200)
print(list)

#5 pop last number
print("\n5 After pop:")
list.pop()
var = list
print(var)

#6 delete number of index
print("\n6 Delete index:")
del list[3]
print(list) 

#7 copy
print("\n7 After Copy:")
copy_here=list.copy()
print(copy_here)

#8 Reverse
print("\n8 After Reverse:")
list.reverse()
print(list)

#9 clear list
print("\n9 After full clear:")
list.clear()
print(list)
print("\n*** THANK YOU ***\n")


