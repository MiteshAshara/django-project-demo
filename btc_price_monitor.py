#!/usr/bin/env python3
"""
BTCUSDT Live Price Monitor

This script connects to Binance's WebSocket API and prints the live market price
of BTC/USDT pair in the console.
"""

import websocket
import json

def on_message(ws, message):
    """Handle incoming WebSocket messages."""
    # print(message)
    data = json.loads(message)
    if 'c' in data: 
        price = data['c']
        print(f"BTC/USDT: ${float(price):.10f}")

def on_error(ws, error):
    """Handle WebSocket errors."""
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    """Handle WebSocket connection close."""
    print("Connection closed")

def on_open(ws):
    """Handle WebSocket connection open."""
    print("Connection established")

if __name__ == "__main__":
    socket = "wss://stream.binance.com:9443/ws/btcusdt@ticker"
   
    ws = websocket.WebSocketApp(socket,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    
    print("Connecting to Binance WebSocket API...")
    print("Press Ctrl+C to stop")

    ws.run_forever()