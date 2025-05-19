def decode(message_file):
    with open(message_file, 'r') as f:
        message_dict = {}
        for line in f:
            number, word = line.split()
            message_dict[int(number)] = word
    
    total = len(message_dict)
    last_numbers = []
    current_num = 1
    next_num = 1
    while next_num <= total:
        line_end = next_num + current_num -1
        if line_end > total:
            break
        last_numbers.append(line_end)
        next_num = line_end + 1
        current_num += 1

    encoded_message = [message_dict[num] for num in sorted(last_numbers)]
    return ' '.join(encoded_message)