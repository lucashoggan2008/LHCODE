def encode(text):
	answer =""
	for let in text:
		if let == 'a':
			answer += '!'
		if let == 'b':
			answer += 'h'
		if let == 'c':
			answer += 'i'
		if let == 'd':
			answer += 'j'
		if let == 'e':
			answer += '"'
		if let == 'f':
			answer += 'l'
		if let == 'g':
			answer += 'm'
		if let == 'h':
			answer += 'n'
		if let == 'i':
			answer += '£'
		if let == 'j':
			answer += 'p'
		if let == 'k':
			answer += 'q'
		if let == 'l':
			answer += 'r'
		if let == 'm':
			answer += 's'
		if let == 'n':
			answer += 't'
		if let == 'o':
			answer += '$'
		if let == 'p':
			answer += 'v'
		if let == 'q':
			answer += 'w'
		if let == 'r':
			answer += 'x'
		if let == 's':
			answer += 'y'
		if let == 't':
			answer += 'z'
		if let == 'u':
			answer += '%'
		if let == 'v':
			answer += 'b'
		if let == 'w':
			answer += 'c'
		if let == 'x':
			answer += 'd'
		if let == 'y':
			answer += 'e'
		if let == 'z':
			answer += 'f'
		if let == ' ':
			answer += '^'
		if let == '.':
			answer += '&'
		if let == ',':
			answer += '*'
		if let == '@':
			answer += '('
		if let == '#':
			answer += ')'
		if let == '.':
			answer += '&'
		if let == ':':
			answer += '-'
		if let == '(':
			answer += '@'
		if let == ')':
			answer += '#'
			
		
		
	return answer
		
def decode(text):
		answer = ''
		for let in text:
			if let == '!':
				answer += 'a'
			if let == 'h':
				answer += 'b'
			if let == 'i':
				answer += 'c'
			if let == 'j':
				answer += 'd'
			if let == '"':
				answer += 'e'
			if let == 'l':
				answer += 'f'
			if let == 'm':
				answer += 'g'
			if let == 'n':
				answer += 'h'
			if let == '£':
				answer += 'i'
			if let == 'p':
				answer += 'j'
			if let == 'q':
					answer += 'k'
			if let == 'r':
				answer += 'l'
			if let == 's':
				answer += 'm'
			if let == 't':
				answer += 'n'
			if let == '$':
				answer += 'o'
			if let == 'v':
				answer += 'p'
			if let == 'w':
				answer += 'q'
			if let == 'x':
				answer += 'r'
			if let == 'y':
				answer += 's'
			if let == 'z':
				answer += 't'
			if let == '%':
				answer += 'u'
			if let == 'b':
				answer += 'v'
			if let == 'c':
				answer += 'w'
			if let == 'd':
				answer += 'x'
			if let == 'e':
				answer += 'y'
			if let == 'f':
				answer += 'z'
			if let == '^':
				answer += ' '
			if let == '&':
				answer += '.'
			if let == '*':
				answer += ','
			if let == '(':
				answer += '@'
			if let == ')':
				answer += '#'
			if let == '-':
				answer += ':'
			if let == '@':
				answer += '('
			if let == '#':
				answer += ')'
	
	
				answer += ' None '	
		
		
		
		return answer
		

			
			
			
		
		
		