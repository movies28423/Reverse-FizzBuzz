	fizz_buzz_text = open(r'fizz_buzz.txt','r')
	fizz_buzz_info = fizz_buzz_text.readline().split(' ')
	fizz_buzz_words = int(fizz_buzz_info[0])
	fizz_buzz_length = int(fizz_buzz_info[1].strip('\n'))
	fizz_buzz_word_pos_list = {}
	fizz_buzz = fizz_buzz_text.readlines()
	i = 0
	for line in fizz_buzz:
		words = line.strip('\n').split(' ')
		for word in words:
			if word in fizz_buzz_word_pos_list.keys():
				fizz_buzz_word_pos_list[word].append(i)
			else:
				fizz_buzz_word_pos_list.update({word:[i]})
		i+= 1

	for word in fizz_buzz_word_pos_list.keys():
		word_count = len(fizz_buzz_word_pos_list[word])
		word_divisor = int((fizz_buzz_length -(fizz_buzz_length % word_count))/word_count)
		print(word + ': ' + str(word_divisor))
