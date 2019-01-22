def is_well_formed(s):

	left_chars = []

	lookup = {'(':')', '{':'}', '[':']'}

	for c in s:
		if c in lookup:
			left_chars.append(c)
		elif len(left_chars) == 0 or lookup[left_chars.pop()] != c:
			return False
	return len(left_chars) == 0


print(is_well_formed('(((((')) #false
print(is_well_formed('[][][]')) #true
print(is_well_formed('[[]]]]]')) #false
print(is_well_formed(']'))#false
print(is_well_formed('['))#false
print(is_well_formed('{[()]}'))#true
print(is_well_formed('}])([{'))#false