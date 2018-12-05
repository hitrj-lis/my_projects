string_list = []
error_syntax = "error_syntax"
sp = ">>"
point = "."
string = input(">> : ")
split_1 = string.split()
len_string = len(split_1)
print(len_string)
print(split_1)
for _ in split_1:
	if sp in _:
		split_2 = _.split(">>")
		print("s2", split_2)
	else:
		print(error_syntax)
		break
	for i in split_2:
		if point in i:
			split_3 = i.split(".")
			print("s3", split_3)
			string_list.append(split_3)
		else:
				string_list.append(i)
	print("string=", string_list)
