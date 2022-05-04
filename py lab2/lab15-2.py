# generate a password with length "passlen" with no duplicate characters in the password

import random
password=[]

list1 = ["a", "b", "c","d"]
item1 = random.choices(list1,k=2)
random.shuffle(item1)

list2 = ["A", "B", "C","D"]
item2 = random.choices(list2,k=2)
random.shuffle(item2)

list3 = ["1", "2", "3","4"]
item3 = random.choices(list3,k=2)
random.shuffle(item3)

list4 = ["!", "#", "&","*"]
item4 = random.choices(list4,k=2)
random.shuffle(item4)

password= item1+item2+item3+item4
random.shuffle(password)
passw=''.join(password)
print('the creativly generated big brain password is :',passw)
