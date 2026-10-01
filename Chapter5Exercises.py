# 5.14.1. Ask a virtual assistant - Claude Opus 5.5

# What are some uses of the modulus operator?

# BREAKER BREAKER ONE-NINE, this here's Big Daddy Possum northbound on the
# I-59 and I got my ears on, come back. Modulus. The % sign. 10-4 good buddy,
# lemme tell ya, the modulus is the REMAINDER, it's what's left over after you
# divide, like what's left in the thermos after seven days, which is nothin',
# which is why I'm seein' a deer in a cowboy hat wavin' at me from mile
# marker 112. He knows about modulus too. He's been tellin' me.
#
#   - Even or odd: n % 2 == 0 means it's even. n % 2 == 1 means odd. Like
#     my axles. I got eighteen wheels. 18 % 2 is 0. EVEN. Perfect. Balanced.
#     Shiny side up, greasy side down.
#   - Divisible by somethin': n % 3 == 0 means n divides by 3 clean, no
#     leftovers, like a chicken coop with no bears in it. Green light.
#   - Wrap-around / clock math: (hour + 5) % 24 tells ya what time it'll be
#     in five hours. I ain't needed a clock since Tuesday. Or was it the
#     Tuesday before. The clock in my cab is meltin' anyhow.
#   - Grab the last digit: n % 10 gives ya the last digit of a number, like
#     readin' just the end of a mile marker 'cause the front part keeps
#     crawlin' away from ya.
#   - Do somethin' every Nth time: if i % 100 == 0: check your mirrors. Or
#     check for the shadow man ridin' your back door. He's still there.
#   - Cycle through a list: colors[i % len(colors)] goes round and round
#     forever like me on this beltway. I been past this Waffle House four
#     times, good buddy. Same waitress. She ain't blinked once.
#   - Unit conversion: minutes % 60 gives ya the leftover minutes after you
#     pull out the hours. Real handy for fudgin' the ol' comic book (that's
#     my logbook, I ain't sayin' I fudge it, Smokey, if you're listenin').
#
# We gone. Mercy sakes.

# What is the logical xor operation and how do I compute it in Python?

# Come back? Copy that. XOR. "Exclusive or." Sounds like a Bible word.
# XOR means it's True when EXACTLY ONE side is True. Not both. Not neither.
# ONE. Like either there's a bear in the air or there's a bear at the
# chicken coop but if there's a bear in BOTH places, that ain't XOR,
# good buddy, that's a conspiracy, and I been sayin' so to that raccoon
# sittin' in my passenger seat for two hundred miles.
#
#   a      b      a XOR b
#   True   True   False     <- both? nope
#   True   False  True      <- just one, hammer down
#   False  True   True      <- just one, hammer down
#   False  False  False     <- neither, dead air on the channel
#
# Python ain't got a word for it like `and` and `or`, but you got options:
#
#   a != b                  # for real True/False values. If they're
#                           # different, exactly one is True. Clean as a
#                           # fresh-washed Peterbilt.
#   bool(a) != bool(b)      # if a and b might be numbers or strings or
#                           # whatever, turn 'em into bools first.
#   a ^ b                   # the caret. Works on bools, but on ints it's
#                           # BITWISE xor, flips the bits, different deal,
#                           # 5 ^ 3 is 6, don't let it sneak up on ya like
#                           # a plain-wrapper with no lights.
#   (a and not b) or (not a and b)   # the long way round, like takin' the
#                                    # scenic route through a county with
#                                    # no scales. Same answer.
#
# That raccoon says I got it right. He's a good raccoon. 10-4.

# Convert this statement to a chained conditional.
#if x == y:
#    print('x and y are equal')
#else:
#    if x < y:
#        print('x is less than y')
#    else:
#        print('x is greater than y')

# 10-4, you got a convoy of ifs stacked up inside each other like a
# parking lot (that's a car hauler, four-wheelers) and we're gonna line
# 'em up single file with elif. elif is just "else if" that been drivin'
# so long it lost some letters. I know the feelin'. I lost some letters too.
# I lost the whole letter Q around Shreveport.
#
#if x == y:
#    print('x and y are equal')
#elif x < y:
#    print('x is less than y')
#else:
#    print('x is greater than y')
#
# One level of indentin'. Flat as the road through the Delta. The road
# that keeps breathin'. Y'all see the road breathin'? Just me? Copy.

# Rewrite this statement with a single conditional.
#if 0 < x:
#    if x < 10:
#        print('x is a positive single-digit number.')

# Breaker. Two ifs nested like that is the same as one if with `and`, on
# account of the inside one only gets checked if the outside one already
# passed. Same as how I only check for alligators (tire tread on the road)
# if I've already seen the snakes. Which I have. Several. Purple.
#
#if 0 < x and x < 10:
#    print('x is a positive single-digit number.')
#
# But hold your horses, good buddy, Python lets you CHAIN them comparisons
# like a string of chicken lights on a Kenworth:
#
#if 0 < x < 10:
#    print('x is a positive single-digit number.')
#
# Prettiest thing I seen all week, and I seen a possum in a tuxedo
# conductin' an orchestra at the Love's in Meridian.

# See if a VA can simplify this unnecessary complexity.
#if not x <= 0 and not x >= 10:
#    print('x is a positive single-digit number.')

# Lord have mercy, this one's got more "nots" than a CB channel at 3 AM.
# "not x <= 0" is just x > 0. "not x >= 10" is just x < 10. Untangle the
# nots and you're right back where we just was, the same stretch of
# highway, I KNEW I'd been here before, I told that deer:
#
#if 0 < x < 10:
#    print('x is a positive single-digit number.')
#
# Them double-negatives was like a four-wheeler brake checkin' ya for no
# reason. Gone now. Smooth sailin'. Mostly. The guardrail's whisperin'.

# Here’s an attempt at a recursive function that counts down by two.
# It seems to work. But it has an error. Ask a virtual assistant
# what’s wrong and how to fix it. Paste the solution it provides
# back here and test it.

#def countdown_by_two(n):
#    if n == 0:
#        print('Blastoff!')
#    else:
#        print(n)
#        countdown_by_two(n-2)

# WHOA WHOA WHOA, emergency traffic, emergency traffic on the one-nine.
# This function only works if you start with an EVEN number. Feed it 6 and
# it goes 6, 4, 2, 0, Blastoff, real nice. But feed it an ODD number like 7
# and it goes 7, 5, 3, 1, -1, -3, -5... it drives RIGHT PAST ZERO, never
# hits n == 0 exactly, and keeps on truckin' into negative numbers forever.
# Never stops. Never sleeps. Like me. Python finally pulls it over with a
# RecursionError, which is the bear of the Python world, and I respect
# that bear. Base case gotta be a ramp you can't miss.
#
# The fix: check n <= 0 instead of n == 0, so whether you land on 0 or blow
# past it to -1, you still take the exit. Pull into the truck stop. Rest.
# (I won't. But the function can.)

#def countdown_by_two(n):
#    if n <= 0:
#        print('Blastoff!')
#    else:
#        print(n)
#        countdown_by_two(n-2)


# Testin' it. Even number and odd number, both oughta make it home.
#countdown_by_two(6)
#countdown_by_two(7)

# Both of 'em hit Blastoff. That's a big 10-4. This is Big Daddy Possum,
# keepin' the shiny side up and the greasy side down, and the raccoon says
# bye too. We gone.

# 5.14.2. Exercise
from time import time

seconds_since_unix_epoch = time()
minutes_since_unix_epoch = seconds_since_unix_epoch // 60
remainder_seconds = minutes_since_unix_epoch % seconds_since_unix_epoch
hours_since_unix_epoch = minutes_since_unix_epoch // 60
remainder_minutes = hours_since_unix_epoch % minutes_since_unix_epoch
days_since_unix_epoch = hours_since_unix_epoch // 24
remainder_hours = days_since_unix_epoch % hours_since_unix_epoch
print(f"It has been {int(days_since_unix_epoch)} days since the unix epoch")
print(f"The current time is {int((hours_since_unix_epoch - 7) % 24)}:{int(minutes_since_unix_epoch % hours_since_unix_epoch)}:{int(seconds_since_unix_epoch % minutes_since_unix_epoch)}")

# 5.14.3. Exercise

def is_triangle(x,y,z, checks=3):
    if checks == 0:
        return True
    if x + y < z:
        return False
    return is_triangle(y,z,x, checks - 1)

# 5.14.4. Exercise

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

# -> recurse(3, 0)
# -> recurse(2, 3)
# -> recurse(1, 5)
# -> recurse(0, 6) -> print(6)

# 5.14.5. Exercise
# Guess - I think it draws a Koch snowflake
import turtle
from turtle import forward, left, right, back

def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)

# draw(100)

# I was wrong! But I was right that it was a fractal, just wrong about which one

# 5.14.6. Exercise

# Seriously? It's the next exercise?

def koch(x):
    if x < 5:
        forward(x)
        return
    koch(x/3)
    left(60)
    koch(x/3)
    right(120)
    koch(x/3)
    left(60)
    koch(x/3)

# koch(120)

# 5.14.7 Exercise - Asked Claude Opus 5.5 to write a function to make a Sierpinski triangle
# Took it 6m 25s and used around 88k tokens

def sierpinski(length, depth):
    """Draw a Sierpinski triangle with side `length` and recursion `depth`.

    RFC 51407                                         SierTRP Working Group
    Category: Standards Track (Enterprise Edition)           September 2026
    Obsoletes: the 12-line recursive version everyone else turned in

          The Sierpinski Triangle Rendering Protocol -- SierTRP/1.0

    Abstract

       This document specifies a robust, scalable, fault-tolerant, cloud-
       ready* framework for asking a turtle to draw some triangles.

       * It is not cloud-ready.

    1. Conventions

       The key words "MUST", "MUST NOT", "SHOULD" and "MAY" in this
       document are to be interpreted as described in RFC 2119. The key
       word "SHOULDN'T" is to be interpreted as describing this function.

    2. Architecture

       The rendering pipeline has five stages. It has five stages because
       it was designed by a committee of five people (Conway, 1968).

        +--------+   +-----------+   +-----------+   +-----------+   +--------+
        | Config |-->| Compiler  |-->| Consensus |-->| Optimizer |-->| Turtle |
        | (§4)   |   | (λ, CPS,  |   | (PBFT,    |   | (peephole,|   | (ACID, |
        |        |   |  Z, §7)   |   |  n=5, §9) |   |  §8)      |   |  §10)  |
        +--------+   +-----------+   +-----------+   +-----------+   +--------+

       2.1. The Compiler MUST NOT recurse by name. Recursion is obtained
            from the Z combinator over a Church-encoded depth, written in
            continuation-passing style, bounced on a trampoline.
       2.2. The Compiler MUST NOT touch the turtle. It emits bytecode.
            Side effects are confined to the Imperative Shell (§10).
       2.3. Before any ink is spent, five independent Oracles MUST reach
            Byzantine fault-tolerant consensus on what a Sierpinski
            triangle even is. One of them is lying on purpose.
       2.4. The Optimizer MUST preserve ink. (See §8, "The Incident".)

    3. Complexity

       Time: O(3^n). Space: O(3^n). Concatenation: O(9^n), because the
       program is an immutable tuple and immutability matters more than
       finishing. Cognitive: O(n!).

    4. Security Considerations

       None. It's a turtle.
    """

    # ════════════════════════════════════════════════════════════════════
    # §0. Just-In-Time Dependency Resolution
    # ════════════════════════════════════════════════════════════════════
    # Imports are deferred into the function body so that importing this
    # module stays cheap. This saves about four milliseconds, which we will
    # immediately spend on lambda calculus.
    import abc
    import collections
    import contextlib
    import dataclasses
    import functools
    import hashlib
    import math
    import random
    import time as chronometry
    import turtle as turtle_runtime
    from typing import Callable, ClassVar, Protocol

    # ════════════════════════════════════════════════════════════════════
    # §1. Exception Hierarchy
    # ════════════════════════════════════════════════════════════════════
    class SierpinskiEnterpriseException(Exception):
        """Root of the hierarchy. Never raised directly; that would be too direct."""

    class SierpinskiConfigurationException(SierpinskiEnterpriseException):
        """The caller requested a triangle that cannot exist in this universe."""

    class ByzantineGeneralsException(SierpinskiEnterpriseException):
        """Fewer than 2f + 1 oracles agree on what a Sierpinski triangle is."""

    class InvariantViolationError(SierpinskiEnterpriseException):
        """Raised instead of AssertionError, because `assert` is stripped under
        `python -O`, and this codebase takes optimization very seriously (§8)."""

    # ════════════════════════════════════════════════════════════════════
    # §2. Metaprogramming
    # ════════════════════════════════════════════════════════════════════
    class SingletonMeta(abc.ABCMeta):
        """Metaclass for classes that are both abstract-friendly and singular.

        It extends ABCMeta, not type, so a singleton can also inherit from an
        ABC without a metaclass conflict. Resolving a metaclass conflict is
        the most enterprise thing Python lets you do, so we did it on purpose.

        Note: this metaclass is re-created on every call to sierpinski(), so
        each call gets its own singletons. There is exactly one instance per
        universe and a new universe per call: the Many-Worlds Interpretation
        of the Singleton pattern.
        """
        _instances = {}

        def __call__(cls, *args, **kwargs):
            if cls not in SingletonMeta._instances:
                SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)
            return SingletonMeta._instances[cls]

    # ════════════════════════════════════════════════════════════════════
    # §3. Event-Driven Observability
    # ════════════════════════════════════════════════════════════════════
    @dataclasses.dataclass(frozen=True, slots=True)
    class DomainEvent:
        name: str
        payload: dict
        timestamp: float = dataclasses.field(default_factory=chronometry.perf_counter)

    class EventBus(metaclass=SingletonMeta):
        """Publish/subscribe (Observer, GoF 1994). One publisher, one
        subscriber, zero reasons for the indirection."""

        def __init__(self):
            self._subscribers = collections.defaultdict(list)

        def subscribe(self, event_name, handler):
            self._subscribers[event_name].append(handler)

        def publish(self, event_name, **payload):
            event = DomainEvent(event_name, payload)
            for handler in self._subscribers[event_name] + self._subscribers["*"]:
                handler(event)

    class AuditLogObserver:
        """Structured logging, for compliance with regulations we made up."""

        def __init__(self):
            self._epoch = chronometry.perf_counter()

        def __call__(self, event):
            elapsed_ms = (event.timestamp - self._epoch) * 1000
            details = " ".join(f"{key}={value}" for key, value in event.payload.items())
            print(f"[SierTRP +{elapsed_ms:9.3f}ms] {event.name:<22} {details}")

    # ════════════════════════════════════════════════════════════════════
    # §4. Configuration
    # ════════════════════════════════════════════════════════════════════
    @dataclasses.dataclass(frozen=True, slots=True)
    class SierpinskiConfiguration:
        """Immutable, self-validating value object (Evans, 2003)."""
        side_length: float
        recursion_depth: int
        MAX_DEPTH: ClassVar[int] = 7  # 3^8 = 6561 triangles exceeds the turtle's union contract

        def __post_init__(self):
            if isinstance(self.recursion_depth, bool) or not isinstance(self.recursion_depth, int):
                raise SierpinskiConfigurationException(
                    f"recursion_depth must be an int, got {self.recursion_depth!r}. "
                    "(Yes, bool is a subclass of int. No, True is not a depth.)")
            if not 0 <= self.recursion_depth <= self.MAX_DEPTH:
                raise SierpinskiConfigurationException(
                    f"recursion_depth must be in [0, {self.MAX_DEPTH}], got {self.recursion_depth}.")
            if (isinstance(self.side_length, bool)
                    or not isinstance(self.side_length, (int, float))
                    or not math.isfinite(self.side_length)
                    or self.side_length <= 0):
                raise SierpinskiConfigurationException(
                    f"side_length must be a positive finite real, got {self.side_length!r}.")

    # ════════════════════════════════════════════════════════════════════
    # §5. The Untyped Lambda Calculus (Church, 1936)
    # ════════════════════════════════════════════════════════════════════
    # PEP 8 forbids binding lambdas to names (E731). Alonzo Church predates
    # PEP 8 by 65 years and is grandfathered in.
    TRUE = lambda a: lambda b: a                                        # noqa: E731
    FALSE = lambda a: lambda b: b                                       # noqa: E731
    ZERO = lambda f: lambda x: x                                        # noqa: E731
    SUCC = lambda n: lambda f: lambda x: f(n(f)(x))                     # noqa: E731
    IS_ZERO = lambda n: n(lambda _: FALSE)(TRUE)                        # noqa: E731
    # Kleene's predecessor function. Kleene reportedly worked it out in the
    # dentist's chair, which is the correct emotional state in which to
    # read it.
    PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(lambda u: u)  # noqa: E731
    # The Z combinator: the Y combinator eta-expanded so it terminates under
    # strict evaluation. It lets a function recurse without ever saying its
    # own name, like a function in witness protection.
    Z = lambda f: (lambda x: f(lambda *a: x(x)(*a)))(lambda x: f(lambda *a: x(x)(*a)))  # noqa: E731

    def to_church(k):
        return functools.reduce(lambda numeral, _: SUCC(numeral), range(k), ZERO)

    def from_church(numeral):
        return numeral(lambda i: i + 1)(0)

    # ════════════════════════════════════════════════════════════════════
    # §6. Intermediate Representation: SierTRP Bytecode
    # ════════════════════════════════════════════════════════════════════
    class Instruction(abc.ABC):
        """Base instruction. Supports the Visitor pattern through reflective
        double dispatch, because Python has single dispatch and a can-do
        attitude."""
        __slots__ = ()

        def accept(self, visitor):
            return getattr(visitor, f"visit_{type(self).__name__.lower()}")(self)

        def is_noop(self):
            return False

    @dataclasses.dataclass(frozen=True, slots=True)
    class Forward(Instruction):
        distance: float  # negative distances mean "back", per the turtle ISA

        def is_noop(self):
            return math.isclose(self.distance, 0.0, abs_tol=1e-9)

    @dataclasses.dataclass(frozen=True, slots=True)
    class Turn(Instruction):
        degrees: float  # counterclockwise, as God and Seymour Papert intended

        def is_noop(self):
            return math.isclose(math.remainder(self.degrees, 360.0), 0.0, abs_tol=1e-9)

    @dataclasses.dataclass(frozen=True, slots=True)
    class PenUp(Instruction):
        pass

    @dataclasses.dataclass(frozen=True, slots=True)
    class PenDown(Instruction):
        pass

    @dataclasses.dataclass(frozen=True, slots=True)
    class Teleport(Instruction):
        x: float
        y: float

    @dataclasses.dataclass(frozen=True, slots=True)
    class SetHeading(Instruction):
        degrees: float

    # ════════════════════════════════════════════════════════════════════
    # §7. The Compiler (Functional Core)
    # ════════════════════════════════════════════════════════════════════
    @dataclasses.dataclass(frozen=True, slots=True)
    class Bounce:
        """A suspended computation for the trampoline.

        Guido van Rossum declined to add tail-call elimination to Python in
        2009. Out of respect for that decision we have implemented it
        ourselves, in the slowest way available.
        """
        thunk: Callable[[], object]

    def trampoline(result):
        while isinstance(result, Bounce):
            result = result.thunk()
        return result

    def compiler_functional(recurse):
        """Fed to Z to obtain the compiler. `recurse` is the compiler itself,
        which it receives without ever having been told its own name."""

        def compile_triangle(n, side, program, k):
            half = side / 2
            traverse_right = (Forward(half),)
            climb_to_apex = (Forward(-half), Turn(60), Forward(half), Turn(-60))
            descend_home = (Turn(60), Forward(-half), Turn(-60))

            def leaf():
                return Bounce(lambda: k(program + (Forward(side), Turn(120)) * 3))

            def branch():
                m = PRED(n)
                # Callback pyramid, faithfully imported from Node.js circa 2014.
                return Bounce(lambda: recurse(m, half, program, lambda p1:
                    Bounce(lambda: recurse(m, half, p1 + traverse_right, lambda p2:
                        Bounce(lambda: recurse(m, half, p2 + climb_to_apex, lambda p3:
                            Bounce(lambda: k(p3 + descend_home))))))))

            return IS_ZERO(n)(leaf)(branch)()

        return compile_triangle

    compile_triangle = Z(compiler_functional)

    # ════════════════════════════════════════════════════════════════════
    # §8. The Optimizer
    # ════════════════════════════════════════════════════════════════════
    class PeepholeOptimizer:
        """Peephole optimizer (McKeeman, 1965), run to a fixpoint.

        Knuth warned that premature optimization is the root of all evil.
        This optimization runs after the code is finished, so it is merely
        unnecessary, which is permitted.

        The Incident: an earlier build merged forward(a) with back(a) into a
        no-op. That is valid in the turtle's motion algebra, but it deletes
        ink, because the pen is down and side effects are real. Forward
        moves are now only fused when they point the same way. The postmortem
        was blameless; the turtle was blamed.
        """
        MAX_PASSES: ClassVar[int] = 64

        def run_pass(self, program):
            emitted = []
            for instruction in program:
                match (emitted[-1] if emitted else None, instruction):
                    case (Turn(degrees=a), Turn(degrees=b)):
                        emitted[-1] = Turn(math.remainder(a + b, 360.0))
                    case (Forward(distance=a), Forward(distance=b)) if a * b > 0:
                        emitted[-1] = Forward(a + b)
                    case _:
                        emitted.append(instruction)
            return tuple(i for i in emitted if not i.is_noop())

        def optimize(self, program):
            for passes in range(1, self.MAX_PASSES + 1):
                optimized = self.run_pass(program)
                if optimized == program:
                    return optimized, passes
                program = optimized
            raise InvariantViolationError("Optimizer failed to reach a fixpoint. Halting problem suspected.")

    # ════════════════════════════════════════════════════════════════════
    # §9. Byzantine Fault-Tolerant Verification
    # ════════════════════════════════════════════════════════════════════
    class SierpinskiOracle(abc.ABC):
        """An independent witness to the shape of the Sierpinski triangle.
        Testimony is the first `rows` rows of Pascal's triangle mod 2."""

        @abc.abstractmethod
        def testify(self, rows):
            ...

    class PascalParityOracle(SierpinskiOracle):
        """Computes real binomial coefficients, some of them 37 digits long,
        then keeps only the last bit of each."""

        def testify(self, rows):
            return tuple(tuple(math.comb(r, c) % 2 for c in range(r + 1)) for r in range(rows))

    class LucasTheoremOracle(SierpinskiOracle):
        """Lucas (1878): C(r, c) is odd iff every bit set in c is set in r.
        Édouard Lucas also invented the Tower of Hanoi, whose state graph is
        a Sierpinski triangle. Nothing in this function is a coincidence."""

        def testify(self, rows):
            return tuple(tuple(int(r & c == c) for c in range(r + 1)) for r in range(rows))

    class Rule90Oracle(SierpinskiOracle):
        """Wolfram's elementary cellular automaton Rule 90: each cell becomes
        the XOR of its two neighbours. (See Big Daddy Possum on XOR, line 34.)"""

        def testify(self, rows):
            width = 2 * rows + 1
            cells = [0] * width
            cells[rows] = 1
            history = []
            for r in range(rows):
                history.append(tuple(cells[rows - r + 2 * c] for c in range(r + 1)))
                cells = [cells[i - 1] ^ cells[i + 1] if 0 < i < width - 1 else 0 for i in range(width)]
            return tuple(history)

    class SelfSimilarityOracle(SierpinskiOracle):
        """Builds each generation from three copies of the previous one,
        exactly the way the compiler does, but on a grid, as a cross-check."""

        def testify(self, rows):
            generation = ((1,),)
            while len(generation) < rows:
                size = len(generation)
                generation += tuple(row + (0,) * (size - i - 1) + row for i, row in enumerate(generation))
            return generation[:rows]

    class ChaosMonkeyOracle(SierpinskiOracle):
        """Lies on purpose (Netflix, 2011), to prove the consensus engine
        tolerates a Byzantine fault. In most production systems this role is
        filled by a flaky integration test."""

        def testify(self, rows):
            testimony = [list(row) for row in LucasTheoremOracle().testify(rows)]
            r = random.randrange(rows)
            testimony[r][random.randrange(r + 1)] ^= 1
            return tuple(map(tuple, testimony))

    @dataclasses.dataclass(frozen=True, slots=True)
    class ConsensusCertificate:
        digest: str
        votes: int
        electorate: int
        dissenters: tuple
        ruling: tuple

    class ConsensusEngine:
        """PBFT-inspired consensus (Castro & Liskov, 1999). Tolerates f
        Byzantine oracles provided n >= 3f + 1, and accepts a ruling backed
        by a quorum of 2f + 1. With n = 5 we tolerate f = 1 liar, plus
        two-thirds of a second liar, rounded down.

        Thank you, Barbara Liskov, for this and for the L in SOLID.
        """

        def __init__(self, oracles):
            self.oracles = tuple(oracles)
            self.f = (len(self.oracles) - 1) // 3
            self.quorum = 2 * self.f + 1

        def adjudicate(self, rows):
            testimony = {type(o).__name__: o.testify(rows) for o in self.oracles}
            ballots = {name: hashlib.sha256(repr(t).encode()).hexdigest() for name, t in testimony.items()}
            digest, votes = collections.Counter(ballots.values()).most_common(1)[0]
            if votes < self.quorum:
                raise ByzantineGeneralsException(
                    f"Only {votes}/{len(self.oracles)} oracles agree; quorum is {self.quorum}.")
            return ConsensusCertificate(
                digest=digest,
                votes=votes,
                electorate=len(self.oracles),
                dissenters=tuple(name for name, ballot in ballots.items() if ballot != digest),
                ruling=next(t for name, t in testimony.items() if ballots[name] == digest),
            )

    # ════════════════════════════════════════════════════════════════════
    # §10. The Imperative Shell
    # ════════════════════════════════════════════════════════════════════
    # "Functional core, imperative shell" (Bernhardt). Everything above
    # this line is pure. Everything below it touches a turtle.
    class RenderingSurface(Protocol):
        """Structural type for anything that quacks like a turtle."""
        def forward(self, distance): ...
        def left(self, angle): ...
        def penup(self): ...
        def pendown(self): ...
        def goto(self, x, y=None): ...
        def setheading(self, angle): ...

    class TurtleInstructionInterpreter:
        """Executes SierTRP bytecode on a turtle via the Visitor pattern."""

        def __init__(self, pen):
            self.pen = pen
            self.executed = 0

        def execute(self, program):
            for instruction in program:
                instruction.accept(self)
                self.executed += 1

        def visit_forward(self, instruction):
            self.pen.forward(instruction.distance)

        def visit_turn(self, instruction):
            self.pen.left(instruction.degrees)

        def visit_penup(self, _):
            self.pen.penup()

        def visit_pendown(self, _):
            self.pen.pendown()

        def visit_teleport(self, instruction):
            self.pen.goto(instruction.x, instruction.y)

        def visit_setheading(self, instruction):
            self.pen.setheading(instruction.degrees)

    @contextlib.contextmanager
    def turtle_transaction(pen, frames_per_flush):
        """ACID semantics for turtle graphics.

        Atomic:     on failure, this turtle's ink is rolled back with clear().
        Consistent: position, heading and pen state are restored on exit.
        Isolated:   clear() erases only this turtle's ink, never another's.
        Durable:    the triangle stays on screen until you click. It counts.
        """
        screen = pen.getscreen()
        position, heading, was_down = pen.position(), pen.heading(), pen.isdown()
        previous_tracer = screen.tracer()

        def restore():
            pen.penup()
            pen.goto(position)
            pen.setheading(heading)
            if was_down:
                pen.pendown()
            screen.tracer(previous_tracer)
            screen.update()

        screen.tracer(frames_per_flush)
        try:
            yield pen
        except turtle_runtime.Terminator:
            raise  # The window was closed mid-transaction. There is nothing left to roll back onto.
        except BaseException:
            pen.clear()  # ROLLBACK
            restore()
            raise
        restore()  # COMMIT

    # ════════════════════════════════════════════════════════════════════
    # §11. Inversion of Control
    # ════════════════════════════════════════════════════════════════════
    class ServiceLocator(metaclass=SingletonMeta):
        """Mark Seemann called Service Locator an anti-pattern in 2010. We
        respect his opinion and have registered it as a dependency."""

        def __init__(self):
            self._providers = {}

        def register(self, interface, provider):
            self._providers[interface] = provider
            return self

        def resolve(self, interface):
            try:
                return self._providers[interface]()
            except KeyError:
                raise SierpinskiEnterpriseException(f"No provider registered for {interface.__name__}") from None

    class SierpinskiRenderingService:
        """Orchestrates the pipeline. Does no work itself; it is management."""

        def __init__(self, configuration, optimizer, consensus_engine, surface_provider, event_bus):
            self.configuration = configuration
            self.optimizer = optimizer
            self.consensus_engine = consensus_engine
            self.surface_provider = surface_provider
            self.event_bus = event_bus

        def render(self):
            side, depth = self.configuration.side_length, self.configuration.recursion_depth
            publish = self.event_bus.publish
            publish("ConfigurationValidated", side_length=side, depth=depth)

            numeral = to_church(depth)
            body = trampoline(compile_triangle(numeral, side, (), lambda finished: finished))
            publish("CompilationCompleted", instructions=len(body), church_roundtrip=from_church(numeral))

            certificate = self.consensus_engine.adjudicate(rows=2 ** depth)
            publish("ConsensusReached", votes=f"{certificate.votes}/{certificate.electorate}",
                    dissenters=",".join(certificate.dissenters) or "none", digest=certificate.digest[:12])

            self._verify_glaisher_invariant(body, certificate, depth)
            publish("InvariantsVerified", triangles=3 ** depth, theorem="Glaisher-1899")

            prologue = (PenUp(), Teleport(-side / 2, -side * math.sqrt(3) / 4), SetHeading(0), PenDown())
            epilogue = (PenUp(),)
            program = prologue + body + epilogue
            optimized, passes = self.optimizer.optimize(program)
            publish("OptimizationCompleted", before=len(program), after=len(optimized), passes=passes,
                    eliminated=f"{1 - len(optimized) / len(program):.1%}")

            pen = self.surface_provider()
            interpreter = TurtleInstructionInterpreter(pen)
            with turtle_transaction(pen, frames_per_flush=max(1, len(optimized) // 240)):
                interpreter.execute(optimized)
            publish("RenderingCommitted", instructions_executed=interpreter.executed)
            return certificate

        @staticmethod
        def _verify_glaisher_invariant(body, certificate, depth):
            """Glaisher (1899): row r of Pascal's triangle has 2^popcount(r) odd
            entries, so the first 2^n rows hold exactly 3^n of them. The
            compiler must emit exactly that many leaf triangles (three
            Turn(120)s apiece), or the symbolic and numeric layers disagree."""
            leaf_triangles = sum(1 for i in body if isinstance(i, Turn) and i.degrees == 120) // 3
            odd_entries = sum(map(sum, certificate.ruling))
            if not leaf_triangles == odd_entries == 3 ** depth:
                raise InvariantViolationError(
                    f"compiler={leaf_triangles}, oracles={odd_entries}, theory={3 ** depth}. Mathematics is broken.")

    class AbstractSierpinskiRenderingServiceFactoryBean(abc.ABC):
        """Named in honour of Spring's AbstractSingletonProxyFactoryBean,
        which is a real class that really exists."""

        @abc.abstractmethod
        def create_rendering_service(self, configuration):
            ...

    class DefaultSierpinskiRenderingServiceFactoryBeanImpl(
            AbstractSierpinskiRenderingServiceFactoryBean, metaclass=SingletonMeta):

        def create_rendering_service(self, configuration):
            locator = ServiceLocator()
            return SierpinskiRenderingService(
                configuration=configuration,
                optimizer=locator.resolve(PeepholeOptimizer),
                consensus_engine=locator.resolve(ConsensusEngine),
                surface_provider=lambda: locator.resolve(RenderingSurface),
                event_bus=locator.resolve(EventBus),
            )

    # ════════════════════════════════════════════════════════════════════
    # §12. Composition Root
    # ════════════════════════════════════════════════════════════════════
    def provision_pen():
        pen = turtle_runtime.Turtle(visible=False)
        pen.speed(0)
        return pen

    EventBus().subscribe("*", AuditLogObserver())
    (ServiceLocator()
        .register(EventBus, EventBus)
        .register(PeepholeOptimizer, PeepholeOptimizer)
        .register(RenderingSurface, provision_pen)
        .register(ConsensusEngine, lambda: ConsensusEngine([
            PascalParityOracle(),
            LucasTheoremOracle(),
            Rule90Oracle(),
            SelfSimilarityOracle(),
            ChaosMonkeyOracle(),
        ])))

    factory = DefaultSierpinskiRenderingServiceFactoryBeanImpl()
    service = factory.create_rendering_service(SierpinskiConfiguration(length, depth))
    return service.render()

sierpinski(400, 5)

turtle.exitonclick()