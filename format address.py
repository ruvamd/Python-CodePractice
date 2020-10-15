
def format_address(address_string):
  # Declare variables
        house_number=[]
        street_name=[]
  # Separate the address string into parts
        house_number,street_name=address_string.split(' ',1)
  # Traverse through the address parts
  
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
        return f"house number {house_number} on street named {street_name}"

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"