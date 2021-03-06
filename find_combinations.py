import csv
import sys
from datetime import datetime, timedelta


class Flight(object):
    def __init__(self, source, destination, departure, arrival, flight_number,
                 price, bags_allowed, bag_price):
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.bags_allowed = bags_allowed
        self.bag_price = bag_price
        self.flight_number = flight_number

    def __str__(self):
        return 'From: %s, To: %s, FlightNumber: %s, Departure: %s, Arrival: %s' \
               % (self.source, self.destination, self.flight_number, self.departure, self.arrival)


class FlightsCombination(object):
    def __init__(self, flights):
        self.flights = flights

    def __str__(self):
        str_flights_combination = ''
        for flight in self.flights:
            str_flights_combination += str(flight) + '\n'
        return str_flights_combination

    def get_route(self):
        """
        :return: Route as string
        """
        route = self.flights[0].source
        for stop in flights_combination.flights:
            route = route + '->' + stop.destination
        return route

    def get_zero_bag_price(self):
        """
        :return: Intiger, price for flights combination for passenger without bags
        """
        return sum([int(stop.price) for stop in flights_combination.flights])

    def get_one_bag_price(self):
        """
        :return: Intiger, price for flights combination for passenger with one bag
        """
        return self.get_zero_bag_price() + sum([int(stop.bag_price) for stop in flights_combination.flights])


    def get_two_bags_price(self):
        """
        :return: Intiger, price for flights combination for passenger with two bags
        """
        return self.get_zero_bag_price() + 2*sum([int(stop.bag_price) for stop in flights_combination.flights])

    def get_max_bags_allowance(self):
        """
        :return: Intiger, maximum number of bags that passenger could take for a flight combination
        """
        return min([int(stop.bags_allowed) for stop in flights_combination.flights])

def find_combinations(flight, available_flight, flights_combination):
    """
    Recursive function that search for flights combinations
    :param flight: Picked source flight
    :param available_flight: All available flights
    :param flights_combination: Flights combinations that has been found so far
    :return:
    """
    for fl in [elem for elem in available_flights if elem.source == flight.destination]:
        if fl.source not in [stop.source for stop in flights_combination]:
            min_departure_time = flight.arrival + timedelta(hours=1)
            max_departure_time = flight.arrival + timedelta(hours=4)
            if fl.departure > min_departure_time and fl.departure < max_departure_time:
                find_combinations(fl, available_flights, flights_combination)
                flights_combination.append(fl)


def load_csv():
    """
    Function load csv file from stdin
    :return: List of Flights objects
    """
    available_flights = []
    stdin_input = sys.stdin.readlines()
    if not stdin_input:
        sys.stderr.write("[Error] No CSV data has been provided!\n")
        exit(1)
    csv_input = csv.DictReader(stdin_input)
    next(csv_input, None)  # skip the headers
    for row in csv_input:
        available_flights.append(Flight(source=row['source'], destination=row['destination'],
                                        departure=datetime.strptime(row['departure'], '%Y-%m-%dT%H:%M:%S'),
                                        arrival=datetime.strptime(row['arrival'], '%Y-%m-%dT%H:%M:%S'),
                                        flight_number=row['flight_number'], price=row['price'],
                                        bags_allowed=row['bags_allowed'], bag_price=int(row['bag_price'])
                                        ))
    return available_flights


if __name__ == '__main__':
    available_flights = load_csv()
    all_combinations = []
    for fl in available_flights:
        flights_combination = FlightsCombination([fl])
        find_combinations(fl, available_flights, flights_combination.flights)
        if flights_combination.flights.__len__() > 1:
            all_combinations.append(flights_combination)

    print("===Combimantions of flights suitable for passengers with no bags===")
    for flights_combination in all_combinations:
        print("Route: %s, no bags: %s€" % (flights_combination.get_route(),
                                                   flights_combination.get_zero_bag_price()))
        print(flights_combination)

    print("===Combimantions of flights suitable for passengers with one bag===")
    for flights_combination in all_combinations:
        if flights_combination.get_max_bags_allowance() >= 1:
            print("Route: %s, one bag: %s€" % (flights_combination.get_route(),
                                               flights_combination.get_one_bag_price()))
            print(flights_combination)

    print("===Combimantions of flights suitable for passengers with two bags===")
    for flights_combination in all_combinations:
        if flights_combination.get_max_bags_allowance() >= 2:
            print("Route: %s, two bags: %s€" % (flights_combination.get_route(),
                                               flights_combination.get_two_bags_price()))
            print(flights_combination)



