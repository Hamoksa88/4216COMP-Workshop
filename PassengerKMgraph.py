import matplotlib.pyplot as plt

input_values = [1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
squares = [47.0, 37.0, 34.2, 34.0, 32.5, 33.5, 33.3, 33.5, 33.3, 32.7, 34.0, 36.4, 35.0, 35.8, 34.7, 33.9, 31.8, 31.5, 32.0, 30.1, 29.7, 29.1, 28.7, 29.6, 30.4, 30.1, 28.3, 29.8, 30.9, 30.3, 28.6, 29.3, 30.7, 32.0, 30.3, 29.7, 27.2, 29.5, 29.5, 30.4, 30.8, 32.4, 34.3, 33.3, 33.2, 32.5, 31.7, 30.4, 28.7, 30.0, 32.1, 34.7, 36.3, 38.6, 38.3, 39.3, 39.8, 41.0, 41.8, 43.3, 46.3, 49.1, 50.9, 51.5, 54.5, 57.1, 58.3, 60.2, 62.9, 64.7, 66.0, 66.2, 67.7, 66.8, 12.5]

fig, ax = plt.subplots()

fig.suptitle("Passenger Kilometres Travelled in Great Britain", fontsize=16)

ax.set_title("1946-2020", fontsize=14)

ax.set_xlabel("Year", fontsize=12)

ax.set_ylabel("Kilometres (Billions)", fontsize=12)


ax.plot(input_values, squares)

plt.show()
