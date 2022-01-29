"""
knjiga osnove programiranja
stran 29
"""

# input -> returns string
masa = input("vpiši svojo telesno maso [kg]:  ")
# string to float conversion
masa = float(masa) 
visina = float(input("vpiši svojo višino [m]:  ")) 

itm = masa /visina**2

print(f"tvoj ITM je {itm}")


 17.5 <= itm <= 25
if itm < 17.5:
    print("tvoja telesna masa je premajhna")
if itm > 25:
    print("tvoja telesna masa je prevelika")
if 17.5 <= itm and itm <= 25:
    print("tvoja telesna masa je ustreza")

