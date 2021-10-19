# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE

  n = list(str(n))
  diction = {}
  diction[3] = diction[6] = diction[9] = 0
#for loop
  for i in n:
      k = int(i)
      #if k/3 = 0 and k != 0 then add k+1 to the k position
      if k % 3 == 0 and k != 0:
        diction[k] = diction[k] + 1
#initialize variables
  max = -1
  index = -1
#loop to find max
  for j,v in diction.items():
    #if v position is greater than current max, set max to v position and index to j
    if v > max:
      max = v
      index = j
  return index
# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  x = list(s)
  y = len(s)
  count = 1
#create dictionary
  diction = {}
#for loop
  for i in range (0, y - 1):
    #if current i position != the next i position then continue
    if (x[i] != x[i+1]):
      if (x[i] in diction and diction[x[i]] > count):
        continue
      #else
      else:
        diction[x[i]] = count
        count = 1
    #else add to count
    else:
      count = count + 1
  diction[x[y-1]] = count
#initialize variable
  max = -1
#find max
  for j, k in diction.items():
    #if k is greater than max set new max to k
    if k > max:
      max = k
  #create list
  lst = []
  #for loop
  for j, k in diction.items():
    #if k id equal to max then add j to list
    if k == max:
      lst.append(j)

  return lst

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  s = s.replace(" ", "");
  s = s.lower()

  return s == s[::-1]
