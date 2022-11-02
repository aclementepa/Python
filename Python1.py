list1 = [1,2,3,4]
list2 = ["Elie", "Tim", "Matt"]
new_list = list()

for word in list2:
    for letter in word:
        new_list.append(letter)
        break

new_list.clear()
list3 = [1,2,3,4,5,6]
for num in list3:
    if (num % 2 == 0):
        new_list.append(num)

new_list.clear()
for word in list2:
    new_list.append(word.lower()[::-1])        
        
# for var in new_list:
    # print(var)

d = {'a': 1, 'c': 3, 'e': 5}
asdf = [v for k,v in d.items()] # [1, 5, 3]
fdsa = [k for k,v in d.items()] # ['a', 'e', 'c']