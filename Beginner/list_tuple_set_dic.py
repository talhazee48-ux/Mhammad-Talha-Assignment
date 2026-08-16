#list practice


num = [1,6,21,64]


print(num[0])
print(num[1])
print(num[2])
print(num[3])


#list length


colors = ["red","blue","green"]


print(len(colors))
colors.append("yellow")
print(colors)


#insert into list


fruites = ["apple","orange"]


fruites.insert(1,"guava")
print(fruites)


#remove from list


fruites.remove("orange")
print(fruites)


#remove from list using pop


items = ["pen","pencil","eraser"]
items.pop(1)
print(items)


#check if an item is in the list


numbers = [1,2,3,4,5]


print(3 in numbers)
print(6 in numbers)


#list slicing 


num2 = [10,20,30,40,50]


print(num2[2:4])
print(num2)
num2[num2.index(30)] = 35
print(num2)


#counting the number of occurrences of an item in a list


list2 = [1,2,2,3,2,4,5]
print(list2.count(2))


#tuple practice 


tuple = (10,20,30,40)
print(tuple[1])


print(len(tuple))


#tuple unpacking


someone = ("khan",22)


name,age = someone


print(name)
print(age)


#tuple concatenation


tuple_num = (20,30,50,60)


print(20 in tuple_num)


tuple1=()


#type of tuple


print(type(tuple1))


tupleno1=(1,2,3)
tupleno2=(4,5,6)


tupleno3 = tupleno1 + tupleno2
print(tupleno3)


#repeat the tuple int


numbers2 = (7,)
print(numbers2 * 3)


numbers3 = (1,2,3,4,5,6,7)


print(numbers3.index(1))
print(numbers3.index(4))


print(numbers3.count(2))


numbers4 = (5,)
print(type(numbers4))


#set practice


set1 = {1,2,3,4,5}
print(set1)


#adding and removing elements from a set


set1.add(6)
print(set1)


#removing elements from a set


set1.remove(3)
print(set1)


#checking if an element is in a set


print(4 in set1)


print(len(set1))


#clearing a set


set1.clear()
print(set1)


#adding elements to a set using update


set2 = {"a", "b", "c"}
if "d" not in set2:
    set2.add("d")
print(set2)


#removing elements from a set using discard


numbers5 = [1,2,3,3,4,5,5]
unique_numbers = set(numbers5)
print(unique_numbers)


#union intersection


set3 = {1,2,3}
set4 = {3,4,5}


print(set3.union(set4))
print(set3.intersection(set4))


#dictionary practice


my_dict = {"name":"Alice", "age":30, "city":"New York"}
print(my_dict["name"])
print(my_dict["age"])


#adding and updating key-value pairs in a dictionary


my_dict["book"] = "Python Programming"
print(my_dict)


my_dict["age"] = 31
print(my_dict)


del my_dict["city"]
print(my_dict)


print("salary" in my_dict)


print(my_dict.keys())


print(my_dict.values())


for k , v in my_dict.items():
    print(k,v)


print(my_dict.get("score",0))


#creating a dictionary using the dict() constructor


my_dict = dict(zip(["name","age"],["Bob",25]))
print(my_dict)



print("End of basic practice of list, tuple, set and dictionary")


#End of basic practice of list, tuple, set and dictionary

