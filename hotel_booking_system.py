
"""Hotel room reservation and booking management module."""

import hashlib
import json
import secrets

ROOM_INVENTORY = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Book an available room and optionally record the reservation."""
    if booking_log is None:
        booking_log = []

    if room_num not in ROOM_INVENTORY:
        return False

    if ROOM_INVENTORY[room_num]["is_booked"]:
        return False

    ROOM_INVENTORY[room_num]["is_booked"] = True
    booking_log.append(
        f"Reserved room {room_num} for guest {guest_name}"
    )
    return True


def cancel_booking(room_num):
    """Cancel a booking if the room exists."""
    if room_num not in ROOM_INVENTORY:
        return False

    ROOM_INVENTORY[room_num]["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return True if a room exists and is available."""
    room = ROOM_INVENTORY.get(room_num)
    return room is not None and not room["is_booked"]


def compute_seasonal_rate(room_num, multiplier):
    """Calculate a room's price using a numeric seasonal multiplier."""
    if room_num not in ROOM_INVENTORY:
        raise ValueError(f"Unknown room number: {room_num}")

    if multiplier <= 0:
        raise ValueError("The seasonal multiplier must be positive.")

    base_price = ROOM_INVENTORY[room_num]["price"]
    return base_price * multiplier


def generate_guest_hash(guest_id):
    """Generate a SHA-256 digest for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate a random four-digit booking reference."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export the room inventory to a JSON-formatted ledger."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(ROOM_INVENTORY, file, indent=4)

    print(f"Hotel ledger exported to: {filename}")


def main():
    """Demonstrate the hotel booking management functions."""
    book_room("101", "Emma Watson")
    cancel_booking("102")

    print("Is 103 available:", check_room_status("103"))
    print(
        "Surge price:",
        compute_seasonal_rate("101", 1.25),
    )
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())

    export_room_ledger()


if __name__ == "__main__":
    main()
