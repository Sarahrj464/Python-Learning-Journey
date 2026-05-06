# palindrome ---> from start and from end we have shown same sequence of elements
# palindrome --> copy -- reverse

# list1=[1,2,1]
# list2=[1,2,3]
# copy_list2=list2.copy()
# copy_list2.reverse()

# if(copy_list2 == list2):
#   print("palindrome")
# else:
#   print("not palindrome")



list = [1,"abc",1]
copy_list=list.copy()
copy_list.reverse()

if(copy_list == list):
  print("palindrome")
else:
  print("not palindrome")
