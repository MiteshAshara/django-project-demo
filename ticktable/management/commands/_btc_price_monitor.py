#!/usr/bin/env python3
"""
BTCUSDT Live Price Monitor

This script connects to Binance's WebSocket API and prints the live market price
of BTC/USDT pair in the console.
"""

import websocket
import json
from ticktable.models import Tick
from datetime import datetime
from django.utils import timezone

script_local = None

def on_message(ws, message):
    data = json.loads(message)
    
    if 'data' in data and 'stream' in data:
        stream_name = data['stream']
        data = data['data']
        
        script = None
        for s in script_local:
            if stream_name.lower().startswith(s.token.lower()):
                script = s
                break
                
        if not script:
            print(f"No matching script found for stream: {stream_name}")
            return
    else:
        script = script_local[0] if isinstance(script_local, list) else script_local
    
    if 'c' in data:
        price = data['c']
        timestamp = timezone.make_aware(datetime.fromtimestamp(data.get('E', 0) / 1000))
        print(f"{script.name} ${float(price):.10f}")
        tick = Tick()
        tick.live_price = price
        tick.event_type = data.get('e')
        tick.event_time = data.get('E')
        tick.symbol = data.get('s')
        tick.price_change = data.get('p')
        tick.price_change_percent = data.get('P')
        tick.weighted_avg_price = data.get('w')
        tick.first_trade_price = data.get('x')
        tick.last_price = data.get('c')
        tick.last_quantity = data.get('Q')
        tick.best_bid_price = data.get('b')
        tick.best_bid_quantity = data.get('B')
        tick.best_ask_price = data.get('a')
        tick.best_ask_quantity = data.get('A')
        tick.open_price = data.get('o')
        tick.high_price = data.get('h')
        tick.low_price = data.get('l')
        tick.total_traded_base_volume = data.get('v')
        tick.total_traded_quote_volume = data.get('q')
        tick.statistics_open_time = data.get('O')
        tick.statistics_close_time = data.get('C')
        tick.first_trade_id = data.get('F')
        tick.last_trade_id = data.get('L')
        tick.total_trades = data.get('n')
        tick.timestamp = timestamp
        tick.script_id = script.pk  
        tick.save()
    

def on_error(ws, error):
    """Handle WebSocket errors."""
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    """Handle WebSocket connection close."""
    print("Connection closed")

def on_open(ws):
    """Handle WebSocket connection open."""
    print("Connection established")

def run_ticker(scripts):
    global script_local
    script_local = scripts
    
    if isinstance(scripts, list):
        streams = "/".join([f"{script.token.lower()}" for script in scripts])
    else:
        scripts = [scripts]
        streams = f"{scripts.token.lower()}"
        
    # print(f"Streams: {streams}")
    socket = f"wss://stream.binance.com:9443/stream?streams={streams}"
    ws = websocket.WebSocketApp(socket,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    
    print("Press Ctrl+C to stop")

    try:
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()