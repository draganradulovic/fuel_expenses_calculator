from fuel_price import get_fuel_price
from route_lenght import get_route_lenght

def expenses_calculator():
    start=input("Enter the starting city: ")
    finish=input("Enter the destination city: ")
    consumption=input("Enter car consumption (l/100km): ")
    consumption=float(consumption)
    fueling_state=input("enter the country where you want to refuel: ")
    fuel_type=input("enter type of fuel (diesel/petrol): ")

    route_lenght= get_route_lenght(start,finish)
    fuel_price=get_fuel_price(fueling_state,fuel_type)

    fuel_liters=(route_lenght/100.00)*consumption
    total_price=fuel_liters*fuel_price
    total_price = "{:.2f}".format(total_price)
    
    print("--TRAVEL INFO:--")
    print("Amount of money needed for fuel: ",total_price,"€")
    print("Path lenght: "+str(route_lenght)+" km")
    print(fuel_type+" price in "+fueling_state+" is "+str(fuel_price))
    return total_price


if __name__ == '__main__':
    expenses_calculator()


