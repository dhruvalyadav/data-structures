# in the given string find the same characters when the string i reversed.
# for example, s=alphxxdida the output should be 4 as when reversed, characters gets repeated

# this is a 2 pointer type approach that has one pointer at start and end at last
s="alphxxdida"
count=0
for i in range(0,len(s)):
    if(s[i]==s[len(s)-i-1]):
        count+=1
print(count)

#2
# from the input of arrays, take another number as k. th main task is to find the number of numbers that is less than k value and print the count

a = [1,7,4,5,6,3,2]
k=5
count=0
for i in range(len(a)):
    if(a[i]<k):
        count+=1
print(count)

#3
#given an array . we just have to print the index values of arrays of number
a = [30,20,40,55,25]
for i in range(len(a)):
    print(i,end=" ")

#4
# eliminate vowels and print only consosnets from the given string

s="Hello"
ans=""
vov=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i not in vov:
        ans+=i
print(ans)

#5
#