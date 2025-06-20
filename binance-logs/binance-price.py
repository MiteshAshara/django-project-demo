from datetime import datetime
import json
from time import sleep
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
import logzero

logzero.logfile("binance_websocket.log", mode="a")
logger = logzero.logger
symbols = ["btcusdt", "ethusdt", "solusdt", "dogeusdt"]

def message_handler(_, message):
    data = json.loads(message)
    symbol = data.get("s")
    quantity = float(data.get("q", 0))
    trade_time = data.get("T")
    price = float(data.get("p", 0))
    if symbol and quantity and trade_time and price:
        timestamp = datetime.fromtimestamp(trade_time / 1000).isoformat(timespec="seconds")
        log_entry = {
            "symbol": symbol,
            "price": price,
            "quantity": quantity,
            "timestamp": timestamp
        }
        logger.info(json.dumps(log_entry))

logs = UMFuturesWebsocketClient(on_message=message_handler)

for sym in symbols:
    logs.agg_trade(symbol=sym)

print("Press Ctrl+C to stop")

try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    logs.stop()