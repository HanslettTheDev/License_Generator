def verify(self, key):
    global score 
    score = 0

    check_digit = key[2] # check digit key
    check_digit_2 = key[8]
    count_1 = 0 # check digit count
    count_2 = 0

    # get the chunks by using the split method and use a for loop to check the digit
    chunks = key.split("-")
    print(chunks)
    for chunk in chunks:
        if len(chunk) != 5:
            return False
        
        for char in chunk:
            if char == check_digit:
                count_1 += 1
            if char == check_digit_2:
                count_2 += 1
            score += ord(char) # convert each char to a score 
    
    # rules
    if score > 2200 and score < 2300 and count_1 == 4 and count_2 == 2:
        return True
    else:
        return False   
                