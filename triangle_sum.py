import math as m
#create triangle
triangle_text = open("triangle.txt", "r")
rows = []
for line in triangle_text:
    line = line.rstrip()
    rows.append(line.split(' '))

triangle_text.close()

#rows will be a crude tree
# print(rows)

#function to compare which child node to check next?
# def get_higher_child(parent_row, parent_index):
#     if parent_row < len(rows):
#         if rows[parent_row+1][parent_index] > rows[parent_row+1][parent_index+1]:
#             return rows[parent_row+1][parent_index]
#         else:
#             return rows[parent_row+1][parent_index+1]
#     else:
#         return -1

# def add_value_to_stack(stack, parent_row, parent_index):
#     if parent_row < len(rows):
#         stack.append(rows[parent_row+1][parent_index])
#         stack.append(rows[parent_row+1][parent_index+1])

# to_check = []
# curr_total = 0
# max_total = -1
# to_check.append(rows[0][0]) #add root
# while to_check != []:
#     add_value_to_stack(to_check, )
# row_sums = []




#iterate over each row, at the completion of each row, we should have a new
# "squashed" row
total_squashed_row = []
for i in range(len(rows)-1, 0, -1):
    # print("i = " + str(i))
    curr_squashed_row = []
    curr_range = m.ceil(len(total_squashed_row)/len(rows[i-1]))
    for j in range(len(rows[i-1])):
        curr_value = int(rows[i-1][j])
        #need to add curr value to the range applicable
        start = j*curr_range
        #initialize total_squashed_row (first pass, its ugly im sorry)
        if total_squashed_row == []:
            curr_squashed_row.append(curr_value+int(rows[i][j]))
            curr_squashed_row.append(curr_value+int(rows[i][j+1]))
        else:
            for k in range(start, (j+1)*curr_range):
                curr_squashed_row.append(curr_value+int(total_squashed_row[k]))

    total_squashed_row = curr_squashed_row

print(max(total_squashed_row))




        # curr_value = int(total_squashed_row[j])

        # print('parent = ' + str(curr_value))
        # print('child one = ' + str(rows[i+1][j]))
        # print('child two = ' + str(rows[i+1][j+1]))

        # child_one_value = curr_value + int(rows[i+1][j])
        # child_two_value = curr_value + int(rows[i+1][j+1])
        # curr_squashed_row.append(child_one_value)
        # curr_squashed_row.append(child_two_value)
    #     total_squashed_row = curr_squashed_row
    # row_sums.append(curr_squashed_row)

# print(row_sums)