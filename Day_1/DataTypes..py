# ============================================================
#   PYTHON CONCEPTS — 01. DATA TYPES
#   Tuple vs List
# ============================================================


# ─────────────────────────────────────────
# TUPLE — immutable, fixed-meaning, positional
# ─────────────────────────────────────────

point = (28.6, 77.2)           # lat, lon — order matters, never changes
person = ("Ram", 22, "India")  # structured record

# Accessing tuple elements
print(point[0])   # 28.6
print(person[1])  # 22

# Tuples CANNOT be changed
a = (1, 2, 3)
# a.append(4)   # ❌ AttributeError: 'tuple' object has no attribute 'append'
# a[0] = 99     # ❌ TypeError: 'tuple' object does not support item assignment


# ─────────────────────────────────────────
# LIST — mutable, grows/shrinks freely
# ─────────────────────────────────────────

scores = [95, 88, 72]
scores.append(100)     # ✅ [95, 88, 72, 100]
scores[0] = 99         # ✅ [99, 88, 72, 100]
scores.remove(88)      # ✅ [99, 72, 100]
scores.pop()           # ✅ removes last → [99, 72]

print(scores)


# ─────────────────────────────────────────
# CONVERSION between them
# ─────────────────────────────────────────

a = (1, 2, 3)
b = list(a)    # tuple → list
b.append(4)    # now b = [1, 2, 3, 4]
c = tuple(b)   # list → tuple: (1, 2, 3, 4)

print(type(a))  # <class 'tuple'>
print(type(b))  # <class 'list'>
print(type(c))  # <class 'tuple'>


# ─────────────────────────────────────────
# KEY RULE
# ─────────────────────────────────────────

# Use TUPLE → fixed, structured, positional data
coordinates = (19.07, 72.87)   # Mumbai lat/lon — never changes

# Use LIST → collection of similar items that grows or changes
expenses = [200, 150, 500]     # grows as you add more