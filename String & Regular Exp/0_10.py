#Count the occurrences of each word in a given sentence
str='sachin ramesh sachin'

#counts = dict()
counts = {}

words = str.split()

for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    
print(counts)

