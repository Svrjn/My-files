import datetime

current_month = datetime.datetime.now().strftime("%B").upper()
print("ACCOUNT FOR THE MONTH OF", current_month)


income = float(input("Enter income: "))
print("Total amount:", income)



if income >= 100 and income < 20000:
    
    district = 0.25 * income
    section = 0.03 * income
    basic_salary = 0.38 * income
    pension= 0.10 * basic_salary
    	
    print(f"25% to district = {district}")
    print(f"3% to section = {section}")
    print("PASTOR BASIC SALARY: ", basic_salary)


elif income >= 20001 and income < 49999:
    basic_salary = 12000 + ((income - 20000)*0.35)
    district = 0.30 * income
    section = 0.03 * income
    
    allowance = 0.25 * basic_salary
    pension= 0.10 * basic_salary
    
    print(f"30% to district = {district}")
    print(f"3% to section = {section}")
    
    print("PASTOR BASIC SALARY: ", basic_salary)
    print(f"ALLOWANCE: {allowance}\n 10% PENSION: {pension}")

    
elif income >= 50000 and income < 69999:
    basic_salary = (12000 + ((income - 22000)*0.35))
    
    allowance = 0.25 * basic_salary
    pension = 0.10 * basic_salary
    
    district = 0.30 * income
    section = 0.03 * income
    
    local_church = 0.67 * income
    
    print(f"30% to district = {district} \n3% to section = {section} \n67% TO LOCAL CHURCH: {local_church}")
  
    
    print("PASTOR BASIC SALARY: ", basic_salary)
    print(f"ALLOWANCE: {allowance}\n 10% PENSION: {pension}")







gas = 3000

special_off = float(input("Enter total special offering: "))

dist= district + section + special_off
total= gas + dist + allowance + pension + basic_salary
print(f"District money: {dist}")
print(f"TOTAL RETURNS: {total}")