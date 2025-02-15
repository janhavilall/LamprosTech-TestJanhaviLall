def top_k_frequent_elements(nums, k):
    
    # empty dictinary to store count of each number
    freq_map = {}  # store as {5: 3, 2: 1, 3: 2, 1: 1} (e.g. 5 appears 3 times)

    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    # freq_map.keys() - gives unique numbers [5,2,3,1]
    # will sort based on frequency
    sorted_list = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
    
    return sorted_list[:k]

# list of numbers
nums = [5, 2, 5, 3, 5, 3, 1]

# number of most frequent elements we want
k = 2  

print(top_k_frequent_elements(nums, k)) 
