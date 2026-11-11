def my_function(string):
    if (string==string[::-1]):
        return "True"
    elif (string=="stop"):
        print("End")
    else:
        return "False" 
 

print("This will check if your word is a pallendrom or not, type in 'stop' to end.")
while (True):
    string = input("Enter string: ")
    if (string!="stop"):
      my_function(string)
    else:
        print("End")
        break
    print(my_function(string))
    

