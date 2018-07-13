
def main():
    counter = 2520
    done = False
    print("Calculating.")
    while done == False:
        x = 2
        while x <= 20:
            if counter % x == 0:
                if x == 20:
                    done = True
                else:
                    x+=1
            else:
                print(counter, "is incorrect")
                counter +=20
                x=2
    print(counter)

main()
                
            
            
        
