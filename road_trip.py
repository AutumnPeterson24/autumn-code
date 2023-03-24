"""
Best Road Trip Ever! - CS 118 Final Project
Program that gives the "best" route for your road trip regarding temp and hotel accommodations
By: Autumn Peterson
12 DEC 2022
"""

from itertools import permutations, combinations_with_replacement
from json import load


def get_city_name(lst) -> str:
    """
    gives city names with ' -> '
    """
    return " -> ".join([d["name"] for d in lst])


def avg_temp(route: tuple) -> float:
    """
    :param : list of cities
    :return: average temperature
    """
    t = 0
    for i in range(len(route)):
        t += route[i-1]["temperatures"][i-1]
    return t / len(route)


def hotel_costs(hotels: tuple) -> int:
    """
    Hotel cost total
    :param hotels: list of hotel names like:
    :return: sum of the per night cost
    """
    cost = 0
    for i in hotels:
        cost += i[1]
    return cost if cost <= HOTEL_BUDGET else 0


with open("city_temp_dist.json") as file:  # load json structure representing a list of dictionaries
    cities = load(file)  # city list

with open("hotel_rates.json") as file:  # load json structure representing a dictionary
    hotel_rates = load(file)  # hotel dictionary

HOTEL_BUDGET = 850

best_temp_route = max(permutations(cities), key=avg_temp)  # average temp calculations
final_avg_temp = avg_temp(best_temp_route)
final_route = get_city_name(best_temp_route)

prices = list(hotel_rates.items())  # list items of hotel_rates dict
combi2 = list(combinations_with_replacement(prices, len(cities)))  # tuple of every price combo
best_max_hotel = list((max(combi2, key=hotel_costs)))  # list of prices for max budget
final_budget = hotel_costs(best_max_hotel)  # max budget
final_hotel = ", ".join([t[0] for t in best_max_hotel])

print(f"\nYour optimal route for the BEST ROAD TRIP EVER is: \n{final_route}")
print(f"The average daily max temperature will be: {final_avg_temp}F\n")
print(f"To max out your hotel budget, stay at: \n{final_hotel}, for a total of ${final_budget}\n")
