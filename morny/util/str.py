def strm(*strs: str) -> str:
	output: str = ""
	for i in range(len(strs)-1):
		output += strs[i]
		output += "\n"
	output += strs[len(strs)-1]
	return output

# test for this
if __name__ == "__main__":
	
	print(strm(
		"Aaa",
		"  bbb",
		"  ccc",
		"Xxx",
		"  yyy"
	))
	