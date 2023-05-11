def strm(*strs: str) -> str:
	output: str = ""
	for i in range(len(strs)-1):
		output += strs[i]
		output += "\n"
	output += strs[len(strs)-1]
	return output