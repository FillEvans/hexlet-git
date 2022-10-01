def find_index(i, text):
    for (index, elem) in enumerate(text):
        if elem == i:
            return index
            
            
print(find_index('t', 'cat'))