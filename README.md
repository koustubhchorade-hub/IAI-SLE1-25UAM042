# AI Travel & Hotel Booking Agent

## 📌 About the Project

This project is a **PEAS-based AI Travel & Hotel Booking Agent** developed as part of **SLE-1 for Introduction to Artificial Intelligence (02AML204)**.

The agent is designed to help a user find a suitable hotel based on their travel requirements such as **destination, budget, minimum hotel rating, and number of travelers**.

The project demonstrates how an intelligent agent can receive information from its environment, process the information, and make a suitable recommendation.

---

## 🧠 PEAS Framework

### P — Performance Measure

The agent aims to:

* Find suitable hotels according to user requirements.
* Select hotels within the user's budget.
* Consider hotel ratings.
* Prefer suitable and nearby hotels.
* Provide the best overall recommendation.

### E — Environment

The environment is represented by a simulated hotel database containing:

* Hotel names
* Locations
* Prices
* Ratings
* Distance from the destination
* Room availability

### A — Actuators

The agent performs the following actions:

* **Search** for hotels
* **Filter** hotels according to requirements
* **Compare** suitable hotels
* **Recommend** the best hotel

### S — Sensors

The agent receives the following information from the user:

* Destination
* Maximum budget per night
* Minimum hotel rating
* Number of travelers

---

## ⚙️ How the Agent Works

The agent follows these steps:

```text
User Input
    ↓
Search Hotels
    ↓
Filter Hotels
    ↓
Compare Suitable Hotels
    ↓
Calculate AI Score
    ↓
Recommend Best Hotel
```

The recommendation is based on factors such as **hotel rating, price, and distance**.

---

## 📂 Files in This Repository

### `Hotel_and_Travaling_AI_agent.py`

Python implementation of the AI Travel & Hotel Booking Agent.

### `AI_Travel_Hotel_Booking_Agent.pptx`

Presentation explaining the PEAS framework of the proposed intelligent agent.

### `AI_Contribution_log.md`

AI Contribution Log describing the AI tools used, AI-assisted parts, personal contribution, testing, and issues/fixes.

---

## ▶️ How to Run

### Requirements

* Python 3.x
* No external Python libraries are required.

### Steps

1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the Python file using:

```bash
python Hotel_and_Travaling_AI_agent.py
```

4. Enter the requested travel preferences.
5. The agent will search, filter, compare, and recommend a suitable hotel.

---

## 🧪 Example Input

```text
Destination: Goa
Maximum budget per night: ₹3000
Minimum hotel rating: 4.0
Number of travelers: 2
```

The agent processes these requirements and provides the most suitable hotel from the available simulated data.

---

## 🎯 Objective

The main objective of this project is to understand the working of an **intelligent agent using the PEAS framework** and demonstrate how an AI agent can make decisions based on user preferences and environmental information.

---

## 🤖 AI Contribution

ChatGPT was used as an assistance tool for:

* Understanding the PEAS framework.
* Designing the initial structure of the Python agent.
* Getting suggestions for the search, filtering, comparison, and recommendation logic.
* Debugging and improving the program.

The code was reviewed, modified, and tested according to the project requirements.

Detailed information is provided in **`AI_Contribution_log.md`**.

---

## 📌 Conclusion

The AI Travel & Hotel Booking Agent demonstrates the basic working of a PEAS-based intelligent agent. It takes user requirements as input, processes available hotel information, compares suitable options, and recommends the best available choice. The project provides a simple practical understanding of how AI agents can use sensors, actuators, environments, and performance measures to make decisions.
