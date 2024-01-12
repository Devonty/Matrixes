from Table import Table


if __name__ == '__main__':
	with open("paintMatrix.txt", "r") as file:
		f_list = list(map(int, (file.readline().split())))

	my_table = Table(2)
	my_table.set_f_list(f_list)

	print("cnf:")
	print(my_table.to_cnf())

	print("dnf:")
	print(my_table.to_dnf())

	print("f:")
	print(my_table.f_list)

	print("args:")
	print("\n".join(map(list.__str__, my_table.arg_list)))
