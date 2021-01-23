import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "tr"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "tr"))

time_number = phonenumbers.parse(number, "TZ")
print(timezone.time_zones_for_number(time_number) ) 