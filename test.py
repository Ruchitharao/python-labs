#we will be discussing about return and print inside a function

def sum(a,b):
    try:
        c=a+b
        # print(c)
        return c
    except:
        # print('error occured')
        return "error"
sum(2,5)