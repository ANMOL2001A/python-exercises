#converts neter into miles,feet,inch

METERS_TO_MILES = 0.000621371
METERS_TO_FEET = 3.28084
METERS_TO_INCHES = 39.3701
 
measurement_in_meters = float(input("Enter a measurement in meters: "))
print(f"{measurement_in_meters} meters")
 
measurement_in_miles = measurement_in_meters * METERS_TO_MILES
measurement_in_feet = measurement_in_meters * METERS_TO_FEET
measurement_in_inches = measurement_in_meters * METERS_TO_INCHES
 
#results

print(f"meters into {measurement_in_miles:} miles")
print(f"meters into{measurement_in_feet:} feet")
print(f"meters into{measurement_in_inches:} inches")