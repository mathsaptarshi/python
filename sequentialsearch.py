def sequentialsearch(list,item):
	pos = 0
	found=False
	while pos < len(list) and not found:
		if list[pos]==item:
			found =True
		else:
			pos=pos+1
	return found
'''testlist=[9,8,7,6,5,4,55,44,66]
print(sequentialsearch(testlist,565))'''

if __name__=="__main__":
	shopping=["apple","banana","chocolate","pasta"]
	item = input("what do you want to find ?")
	isitfound = sequentialsearch(shopping,item)
	if isitfound:
		print("Your item is in your list.")
	else:
		print("your item is not in the list.")