//Approach A
def TwoPassFrequencySearch(s):
    n = len(s)
    CharCounts = {}
    
    for i in range(n):
        current_char = s[i]
        if current_char in CharCounts:
            CharCounts[current_char] += 1
        else:
            CharCounts[current_char] = 1
            
    for i in range(n):
        current_char = s[i]
        if CharCounts[current_char] == 1:
            return i
            
    return -1


//Approach B
def OrderedMapSearch(s):
    n = len(s)
    OrderedCounts = {}
    
    for i in range(n):
        current_char = s[i]
        if current_char in OrderedCounts:
            OrderedCounts[current_char]['count'] += 1
        else:
            OrderedCounts[current_char] = {'count': 1, 'first_index': i}
            
    for key in OrderedCounts:
        if OrderedCounts[key]['count'] == 1:
            return OrderedCounts[key]['first_index']
            
    return -1
