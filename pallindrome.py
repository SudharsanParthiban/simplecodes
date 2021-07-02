def pallindrome(n):
  temp=n
  rev=0
  while(t>0):
    digit=temp%10
    rev=rev*10+digit
    t=t//10
  if(rev==n):
    return 1
  else:
    return 0
  
n=int(input())
if(pallindrome(n)):
  print("The Given number is Pallindrome")
else:
  print("The Given number is not Pallindrome")
