import matplotlib.pyplot as plt

#These Need to Be Replaced with the CSV Data Instead
year = [1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
kilometres = [47.0, 37.0, 34.2, 34.0, 32.5, 33.5, 33.3, 33.5, 33.3, 32.7, 34.0, 36.4, 35.0, 35.8, 34.7, 33.9, 31.8, 31.5, 32.0, 30.1, 29.7, 29.1, 28.7, 29.6, 30.4, 30.1, 28.3, 29.8, 30.9, 30.3, 28.6, 29.3, 30.7, 32.0, 30.3, 29.7, 27.2, 29.5, 29.5, 30.4, 30.8, 32.4, 34.3, 33.3, 33.2, 32.5, 31.7, 30.4, 28.7, 30.0, 32.1, 34.7, 36.3, 38.6, 38.3, 39.3, 39.8, 41.0, 41.8, 43.3, 46.3, 49.1, 50.9, 51.5, 54.5, 57.1, 58.3, 60.2, 62.9, 64.7, 66.0, 66.2, 67.7, 66.8, 12.5]
year2 = ['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
ticket = [1047, 1168, 1291, 1357, 1483, 1514, 1551, 1577, 1559, 1720, 1870, 2048, 2242, 2463, 2463, 2585, 2693, 2890, 3088, 3323, 3714, 4120, 4443, 4608, 4965, 5447, 5816, 6162, 6649, 7008, 7269, 7584, 8106, 8133, 1560]
s_ticket = [395, 454, 512, 550, 574, 603, 603, 616, 611, 660, 702, 773, 847, 905, 950, 964, 970, 1011, 1071, 1170, 1298, 1434, 1561, 1571, 1654, 1782, 1890, 2041, 2153, 2205, 2171, 2072, 2136, 2076, 333]
f_revenue = [1443, 1622, 1803, 1907, 2057, 2117, 2154, 2193, 2171, 2379, 2573, 2821, 3089, 3368, 3413, 3548, 3663, 3901, 4158, 4493, 5012, 5555, 6004, 6179, 6620, 7229, 7707, 8203, 8803, 9213, 9441, 9655, 10241, 10208, 1894]
nf_revenue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 52, 63, 58, 64, 67, 69, 74, 80, 80, 104, 131, 151, 157, 167, 179, 192, 188, 196, 198, 200, 190, 12]


fig1, ax1 = plt.subplots()

fig1.suptitle("Passenger Revenue by Ticket Type", fontsize=16)

ax1.set_title("Apr1986 - Apr2020", fontsize=14)

ax1.set_xlabel("Year", fontsize=12)

ax1.set_ylabel("(£ million)", fontsize=12)

ax1.plot(year2, ticket)
ax1.plot(year2, s_ticket)

ax1.xaxis.grid()
ax1.yaxis.grid()

plt.show()



fig, ax = plt.subplots()

fig.suptitle("Passenger Kilometres Travelled in Great Britain", fontsize=16)

ax.set_title("1946-2020", fontsize=14)

ax.set_xlabel("Year", fontsize=12)

ax.set_ylabel("Kilometres (Billions)", fontsize=12)

ax.plot(year, kilometres, 'ro-')

ax.xaxis.grid()
ax.yaxis.grid()

plt.show()