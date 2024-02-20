import sys

# try:
#     print(f"Hello, {sys.argv[1]}")
    
# except IndexError:
#     sys.exit("Too few argument")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#sys.argv.pop(0)
for arg in sys.argv[1:]:

#else:
    #print(f"Hello, {sys.argv[1]}")
    
    print(f"Hello, {arg}")
    
    
    


    

