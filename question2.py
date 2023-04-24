# question 2
about_me = '''Hey,<name> Here!
My SID is <sid>
I am from <department> department and my CGPA is <cgpa>
'''
# here about_me is a variable 
# here we are using '''  ''' three quotes strings because we need multiple line string
name = input("enter your name:")
sid = input("enter your sid:")
department = input("enter your department:")
cgpa = input("enter your cgpa:")
# here we are taking input from the user about his details and further we will replace them 

about_me = about_me.replace("<name>",name)
about_me = about_me.replace("<sid>",sid)
about_me = about_me.replace("<department>",department)
about_me = about_me.replace("<cgpa>",cgpa)
# here we are using replace function in a string
print(about_me)