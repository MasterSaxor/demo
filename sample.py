def search(alist, num):
  """
  Search a number from a given list

  Precondition: alist should not be empty
  Postcondition: Return True if num exists otherwise False
  """

  if len(alist) == 0:
    return False
  
  for val in alist:
    if num == val:
      return True
  return False
