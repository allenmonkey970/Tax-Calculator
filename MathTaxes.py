bracketAcsi = """
|--------------------|
|       |10%         |
|--------------------|
|       |12%         |
|--------------------|
|       |22%         |
|--------------------|
|       |24%         |
|--------------------|
|       |32%         |
|--------------------|
|       |35%         |
|--------------------|
|       |37%         |
|--------------------|
"""
tax_Deduction = 14600

def get_Taxable_Salary():
    while True:
        try:
            gross_Salary = float(input('How much do you make a year? '))
            break
        except ValueError:
            print('Please enter a number or remove the comma ')
    taxable_Salary = gross_Salary - tax_Deduction
    if taxable_Salary > 0:
        return taxable_Salary
    else:
        print("You do not need to pay taxes")
        return 0

def tax_Bracket(taxable_Salary):
    brackets = {
        0.1: 9950,
        0.12: 40525,
        0.22: 86375,
        0.24: 164925,
        0.32: 209425,
        0.35: 523600,
        0.37: float('inf')
    }
    tax_amount = 0
    prev_amount = 0
    for rate, amount in brackets.items():
        if taxable_Salary > amount:
            tax_amount += (amount - prev_amount) * rate
            prev_amount = amount
        else:
            tax_amount += (taxable_Salary - prev_amount) * rate
            break
    print(f'Tax owed: ${tax_amount:,.2f}')

def main():
    taxable_Salary = get_Taxable_Salary()
    if taxable_Salary > 0:
        print(f'Taxable Salary: ${taxable_Salary:,.2f}')
        tax_Bracket(taxable_Salary)

if __name__ == '__main__':
    main()
