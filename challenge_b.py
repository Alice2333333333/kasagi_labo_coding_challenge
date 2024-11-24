import sys

def determine_type(obj):
    obj = obj.strip()
    
    if obj.isdigit() or (obj.startswith('-') and obj[1:].isdigit()):
        return "Integer"
    
    try:
        float(obj)
        return "Real Number"
    except ValueError:
        pass

    if obj.isalpha():
        return "Alphabetical strings"
    
    return "Alphanumerics"
        

def process_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        objects = infile.read().split(',')
        for obj in objects:
            if obj.strip():
                obj_type = determine_type(obj)
                outfile.write(f"Object: '{obj.strip()}' | Type: {obj_type}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_file(input_file, output_file)
