# Chapter 24: Capstone B -- Barangay Management System (Part 2)

??? example "📋 Chapter Info"
    | | |
    |---|---|
    | **Difficulty** | ⭐⭐⭐ Advanced |
    | **Time** | 60 min |
    | **XP** | +200 XP |

> **Story Hook:** The barangay captain is impressed with the basic system. "Galing!" he says. "Pero kailangan namin ng certificates -- barangay clearance, indigency, residence certification. And the residents keep asking when their fees are due. And the municipal office wants a report every month." You nod. "I know. I'm building it."

---

## What You'll Add

In this chapter, you'll extend the Barangay Management System from Chapter 23 with:

1. **Certificate generation** -- Barangay clearances, indigency, residency certs
2. **Advanced reporting** -- Monthly and yearly summaries
3. **API integration** -- Connecting to external data services
4. **Improved error handling** -- Graceful failures
5. **A web interface option** -- For officials who prefer browsers

## Part 1: Certificate Generation

```python
# Certificate Generation
# Chapter 24 -- Part 2

from datetime import datetime, timedelta
import os


class CertificateGenerator:
    """Generates barangay certificates."""

    CERTIFICATE_TEMPLATES = {
        "clearance": """
╔══════════════════════════════════════════════╗
║           BARANGAY CERTIFICATE OF CLEARANCE  ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   {address}                                  ║
║   is a registered resident of this barangay  ║
║   with NO pending cases or obligations.      ║
║                                              ║
║   Issued on: {date}                          ║
║   Valid until: {expiry}                      ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
        "indigency": """
╔══════════════════════════════════════════════╗
║        BARANGAY CERTIFICATE OF INDIGENCY     ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   {address}                                  ║
║   is a resident of this barangay and is      ║
║   financially indigent.                      ║
║                                              ║
║   This certificate is issued for the         ║
║   purpose of: {purpose}                      ║
║                                              ║
║   Issued on: {date}                          ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
        "residency": """
╔══════════════════════════════════════════════╗
║     BARANGAY CERTIFICATE OF RESIDENCY        ║
║                                              ║
║   This certifies that                        ║
║   {name}                                     ║
║   has been a resident of this barangay       ║
║   since {residency_start}                    ║
║   at {address}                               ║
║                                              ║
║   This certificate is issued for the         ║
║   purpose of: {purpose}                      ║
║                                              ║
║   Issued on: {date}                          ║
║                                              ║
║   {captain_name}                             ║
║   Barangay Captain                           ║
║   Barangay {barangay_name}                   ║
║   {municipality}, {province}                 ║
╚══════════════════════════════════════════════╝
        """,
    }

    def __init__(self, barangay_name="Barangay San Isidro",
                 municipality="Municipality", province="Province",
                 captain_name="Hon. Juan Dela Cruz"):
        self.barangay_name = barangay_name
        self.municipality = municipality
        self.province = province
        self.captain_name = captain_name

    def generate(self, resident, cert_type, purpose=""):
        """Generate a certificate for a resident."""
        template = self.CERTIFICATE_TEMPLATES.get(cert_type)
        if not template:
            raise ValueError(
                f"Unknown certificate type: {cert_type}. "
                f"Choose from: {', '.join(self.CERTIFICATE_TEMPLATES.keys())}"
            )

        now = datetime.now()
        expiry = (now.replace(day=1) + timedelta(days=90)).strftime("%B %d, %Y")

        context = {
            "name": resident.full_name(),
            "address": resident.address,
            "date": now.strftime("%B %d, %Y"),
            "expiry": expiry,
            "purpose": purpose or "General Purpose",
            "barangay_name": self.barangay_name,
            "municipality": self.municipality,
            "province": self.province,
            "captain_name": self.captain_name,
            "residency_start": resident.registration_date.strftime("%B %d, %Y"),
        }

        certificate = template.format(**context)

        # Save to file
        filename = f"certificate_{resident.resident_id}_{cert_type}_{now.strftime('%Y%m%d')}.txt"
        with open(filename, "w") as f:
            f.write(certificate)

        print(f"📄 Certificate generated: {filename}")
        print()
        print(certificate)

        return filename


# Usage
# cert_gen = CertificateGenerator()
# resident = manager.find_resident("juan")[0]
# cert_gen.generate(resident, "clearance")
# cert_gen.generate(resident, "indigency", "Court Requirement")
```

## Part 2: Advanced Reporting

```python
class ReportGenerator:
    """Generates advanced reports for barangay officials."""

    def __init__(self, fee_manager):
        self.fee_manager = fee_manager

    def monthly_summary(self, year=None, month=None):
        """Generate a monthly fee collection summary."""
        if not year:
            year = datetime.now().year
        if not month:
            month = datetime.now().month

        start = f"{year}-{month:02d}-01"
        if month == 12:
            end = f"{year + 1}-01-01"
        else:
            end = f"{year}-{month + 1:02d}-01"

        # Get all transactions for the month
        transactions = [
            t for t in self.fee_manager.transactions
            if start <= t["date"] < end
        ]

        total_collected = sum(t["amount"] for t in transactions)
        unique_payers = len(set(t["resident_id"] for t in transactions))
        total_residents = len(self.fee_manager.residents)

        # By fee type
        by_type = {}
        for t in transactions:
            fee = t["fee_type"]
            if fee not in by_type:
                by_type[fee] = {"count": 0, "total": 0}
            by_type[fee]["count"] += 1
            by_type[fee]["total"] += t["amount"]

        print(f"\n{'=' * 60}")
        print(f"  MONTHLY SUMMARY -- {datetime(year, month, 1).strftime('%B %Y')}")
        print(f"{'=' * 60}")
        print(f"  Residents: {total_residents}")
        print(f"  Paid this month: {unique_payers}")
        print(f"  Collection rate: {(unique_payers/total_residents*100):.1f}%")
        print(f"  Total collected: ₱{total_collected:.2f}")
        print(f"{'-' * 60}")
        print(f"  By Fee Type:")
        for fee_type, data in sorted(by_type.items()):
            bar = "█" * int(data['total'] / 100)
            print(f"    {fee_type:.<30} {bar} ₱{data['total']:>10.2f}")
        print(f"{'=' * 60}\n")

        return {
            "month": f"{year}-{month:02d}",
            "total_collected": total_collected,
            "unique_payers": unique_payers,
            "collection_rate": unique_payers / total_residents * 100,
            "by_type": by_type,
        }

    def resident_status_report(self, resident):
        """Generate a status report for a single resident."""
        print(f"\n{'=' * 60}")
        print(f"  RESIDENT STATUS REPORT")
        print(f"{'=' * 60}")
        print(f"  Name: {resident.full_name()}")
        print(f"  ID: {resident.resident_id}")
        print(f"  Address: {resident.address}")
        print(f"  Contact: {resident.contact}")
        print(f"  Age: {resident.age()}")
        print(f"  Senior: {'Yes' if resident.is_senior() else 'No'}")
        print(f"  Registered: {resident.registration_date}")
        print(f"{'-' * 60}")

        # Fee history
        if resident.fees:
            print(f"  Fee History:")
            for fee_date, fees in sorted(resident.fees.items()):
                print(f"    {fee_date}:")
                for fee_type, status in fees.items():
                    amount = FeeManager.FEE_AMOUNTS.get(fee_type, 500.00)
                    symbol = "✅" if status == PaymentStatus.PAID else "❌"
                    print(f"      {symbol} {fee_type}: ₱{amount:.2f} ({status.value})")
        else:
            print(f"  No fee records found.")

        # Certificates
        if resident.certificates:
            print(f"  Certificates issued:")
            for cert in resident.certificates:
                print(f"    - {cert['type']} ({cert['date']})")

        print(f"{'=' * 60}\n")

    def yearly_comparison(self, year=None):
        """Compare fee collection across months."""
        if not year:
            year = datetime.now().year

        print(f"\n{'=' * 60}")
        print(f"  YEARLY COMPARISON -- {year}")
        print(f"{'=' * 60}")

        monthly_data = []
        for month in range(1, 13):
            start = f"{year}-{month:02d}-01"
            if month == 12:
                end = f"{year + 1}-01-01"
            else:
                end = f"{year}-{month + 1:02d}-01"

            transactions = [
                t for t in self.fee_manager.transactions
                if start <= t["date"] < end
            ]
            total = sum(t["amount"] for t in transactions)
            monthly_data.append((month, total))

        # Display as bar chart (text-based)
        max_amount = max(t for _, t in monthly_data) if monthly_data else 1
        for month, total in monthly_data:
            bar_length = int((total / max_amount) * 40) if max_amount > 0 else 0
            bar = "█" * bar_length
            month_name = datetime(year, month, 1).strftime('%b')
            print(f"  {month_name:>3} | {bar:<40} ₱{total:>10.2f}")

        total_year = sum(t for _, t in monthly_data)
        print(f"{'─' * 60}")
        print(f"  {'TOTAL':>3} |{' ' * 40} ₱{total_year:>10.2f}")
        print(f"{'=' * 60}\n")

        return monthly_data
```

## Part 3: Improved Error Handling

```python
# Enhanced error handling with custom exceptions

class BarangayError(Exception):
    """Base exception for barangay system errors."""
    pass


class ResidentNotFoundError(BarangayError):
    """Raised when a resident is not found."""
    def __init__(self, query):
        self.query = query
        super().__init__(f"Resident not found: '{query}'")


class InvalidFeeError(BarangayError):
    """Raised when a fee type is invalid."""
    def __init__(self, fee_type):
        self.fee_type = fee_type
        super().__init__(f"Invalid fee type: {fee_type}")


class CertificateError(BarangayError):
    """Raised when certificate generation fails."""
    pass


# Example with try/except
def safe_pay_fee(manager, resident_id, fee_type, amount=None):
    """Pay fee with proper error handling."""
    try:
        if resident_id not in manager.residents:
            raise ResidentNotFoundError(resident_id)

        if fee_type not in FeeManager.FEE_AMOUNTS:
            raise InvalidFeeError(fee_type)

        return manager.pay_fee(resident_id, fee_type, amount)

    except ResidentNotFoundError as e:
        print(f"❌ {e}")
        print("   Tip: Use 'Search resident' to find the correct ID.")
    except InvalidFeeError as e:
        print(f"❌ {e}")
        print(f"   Valid fee types: {', '.join(FeeManager.FEE_AMOUNTS.keys())}")
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("   Please try again or contact the system admin.")
```

## Part 4: Web Interface Option

For officials who prefer a browser over a terminal, you can add a simple Flask interface:

```python
# Optional: Web Interface using Flask
# Chapter 24

# Install: pip install flask
# Run: python web_app.py
# Visit: http://localhost:5000

from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Initialize the fee manager
manager = FeeManager()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Barangay Management System</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .form-group { margin: 15px 0; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2980b9; }
        .result { background: #f0f0f0; padding: 15px; margin: 15px 0; border-radius: 4px; }
        .success { color: #27ae60; }
        .error { color: #e74c3c; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #3498db; color: white; }
    </style>
</head>
<body>
    <h1>🏛️ Barangay Management System</h1>

    <h2>Search Resident</h2>
    <div class="form-group">
        <input type="text" id="search" placeholder="Enter name, ID, or address...">
        <button onclick="searchResident()">Search</button>
    </div>
    <div id="results"></div>

    <h2>Register New Resident</h2>
    <div class="form-group">
        <input type="text" id="first_name" placeholder="First Name">
    </div>
    <div class="form-group">
        <input type="text" id="last_name" placeholder="Last Name">
    </div>
    <div class="form-group">
        <input type="text" id="address" placeholder="Address">
    </div>
    <div class="form-group">
        <input type="text" id="contact" placeholder="Contact Number">
    </div>
    <button onclick="registerResident()">Register</button>

    <script>
        async function searchResident() {
            const query = document.getElementById('search').value;
            const response = await fetch(`/api/residents?q=${encodeURIComponent(query)}`);
            const residents = await response.json();
            const results = document.getElementById('results');

            if (residents.length === 0) {
                results.innerHTML = '<div class="result error">No residents found.</div>';
                return;
            }

            let html = '<table><tr><th>ID</th><th>Name</th><th>Address</th><th>Contact</th></tr>';
            for (const r of residents) {
                html += `<tr><td>${r.resident_id}</td><td>${r.first_name} ${r.last_name}</td>
                         <td>${r.address}</td><td>${r.contact}</td></tr>`;
            }
            html += '</table>';
            results.innerHTML = html;
        }

        async function registerResident() {
            const data = {
                first_name: document.getElementById('first_name').value,
                last_name: document.getElementById('last_name').value,
                address: document.getElementById('address').value,
                contact: document.getElementById('contact').value,
            };
            const response = await fetch('/api/residents', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await response.json();
            alert(result.message);
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/api/residents")
def api_search():
    query = request.args.get("q", "")
    results = manager.find_resident(query)
    return jsonify([r.to_dict() for r in results])


@app.route("/api/residents", methods=["POST"])
def api_register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    if not first_name or not last_name:
        return jsonify({"error": "first_name and last_name are required"}), 400

    resident = Resident(
        first_name=first_name,
        last_name=last_name,
        address=data.get("address", ""),
        contact=data.get("contact", ""),
    )
    manager.add_resident(resident)
    return jsonify({"message": "Resident registered!", "id": resident.resident_id}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

## Running the Complete System

```bash
# CLI version (recommended for Termux/phone)
python barangay_system.py

# Web version (for desktop/laptop)
python web_app.py
# Visit http://localhost:5000
```

??? example "Portfolio Tip: Web Application"
    Your Flask web interface for the barangay system is a portfolio centerpiece. Web apps get attention:

    1. **GitHub README** -- Include a live demo screenshot showing the web dashboard. Add a GIF showing the certificate generation flow.
    2. **LinkedIn** -- Post: "Just deployed a web-based barangay management system with Flask. Features include certificate generation, real-time reporting, and role-based access. Built the full stack from database to UI."
    3. **Interview talking point** -- "I built a complete web application with Flask that handles barangay administration. It includes a custom report generator, certificate system, and error handling with custom exceptions. The web interface shows I can build full-stack applications, not just scripts."

## Summary

- Added certificate generation for clearances, indigency, and residency
- Built advanced reporting with monthly summaries and yearly comparisons
- Implemented custom exceptions for proper error handling
- Created an optional Flask web interface
- The system is now a complete, working barangay management tool

## Side Quests

??? note "Optional: Side Quest"
    - Add a "bulk certificate generation" feature for annual clearances
    - Connect to a real SMS API for fee reminders
    - Add a "resident photo" feature using base64 encoding
    - Build a mobile app version using Kivy
    - Add a "document request" system for permits and licenses

## Further Reading

- [Flask documentation](https://flask.palletsprojects.com/)
- [Python exception handling](https://docs.python.org/3/tutorial/errors.html)
- [DILG Barangay Guidelines](https://dilg.gov.ph/)

---

??? example "🧠 Reflection — Capstone B: Barangay Management System (Part 2)"

    - **What did you learn?** Adding certificates, advanced reporting, custom exceptions, and a web interface transforms a CLI tool into a production-ready application.
    - **How can you apply this?** Help your barangay issue clearances and indigency certificates digitally, reducing the paperwork that slows down residents.
    - **What's next?** How could you add role-based access so only authorized officials can view sensitive resident data?

??? checkbox "✅ Chapter Checklist"

    - [ ] Generate text-based certificates (clearance, indigency, residency)
    - [ ] Build monthly and yearly reports with visual bar charts
    - [ ] Implement custom exceptions for proper error handling
    - [ ] Create a Flask web interface for browser-based access
    - [ ] Combine all features into a complete, working barangay system

---

*Next: [Chapter 25: Final Boss](chapter-25-final-boss.md) -- Your ultimate challenge.*
