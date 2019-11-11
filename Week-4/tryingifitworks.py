def concatenate_sentences(sentence1, sentence2):
    sentence1 = sentence1.strip() 
    sentence2 = sentence2.strip()
    
    other = ['.', '?', '!']
    if sentence1[0].isupper() and sentence1[-1] in other: 
        if sentence2[0].isupper() and sentence2[-1] in other: 
            return sentence1 + ' ' + sentence2
        else: 
            return 'Does not meet the criteria'  

