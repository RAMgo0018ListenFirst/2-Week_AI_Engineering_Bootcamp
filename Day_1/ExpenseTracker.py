# ============================================================
#   EXPENSE TRACKER — tracker.py
#   Core logic: load, save, add, view, filter, total
#   Ram's mistakes annotated with # ❌ YOUR MISTAKE
# ============================================================

import json
from datetime import date


def load_expenses(filepath="expenses.json"):
    """Load expenses from JSON file. Returns [] if file doesn't exist."""

    # ❌ YOUR MISTAKE: open("expenses.json","r") — hardcoded filename
    #    Fix: Use 'filepath' parameter so it's reusable and testable

    # ❌ YOUR MISTAKE: print("Error in loading") in except block
    #    Fix: FileNotFoundError on first run is NORMAL — return [] silently

    # ❌ YOUR MISTAKE: Returned True/False instead of actual data
    #    Fix: Return the loaded list on success, [] on failure

    try:
        with open(filepath, "r") as file:
            return json.load(file)   # ✅ return actual data, not True
    except FileNotFoundError:
        return []                    # ✅ empty list, not False or None


def save_expenses(expenses, filepath="expenses.json"):
    """Save expenses list to JSON file."""

    # ❌ YOUR MISTAKE: json.dump(data, expenses, intent=4)
    #    Error 1: First arg was 'data' — undefined variable, should be 'expenses'
    #    Error 2: Second arg was 'expenses' — should be 'file' (the file object)
    #    Error 3: 'intent' is a typo — correct spelling is 'indent'

    with open(filepath, "w") as file:
        json.dump(expenses, file, indent=4)   # ✅ (data, file_object, indent)


def add_expense(expenses, amount, category, note=""):
    """Create a new expense dict and append it to the list."""

    # ❌ YOUR MISTAKE: Hardcoded values like 200, "food", "lunch", "2026-05-20"
    #    Fix: Use parameter names — function must work for ANY expense

    # ❌ YOUR MISTAKE: Hardcoded date "2026-05-20"
    #    Fix: date.today().isoformat() gets today's date dynamically

    expense = {
        "amount": amount,                  # ✅ parameter, not hardcoded 200
        "category": category,              # ✅ parameter, not hardcoded "food"
        "note": note,                      # ✅ parameter, not hardcoded string
        "date": date.today().isoformat()   # ✅ dynamic, not hardcoded string
    }
    expenses.append(expense)
    return expenses


def view_expenses(expenses):
    """Print all expenses in a readable format."""

    # ❌ YOUR MISTAKE: for i in expenses  (missing colon)
    #    Fix: for i in expenses:

    # ❌ YOUR MISTAKE: print(i) prints raw dict
    #    Fix: Use f-string to format nicely

    if not expenses:          # if not expenses: is more Pythonic than len() == 0
        print("No expenses found.")
        return                # guard clause — exit early, keep code clean

    for i in expenses:        # ✅ colon at end
        print(f"[{i['date']}] {i['category']} — Rs.{i['amount']} | {i['note']}")
        # ✅ f-string with key access, not raw print(i)


def filter_by_category(expenses, category):
    """Return only expenses matching the given category (case-insensitive)."""

    # ❌ YOUR MISTAKE: expenses.lower() — can't lowercase a list
    #    Fix: i["category"].lower() — lowercase the value inside each dict

    # ❌ YOUR MISTAKE: Used 'where' instead of 'if'
    #    Fix: Python comprehensions use 'if', not 'where'

    # ❌ YOUR MISTAKE: category=category — single = is assignment, not comparison
    #    Fix: Use == for comparison

    # ❌ YOUR MISTAKE: Used 'category' as loop variable (same as parameter name)
    #    Fix: Use 'i' as loop variable

    return [
        i for i in expenses
        if i["category"].lower() == category.lower()   # ✅ .lower() on both sides
    ]


def total_spent(expenses):
    """Return total amount spent across all expenses."""

    # ❌ YOUR MISTAKE: Used 'sum' as a variable name
    #    'sum' is a Python built-in function — naming your variable 'sum'
    #    overwrites it for the rest of your code!
    #    Fix: Use 'total' as the variable name

    # Your loop approach (correct logic, wrong variable name):
    # total = 0
    # for i in expenses:
    #     total += i["amount"]
    # return total

    # Pythonic one-liner:
    return sum(i["amount"] for i in expenses)
    # i["amount"] for i in expenses → generator that yields each amount
    # sum() adds them all up