# Program for One Stop Insurance Company
# Data written: Nov 20, 2023 - End date
# Author: Cody Oram

# Import required libraries.

import datetime
import FormatValues as FV    # Library for all formats
 
# Set up program constants.

POLICY_NUM = 1944
BASIC_PREM = 869.00
ADDIT_CAR = 0.25
EXTRA_LIAB = 130.00
GLASS_COV = 86.00
LOANER_CAR = 58.00
HST = 0.15
PROC_FEE_MP = 39.99

# Set up program functions.

# Funtions for previous claims

# Function for  calculating monthly payment
def CalHST(TotInsurPrem):
    Hst = TotInsurPrem * HST
    return Hst


def CalTotalCost(TotInsurPrem, Hst):
    TotalCost = TotInsurPrem + Hst
    return TotalCost

# Start the main program.

while True:
    
    while True:
        CustFName = input("Enter customers first name (END to quit): ").title()
        if CustFName == "":
            print("Customers first name cannot be blank - please re-enter.")
        else:
            break

    while True:
        CustLName = input("Enter customers last name: ").title()
        if CustLName == "":
            print("Customers last name cannot be blank - please re-enter.")
        else:
            break

    while True:
        StreetAdd = input("Enter customers street address: ").title()
        if StreetAdd == "":
            print("Customers street address cannot be blank - please re-enter.")
        else:
            break
    
    while True:
        City = input("Enter customers city: ").title()
        if City == "":
            print("Customers city cannot be blank - please re-enter.")
        else:
            break

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank - Please reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 digit code - please reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province - please reenter.")
        else:
            break

    while True:
        PCode = input("Enter customers postal code (X9X9X9): ").upper()
        if City == "":
            print("Customers postal code cannot be blank - please re-enter.")
        else:
            break

    while True:
        PhoneNum = input("Enter customers phone number (999-999-9999): ")
        if PhoneNum == "":
            print("Customers phone number cannot be blank - please re-enter.")
        elif len(PhoneNum) != 12:
            print("Customers phone number must be 10 digits - please re-enter.")
        else:
            break
    
    while True:
        CarsInsured = int(input("Enter the number of cars being insured: "))
        if CarsInsured == "":
            print("The number of cars being insured cannot be blank - please re-enter.")
        else:
            break

    while True:
        ExtraLiab = input("Would you like extra liability up to $1,000,000? (enter Y for Yes or N for No): ").upper()
        if ExtraLiab == "":
            print("The number of cars being insured cannot be blank - please re-enter.")
        elif ExtraLiab != "Y" and ExtraLiab != 'N':
            print("Must enter a Y or N - please re-enter: ")
        else:
            break

    while True:
        GlassCov = input("Would you like glass coverage? (Y or N): ").upper()
        if GlassCov == "":
            print("Glass coverage cannot be blank - please re-enter.")
        elif GlassCov != "Y" and GlassCov != 'N':
            print("Must enter a Y or N - please re-enter: ")
        else:
            break

    while True:
        LoanerCar = input("Would you like a loaner car? (Y or N): ").upper()
        if LoanerCar == "":
            print("Loaner car cannot be blank - please re-enter.")
        elif LoanerCar != "Y" and LoanerCar != 'N':
            print("Must enter a Y or N - please re-enter: ")
        else:
            break

    PayTypeLST = ["Full", "Monthly", "Down Pay"]
    while True:
        PayType = input("Please enter the pay type  (Full, Monthly, Down Pay): ").title()
        if PayType == "":
            print("Error - Pay Type cannot be blank - Please re-enter.")
        elif PayType not in PayTypeLST:
            print("Error - Not a valid type - please re-enter.")
        elif PayType == "Down Pay":
            DownPay = float(input("Enter the amount of the down payment: "))
        else:
            DownPay = 0

    # List to dates and cost   
        DateLst = []
        CostLst = []

        while True:
            while True:
                Date = input("Enter the date of the claim 'MM-DD-YYYY' (or press Enter to finish): ")
                if not Date:  # If the user presses Enter, exit the loop
                    break

                if Date == "":
                    print("Error - Date cannot be blank - Please re-enter.")
                else:
                    break

            if Date == "":
                break

            while True:
                Cost = float(input("Enter the cost of the claim: "))
                if Cost == "":
                    print("Error - The cost cannot be blank - Please re-enter.")
                else:
                    break

        DateLst.append(Date)
        CostLst.append(Cost)

        # Required Program Calculations

        InsurPrem = BASIC_PREM * CarsInsured
        if CarsInsured > 1:
            InsurPrem = (BASIC_PREM * CarsInsured) * .25

        ExtraLiabM = 0
        if ExtraLiab == "Y":
            ExtraLiabM = EXTRA_LIAB * CarsInsured

        GlassCovM = 0
        if GlassCov == "Y":
            GlassCovM = GLASS_COV * CarsInsured

        LoanerCarM = 0
        if LoanerCar == "Y":
            LoanerCarM = LOANER_CAR * CarsInsured

        TotExtraCost = ExtraLiabM + GlassCovM + LoanerCarM

        TotInsurPrem = InsurPrem + TotExtraCost

        Hst = CalHST(TotInsurPrem)

        TotalCost = CalTotalCost(TotInsurPrem, Hst)

        FTotalCost = (TotalCost - DownPay) + PROC_FEE_MP
        MonthlyPay = FTotalCost / 8

        # Set invoice date to the current date
        InvoiceDate = datetime.datetime.now().strftime("%m-%d-%Y")

        # Set the first payment date to the first day of the next month
        FirstPaymentDate = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%m-%d-%Y")

        # Usuer Outputs

        print(f"         1         2         3         4   ")
        print(f"1234567890123456789012345678901234567890126")
        print()
        print(f"         One Stop Insurance Company")
        print('--------------------------------------------')
        print(f"Customer:")
        print(f"   {CustFName:<15s} {CustLName:<15s} ")
        print()
        print(f"Address:")
        print(f"   {StreetAdd:<14s} ")
        print(f"   {City:<15s}, {Prov:<2s} {PCode:<6s}")
        print(f"   {PhoneNum:<10s}")
        print("--------------------------------------------")
        print(f"Cars Insured:                              {CarsInsured:<2}")
        print(f"Extra Liability:                           {ExtraLiab:<3s}")
        print(f"Glass Coverage:                            {GlassCov:<3s}")
        print(f"Loaner Car:                                {LoanerCar}")
        print(f"Payment Type:                       {PayType:<7s}")
        print(f"Down Payment:                      {FV.FDollar2(DownPay):<6}")
        print("--------------------------------------------")
        print(f"Insurance Premiums:                  {FV.FDollar2(InsurPrem):<6}")
        print(f"Extra Liability:                     {FV.FDollar2(ExtraLiabM):<6}")
        print(f"Glass Coverage:                      {FV.FDollar2(GlassCovM):<6}")
        print(f"Loaner Car:                          {FV.FDollar2(LoanerCarM):<6}")
        print("--------------------------------------------")
        print(f"Total Extra Cost:                    {FV.FDollar2(TotExtraCost):<6}")
        print(f"Total Insurance Premium:           {FV.FDollar2(TotInsurPrem):<6}")
        print(f"HST:                                 {FV.FDollar2(Hst):<6}")
        print(f"Total Cost:                        {FV.FDollar2(TotalCost):<7}")
        print(f"Final Total Cost:                    {FV.FDollar2(FTotalCost):<6}")
        print(f"Monthly Payments:                    {FV.FDollar2(MonthlyPay):<6}")
        print(f"Invoice Date:                     {InvoiceDate:<8s}")
        print(f"First Payment:                    {FirstPaymentDate:<8s}") 
        print("--------------------------------------------")
        print(f"Customer's Claims:")
        print()
        print(f"   Claim #      Claim Date        Amount   ")
        print("   -----------------------------------------")
        ClaimNum = 1
        for i in range(0, len(DateLst)):
            print(f"    {ClaimNum:<2d}          {DateLst[i]:>10s}        {FV.FDollar2(CostLst[i]):>7}")
            ClaimNum += 1

        Continue =  input("Enter customers first name (END to quit): ").upper()
        if Continue == "END":
            break 

    print()
    print(f"Thanks for using One Stop Insurance Company")
    print(f"Have a nice day!")    
