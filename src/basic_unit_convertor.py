
def convert_km_to_miles(km):
    return round(km * 0.621371,2)

def convert_kg_to_lbs(kg):
    return round(kg * 2.20462,2)

def convert_celsius_to_fahrenheit(celsius):
    return round((celsius * 1.8) +32, 2)



def unit_converter(val,conversion):
    #print(val)
    if conversion == 1:
        return convert_km_to_miles(val)
    elif conversion == 2:
        return convert_kg_to_lbs(val)
    elif conversion == 3:
        return convert_celsius_to_fahrenheit(val)
    elif conversion == 4:
        return "exit"


def get_valid_input():
    while True:
        user_val = input("enter a value for conversion: ")
        conversion_mtd = int(input("enter a conversion method: \n 1.KM to miles. \n 2.KG to pound \n 3.celsius to fahrenheit \n 4.EXIT  "))
        try:
            user_val = float(user_val)
            if conversion_mtd in [1,2,3,4]:
                return (user_val,conversion_mtd)
                break
            else:
                print("enter conversion method 1 to 4")
        except:
            print("enter valid value for conversion")

val,conversion = get_valid_input()
#unit_converter(val,conversion)
#print(get_valid_input())
print(unit_converter(val,conversion))



