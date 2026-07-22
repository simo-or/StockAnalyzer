import yfinance as fi
symbol = input("Enter the stock ticker symbol: ").upper()
print("\nLoading company data...")
stock = fi.Ticker(symbol)
info = stock.info
def print_line():
    print("=" * 45)
print_line()
print("         < STOCK ANALYZER >")
print_line()
print("Company:", info[ "longName"])
print("Current Price:", info["currentPrice"])
print("Day High:", info["dayHigh"])
print("Day Low:", info["dayLow"])
print("Market Cap:", info["marketCap"])
print("Open:", info["open"])
print("Previous Close:", info["previousClose"])
print("52 Week High:", info["fiftyTwoWeekHigh"])
print("52 Week Low:", info["fiftyTwoWeekLow"])
print("Volume:", info["volume"])
print("Average Volume:", info["averageVolume"])
print("Sector:", info.get("sector", "Not Available"))
print("Country:", info.get("country", "Not Available"))
print("Industry:", info.get("industry", "Not Available"))
print("Employees:", info.get("fullTimeEmployees", "Not Available"))
print("EPS:", info.get("trailingEps", "Not Available"))
print("PE Ratio:", info.get("trailingPE", "Not Available"))
print("Dividend Yield:", info.get("dividendYield", "Not Available"))
print("Website:", info.get("website", "Not Available"))
print("\n")
history = stock.history(period="5d")
print("\nLast 5 Trading Days")
print(history[["Open", "High", "Low", "Close", "Volume"]])

print_line()
print("         < STOCK ANALYSIS >")
print_line()
current_price = info["currentPrice"]
previous_close = info["previousClose"]

price_change = current_price - previous_close
price_change_percent = (price_change / previous_close) * 100

print("Price Change:", round(price_change, 2), "USD")
print("Percentage Change:", round(price_change_percent, 2), "%")
print_line()
print("        < PRICE POSITION >")
print_line()

week_high = info.get("fiftyTwoWeekHigh")
week_low = info.get("fiftyTwoWeekLow")

if week_high and week_low:
    distance_from_high =((week_high - current_price) / week_high) * 100
    distance_from_low = ((current_price - week_low) / week_low) * 100

    print("Distance from 52 Week High: ",round(distance_from_high, 2), "%")
    print("Distance from 52 Week low: ",round(distance_from_low, 2), "%")

print_line()
print("        < INVESTMENT RATING > ")
print_line()

score = 0
pe = info.get("trailingPE")

if pe:
    if pe < 15:
        score+=2
        print("PE Ratio: Excellent!")
    elif pe < 30:
         score += 1
         print("PE Ratio: Good!")
    else: 
        print("PE Ratio: Expensive")
else:
    print("PE Ratio: Not Available")

if week_high:

    if distance_from_high > 25:
        score += 2
        print("Price Position: Far from yearly high")

    elif distance_from_high > 10:
        score += 1
        print("Price Position: Moderately below yearly high")

    else:
        print("Price Position: Near yearly high")

dividend = info.get("dividendYield")

if dividend:

    score += 1
    print("Dividend: Yes")

else:
    print("Dividend: No")

print("\nFinal Score:", score, "/5 \n")

if score >= 4:
    print("Overall Rating: Strong")
elif score >= 2:
    print("Overall Rating: Average")
else:
    print("Overall Rating: Weak")

print_line()
print("       < COMPANY SIZE >")
print_line()
market_cap = info.get("marketCap")

if market_cap:

    if market_cap > 200000000000:
        print("Classification: Mega Cap")

    elif market_cap > 10000000000:
        print("Classification: Large Cap")

    elif market_cap > 2000000000:
        print("Classification: Mid Cap")

    else:
        print("Classification: Small Cap")

print_line()
print("       < RISK ANALYSIS >")
print_line()

beta = info.get("beta")

if beta:

    print("Beta:", round(beta,2))

    if beta < 0.8:
        print("Risk: Low")

    elif beta < 1.3:
        print("Risk: Medium")

    else:
        print("Risk: High")

else:
    print("Beta: Not Available")

print_line()
print("        < FINAL SUMMARY >")
print_line()

print("Company:", info.get("longName", "Not Available"))
print("Ticker:", symbol)
print("Current Price:", current_price, "USD")
print("Market Cap:", info.get("marketCap", "Not Available"))
print("Overall Score:", score, "/5")
print()

if score >= 4:
    print("Recommendation: This company has strong financial indicators.")
elif score >= 2:
    print("Recommendation: This company has average financial indicators.")
else:
    print("Recommendation: This company should be analyzed more carefully.")

print_line()
print("End of Report")
print("Stock analysis completed.")
print_line()
