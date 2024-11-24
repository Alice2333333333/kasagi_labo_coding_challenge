import string
import random

def generate_alphabetical_string(): 
    return ''.join(random.choices(string.ascii_letters, k=10))

def generate_real_number():
    return f"{random.uniform(-1000, 1000):.2f}"

def generate_integer():
    return str(random.randint(-1000, 1000))

def generate_alphanumeric():
    alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    spaces_before = ' ' * random.randint(0, 10)
    spaces_after = ' ' * random.randint(0, 10)
    return f"{spaces_before}{alphanumeric}{spaces_after}"

def generate_file(filename="generate_random_object.txt", target_size_mb=10):
    target_size_bytes = target_size_mb * 1024 * 1024 
    with open(filename, "w") as file:
        while file.tell() < target_size_bytes:
            alpha_str = generate_alphabetical_string()
            real_num = generate_real_number()
            integer = generate_integer()
            alphanumeric = generate_alphanumeric()
            
            output = f"{alpha_str},{real_num},{integer},{alphanumeric},"
            file.write(output)

generate_file("generate_random_object.txt")
