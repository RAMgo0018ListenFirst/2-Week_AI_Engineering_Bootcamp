# ============================================================
#   PYTHON CONCEPTS — 03. FUNCTIONS
#   Default args, *args, **kwargs, keyword-only args
# ============================================================


# ─────────────────────────────────────────
# DEFAULT ARGUMENTS
# ─────────────────────────────────────────

def greet(name, message="Hello"):   # message has a default value
    print(f"{message}, {name}!")

greet("Ram")              # Hello, Ram!       ← uses default
greet("Ram", "Welcome")   # Welcome, Ram!     ← overrides default

# Rule: default arguments must come AFTER non-default ones
# def broken(message="Hi", name):  # ❌ SyntaxError
# def correct(name, message="Hi"): # ✅


# ─────────────────────────────────────────
# *args — extra positional arguments → TUPLE
# ─────────────────────────────────────────

def add_expense(amount, category="general", *tags):
    print(f"Amount:   {amount}")
    print(f"Category: {category}")
    print(f"Tags:     {tags}")      # tags is a TUPLE
    print(f"Type:     {type(tags)}")

add_expense(100, "food", "lunch", "monday", "urgent")
# Amount:   100
# Category: food
# Tags:     ('lunch', 'monday', 'urgent')
# Type:     <class 'tuple'>

print()

# Without extra tags
add_expense(200, "travel")
# Tags: ()   ← empty tuple, not an error


# ─────────────────────────────────────────
# **kwargs — extra keyword arguments → DICT
# ─────────────────────────────────────────

def log_expense(amount, **metadata):
    print(f"Amount:   {amount}")
    print(f"Metadata: {metadata}")   # metadata is a DICT
    print(f"Type:     {type(metadata)}")

log_expense(100, source="UPI", mode="online", verified=True)
# Amount:   100
# Metadata: {'source': 'UPI', 'mode': 'online', 'verified': True}
# Type:     <class 'dict'>

print()

# Accessing specific keys from kwargs
def show_meta(**metadata):
    if "source" in metadata:
        print(f"Paid via: {metadata['source']}")

show_meta(source="UPI", note="dinner")
# Paid via: UPI


# ─────────────────────────────────────────
# KEYWORD-ONLY ARGUMENTS (modern Python)
# * alone as separator — forces caller to use keywords
# ─────────────────────────────────────────

def add(amount, *, category="general", note=""):
    print(f"{amount} | {category} | {note}")

add(100, category="food", note="lunch")   # ✅ explicit, readable
# add(100, "food", "lunch")              # ❌ TypeError — must use keywords

print()


# ─────────────────────────────────────────
# ALL TOGETHER — full signature example
# ─────────────────────────────────────────

def record(amount, category="general", *tags, **metadata):
    print(f"Amount:   {amount}")
    print(f"Category: {category}")
    print(f"Tags:     {tags}")        # tuple
    print(f"Metadata: {metadata}")    # dict

record(500, "travel", "flight", "goa", source="card", trip="vacation")
# Amount:   500
# Category: travel
# Tags:     ('flight', 'goa')
# Metadata: {'source': 'card', 'trip': 'vacation'}