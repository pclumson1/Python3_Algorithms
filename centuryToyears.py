# Given a year, return the century it is in.
# The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.


def centuryFromYear(year):
    if year % 100 == 0:
        return(year/100)
    else:
        return(int(year/100)+1)





def century_from_year(year: int = 0) -> int:
    if isinstance(year, int) and 1 <= year <= 2005:
        century = year // 100
        if year % 100 == 0:
            return century
        else:
            return century + 1
    return 0 



