"""
* Excersise: 
** Flatland is a country with a number of cities, some of which have space 
** stations. Cities are numbered consecutively and each has a road of 1km length 
** connecting it to the next city. It is not a circular route, so the first city 
** doesn't connect with the last city. Determine the maximum distance 
** from any city to its nearest space station.
"""


def flatlandSpaceStations(n: int, c: list[int]) -> int:
    # Agrego inicio y final
    c.sort()
    max_distance = max(c[0], n - 1 - c[-1])
    for i in range(1, len(c)):
        max_distance = max((c[i] - c[i-1]) // 2, max_distance)
    return max_distance
