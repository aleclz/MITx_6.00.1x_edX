# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:57:47 2020

@author: azucker
"""

varA = -9
varB = "adios"

if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    print("wrong")
    
    if type(varA) == str or type(varB) == str:
    print("string involved")
elif int(varA) > int(varB):
    print("bigger")
elif int(varA) == int(varB) :
    print("equal")
else :
print("smaller")

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

num = 10
while num > 3:
    num -= 1
    print(num) 
    
 num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')


count = 2
while count <= 10:
    print(count)
    count += 2
print("Goodbye!")


print("Hello!")
count = 10
while count >= 2:
    print(count)
    count -= 2
  #  break

end = 6
count = 1
total = sum(count)
while count <= end:
   # 1+count
    count += 1
print(str(total))


x = 1
num = 1
i = 1
end = 6

while i < end:
    num += i+1
    i += 1
print(num) 

end = 6
num = 0

for i in range(num, end+1):
    #num += x
    num += i
print(num)


num = 10
for num in range(5):
    print(num)
print(num)

1






for n in range(11, 2, 2):
    print(n)
   # n += 2
print("Goodbye!")


print("Hello!")
for n in range(10, 1, -2):
    print(n)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)


e , e, l, l, l, o, !, ! done



greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')


iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        


count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))







count = 0

for i in 'snhoweuoilsdfaadsuf':
    if i=='e':
        print(count)
    count += 1
    
    print("Number of vowels: " + str(count))



n = 2
while n > 0:
        n -= 1
        print(n)



def main():
	#use a for loop over a collection
	Months = ["Jan","Feb","Mar","April","May","June"]
	for i, m in enumerate (Months):
		print(i,m)

		
if __name__ == "__main__":
	main()


for i in '123':
    print("guru99",i)


total = 0
for item in range(1,5):
    total = total + item

print(total)
#############################################################

x = 3
ans = 0
itersLeft = x

while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + '=' + str(ans))



s = 'hboboboobobpoboobdbobobobwo' #correct answer is 6
print(len(s))
x = 0
letter = 0
while (x <= len(s)):
    str(s.count('bob'))
    letter = x+letter
print("Number of times bob occurs is: " + str(s.count('bob')))

s = 'hboboboobobpoboobdbobobobwo' #correct answer is 6
counter = 0

for i in s:
    print(i)
    while counter <= len(s):
        s.count('bob')
        counter +=1
        print(s.count)
print(counter)



iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 


























































