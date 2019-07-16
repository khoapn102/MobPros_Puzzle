"""
	Khoa Phan - July 15th, 2019
	Python 3.xx
"""
import sys


def solve(file_name):

	class Tree:
		def __init__(self, licFile):
			"""
			Initializing function for Tree object
			:param licFile: License data file consists of HEADER number for parsing
			"""
			self.nNodes = licFile.pop(0)
			nMeta = licFile.pop(0)
			self.nodes = [Tree(licFile) for i in range(self.nNodes)]
			self.metadata = [licFile.pop(0) for j in range(nMeta)]

		# Part 1
		def cal_sum_metadata(self):
			"""
			Calculate the sum of the metadata of all nodes in the Tree using recursive
			:return: Sum of all metadata
			"""
			return sum(self.metadata) + sum(node.cal_sum_metadata() for node in self.nodes)

		# Part 2
		def cal_root_value(self):
			"""
			Calculate root value from all its nodes' metadata values using recursive
			:return: Root value
			"""
			if not self.nNodes:
				return sum(self.metadata)
			return sum([0 if (node_idx - 1) >= self.nNodes else\
				            self.nodes[node_idx - 1].cal_root_value()\
			                        for node_idx in self.metadata])

	# Reading input File
	licenseFile = []
	with open(file_name, 'r') as readfile:
		licenseFile = [int(num) for line in readfile for num in line.strip().split(' ')]
	result = Tree(licenseFile)
	print("Part 1: Sum of the metadata is {}.".format(result.cal_sum_metadata()))
	print("Part 2: The value of root node is {}.".format(result.cal_root_value()))


if __name__ == "__main__":
	try:
		arg = sys.argv[1]
		solve(arg)
	except:
		print("There is no existing file or faulty input, please check !!")

