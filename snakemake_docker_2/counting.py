for _file in snakemake.input:
	ans = {}
	with open(_file) as f:
		_file_name = _file.replace("input/", "")
		text = f.read().lower()
		chars = ''.join(x for x in text if x.isalpha())
		filtered_chars = list(set(chars))
		filtered_chars.sort()
		for char in filtered_chars:
			ans[char] = chars.count(char)
			with open("output/" + _file_name, 'w') as out_file:
				for item in ans.items():
					out_file.write(f"{item[0]}:{item[1]}\n")
