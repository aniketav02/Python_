from my_package.operation import add,subtract
from my_package.utils import print_welcome_message, print_farewell_message

print_welcome_message()

result_add=add(5,3)
result_subtract= subtract(10,4)

print(f"Addtion result: {result_add}")
print(f"Subtraction result: {result_subtract}")

print_farewell_message()
