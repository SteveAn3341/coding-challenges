# return a sting that appears most time and appers the second most time 

arr = ["1","3","4","3","3","1"]


def find_most_frequent(arr):
    # Count the frequency of each number
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Sort items by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Return the most frequent element
    if sorted_frequency:
        return sorted_frequency[0][0]  # Correct for the most frequent
    else:
        return None

# Example
arr = ["1", "3", "4", "3", "3", "1"]
print(find_most_frequent(arr))