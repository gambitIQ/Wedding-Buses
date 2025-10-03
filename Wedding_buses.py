# Wedding Buses Zamambo Mkhize 

import math

def wedding_bus():
#wedding parties
    bride_name = input('\nPlease enter the name of the bride: ' ) 
    groom_name = input('Please enter the name of the groom: ' )
    num_guest  = int(input('How many guests are coming to your wedding? '))

#bus capacity 
    bus_cap = int(40) 
    num_bus = math.ceil(num_guest/bus_cap)
    bus_cap_extra = int((bus_cap * num_bus) - num_guest)

    print(f'For the wedding of {groom_name} and {bride_name} you will need {num_bus} buses.')
    print(f'You will have space for {bus_cap_extra} extra guests on those buses.')

for i in range(1,3):
   wedding_bus()
   
   '''Sample Output
Please enter the name of the bride Mambo
Please enter the name of the groom Havier
How many guests are coming to your wedding? 180
For the wedding of Havier and Mambo you will need 5 buses.
You will have space for 20 extra guests on those buses.

Please enter the name of the bride Mambo
Please enter the name of the groom John
How many guests are coming to your wedding? 175
For the wedding of John and Mambo you will need 5 buses.
You will have space for 25 extra guests on those buses.'''