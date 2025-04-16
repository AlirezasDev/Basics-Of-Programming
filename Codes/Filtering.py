def remaining_statues(heights, index, max_height):
    if index < 0:
        return []
    
    current_height = heights[index]
    
    if current_height > max_height:
        return [current_height] + remaining_statues(heights, index - 1, current_height)
    else:
        return remaining_statues(heights, index - 1, max_height)

input_data = input()
heights = list(map(int, input_data.split(',')))
result = remaining_statues(heights, len(heights) - 1, float('-inf'))
print(list(reversed(result)))
