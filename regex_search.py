import re

def main():
  t ="The rain in Spain"
  
  p="^The.*Spain$"
  re_search(t, p)
  
  p='ai'
  re_findall(t, p)
  
  p ='Portugal'
  re_search(t, p)
  
  p='\s'
  re_search(t, p)
  
  re_split(t, p)
  
  re_split(t, p,1)
  
  nt = "9"
  re_sub(t,p,nt)
  re_sub(t,p,nt,2)
  
  p = r"\bS\w+"
  re_match(t, p)

def re_search(text, pattern):
  ''' The search() function searches the string for a match, and returns a Match object if there is a match.
      If there is more than one match, only the first occurrence of the match will be returned:
  '''
  x = re.search(pattern, text)
  
  if(x):
    print("We have a match!")
    print(f'The first "{pattern}" pattern is located in position {x.start()}')

  else:
    print("No Match")
 
def re_findall(text, pattern):
  x = re.findall(pattern, text)
  print(x)

def re_split(text, pattern,max_count=0):
  '''The split() function returns a list where the string has been split at each match:
    You can control the number of occurrences by specifying the maxsplit parameter:
  '''
  x = re.split(pattern, text,max_count)
  print(x)
  
def re_sub(text, pattern, newtext, max_count=0):
  x = re.sub(pattern,newtext, text, max_count)
  print (x)
  
def re_match(text, pattern):
  '''
  The Match object has properties and methods used to retrieve information about the search, and the result:
  .span() returns a tuple containing the start-, and end positions of the match.
  .string returns the string passed into the function
  .group() returns the part of the string where there was a match
  
  '''
  x = re.search(pattern, text)
  print(f'span ={x.span()}')
  print(f'group = {x.group()}')
  print(f'string = {x.string}')
  
  
if __name__ =='__main__':main()