# power_tower_calc

A calculator for comparing power towers, like Hypercalc. Implements some ideas of mine to avoid the power tower paradox.

Power towers are represented as a list of numbers until they have been fully processed into the internal representation.

The internal representation is as a power tower of 10's with a different number at top (like in Hypercalc), but also stored is the power tower's remainder when divided by a collection of three digit primes. This way, we are keeping information about the approximate size of the power tower, but we are also keeping information about the smallest "digits" of the power tower. The hope is that keeping this information will allow us to tell when two similarly sized power towers are actually different. This method will not allow us to tell which power tower is bigger though, just that they are different.
