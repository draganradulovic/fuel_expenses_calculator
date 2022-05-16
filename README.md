# fuel_expenses_calculator

A program that calculates fuel expences for a trip whose parameters are entered at the input. \
Program takes following parameters from the input: starting city, destination city, car consumption, type of fuel and a refueling country.\
\
Using selenium webdriver, it searches google maps in order to find distance between start and destination.\
Then, using selenium webdriver, it searches https://autotraveler.ru/en/spravka/fuel-price-in-europe.html page, in order to get current fuel price for
the specified fuel and state.\
Program then uses the found data to calculate fuel expenses.\

For better efficiency, it runs on headless browser.
