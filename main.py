# Welcoming the user 
print("**************************************************")
print("Welcome to your personal income tax calculator 😁")
print("**************************************************")
print("We will need some input.")

# Putting all the code in a loop incase the user wants to make multiple calculations
loop_value = True
while loop_value:

    # Asking for taxable income
    taxable_income = float(input("Enter your taxable income($): "))

    # Asking for filing status
    print("What is your filing status? ")
    print("0. Single filers\n1. Married filing jointly or qualified widow(er)\n2. Married filing separately\n3. Head of household.")
    filing_status = input("Enter your filing status(0,1,2 or 3): ")

    total_tax = 0 
    # =======================
    #   FOR SINGLE FILERS
    # =======================
    if filing_status == "0":
        if taxable_income < 0:
            print("Invalid amonut") 
        else:
            if taxable_income > 0 and taxable_income <= 8350:
                total_tax += (0.1 * taxable_income)
            else:
                total_tax += 0.1 * 8350
                if taxable_income <= 33950:
                    total_tax += (0.15 * (taxable_income - 8350))
                else:
                    total_tax += 0.15 * (33950 - 8350)
                    if taxable_income <= 82250:
                        total_tax += (0.25 * (taxable_income - 33950))
                    else:
                        total_tax += 0.25 * (82250 - 33950)
                        if taxable_income <= 171550:
                            total_tax += (0.28 * (taxable_income - 82250))
                        else:
                            total_tax += 0.28 * (171550 - 82250)
                            if taxable_income <= 372950:
                                total_tax += (0.33 * (taxable_income - 171550))
                            else:
                                total_tax += 0.33 * (372950 - 171550)
                                if taxable_income > 372950:
                                    total_tax += (0.35 * (taxable_income - 372950))

        print(f"Your Total tax to pay is: {total_tax}")   

    # ===========================================
    #   FOR MARRIED FILING JOINTLY OR WIDOW(ER)
    # ===========================================
    if filing_status == "1":
        if taxable_income < 0:
            print("Invalid amonut") 
        else:
            if taxable_income >= 0 and taxable_income <= 16700:
                total_tax += (0.1 * taxable_income)
            else:
                total_tax += 0.1 * 16700
                if taxable_income <= 67900:
                    total_tax += (0.15 * (taxable_income - 16700))
                else:
                    total_tax += 0.15 * (67900 - 16700)
                    if taxable_income <= 137050:
                        total_tax += (0.25 * (taxable_income - 67900))
                    else:
                        total_tax += 0.25 * (137050 - 67900)
                        if taxable_income <= 208850:
                            total_tax += (0.28 * (taxable_income - 137050))
                        else:
                            total_tax += 0.28 * (208850 - 137050)
                            if taxable_income <= 372950:
                                total_tax += (0.33 * (taxable_income - 208851))
                            else:
                                total_tax += 0.33 * (372950 - 208850)
                                if taxable_income > 372950:
                                    total_tax += (0.35 * (taxable_income - 372950))

        print(f"Your Total tax to pay is: {total_tax}")   

    # ====================================
    #    FOR MARRIED FILING SEPERATELY
    # ====================================
    if filing_status == "2":
        if taxable_income < 0:
            print("Invalid amonut") 
        else:
            if taxable_income > 0 and taxable_income <= 8350:
                total_tax += (0.1 * taxable_income)
            else:
                total_tax += 0.1 * 8350
                if taxable_income <= 33950:
                    total_tax += (0.15 * (taxable_income - 8350))
                else:
                    total_tax += 0.15 * (33950 - 8350)
                    if taxable_income <= 68525:
                        total_tax += (0.25 * (taxable_income - 33950))
                    else:
                        total_tax += 0.25 * (68525 - 33950)
                        if taxable_income <= 104425:
                            total_tax += (0.28 * (taxable_income - 68525))
                        else:
                            total_tax += 0.28 * (104425 - 68525)
                            if taxable_income <= 186475:
                                total_tax += (0.33 * (taxable_income - 104425))
                            else:
                                total_tax += 0.33 * (186475 - 104425)
                                if taxable_income > 186475:
                                    total_tax += (0.35 * (taxable_income - 186476))

        print(f"Your Total tax to pay is: {total_tax}")   

    # =========================
    #   FOR HEAD OF HOUSEHOLD
    # =========================
    if filing_status == "3":
        if taxable_income < 0:
            print("Invalid amonut") 
        else:
            if taxable_income > 0 and taxable_income <= 11950:
                total_tax += (0.1 * taxable_income)
            else:
                total_tax += 0.1 * 11950
                if taxable_income <= 45500:
                    total_tax += (0.15 * (taxable_income - 11950))
                else:
                    total_tax += 0.15 * (45500 - 11950)
                    if taxable_income <= 117450:
                        total_tax += (0.25 * (taxable_income - 45500))
                    else:
                        total_tax += 0.25 * (117450 - 45500)
                        if taxable_income <= 190200:
                            total_tax += (0.28 * (taxable_income - 117450))
                        else:
                            total_tax += 0.28 * (190200 - 117451)
                            if taxable_income <= 372950:
                                total_tax += (0.33 * (taxable_income - 190200))
                            else:
                                total_tax += 0.33 * (372950 - 190200)
                                if taxable_income > 372950:
                                    total_tax += (0.35 * (taxable_income - 372950))

        print(f"Your Total tax to pay is: {total_tax}")   
    
    # Asking if the user would like to calculate another income tax
    user_answer = input("Would you like to calculate another income tax? (Y/N): ")
    if user_answer.upper() == "N":
        print("Bye, Don't forget to pay your taxes 😑")
        loop_value = False
