#Hello
#Welcome to my first repo

def part_1():
    #Part 1

    print ('Student Version\n')

    #Input credits
    pass_credit = int(input('Please enter your credits at pass: '))
    defer_credit = int(input('Plese enter your credits at defer: '))
    fail_credit = int(input('Plese enter your credits at fail: '))

    #Display Progression Outcome
    if pass_credit == 120: #If pass credit equals to 120, it will be a progress
        print('Progress\n')
    elif pass_credit > 99: #If pass credit is between 99 and 120, it will be a trailer
        print('Progress (module trailer)\n')
    elif fail_credit > 79: #If fail credit is more that 79, it will be an exclude
        print('Exclude\n')
    elif pass_credit < 81: #If pass credit is less than 81, it wil be a retriver
        print('Do not Progress - module retriever\n')

######################################################################################################################################

def part_2():
    #Part 2

    #The program will display ‘Integer required’ if a credit input is the wrong data type
    def type_error():
        print('integer required\n')

    #The program will display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120.
    def out_of_range_error():
        print('out of range\n')
        
    #If there is another error instead of type_error and out_of_range_error the program will display an unexpected error.
    def unexpected_error():
        print('An unexpected error has occured\n')

    print ('Student Version (Validation)\n')

    main_loop = 0
    while main_loop == 0:

        #Input credits
        sub_loop1 = 0
        while sub_loop1 == 0:
            
            try:
                pass_credit = int(input('Please enter your credits at pass: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if pass_credit >= 0 and pass_credit <= 120 and pass_credit % 20 == 0: #If pass credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop1 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop1 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop1 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop1 = 0

        sub_loop2 = 0    
        while sub_loop2 ==0:
            
            try:
                defer_credit = int(input('Please enter your credits at defer: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if defer_credit >= 0 and defer_credit <= 120 and defer_credit % 20 == 0: #If defer credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop2 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop2 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop2 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop2 = 0

        sub_loop3 = 0    
        while sub_loop3 == 0:
            
            try:
                fail_credit = int(input('Please enter your credits at fail: '))

                try:
                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if fail_credit >= 0 and fail_credit <= 120 and fail_credit % 20 == 0: #If fail credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop3 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop3 = 0
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop3 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop3 = 0

        #Check Whether The Total Is Incorrect
        total = pass_credit + defer_credit + fail_credit
        
        if total != 120:
            print('Total incorrect\n') #If the total of pass,defer and fail do not equal 120, the main loop will run again
            main_loop = 0
        else:
            main_loop = 1 #If the total is correct, the main loop will break

    #Display Progression Outcome
    if pass_credit == 120: #If pass credit equals to 120, it will be a progress
        print('Progress\n')
    elif pass_credit > 99: #If pass credit is between 99 and 120, it will be a trailer
        print('Progress (module trailer)\n')
    elif fail_credit > 79: #If fail credit is more that 79, it will be an exclude
        print('Exclude\n')
    elif pass_credit < 81: #If pass credit is less than 81, it wil be a retriver
        print('Do not Progress - module retriever\n')

######################################################################################################################################

def part_3():
    #Part 3


    #The program will display ‘Integer required’ if a credit input is the wrong data type
    def type_error():
        print('integer required\n')

    #The program will display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120.
    def out_of_range_error():
        print('out of range\n')
        
    #If there is another error instead of type_error and out_of_range_error the program will display an unexpected error.
    def unexpected_error():
        print('An unexpected error has occured\n')

    #Print stars in the Horizontal Histogram
    def print_stars (progression_outcome):
        for x in range(0, progression_outcome):
            print('*', end = '')
        print(end = '\n')

    #Assign Ranges
    progress = 0
    trailer = 0
    exclude = 0
    retriver = 0
        
    print ('Staff Version with Histogram\n')

    main_loop = 0
    while main_loop == 0:

        #Input credits
        sub_loop1 = 0
        while sub_loop1 == 0:
            
            try:
                pass_credit = int(input('Please enter your credits at pass: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if pass_credit >= 0 and pass_credit <= 120 and pass_credit % 20 == 0:  #If pass credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop1 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop1 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop1 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop1 = 0

        sub_loop2 = 0    
        while sub_loop2 == 0:
            
            try:
                defer_credit = int(input('Please enter your credits at defer: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if defer_credit >= 0 and defer_credit <= 120 and defer_credit % 20 == 0: #If defer credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop2 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop2 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop2 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop2 = 0

        sub_loop3 = 0    
        while sub_loop3 == 0:
            
            try:
                fail_credit = int(input('Please enter your credits at fail: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if fail_credit >= 0 and fail_credit <= 120 and fail_credit % 20 == 0: #If defer credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop3 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop3 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop3 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop3 = 0

        #Check Whether The Total Is Incorrect
        total = pass_credit + defer_credit + fail_credit
        
        if total != 120:
            print('Total incorrect\n') #If the total of pass,defer and fail do not equal 120, the main loop will run again
            main_loop = 0
        else:
            main_loop = 1 #If the total is correct, the main loop will break
        
        #Display Progression Outcome
        if pass_credit == 120: #If pass credit equals to 120, it will be a progress
            print('Progress\n')
            progress = progress+1
        elif pass_credit > 99: #If pass credit is between 99 and 120, it will be a trailer
            print('Progress (module trailer)\n')
            trailer = trailer + 1
        elif fail_credit > 79: #If fail credit is more that 79, it will be an exclude
            print('Exclude\n')
            exclude = exclude + 1
        elif pass_credit < 81: #If pass credit is less than 81, it wil be a retriver
            print('Do not Progress - module retriever\n')
            retriver = retriver + 1

        total_outcome = progress + trailer + exclude + retriver
                
        #Asking For More Sets Of Data
        print('Would you like to enter another set of data?')

        more_set_loop = 0
        while more_set_loop == 0:
            
            more_sets = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print(end = '\n')

            if more_sets == 'q': #If the user enters 'q', the loop will end
                more_set_loop = 1
                main_loop = 1
                            
            elif more_sets == 'y': #If the user enters 'y', main loop will continue
                more_set_loop = 1
                main_loop = 0

            else: #Else the loop will continue
                more_set_loop = 0    

    #Display Horizontal Histogram
    print('------------------------------------------------------------------------')
    print('Horizontal Histogram')

    print('Progress', progress, ' : ', end = '')
    print_stars (progress)

    print('Trailer', trailer, '  : ', end = '')
    print_stars (trailer)

    print('Retriver', retriver, ' : ',end='')
    print_stars (retriver)

    print('Excluded', exclude, ' : ',end = '')
    print_stars (exclude)
    print(end = '\n')

    print(total_outcome, ' outcomes in total.\n')

######################################################################################################################################

def part_4():
    #Part 4


    #The program will display ‘Integer required’ if a credit input is the wrong data type
    def type_error():
        print('integer required\n')

    #The program will display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120.
    def out_of_range_error():
        print('out of range\n')
        
    #If there is another error instead of type_error and out_of_range_error the program will display an unexpected error.
    def unexpected_error():
        print('An unexpected error has occured\n')

    #Display Vertical Histogram
    def vertical_histogram(progress,trailer,retriver,exclude):
        #Create a credit list
        credit_list = [progress,trailer,retriver,exclude]
        #Assign line variable
        line = 0
        #Total of lines is equal to the maximum credit
        total_lines = max(credit_list)
        #The length of the line will be same as the length of the credit list
        line_length = len(credit_list)

        while (line < total_lines):
            
            iterration = 0
            while iterration < line_length:
                #If line is less than iterration, it will print *
                if line < credit_list[iterration]:
                    print('   ', '*', end='    ')
                #Else there will be no *  
                else:
                    print('   ', ' ', end='    ')
                    
                iterration += 1
                
            line += 1
            print(' ')
            
    #Assign Ranges
    progress = 0
    trailer = 0
    exclude = 0
    retriver = 0
        
    print ('Staff Version with Histogram\n')


    main_loop = 0
    while main_loop == 0:

        #Input credits
        sub_loop1 = 0
        while sub_loop1 == 0:
            
            try:
                pass_credit = int(input('Please enter your credits at pass: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if pass_credit >= 0 and pass_credit <= 120 and pass_credit % 20 == 0: #If pass credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop1 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop1 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop1 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop1 = 0
            
        sub_loop2 = 0    
        while sub_loop2 == 0:
            
            try:
                defer_credit = int(input('Please enter your credits at defer: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if defer_credit >= 0 and defer_credit <= 120 and defer_credit % 20 == 0: #If defer credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop2 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop2 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    sub_loop2 = 0
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop2 = 0
            
        sub_loop3 = 0    
        while sub_loop3 == 0:
            
            try:
                fail_credit = int(input('Please enter your credits at fail: '))

                try:

                    #Check whether the credit in the range 0, 20, 40, 60, 80, 100 and 120
                    if fail_credit >= 0 and fail_credit <= 120 and fail_credit % 20 == 0: #If fail credit is in the range 0, 20, 40, 60, 80, 100 or 120 there will be no error
                        sub_loop3 = 1
                    else:
                        out_of_range_error () #If it is not in range, there will be an error (out of range)
                        sub_loop3 = 0
                    
                except:
                    unexpected_error () #Else there will be another error
                    continue
                
            except:
                type_error () #If the user did not enter a valid integer, the loop may continue
                sub_loop3 = 0

        #Check Whether The Total Is Incorrect
        total = pass_credit + defer_credit + fail_credit
        
        if total != 120:
            print('Total incorrect\n') #If the total of pass,defer and fail do not equal 120, the main loop will run again
            main_loop = 0
        else:
            main_loop = 1 #If the total is correct, the main loop will break
        
        #Display Progression Outcome
        if pass_credit == 120:
            print('Progress\n')
            progress = progress+1
        elif pass_credit > 99:
            print('Progress (module trailer)\n')
            trailer = trailer + 1
        elif fail_credit > 79:
            print('Exclude\n')
            exclude = exclude + 1
        elif pass_credit < 81:
            print('Do not Progress - module retriever\n')
            retriver = retriver + 1
            
        total_outcome = progress + trailer + exclude + retriver

        #Asking For More Sets Of Data
        print('Would you like to enter another set of data?')

        more_set_loop = 0
        while more_set_loop == 0:
            
            more_sets = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print(end = '\n')

            if more_sets == 'q': #If the user enters 'q', the loop will end
                more_set_loop = 1
                main_loop = 1
                            
            elif more_sets == 'y': #If the user enters 'y', main loop will continue
                more_set_loop = 1
                main_loop = 0

            else: #Else the loop will continue
                more_set_loop = 0    


    print('------------------------------------------------------------------------')
    print('Vertical Histogram')

    print('Progress', ' Trailer', ' Retriver', ' Excluded')
    vertical_histogram(progress,trailer,retriver,exclude)

    print(total_outcome, ' outcomes in total.')

######################################################################################################################################

def part_5():
    #- Part 5

    #Print stars in the Horizontal Histogram
    def print_stars (progression_outcome):
        for x in range(progression_outcome):
            print('*', end = '')
        print(end = '\n')

    #Display Progression Outcome
    def display_progression (a):
        if (marks_list[a][0]) == 120: #If pass credit equals to 120, it will be a progress
            print('Progress')
            marks[0] = marks[0]+1
        elif (marks_list[a][0])>99: #If pass credit is between 99 and 120, it will be a trailer
            print('Progress(module trailer)')
            marks[1] = marks[1]+1
        elif (marks_list[a][2]) > 79: #If fail credit is more that 79, it will be an exclude
            print('Exclude')
            marks[2] = marks[2]+1
        elif (marks_list[a][0]) < 81: #If pass credit is less than 81, it wil be a retriver
            print('Do not Progress - module retriever')
            marks[3] = marks[3]+1

    #Assign Ranges
    total_outcome = 0
    #There is an empty list called marks
    marks = [0,0,0,0]

    print('Alternative Staff Version\n')

    #Data List Which Is Used For The Program
    marks_list = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 0], [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]


    for x in range(10):
        display_progression(x)

    #Display Horizontal Histogram
    print('------------------------------------------------------------------------')
    print('Progress', marks[0], ' : ', end = '')
    print_stars (marks[0])

    print('Trailer', marks[1], '  : ', end = '')
    print_stars (marks[1])

    print('Retriver', marks[3], ' : ',end='')
    print_stars (marks[3])

    print('Excluded', marks[2], ' : ',end = '')
    print_stars (marks[2])
    print(end = '\n')

    print(marks[0]+marks[1]+marks[2]+marks[3], ' outcomes in total.')

######################################################################################################################################

#Welcome Message and Instructions
print('Welcome to the progression predicting system.\n')
print('''Follow the instructions below.\n
Part 1 (Student Version) --> Enter 1
Part 2 (Student Version - Validation) --> Enter 2
Part 3 (Staff Version with Histogram) --> Enter 3
Part 4 (Vertical Histogram) --> Enter 4
Part 5 (Alternative Staff Version) --> Enter 5\n''')

version_loop = 0
while version_loop == 0:
    try:
        #Asking for the Version
        version = int (input('Which version do you want to use? : '))
        print('\n')

        if version == 1:
            part_1()

        elif version == 2:
            part_2()

        elif version == 3:
            part_3()

        elif version == 4:
            part_4()

        elif version == 5:
            part_5()

    except:
        version_loop = 0

    #Asking to try another version
    print ('Do you want to try another version?')
    another_version = 0
    while another_version == 0:
        again_try = input ('Enter "y" to try again or "q" to quit : ')
        if again_try == 'q': #If the user enters 'q', the program will end
            another_version = 1
            version_loop = 1
        elif again_try == 'y': #If the user enters 'y', program will continue
            another_version = 1
            version_loop = 0         
        else: #Else the loop will continue
            another_version = 0
