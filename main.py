print("welcome to the test")
name1 = input("please enter the first name: ")
name2 = input("please enter the second name: ")

combo = name1+name2
lowercombined = combo.lower()

c = lowercombined.count("c")
o = lowercombined.count("o")
m = lowercombined.count("m")
p = lowercombined.count("p")
a = lowercombined.count("a")
t = lowercombined.count("t")
i = lowercombined.count("i")
b = lowercombined.count("b")
l = lowercombined.count("l")
e = lowercombined.count("e")

compatible = c+o+m+p+a+t+i+b+l+e


if compatible < 8:
    print("you scored: ", compatible, "so you guys are not compatible")

else:
    print("you scored: ", compatible, "so you guys are very compatible")