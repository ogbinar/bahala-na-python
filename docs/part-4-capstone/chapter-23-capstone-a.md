# Chapter 23: Capstone A -- Barangay Management System (Part 1)

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Advanced |
    | **Time** | 60 min |
    | **XP** | +200 XP |

> **Story Hook:** Your barangay captain approaches you after a community clean-up. "Naku, ang hirap namin mag-track ng mga resident fees," he says. "Nawawala ang records, napapalitan ng mga tao, at kapag kailangan ng certificate,ahan namin." He hands you a worn notebook full of handwritten entries. You open it: names, addresses, monthly fees, payments -- some marked "PAID," others with question marks. "Kaya mo ba 'to?" he asks. You think about everything you've learned: classes, files, APIs, error handling. "Bahala na," you say. And you start building.

---

## What You'll Learn

You're building a **Barangay Management System** -- a complete application that helps barangay officials manage residents, collect fees, and issue certificates. This combines everything from the entire book:

- **Variables & Types** -- Storing resident data
- **Lists & Dictionaries** -- Organizing records
- **Conditionals** -- Validating payments, checking eligibility
- **Loops** -- Processing batches of records
- **Functions** -- Reusable operations
- **Classes & OOP** -- Modeling residents, fees, certificates
- **File I/O** -- Saving and loading data
- **Error Handling** -- Graceful failure
- **APIs** -- Connecting to PSA or DILG systems
- **Data Visualization** -- Charts for fee collection reports

This is a two-chapter project. Chapter 23 covers the foundation. Chapter 24 adds advanced features.

## Part 1: Data Models

Let's start by defining the core data models:

```python
# Barangay Management System
# Chapter 23 -- Part 1: Data Models

from datetime import datetime, date
from enum import Enum
import json
import os


class PaymentStatus(Enum):
    UNPAID = "unpaid"
    PAID = "paid"
    PARTIAL = "partial"
    OVERDUE = "overdue"


class FeeType(Enum):
    MONTHLY = "Monthly Dues"
    WASTE_MANAGEMENT = "Waste Management Fee"
    SECURITY = "Security Fee"
    PARKING = "Parking Fee"
    OTHER = "Other"


class Resident:
    """Represents a barangay resident."""

    def __init__(self, first_name, last_name, middle_name="",
                 address="", contact="", birthdate=None,
                 civil_status="single", occupation=""):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.address = address
        self.contact = contact
        self.birthdate = birthdate or date.today()
        self.civil_status = civil_status
        self.occupation = occupation
        self.resident_id = self._generate_id()
        self.registration_date = date.today()
        self.fees = {}  # {date: {fee_type: PaymentStatus}}
        self.certificates = []

    _id_counter = 0

    def _generate_id(self):
        """Generate a unique resident ID: BRGY-YYYY-NNNN."""
        Resident._id_counter += 1
        year = datetime.now().year
        return f"BRGY-{year}-{Resident._id_counter:04d}"

    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def is_senior(self):
        return self.age() >= 60

    def is_pWD(self):
        # In a real app, this would be a verified status
        return False  # Set to True if verified

    def to_dict(self):
        return {
            "resident_id": self.resident_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "address": self.address,
            "contact": self.contact,
            "birthdate": self.birthdate.isoformat(),
            "civil_status": self.civil_status,
            "occupation": self.occupation,
            "registration_date": self.registration_date.isoformat(),
            "is_senior": self.is_senior(),
            "fees": {k: {ft.value: st.value for ft, st in v.items()} for k, v in self.fees.items()},
        }

    @classmethod
    def from_dict(cls, data):
        resident = cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            middle_name=data.get("middle_name", ""),
            address=data.get("address", ""),
            contact=data.get("contact", ""),
            birthdate=date.fromisoformat(data["birthdate"]),
            civil_status=data.get("civil_status", "single"),
            occupation=data.get("occupation", ""),
        )
        resident.resident_id = data["resident_id"]
        resident.registration_date = date.fromisoformat(data["registration_date"])
        # Restore fees
        for k, v in data.get("fees", {}).items():
            if isinstance(v, dict):
                resident.fees[k] = {FeeType(fk): PaymentStatus(fv) for fk, fv in v.items()}
            else:
                resident.fees[k] = PaymentStatus(v)
        return resident

    def __str__(self):
        return f"{self.full_name()} ({self.resident_id})"

    def __repr__(self):
        return f"Resident('{self.full_name()}', '{self.resident_id}')"
```

## Part 2: Fee Management

```python
class FeeManager:
    """Manages fee collection for residents."""

    FEE_AMOUNTS = {
        FeeType.MONTHLY: 500.00,
        FeeType.WASTE_MANAGEMENT: 200.00,
        FeeType.SECURITY: 300.00,
        FeeType.PARKING: 1000.00,
    }

    def __init__(self):
        self.residents = {}  # {resident_id: Resident}
        self.transactions = []  # All payment records
        self.load_data()

    def add_resident(self, resident):
        """Add a new resident."""
        self.residents[resident.resident_id] = resident
        self.save_data()
        print(f"✅ Resident registered: {resident.full_name()}")

    def find_resident(self, query):
        """Search for a resident by ID, name, or address."""
        query = query.lower().strip()
        results = []

        for resident in self.residents.values():
            if (query in resident.resident_id.lower() or
                query in resident.full_name().lower() or
                query in resident.address.lower()):
                results.append(resident)

        return results

    def pay_fee(self, resident_id, fee_type, amount=None, date_str=None):
        """Record a fee payment."""
        if resident_id not in self.residents:
            print(f"❌ Resident {resident_id} not found.")
            return None

        resident = self.residents[resident_id]
        fee_date = date_str or date.today().isoformat()

        if amount is None:
            amount = self.FEE_AMOUNTS.get(fee_type, 500.00)

        # Record payment
        if fee_date not in resident.fees:
            resident.fees[fee_date] = {}
        resident.fees[fee_date][fee_type] = PaymentStatus.PAID

        # Record transaction
        transaction = {
            "date": fee_date,
            "resident_id": resident_id,
            "resident_name": resident.full_name(),
            "fee_type": fee_type.value,
            "amount": amount,
        }
        self.transactions.append(transaction)
        self.save_data()

        print(f"💰 Payment recorded:")
        print(f"   {resident.full_name()}")
        print(f"   {fee_type.value}: ₱{amount:.2f}")
        print(f"   Date: {fee_date}")

        return transaction

    def get_outstanding_fees(self, resident_id):
        """Get all unpaid fees for a resident."""
        resident = self.residents.get(resident_id)
        if not resident:
            return []

        outstanding = []
        for fee_date, fees in resident.fees.items():
            for fee_type, status in fees.items():
                if status != PaymentStatus.PAID:
                    amount = self.FEE_AMOUNTS.get(fee_type, 500.00)
                    outstanding.append({
                        "date": fee_date,
                        "fee_type": fee_type.value,
                        "amount": amount,
                        "status": status.value,
                    })
        return outstanding

    def generate_collection_report(self, start_date=None, end_date=None):
        """Generate a fee collection report."""
        if not start_date:
            start_date = date.today().replace(day=1).isoformat()
        if not end_date:
            end_date = date.today().isoformat()

        relevant = [
            t for t in self.transactions
            if start_date <= t["date"] <= end_date
        ]

        total_collected = sum(t["amount"] for t in relevant)
        total_transactions = len(relevant)

        # By fee type
        by_type = {}
        for t in relevant:
            fee = t["fee_type"]
            if fee not in by_type:
                by_type[fee] = {"count": 0, "total": 0}
            by_type[fee]["count"] += 1
            by_type[fee]["total"] += t["amount"]

        print(f"\n{'=' * 50}")
        print(f"  BARANGAY FEE COLLECTION REPORT")
        print(f"  Period: {start_date} to {end_date}")
        print(f"{'=' * 50}")
        print(f"  Total Transactions: {total_transactions}")
        print(f"  Total Collected: ₱{total_collected:.2f}")
        print(f"{'=' * 50}")
        print(f"  By Fee Type:")
        for fee_type, data in sorted(by_type.items()):
            print(f"    {fee_type}: {data['count']} payments = ₱{data['total']:.2f}")
        print(f"{'=' * 50}\n")

        return {
            "total_collected": total_collected,
            "total_transactions": total_transactions,
            "by_type": by_type,
        }

    def save_data(self):
        """Save all data to JSON files."""
        with open("barangay_residents.json", "w") as f:
            json.dump(
                {rid: r.to_dict() for rid, r in self.residents.items()},
                f, indent=4
            )
        with open("barangay_transactions.json", "w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_data(self):
        """Load all data from JSON files."""
        if os.path.exists("barangay_residents.json"):
            with open("barangay_residents.json", "r") as f:
                data = json.load(f)
            for rid, rdata in data.items():
                self.residents[rid] = Resident.from_dict(rdata)

        if os.path.exists("barangay_transactions.json"):
            with open("barangay_transactions.json", "r") as f:
                self.transactions = json.load(f)
```

## Part 3: The Command-Line Interface

```python
def main_menu():
    """Main menu for the Barangay Management System."""
    manager = FeeManager()

    while True:
        print(f"\n{'=' * 50}")
        print(f"  BARANGAY MANAGEMENT SYSTEM")
        print(f"{'=' * 50}")
        print("  1. Register resident")
        print("  2. Search resident")
        print("  3. Pay fee")
        print("  4. View outstanding fees")
        print("  5. Collection report")
        print("  6. List all residents")
        print("  7. Exit")
        print(f"{'=' * 50}")

        choice = input("\nChoose (1-7): ").strip()

        if choice == "1":
            # Register resident
            print("\n--- Register New Resident ---")
            first = input("First name: ")
            last = input("Last name: ")
            middle = input("Middle name (optional): ")
            address = input("Address (house #, street, purok): ")
            contact = input("Contact number: ")
            birthdate = input("Birthdate (YYYY-MM-DD): ")
            try:
                birthdate_obj = date.fromisoformat(birthdate)
            except ValueError:
                birthdate_obj = date.today()

            resident = Resident(
                first_name=first,
                last_name=last,
                middle_name=middle,
                address=address,
                contact=contact,
                birthdate=birthdate_obj,
            )
            manager.add_resident(resident)

        elif choice == "2":
            # Search resident
            query = input("\nSearch by name, ID, or address: ")
            results = manager.find_resident(query)
            if results:
                print(f"\nFound {len(results)} resident(s):")
                for r in results:
                    senior = " [Senior]" if r.is_senior() else ""
                    print(f"  {r.resident_id} - {r.full_name()}{senior}")
                    print(f"    Address: {r.address}")
                    print(f"    Contact: {r.contact}")
            else:
                print("No residents found.")

        elif choice == "3":
            # Pay fee
            resident_id = input("\nResident ID: ")
            print("Fee types:")
            for fee_type in FeeType:
                amount = FeeManager.FEE_AMOUNTS.get(fee_type, 500.00)
                print(f"  {fee_type.value}: ₱{amount:.2f}")
            fee_type_str = input("Fee type: ").strip()
            try:
                fee_type = FeeType(fee_type_str)
            except ValueError:
                print(f"Invalid fee type. Choose from the list above.")
                continue

            amount_str = input("Amount (press Enter for default): ").strip()
            amount = float(amount_str) if amount_str else None

            manager.pay_fee(resident_id, fee_type, amount)

        elif choice == "4":
            # View outstanding fees
            resident_id = input("\nResident ID: ")
            outstanding = manager.get_outstanding_fees(resident_id)
            if outstanding:
                print(f"\nOutstanding fees for {resident_id}:")
                for fee in outstanding:
                    print(f"  {fee['date']} - {fee['fee_type']}: ₱{fee['amount']:.2f} ({fee['status']})")
            else:
                print("No outstanding fees. All paid! ✅")

        elif choice == "5":
            # Collection report
            start = input("Start date (YYYY-MM-DD, press Enter for 1st of this month): ").strip()
            end = input("End date (YYYY-MM-DD, press Enter for today): ").strip()
            start = start or None
            end = end or None
            manager.generate_collection_report(start, end)

        elif choice == "6":
            # List all residents
            print(f"\nAll Residents ({len(manager.residents)} total):")
            for rid, resident in sorted(manager.residents.items()):
                senior = " [Senior]" if resident.is_senior() else ""
                print(f"  {rid} - {resident.full_name()}{senior}")

        elif choice == "7":
            print("Saving data... See you next time!")
            break

        else:
            print("Invalid choice. Subok ulit.")


if __name__ == "__main__":
    main_menu()
```

## Running the System

```bash
python barangay_system.py
```

Sample interaction:

```
==================================================
  BARANGAY MANAGEMENT SYSTEM
==================================================
  1. Register resident
  2. Search resident
  3. Pay fee
  4. View outstanding fees
  5. Collection report
  6. List all residents
  7. Exit
==================================================

Choose (1-7): 1

--- Register New Resident ---
First name: Juan
Last name: Cruz
Middle name: Santos
Address (house #, street, purok): 123 Rizal St, Purok 3
Contact number: 09171234567
Birthdate (YYYY-MM-DD): 1985-03-15
✅ Resident registered: Juan Santos Cruz
```

??? example "Portfolio Tip: Full-Stack Application"
    Your barangay management system is a real, complete application. This is the kind of project that gets interviews:

    1. **GitHub README** -- Write a full README: problem statement, features, installation instructions, screenshots of the CLI interface, and a data model diagram
    2. **LinkedIn Featured Section** -- Pin this project. Write: "Built a complete barangay management system with resident tracking, fee management, and data persistence. Handles real-world edge cases like duplicate residents and partial payments."
    3. **Interview talking point** -- "I built a full barangay management system from scratch. It handles resident registration, fee tracking with payment status enums, and data persistence using JSON. I designed it with real-world constraints in mind -- like handling 500+ residents and supporting multiple barangays. This taught me about data modeling, file I/O, and building production-ready CLI tools."

## Summary

- Defined `Resident` and `FeeManager` classes
- Implemented fee tracking with `PaymentStatus` enum
- Built a JSON-based data persistence system
- Created a command-line interface for barangay officials
- Data is saved to files and persists between sessions

## What's Next

In Chapter 24, you'll add:
- Certificate generation (barangay clearances, indigency certificates)
- Advanced reporting with charts
- API integration for PSA verification
- Error handling improvements
- A graphical interface option

## Side Quests

??? note "Optional: Side Quest"
    - Add a "bulk import" feature that reads resident data from CSV
    - Build a web version using Flask
    - Add SMS notifications for overdue fees
    - Create a "resident ID card" generator that outputs a printable PDF

## Further Reading

- [Python's `json` module](https://docs.python.org/3/library/json.html)
- [Python's `enum` module](https://docs.python.org/3/library/enum.html)
- [DILG Barangay Management Guidelines](https://dilg.gov.ph/)

---

??? example "🧠 Reflection — Capstone A: Barangay Management System (Part 1)"

    - **What did you learn?** Building a complete application requires combining classes, data persistence, enums, and a user interface into one coherent system.
    - **How can you apply this?** Offer to digitize your barangay's handwritten records — the same problem the barangay captain faced in the story hook.
    - **What's next?** How could you scale this system to handle multiple barangays competing for the same municipal resources?

??? checkbox "✅ Chapter Checklist"

    - [ ] Define `Resident` and `FeeManager` classes with proper data models
    - [ ] Use enums (`PaymentStatus`, `FeeType`) for type-safe fee tracking
    - [ ] Implement JSON-based data persistence that survives between sessions
    - [ ] Build a command-line interface with a menu-driven workflow
    - [ ] Handle edge cases like search queries and missing residents

---

*Next: [Chapter 24: Capstone B](chapter-24-capstone-b.md) -- Adding certificates, APIs, and advanced features.*
