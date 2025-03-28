import streamlit as st
import datetime

# Sample Data
destinations = {
    "Mars Colony": {"economy": 5000, "luxury": 15000, "vip": 30000},
    "Lunar Hotel": {"economy": 2000, "luxury": 10000, "vip": 20000},
    "Orbital Station Alpha": {"economy": 1000, "luxury": 5000, "vip": 10000},
}

accommodations = {
    "Mars Colony": ["Red Dust Inn", "Olympus Mons Suites"],
    "Lunar Hotel": ["Crater View Lodge", "Zero-Gravity Pods"],
    "Orbital Station Alpha": ["Stellar Stay", "Galactic Suite"],
}

# Initialize session state for user bookings
if "bookings" not in st.session_state:
    st.session_state.bookings = []

# Page Title
st.title("🚀 Space Travel Booking Platform")
st.write("Welcome to the future of space travel! Book your trip to the stars today.")

# Sidebar for Navigation
st.sidebar.title("Menu")
menu_choice = st.sidebar.radio(
    "Choose an option:",
    ["Book a Trip", "View Bookings", "Countdown to Launch", "AI Travel Tips"],
)

# Book a Trip
if menu_choice == "Book a Trip":
    st.header("Book Your Space Trip")

    # Destination Selection
    destination = st.selectbox("Choose your destination:", list(destinations.keys()))

    # Display Pricing Options
    st.subheader("Pricing Options")
    seat_classes = destinations[destination]
    for seat_class, price in seat_classes.items():
        st.write(f"- **{seat_class.capitalize()}**: ${price}")

    # Seat Class Selection
    seat_class = st.selectbox("Choose your seat class:", list(seat_classes.keys()))
    price = seat_classes[seat_class]

    # Departure Date Selection
    departure_date = st.date_input("Select your departure date:", min_value=datetime.date.today())

    # Confirm Booking
    if st.button("Confirm Booking"):
        booking = {
            "destination": destination,
            "seat_class": seat_class,
            "price": price,
            "departure_date": departure_date,
        }
        st.session_state.bookings.append(booking)
        st.success(f"Booking confirmed! You're heading to {destination} in {seat_class} class for ${price}.")

        # Show recommended accommodations
        st.subheader("Recommended Accommodations")
        for accommodation in accommodations[destination]:
            st.write(f"- {accommodation}")

# View Bookings
elif menu_choice == "View Bookings":
    st.header("Your Bookings")
    if not st.session_state.bookings:
        st.write("No bookings found.")
    else:
        for idx, booking in enumerate(st.session_state.bookings, 1):
            st.write(
                f"{idx}. Destination: {booking['destination']}, "
                f"Seat Class: {booking['seat_class']}, "
                f"Price: ${booking['price']}, "
                f"Departure Date: {booking['departure_date']}"
            )

# Countdown to Launch
elif menu_choice == "Countdown to Launch":
    st.header("Countdown to Launch")
    if not st.session_state.bookings:
        st.write("No bookings found.")
    else:
        booking_idx = st.selectbox(
            "Select a booking:", range(len(st.session_state.bookings)), format_func=lambda x: f"Booking {x + 1}"
        )
        launch_date = st.session_state.bookings[booking_idx]["departure_date"]
        today = datetime.date.today()
        delta = launch_date - today
        if delta.days < 0:
            st.write("Your trip has already launched!")
        else:
            st.write(f"Countdown to launch: {delta.days} days.")

# AI Travel Tips
elif menu_choice == "AI Travel Tips":
    st.header("AI Travel Tips")
    tips = [
        "Pack light: Space luggage limits are strict!",
        "Practice zero-gravity exercises before your trip.",
        "Don't forget your space suit!",
    ]
    for tip in tips:
        st.write(f"- {tip}")
