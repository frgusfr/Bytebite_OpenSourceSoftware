# ======================================================
# ADVANCED PROGRAM: Smart Travel Calculator
# ======================================================

# Emission factors (kg CO2 per km per person)
EMISSION_FACTORS = {
    "car": 0.120,
    "bus": 0.027,
    "train": 0.014,
    "plane": 0.255,
    "motorcycle": 0.072,
    "bike": 0.0,
    "walk": 0.0
}

# Average speeds (km/h)
SPEEDS = {
    "car": 90,
    "bus": 70,
    "train": 150,
    "plane": 800,
    "motorcycle": 80,
    "bike": 20,
    "walk": 5
}

# Estimated cost per km (€)
COSTS = {
    "car": 0.12,
    "bus": 0.05,
    "train": 0.08,
    "plane": 0.15,
    "motorcycle": 0.07,
    "bike": 0.0,
    "walk": 0.0
}

# Traffic modifiers
TRAFFIC = {
    "low": 1.0,
    "medium": 1.2,
    "high": 1.5
}

travel_log = []


# ------------------------------------------------------
# MAIN FUNCTIONS
# ------------------------------------------------------

def calculate_emissions(distance, transport, people):
    return (distance * EMISSION_FACTORS[transport]) / people


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


# ------------------------------------------------------
# MENU
# ------------------------------------------------------

def menu():
    while True:
        print("\n=== SMART TRAVEL CALCULATOR ===")
        print("1. Log a trip")
        print("2. Smart transport comparator")
        print("3. View trip log")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            distance = float(input("Distance in km: "))
            transport = input("Transport: ").lower()
            people = int(input("Number of people sharing the transport: "))
            traffic = input("Traffic level (low/medium/high): ").lower()

            emissions, time, cost = log_trip(distance, transport, people, traffic)

            print(f"\n--- TRIP LOGGED ---")
            print(f"Emissions: {emissions:.2f} kg CO₂")
            print(f"Estimated time: {time:.2f} hours")
            print(f"Approximate cost: {cost:.2f} €")

        elif option == "2":
            distance = float(input("Distance in km: "))
            people = int(input("Number of people: "))
            traffic = input("Traffic level (low/medium/high): ").lower()

            best, data = smart_comparator(distance, people, traffic)
            emi, time, cost, _ = data

            print("\n--- BEST OVERALL OPTION ---")
            print(f"Recommended transport: {best}")
            print(f"Emissions: {emi:.2f} kg CO₂")
            print(f"Time: {time:.2f} h")
            print(f"Cost: {cost:.2f} €")

        elif option == "3":
            print("\n--- TRIP LOG ---")
            for trip in travel_log:
                print(trip)

        elif option == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
