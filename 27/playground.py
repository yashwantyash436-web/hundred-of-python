# def add(*args):
#     sum=0
#     for n in args:
#         sum+=n
#     return sum    

# print(add(3,4,6,6))
        

# def multiply(*args):
#     sum=1
#     for n in args:
#         sum *=n
#     return sum

# print(multiply(2,4))
    
    
# def calculate( n,**kwargs):

#     # for key,value in kwargs.items():
#     #     print(value)
#     #     print(key)
#     n +=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)
# calculate(3,add=3 , multiply=5)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)