# ============================================================
#   PYTHON CONCEPTS — 02. COMPREHENSIONS
#   List, Set, Dict, Generator
# ============================================================


# ─────────────────────────────────────────
# FORMAT
# [transform   for item in iterable   if condition]
#  what to do   loop                   filter (optional)
# ─────────────────────────────────────────

words   = ["hello", "world", "python", "intern", "code"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ─────────────────────────────────────────
# LIST COMPREHENSION
# ─────────────────────────────────────────

# Without comprehension (old way)
result = []
for word in words:
    if len(word) > 4:
        result.append(word.upper())
print(result)  # ['HELLO', 'WORLD', 'PYTHON', 'INTERN']

# With comprehension (Pythonic way) — same result, one line
result = [word.upper() for word in words if len(word) > 4]
print(result)  # ['HELLO', 'WORLD', 'PYTHON', 'INTERN']

# Even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]

# Squares of all numbers
squares = [n ** 2 for n in numbers]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# No filter — transform only
doubled = [n * 2 for n in numbers]
print(doubled) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# ─────────────────────────────────────────
# SET COMPREHENSION — unique values, use { }
# ─────────────────────────────────────────

lengths = {len(word) for word in words}
print(lengths)  # {4, 5, 6}  ← no duplicates, unordered


# ─────────────────────────────────────────
# DICT COMPREHENSION — key: value pairs, use { : }
# ─────────────────────────────────────────

word_map = {word: len(word) for word in words}
print(word_map)
# {'hello': 5, 'world': 5, 'python': 6, 'intern': 6, 'code': 4}


# ─────────────────────────────────────────
# GENERATOR EXPRESSION — lazy, no brackets
# Used inside sum(), max(), min(), any(), all()
# ─────────────────────────────────────────

# sum of all word lengths
total = sum(len(word) for word in words)
print(total)  # 26

# sum of even squares
even_sq_sum = sum(n ** 2 for n in numbers if n % 2 == 0)
print(even_sq_sum)  # 220

# Difference: list comprehension vs generator
lc = [n * 2 for n in numbers]   # builds full list in memory immediately
ge = (n * 2 for n in numbers)   # lazy — computes one by one when needed
# For large data, generator is more memory-efficient