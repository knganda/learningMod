def main():
    x = get_int("What's x? ")
    print(f"The number entered is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))   
            break 
            # return int(input("What's x? "))
        except ValueError:
            #continue
            #print("x is not an integer") 
            pass
        # else:
        #     break
    return x

if __name__=="__main__":
    main()
    

    
    

