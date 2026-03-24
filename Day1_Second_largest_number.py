arr = [1,3,2,4,87,9,5,6]

#if list size is 0 or 1 there is no second largest element in list
if len(arr) == 0 | len(arr) == 1:
  print(None)
  exit()

# if there are only two elements in list
first_largest = arr[0]
second_largest = arr[1]

if arr[1] > arr[0]:
  first_largest = arr[1]
  second_largest = arr[0]

# Targeting second element if first element is almost biggest then all others which are bigger than current second number will get escaped so targetting second element
for x in arr:
#Targeting second element based on current loop
  if second_largest < x :

    # if current element is bigger than first_element change both first element and second element both
    if x > first_largest:
      second_largest = first_largest
      first_largest = x

    # if current element is equal to first_element it should be escaped or passed without making any change
    elif x == first_largest :
      continue

    # if the condition is successfull and has enter in this condition it is definitley bigger than second largest so second largest is updated
    else:
      second_largest = x


print(second_largest)
