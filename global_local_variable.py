'''def f():
	print(str)
str = "I am a global variable"
f()'''


'''def f():
	str = "I am a local variable"
	print(str)
str = "I am a global variable"
f()'''

def f():
	global s
	print(s)#in this case we need to make s as global
	s = "Me too."
	print(s)
# Global scope
s = "Python is Great"
f()
print(s)