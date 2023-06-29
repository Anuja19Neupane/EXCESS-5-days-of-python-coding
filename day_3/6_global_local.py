def calc_fuel(distance,milage):
    fuel_consumed=distance/milage
    return fuel_consumed
distance1=100 #km
fuel=calc_fuel(distance1,16)

print(f"Fuel consumed:{fuel}L")
# fuel_consumed: local variable
# distance1: global variable
# fuel: global variable

    
