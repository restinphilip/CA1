EMP_FILE = 'Employees.txt'
HR_FILE = 'Hours.txt'
STD_TAX_RATE = 0.2
HIGH_TAX_RATE = 0.4

class Employee:
    def __init__(self, id, lastName, firstName, regHrs, rate, otm, taxCred, stdBand):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.regHrs = float(regHrs)
        self.rate = float(rate)
        self.otm = float(otm)
        self.taxCred = float(taxCred)
        self.stdBand = float(stdBand)

    def computePayment(self, hrs, date):
        otHrs = hrs - self.regHrs if hrs > self.regHrs else 0
        otRate = self.rate * self.otm
        regPay = self.rate * self.regHrs
        otPay = otRate * otHrs
        grossPay = regPay + otPay
        highPay = grossPay - self.stdBand
        stdTax = self.stdBand * STD_TAX_RATE
        highTax = highPay * HIGH_TAX_RATE
        deduct = max(stdTax + highTax - self.taxCred, 0)
        
        return {
            'name': '{0} {1}'.format(self.firstName,self.lastName),
            'Date': date,
            'Regular Hours Worked': self.regHrs,
            'Overtime Hours Worked': otHrs,
            'Regular Rate': self.rate,
            'Overtime Rate': otRate,
            'Regular Pay': regPay,
            'Overtime Pay': otPay,
            'Gross Pay': grossPay,
            'Standard Rate Pay': self.stdBand,
            'Higher Rate Pay': highPay,
            'Standard Tax': stdTax,
            'Higher Tax': highTax,
            'Total Tax': stdTax + highTax,
            'Tax Credit': self.taxCred,
            'Net Deductions': deduct,
            'Net Pay': grossPay - deduct
        }


def computeAllPayment(employeeFile, hoursFile):
    employees = []
    payments = []
    with open(employeeFile,'r') as file:
        data = file.readlines()
        for line in data:
            words = line.split()
            employees.append(Employee(*words))
            print(*words)
    
    with open(hoursFile, 'r') as file:
        data = file.readlines()
        for line in data:
            words = line.split()
            emp = next(i for i in employees if i.id == words[0])
            payments.append(emp.computePayment(float(words[2]), words[1]))

    return payments

    


print(computeAllPayment(EMP_FILE,HR_FILE))