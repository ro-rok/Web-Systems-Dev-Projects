a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    
    #rk868 09/24/2023

    ans=[]
    for x in arr:
        if type(x)== int or type(x)== float:
            ans+=[abs(x)]
        elif type(x)== str:
            try:
                ans+=[str(abs(int(x)))]
            except:
                print("Error: {} is not a number".format(x))
        else:
            print("Error: {} is not a number".format(x))
    print(ans)    

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
