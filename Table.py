arg_names = ['a', 'b', 'c', 'd', 'e']


class Table:
	def __init__(self, n: int):
		self.n = n
		self.f_list = [0 for _ in range(1 << n)]
		self.arg_list = list()
		self.generate_arg_list()

	def generate_arg_list(self):
		# 2 в степени n
		for i in range(1 << self.n):
			row = [0 for _ in range(self.n)]

			j = self.n - 1
			num = i
			while num > 0:
				row[j] = num % 2
				j -= 1
				num //= 2

			self.arg_list.append(row)

	def set_f_list(self, new_f_list: list):
		# new_f_list len must be equals n
		if len(new_f_list) != len(self.f_list):
			raise RuntimeError("Не равные размеры")

		self.f_list = list(new_f_list)

	@staticmethod
	def row_to_cnf(arg_row: list) -> str:
		# arg_row : a,b,c,d,e
		# without f

		global arg_names
		cnf = list()
		for i in range(len(arg_row)):
			cnf.append("!" + arg_names[i] if arg_row[i] else arg_names[i])
		return '(' + "+".join(cnf) + ')'

	@staticmethod
	def row_to_dnf(arg_row: list) -> str:
		# arg_row : a,b,c,d,e
		# without f
		cnf = list()
		for i in range(len(arg_row)):
			cnf.append("!" + arg_names[i] if not arg_row[i] else arg_names[i])
		return '(' + "".join(cnf) + ')'

	def to_cnf(self) -> str:
		cnf_row = list()
		for i in range(1 << self.n):
			if not self.f_list[i]:
				cnf_row.append(Table.row_to_cnf(self.arg_list[i]))
		return " * ".join(cnf_row)

	def to_dnf(self) -> str:
		dnf_row = list()
		for i in range(1 << self.n):
			if self.f_list[i]:
				dnf_row.append(Table.row_to_dnf(self.arg_list[i]))
		return " + ".join(dnf_row)
