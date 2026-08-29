# AI Travel & Hotel Booking Agent
# SLE-1 - PEAS Based Intelligent Agent

# -------------------------------
# HOTEL DATABASE (Environment)
# -------------------------------

hotels = [
    {
        "name": "Goa Beach Resort",
        "location": "Goa",
        "price": 2500,
        "rating": 4.5,
        "distance": 1.5,
        "rooms": 3
    },
    {
        "name": "Palm Paradise Hotel",
        "location": "Goa",
        "price": 1800,
        "rating": 4.1,
        "distance": 3.0,
        "rooms": 5
    },
    {
        "name": "Ocean View Hotel",
        "location": "Goa",
        "price": 3200,
        "rating": 4.7,
        "distance": 1.0,
        "rooms": 2
    },
    {
        "name": "City Comfort Inn",
        "location": "Mumbai",
        "price": 2200,
        "rating": 4.0,
        "distance": 2.5,
        "rooms": 4
    },
    {
        "name": "Mumbai Grand Hotel",
        "location": "Mumbai",
        "price": 3500,
        "rating": 4.6,
        "distance": 1.2,
        "rooms": 3
    }
]


# -------------------------------
# SENSOR
# Gets information from the user
# -------------------------------

def get_user_preferences():
    print("\n===== TRAVEL PREFERENCES =====")

    destination = input("Enter destination: ")
    budget = float(input("Enter maximum budget per night (₹): "))
    min_rating = float(input("Enter minimum hotel rating (0-5): "))
    travelers = int(input("Enter number of travelers: "))

    return destination, budget, min_rating, travelers


# -------------------------------
# SEARCH ACTUATOR
# Finds hotels in the destination
# -------------------------------

def search_hotels(destination):
    results = []

    for hotel in hotels:
        if hotel["location"].lower() == destination.lower():
            results.append(hotel)

    return results


# -------------------------------
# FILTER ACTUATOR
# Filters according to preferences
# -------------------------------

def filter_hotels(hotels_found, budget, min_rating, travelers):
    suitable = []

    for hotel in hotels_found:

        if (hotel["price"] <= budget and
                hotel["rating"] >= min_rating and
                hotel["rooms"] > 0):

            suitable.append(hotel)

    return suitable


# -------------------------------
# COMPARE ACTUATOR
# Calculates a score for each hotel
# -------------------------------

def calculate_score(hotel, budget):

    # Higher rating = better
    rating_score = hotel["rating"] * 20

    # Lower price = better
    price_score = ((budget - hotel["price"]) / budget) * 30

    # Closer hotel = better
    distance_score = max(0, 20 - (hotel["distance"] * 5))

    total_score = rating_score + price_score + distance_score

    return total_score


# -------------------------------
# RECOMMEND ACTUATOR
# Selects the best hotel
# -------------------------------

def recommend_hotel(suitable_hotels, budget):

    if not suitable_hotels:
        return None

    best_hotel = suitable_hotels[0]
    best_score = calculate_score(best_hotel, budget)

    for hotel in suitable_hotels[1:]:

        score = calculate_score(hotel, budget)

        if score > best_score:
            best_score = score
            best_hotel = hotel

    return best_hotel, best_score


# -------------------------------
# DISPLAY RESULTS
# -------------------------------

def display_results(hotels_found):

    print("\n===== AVAILABLE HOTELS =====")

    for hotel in hotels_found:
        print(
            f"{hotel['name']} | "
            f"₹{hotel['price']}/night | "
            f"Rating: {hotel['rating']} | "
            f"Distance: {hotel['distance']} km"
        )


# -------------------------------
# MAIN AI AGENT
# -------------------------------

def travel_agent():

    print("======================================")
    print("   AI TRAVEL & HOTEL BOOKING AGENT")
    print("======================================")

    # Sensor: Get user information
    destination, budget, min_rating, travelers = get_user_preferences()

    print("\nSearching for hotels...")

    # Actuator: Search
    found_hotels = search_hotels(destination)

    if not found_hotels:
        print("Sorry! No hotels found for this destination.")
        return

    display_results(found_hotels)

    # Actuator: Filter
    suitable_hotels = filter_hotels(
        found_hotels,
        budget,
        min_rating,
        travelers
    )

    if not suitable_hotels:
        print("\nNo hotels match your preferences.")
        return

    print("\n===== SUITABLE HOTELS =====")
    display_results(suitable_hotels)

    # Actuator: Compare + Recommend
    recommendation = recommend_hotel(
        suitable_hotels,
        budget
    )

    best_hotel, score = recommendation

    print("\n======================================")
    print("       AI AGENT RECOMMENDATION")
    print("======================================")

    print(f"Recommended Hotel : {best_hotel['name']}")
    print(f"Price             : ₹{best_hotel['price']}/night")
    print(f"Rating            : {best_hotel['rating']}/5")
    print(f"Distance          : {best_hotel['distance']} km")
    print(f"AI Score          : {score:.2f}")

    print("\nReason:")
    print("- Within your budget")
    print("- Meets your minimum rating")
    print("- Suitable location")
    print("- Best overall score among available hotels")

    print("\nBooking simulation completed.")


# -------------------------------
# RUN THE AGENT
# -------------------------------

travel_agent()
