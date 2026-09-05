count =0
def Greet():
    global count
    if count==4:
        return
    print("Hello")
    # the function called inside of the loop so it will continue prints the Hello
    count+=1
    Greet()
# Loop will start when the function will get call
Greet()