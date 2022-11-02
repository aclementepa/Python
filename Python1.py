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

str1 = "ABC"
str2 = "123"
yak1 = {str1[i]: str2[i] for i in range(0,len(str2))} # {'A': '1', 'B': '2', 'C': '3'}

num_list = [1,2,3,4]
# print({num:("even" if num % 2 == 0 else "odd") for num in num_list})
yak2 = {num:("even" if num % 2 == 0 else "odd") for num in num_list}

# for key,val in yak2.items():
#     print(val)

x = (1,2,3)
if(3 in x ):
    print(x)
