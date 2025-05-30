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

def on_message(ws, message):
    """Handle incoming WebSocket messages."""
    # print(message)
    data = json.loads(message)
    if 'c' in data: 
        price = data['c']
        timestamp = timezone.make_aware(datetime.fromtimestamp(data.get('E', 0) / 1000))
        print(f"BTC/USDT: ${float(price):.10f}")
        tick=Tick()
        tick.live_price = price
        tick.timestamp = timestamp
        tick.script_id = 1  
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

def run_ticker(token):
    socket = f"wss://stream.binance.com:9443/ws/{token}@ticker"
   
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
        print("Connection closed successfully")