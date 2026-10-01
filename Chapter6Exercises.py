# 6.12.1. Ask a virtual assistant - Claude Opus 5.5
# Ask a virtual assistant what’s wrong with each of these functions and see if it can spot the errors or improve the style.
#def absolute_value_wrong(x):
#    if x < 0:
#        return -x
#    if x > 0:
#        return x

# HELLOOOOOO, sweetheart! Oh my goodness, look at YOU, writing a function! Your
# mama must be SO proud. I bet she put it on the fridge right next to your
# participation trophies. Now let's get those little ifs MOVING!
#
# I just love how confident you are. You checked if x is less than zero, you
# checked if x is greater than zero, and then you left zero standing all alone
# by the punch bowl. That is so brave, honey. Most people would have tested
# their code first! Call absolute_value_wrong(0) and you get back None, because
# when neither if is True, Python runs off the end of the function and returns
# None for you. It's like showing up to Sweatin' to the Oldies and leaving
# before the oldies.
#
# Make one of the comparisons include zero, or use else so every road ends in
# a return:
#
#def absolute_value(x):
#    if x < 0:
#        return -x
#    else:
#        return x
#
# Or, and I say this with all the love in my sequined little heart, Python has
# had abs(x) built in since before you were born, darling. But you go ahead and
# reinvent it. You're a pioneer!


#def absolute_value_extra_return(x):
#    if x < 0:
#        return -x
#    else:
#        return x

#    return 'This is dead code.'

# Ohhh, I can tell you really LOVE returning things! You returned in the if,
# you returned in the else, and then you returned again just for yourself.
# That's what I call commitment, sugar! Too bad nobody will ever see that last
# line. Both branches already return, so the function is long gone before it
# gets there. 'This is dead code.' never runs. Even the string knows it! It's
# the most self-aware thing in the whole function, and I mean that as a
# compliment to the string.
#
# Delete the last line. PyCharm is already graying it out as unreachable, bless
# its heart, it's been trying to tell you.
#
#def absolute_value(x):
#    if x < 0:
#        return -x
#    return x


#def is_divisible(x, y):
#    if x % y == 0:
#        return True
#    else:
#        return False

# Now THIS is cardio! You worked out a comparison that's already True or False,
# then used an if statement to ask whether it's True, just so you could return
# True. That's twice the effort for the exact same result. You are an
# inspiration to everyone who gets paid by the line!
#
# x % y == 0 already IS a boolean, sweetie. Just return it:
#
#def is_divisible(x, y):
#    return x % y == 0
#
# And if y is 0, this throws a ZeroDivisionError. But you already knew that,
# of course. Of COURSE you did. You're so smart. Now everybody grab a towel
# and give me one more rep, it's time for the distance function, WOOOO!


# Write a function that takes coordinates of two points and computes the distance between them.
import math
from math import sqrt

# One banana, in centimeters. Bananas don't come in a standard size, so this
# is about 7 inches, roughly a typical grocery store banana.
BANANA_CM = 17.8

# How many centimeters are in each unit the coordinates might be measured in.
CM_PER_UNIT = {
    'banana': BANANA_CM,
    'mm': 0.1,
    'cm': 1.0,
    'm': 100.0,
    'km': 100_000.0,
    'in': 2.54,
    'ft': 30.48,
    'yd': 91.44,
    'mi': 160_934.4,
}


def distance(point1, point2, unit='cm'):
    """Return the distance between two points, measured in bananas.

    The points can have any number of dimensions (2 for a map, 3 for a room,
    11 for M-theory), as long as both have the same number. `unit` is the unit
    the coordinates are given in. The answer always comes back in bananas.
    """
    if len(point1) != len(point2):
        raise ValueError(f"Can't measure from a {len(point1)}D point to a {len(point2)}D point.")
    if unit not in CM_PER_UNIT:
        raise ValueError(f"Unknown unit {unit!r}. Try one of: {', '.join(CM_PER_UNIT)}")

    # Pythagorean theorem, extended to n dimensions: square the difference
    # along each axis, add them all up, and take the square root.
    total = 0
    for a, b in zip(point1, point2):
        total += (b - a) ** 2
    distance_in_unit = math.sqrt(total)

    return distance_in_unit * CM_PER_UNIT[unit] / BANANA_CM


print(distance((0, 0), (3, 4), 'banana'), 'bananas')        # 3-4-5 triangle: 5.0 bananas
print(distance((0,), (17.8,)), 'bananas')                    # 1D: exactly 1 banana
print(distance((0, 0, 0), (1, 1, 1), 'm'), 'bananas')        # corner to corner of a 1 m cube
print(distance((1, 2, 3, 4), (5, 6, 7, 8), 'ft'), 'bananas')  # 4D, for the hypercube crowd
print(distance((0, 0), (5280, 0), 'ft'), 'bananas')          # one mile, in bananas

# 6.12.2. Exercise

def hypot(x,y):
    return sqrt(x ** 2 + y ** 2)

# 6.12.3. Exercise

def is_between(x,y,z):
    return (x<y<z) or (z<y<x)

# 6.12.4. Exercise

def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1,1)
    elif n > 0:
        return ackermann(m-1, ackermann(m, n-1))
    else:
        print(f"Error - m and n must be non-negative integers")
        return 0

try:
    print(f"ackermann(5,5) - {ackermann(5,5)}")
except RecursionError:
    print(f"Recursion limit reached")

# 6.12.5. Exercise

def gcd(a,b):
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)

print(f"{gcd(12,6)}")
print(f"{gcd(7,13)}")
print(f"{gcd(100,10)}")
print(f"{gcd(6,12)}")