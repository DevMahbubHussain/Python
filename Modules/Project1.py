from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai']
designations=['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']


def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2,9)
    #print(n)
    for i in range(n):
        name = name + choice(alphabets)
    return name

#print(get_fake_name())

def get_fake_eno():
    eno = 'e-'
    for i in range(4):
        eno = eno + choice(digits)
    return eno
#print(get_fake_eno())

def fake_em_salary():
    esl = uniform(10000,50000)
    return esl

#print(fake_em_salary())

def fake_emplyee_cities():
    city = choice(cities)
    return city
#print(fake_emplyee_cities())

def get_fake_mno():
    mno = choice('+880')
    for i in range(10):
        mno = mno + choice(digits)
    return mno
#print(get_fake_mno())

def get_fake_designation():
    designation=choice(designations)
    return designation

#print(get_fake_designation())

def fake_employee_details_data():
    print("Employee Name : ", get_fake_name())
    print("Employee Number : ", get_fake_eno())
    print("Employee Salary:{:.2f} : " .format(fake_em_salary()) )
    print("Employee City : ", fake_emplyee_cities())
    print("Employee Mobile Number : ", get_fake_mno())
    print("Employee Designation: ", get_fake_designation())


for i in range(5):
    fake_employee_details_data()
    print("===============")
