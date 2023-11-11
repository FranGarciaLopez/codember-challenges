operations = "&###@&&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

def increment(value):
       return value + 1

def decrement(value):
       return value - 1

def multiply(value):
       return value * value

def print_value(value):
       print(value, end="")

def not_a_fun():
       print("not a valid function name")

value = int(input("Enter a value: "))

def mathematical_operations(value):
       for operation in operations:
              encrypted_operation = {
                     "#": increment,
                     "@": decrement,
                     "*": multiply,
                     "&": print_value
              }.get(operation, not_a_fun)

              if operation == "&":
                     encrypted_operation(value)
              else:
                     value = encrypted_operation(value)

mathematical_operations(value)