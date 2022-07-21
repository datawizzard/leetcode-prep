import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
s=input()
phone_number=phonenumbers.parse(s)
print(geocoder.description_for_number(phone_number,"en"))
print(carrier.name_for_number(phone_number,"en"))