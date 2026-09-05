def greet(count):
    if count == 4:
        return
    count += 1
    greet(count)     # Fixed: Passed 'count' to the recursive call
    # here the count will be count till 0,1,2,3,4 the functions and 
    # then afer the calling all function it will print an "hello"
    print("hello")
greet(0)            # Fixed: Passed the initial value (0) to start