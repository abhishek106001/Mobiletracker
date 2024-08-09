import phonenumbers
from phonenumbers import geocoder

number = input("Enter a phone number (include country code, +91): \n")
pepnumber = phonenumbers.parse(number, None)
location = geocoder.description_for_number(pepnumber, "en")
print(f"The location of the phone number is: \n {location}")

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
