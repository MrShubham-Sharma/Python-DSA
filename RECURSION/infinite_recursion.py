count =0
def Greet():
    # we have to declear count as the global variable if not the we got UnboundLocalError 
    global count
    if count==4:
        return
    print("Hello")
    # the function called inside of the loop so it will continue prints the Hello
    count+=1
    # we declare the count before the function call to count 
    # if we declare after call it will stil work as infinite
    Greet()
# Loop will start when the function will get call
Greet()