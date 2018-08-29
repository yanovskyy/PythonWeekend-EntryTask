import csv


class Flight(object):
    source = ""
    def __init__(self, source, destination, departure, arrival, price,
                 bags_allowed, bag_price, flight_number):
        self.source = str(source),
        self.destination = destination,
        self.departure = departure,
        self.arrival = arrival,
        self.price = price,
        self.bags_allowed = bags_allowed,
        self.bag_price = bag_price,
        self.flight_number = flight_number

    # def __str__(self):
    #     return 'From: %s, To: %s' % (self.source, self.destination)

with open('input.csv', 'r') as csvfile:
    csv_input = csv.reader(csvfile)
    next(csv_input, None)  # skip the headers

    available_flights = []
    for row in csv_input:
        source = str(row[0])
        available_flights.append(Flight(source=source, destination=row[1], departure=row[2],
                     arrival=row[3],flight_number=row[4] ,price=row[5],
                     bags_allowed=row[5], bag_price=row[6]
                     ))

        #print(available_flights[0].source)

dictionary = []
airports = set([])
for flight in available_flights:
    airports.add(flight.source)
    airports.add(flight.destination)

print(airports)