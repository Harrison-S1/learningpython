user_input = input ("Enter your name: ")
#Works with python 2 and 3.0
message = "Hello %s!" % user_input
#Works with python 3.6 and above
message = f"Hello {user_input}"
print (message)