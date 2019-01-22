def permuate(stringF):
	def helper(s, chosen):
		if len(s) == 0: #
			perms.append(chosen)
		else:
			#choose/explore/unchoose
			#try all possible letters that could come next
			for i in range(len(s)):
				char = s[i] #choose
				chosen += char
				#remove char from s
				indOfChar = s.find(char)
				s = s[:indOfChar] + s[indOfChar+1:]
				helper(s, chosen) #explore

				s = s[:i] + chosen + s[i+1:]

				indOfChar = chosen.find(char)
				s = chosen[:indOfChar] + chosen[indOfChar+1:]


	
	perms = []
	helper(stringF, "")	

	print(perms)


permuate("MARTY")