s = 'aaron'

def balancedStringSplit(s): 
  count=0 
  re=0 
  for i in s: 
    if i=='R': 
      count+=1 
    if i=='L': 
      count-=1 
    if count==0: 
      re+=1 
  return re 
