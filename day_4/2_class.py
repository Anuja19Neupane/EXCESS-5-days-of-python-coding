class Car:
    def __init__(self,make,model,milage):
        self.make=make
        self.model= model
        self.milage=milage
        self.total_distance=0
    
    def drive(self,distance):
        fuel_consumed = self.calc_fuel(distance)
        print(f"Distance is:{distance}km.")
        print(f"Fuel consuemed is:{fuel_consumed}L.")
        print(f"Total Distance is:{self.total_distance}km.")

    def calc_fuel(self,distance):
        fuel_consumed = distance/self.milage
        self.total_distance += distance
        return fuel_consumed
     
car = Car("tesla","model-x", 12)  #assuming a car named tesla made by elon dai and the fuel consumption is 12km/hr
carnext = Car("lambo", "koitahola", 6)   #same as abhove tara naam farak xa

print(car.milage)
print(car.model)



