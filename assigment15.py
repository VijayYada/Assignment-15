

#1.import re

s= " zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")

result=p.match(s)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))
# print(result.group(8))
# print(result.group(9))

a=tuple([result.group(1),result.group(2),result.group(3)])
b=tuple([result.group(4),result.group(5),result.group(6)])
c=tuple([result.group(7),result.group(8),result.group(9)])

l=[]
l.append(a)
l.append(b)
l.append(c)
print(l)




2.import re
# s = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
#
# p= re.compile(r"b[i]t")
# result=p.finditer(s)
# for r in result:
#     print(r)
# a=re.compile(r"b[a-z][a-z][a-z][a-z][a-z]")
# file=a.finditer(s)
# for r in file:
#     print(r)
# b=re.compile(r"B[a-z][a-z][a-z]y")
# arr=b.finditer(s)
# for r in arr:
#     print(r)
# p= re.compile(r"B[u]t")
# result=p.finditer(s)
# for r in result:
#     print(r)

# p=re.compile(r"(.*)(.*)a(.*)of(.*),(.*)the(.*)was so (.*),So she (.*)some(.*)(.*),To make the(.*)(.*)(.*)")
#
# result=p.match(s)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))
# print(result.group(8))
# print(result.group(9))
# print(result.group(10))
# print(result.group(11))
# print(result.group(12))
# print(result.group(13))


s = 'Bettey bought a bit of butter but the butter was bitter so she bought some more butter to make bitter butter better'

p = re.compile(r"\b[Bb]\w+")

result = p.findall(s)

for r in result:
    print(r)
	

3.import re
sentence = "A, very very; irregular_sentence"

# p = re.compile(r"[^,;_]")
# result=p.finditer(sentence)
# for r in result:
#     print(r)

p=re.sub(",|;","","A, very very; irregular_sentence")
p=re.sub(r"_"," ",p)
print(p)



4.import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

p=re.sub("!|RT @TheNextWeb:|:|http://t.co/lbwej0pxOd cc: @garybernhardt #rstats","",'''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''')
# result=p.finditer(tweet)
# for r in result:
#     print(r)
print(p)



