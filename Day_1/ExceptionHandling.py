# ============================================================
#   PYTHON CONCEPTS — 04. EXCEPTION HANDLING
#   try, except, finally, raise
# ============================================================


# ─────────────────────────────────────────
# BASIC try / except
# ─────────────────────────────────────────

def parse_amount(value):
    try:
        return float(value)        # attempt this
    except ValueError:
        print("Invalid amount")    # runs ONLY if float() fails

print(parse_amount("99.5"))  # 99.5
print(parse_amount("abc"))   # Invalid amount → None


# ─────────────────────────────────────────
# try / except / finally
# finally ALWAYS runs — success or failure
# ─────────────────────────────────────────

def parse_with_finally(value):
    try:
        result = float(value)
        return result
    except ValueError:
        print("Invalid amount")
    finally:
        print("Done")              # runs no matter what

# parse_with_finally("abc")  → prints "Invalid amount", then "Done", returns None
# parse_with_finally("99.5") → prints "Done", returns 99.5

parse_with_finally("abc")
print("---")
parse_with_finally("99.5")


# ─────────────────────────────────────────
# finally is used for CLEANUP
# Things that must happen regardless of success/failure
# ─────────────────────────────────────────

def read_file_manual(path):
    f = open(path)
    try:
        return f.read()
    except OSError:
        print("File error")
    finally:
        f.close()    # always closes, even if error occurred

# Modern Python — use 'with' which handles cleanup automatically
def read_file_modern(path):
    try:
        with open(path, "r") as f:
            return f.read()          # file auto-closes after with block
    except FileNotFoundError:
        return ""


# ─────────────────────────────────────────
# MULTIPLE except blocks
# ─────────────────────────────────────────

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Both values must be numbers")
    finally:
        print("Division attempted")

safe_divide(10, 2)    # 5.0
safe_divide(10, 0)    # Cannot divide by zero
safe_divide(10, "a")  # Both values must be numbers


# ─────────────────────────────────────────
# raise — throw your own exceptions
# ─────────────────────────────────────────

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return amount

try:
    validate_amount(-50)
except ValueError as e:
    print(f"Error: {e}")   # Error: Amount must be positive


# ─────────────────────────────────────────
# COMMON EXCEPTION TYPES
# ─────────────────────────────────────────

# ValueError      → wrong value type  (float("abc"))
# TypeError       → wrong type        (10 + "a")
# FileNotFoundError → file missing    (open("x.txt"))
# ZeroDivisionError → divide by zero  (10 / 0)
# KeyError        → dict key missing  (d["missing"])
# IndexError      → list index OOB    ([1,2,3][99])
# AttributeError  → no such method    ((1,2).append(3))