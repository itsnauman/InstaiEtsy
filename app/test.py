# def keywordAlgo(ARR):
# 	master = []
#     start = ARR[0]
# 	    for i in range(1,4):
# 	        current = ARR[i]
# 	        next = ARR[i+1]
# 	        for j in current:
# 	            for k in next:
# 	                if (j==k) & (j in start):
# 	                    master.append(j)

# 	    	start = current
#     return (master)

def keywordAlgo2(ARR):
	rough = ARR[0]+ARR[1]+ARR[2]+ARR[3]+ARR[4]
	master = {}
	master[rough[0]] = 0

	for element in rough:
		if not element in master:
			master[element] = 1
		else:
			master[element] += 1
	print (master)
	
	MASTER = {}
	cutoff = (1/2)
	for entry in master:
		if ((int(entry.value())/(len(master)) >= cutoff):
			MASTER[j] = k

	return 0

def keywordAlgo(liked_media):
    rough = []
    master = {}
    master[rough[0]] = 0
    for i in range(0,4):
        range.append(tag5(get_tags_for_photo(liked_media[i])))

    for element in rough:
        if not element in master:
            master[element] = 1
        else:
            master[element] += 1

    return (master)
    
def main():
	arr1 = ['cat', 'dog', 'poop', 'cabbage', 'yo']
	arr2 = ['dog', 'rice', 'coffee', 'nyc', 'git']
	arr3 = ['go', 'cat', 'cop', 'doctor', 'coffee']
	arr4 = ['wait', 'coffee', 'wait', 'doctor', 'where']
	arr5 = ['coffee', 'island', 'git', 'lose', 'coffee']

	ARR = [arr1, arr2, arr3, arr4, arr5]
	keywordAlgo2(ARR)

main()