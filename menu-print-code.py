Emission = {
    "car": 0.120,
    "bus": 0.027,
    "train": 0.014,
    "plane": 0.255,
    "motorcycle": 0.072,
    "bike": 0.0,
    "walk": 0.0
}

Speeds = {
    "car": 90,
    "bus": 70,
    "train": 150,
    "plane": 800,
    "motorcycle": 80,
    "bike": 20,
    "walk": 5
}

Costs = {
    "car": 0.12,
    "bus": 0.05,
    "train": 0.08,
    "plane": 0.15,
    "motorcycle": 0.07,
    "bike": 0.0,
    "walk": 0.0
}

Traffic = {
    "low": 1.0,
    "medium": 1.2,
    "high": 1.5
}

# FUNCTIONS

def calculate_emissions(distance, transport, people):
    return (distance * EMISSION[transport]) / people


def calculate_time(distance, transport, traffic_level):
    speed = SPEEDS[transport]
    return (distance / speed) * TRAFFIC[traffic_level]


def calculate_cost(distance, transport, people):
    return (distance * COSTS[transport]) / people

def log_trip(distance, transport, people, traffic):
    emissions = calculate_emissions(distance, transport, people)
    time = calculate_time(distance, transport, traffic)
    cost = calculate_cost(distance, transport, people)

    travel_log.append((distance, transport, people, emissions, time, cost))

    return emissions, time, cost

def smart_comparator(distance, people, traffic):
    results = {}

    for t in EMISSION_FACTORS.keys():
        emi = calculate_emissions(distance, t, people)
        time = calculate_time(distance, t, traffic)
        cost = calculate_cost(distance, t, people)

        # Weighted scoring system
        score = emi * 0.4 + time * 0.3 + cost * 0.3

        results[t] = (emi, time, cost, score)

    best = min(results, key=lambda x: results[x][3])
    return best, results[best]

# MENU

def menu():
    while True:
        print("\n=== SMART TRAVEL CALCULATOR ===")
        print("1. Log a trip")
        print("2. Smart transport comparator")
        print("3. View trip log")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            

        elif option == "2":
            

        elif option == "3":
          

        elif option == "4":

        else:
            print("Invalid option.")
