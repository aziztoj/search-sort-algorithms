# Comment
import time
names = ['Alice',"Bob","Charlie","Josh",'James', 'Ethan','David','Jackson','Peter','Mohammed','Joseph','Kim','Michael','Ian','Chris','Aziz','Eeshan','Karl','Thomas','Brian']
user = input("Enter a name to search: ")

start_time = time.perf_counter()
def linsearch(names,user):
    for i in range(20):
        if names[i] == user:
            return "Found at position", i 
    return "not found"
end_time = time.perf_counter()
timetaken = end_time - start_time
print(linsearch(names,user))
print(f"{timetaken:.40f}")

names2 = [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],[None]]
def hashing(user):
    product = 1
    for letter in user:
        product = product * ord(letter)
    value = product / 1000
    value = value % 10
    return int(value) 


def search(user):
    index = hashing(user)
    for i in names2[index]:
        if i == user:
            return "Found"
        else:
            return "Not Found"

for i in names:
    index = hashing(i)
    if names2[index][0] == None:
        names2[index][0] = i
    else:
        names2[index].append(i)
print(names2)
start_time2 = time.perf_counter()
print(search(user))
end_time2 = time.perf_counter()
total = end_time2 - start_time2
print(f"{total:.40f}")