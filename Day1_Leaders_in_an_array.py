arr = [12, -3, 7, 0, 25, 18, -10, 5, 42, 7, 3, 99, -1]

# if list is empty break the program and return nothing
if len(arr)==0:
  exit()

''' as we have to find leaders in this list Means ---> In array a element will be called a leader if there is no element bigger than that after his position
so he will be called leader upto that position.        Examples --->

[16, 17, 4, 3, 5, 2] ---> [17, 5, 2]
[1, 2, 3, 4, 5, 2] ----> [5, 2]

'''

# copying arr into a different array
reversed_arr = arr.copy()

#reversing the array for choosing leader from last 
reversed_arr.reverse()

# the last element is going to be automatic a leader
leader = reversed_arr[0]

# this is going to be a list of all leader which already include the last element which comes as a automatic leader
leader_list = [leader]

# For loop for checking the next leader in the list which is bigger element to be called next leader
for x in reversed_arr:
  if x > leader:
    leader = x
    leader_list.append(x)

# reverse the leader list to represent it in order it was
leader_list.reverse()
print(leader_list)
  
