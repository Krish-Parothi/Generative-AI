from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Krish'  # Default value
    age: Optional[int] = None # if age value is not set then it is set to None.
    email:EmailStr # Validates if it is a valid email or not.
    cgpa: float = Field(gt=0,lt=10, default=5, description="A Decimal Value Representing the cgpa of the Student.") # Field Se Hum Constraints laga skte hai and here is Greater than Zero and less than 10. Field can also contain default value 5.

# new_student = {'name': "Krish Parothi"}
new_student = {'age':'19','email':'abc@new.com','cgpa':5}

student = Student(**new_student)

print(type(student))
print(student)
# student_dict = dict(student)
student_dict = student.model_dump() # same but better version than dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)

# Benefit of Pydantic is that, if you do age:"32", since age is a integer but you sent age as string, so pydantic will automatically type convert the string to number. This is called Type Coarsing in Python.

# output: name='Krish' age=19
# <class '__main__.Student'>



# new_student ke andar if aapne cgpa daala ya nahi daala tabhi bhi vo value apne aap set ho jayegi, and output mein print krega...!