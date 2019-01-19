def evaluate(RPN_EXPRESSION):
	int_results = []
	delim = ','
	operators = {
		'+': lambda y, x: x + y, '-': lambda y, x: x-y, '*':
		lambda y, x: x*y, '/':lambda y, x: int(x/y)
	}

	for token in RPN_EXPRESSION.split(delim):
		if token in operators:
			int_results.append(operators[token](int_results.pop(), int_results.pop()))
		else: #token is a number
			int_results.append(int(token))
	return int_results[-1]


print(evaluate('5,10,+,2,*,3,/'))