import datetime
import json
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Deepi@1234", database="userdetails")
cursor = mydb.cursor()
cursor.execute('select * from request ')
for i in cursor:
    print(i)


def details():   #pylint: disable=too-many-statements
    try:
        try:
            id = 2  #pylint: disable=(invalid-name)
            firstname = input('Enter the name:')
            id = id + 1
            if len(firstname) == 0 or firstname.isdigit():
                raise Exception  #pylint:disable=invalid-namep
        except:
            print("Enter the first Name properly")
            raise Exception  #pylint: disable=unused-variable
        middle_name = input('Enter the middle name: ')  #pylint: disable=raise-missing-from
        try:
            lastname = input("Enter the last name: ")
            if len(lastname) == 0 or lastname.isdigit():
                raise Exception  #pylint:disable=invalid-name
        except:
            print("name cannot be in digit")
            raise Exception  #pylint:disable=invalid-name
        try:
            dob = input("What is your B'day? (in YYYY-MM-DD): ")
            datetime.datetime.strptime(dob, '%Y-%m-%d') != 0  #pylint:disable=expression-not-assigned

        except ValueError:
            print("Enter DOb properly")
            raise Exception  #pylint:disable=invalid-name
        try:
            gender = input("Enter the gender:")
            if gender != 'male' and gender != 'female':  #pylint:disable=consider-using-in
                raise Exception
        except:
            print("specify the gender properly")
            raise Exception  #pylint: disable=raise-missing-from
        try:
            nationality = input("Enter your Nationality: ")
            if len(nationality) <= 3 or nationality.isnumeric():
                raise Exception
        except:
            print("specify the Nationality properly")
            raise Exception  #pylint:disable=raise-missing-from
        try:
            city = input("Enter the Current city: ")
            if len(city) <= 3 or city.isnumeric():
                raise Exception
        except:
            print("Enter the city properly")
            raise Exception  #pylint: disable=raise-missing-from
        try:
            state = input("enter your state: ")
            if len(state) <= 3 or state.isnumeric():
                raise Exception   #pylint:disable=raise-missing-from
        except:
            print("state cannot be numeric")
            raise Exception  #pylint:disable=raise-missing-from
        try:
            pin = int(input("enter your pin: "))
            a = str(pin)  #pylint:disable=invalid-name
            if len(a) < 6:
                raise Exception  #pylint:disable=invalid-name
        except:
            print("pin should be 6 digit number")
            raise Exception  #pylint:disable=invalid-name
        try:
            qualification = input("Enter the Qualification: ")
            if qualification.isnumeric():
                raise Exception  #pylint:disable=invalid-name
        except:
            print("enter the qualification in current format")
            raise Exception  #pylint:disable=invalid-name
        try:
            salary = int(input("Enter the salary: "))
            if salary == 0:
                raise Exception  #pylint:disable=invalid-name
        except:
            print("salary cannot")
            raise Exception  #pylint:disable=invalid-name
        try:
            pan_number = input("enter your pan number")
            if len(pan_number) < 10 or pan_number.isalnum() == False:  #pylint:disable=singleton-comparison
                raise Exception
        except:
            print("enter the pan number in correct format")
            raise Exception  #pylint:disable=raise-missing-from
    except:
        print("check the details and try again")
    insert = "INSERT INTO request VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (id, firstname, lastname, dob, gender, nationality, city, state, pin, qualification, salary, pan_number)
    try:
        cursor.execute(insert,data)
        mydb.commit()
    except:  #pylint:disable=bare-except
        mydb.rollback()
    try:
        id = 0
        dmy = dob
        cdob = dmy[8:] + "/" + dmy[5:7] + "/" + dmy[:4]
        born = datetime.datetime.strptime(cdob, "%d/%m/%Y").date()
        today = datetime.date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        print(age)
        id = id + 1
        if(age > 21 and gender == "male") or (age > 18 and gender == "female"):
            if nationality == "indian" or nationality == "american":  #pylint:disable=consider-using-in
                if(state == "Andhra Pradesh" or state == "Arunachal Pradesh" or state == "Assam" or state == "Bihar" or state == "Chhattisgarh" or state == "tamilnadu" or state == "Karnataka" or state == "Madhya Pradesh" or state == "Odisha" or state == "Telangana" or state == "West Bengal"):  #pylint: disable=consider-using-in
                    if(salary > 10000) and (salary < 90000):  #pylint: disable=chained-comparison
                        jdetails = {
                            "firstname": firstname,
                            "lastname": lastname,
                            "dob": dob,
                            "gender": gender,
                            "nationality": nationality,
                            "city": city,
                            "state": state,
                            "pin": pin,
                            "qualification": qualification,
                            "salary": salary,
                            "pan": pan_number
                        }
                        loads = json.dumps(jdetails)
                        print(loads)

                        print(json.dumps(jdetails['firstname']))
                        inserting = "INSERT INTO response VALUES (%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        data1 = (2, json.dumps(jdetails['firstname']), json.dumps(jdetails['lastname']), json.dumps(jdetails['dob']), json.dumps(jdetails['gender']), json.dumps(jdetails['nationality']), json.dumps(jdetails['city']), json.dumps(jdetails['state']), json.dumps(jdetails['pin']), json.dumps(jdetails['qualification']), json.dumps(jdetails['salary']), json.dumps(jdetails['pan']))
                        cursor.execute(inserting, data1)
                        mydb.commit()
                        print("done")
    except:  #pylint:disable=bare-except
        mydb.rollback()
        print("invalid")
details()