# Cryptocurrency Ticker Variables

The following explains each field in the 24-hour ticker data format:

| Variable | Name | Description |
|----------|------|-------------|
| `e` | Event Type | Type of event (here: "24hrTicker") |
| `E` | Event Time | Timestamp of the event in milliseconds |
| `s` | Symbol | Trading pair symbol (e.g., "BTCUSDT") |
| `p` | Price Change | Absolute price change |
| `P` | Price Change Percent | Percentage price change |
| `w` | Weighted Average Price | Volume-weighted average price |
| `x` | First Price | Price at the beginning of the 24hr period |
| `c` | Current/Close Price | Latest/closing price |
| `Q` | Last Quantity | Quantity of the last executed trade |
| `b` | Best Bid Price | Highest buy order price |
| `B` | Best Bid Quantity | Quantity of the highest buy order |
| `a` | Best Ask Price | Lowest sell order price |
| `A` | Best Ask Quantity | Quantity of the lowest sell order |
| `o` | Open Price | Opening price 24hrs ago |
| `h` | High Price | Highest price in the last 24hrs |
| `l` | Low Price | Lowest price in the last 24hrs |
| `v` | Base Volume | Total trading volume in the base asset |
| `q` | Quote Volume | Total trading volume in the quote asset |
| `O` | Open Time | Start time of the statistics period |
| `C` | Close Time | End time of the statistics period |
| `F` | First Trade ID | ID of the first trade in the period |
| `L` | Last Trade ID | ID of the last trade in the period |
| `n` | Trade Count | Total number of trades in the period |
