sub1=int(input("enter your first score"))
sub2=int(input("enter your second score"))
sub3=int(input("enter your third score"))
sub4=int(input("enter your fourth score"))
sub5=int(input("enter your fifth score"))
total=sub1+sub2+sub3+sub4+sub5
average=total/5
print("your average is",average)

if average>=80:
 print("mastery")
elif average>=75:
  
 print("proficient")
elif average>=65:
   print("competent")
elif average>=49:
 print("not yet competent")
else:
  print("no such values")
