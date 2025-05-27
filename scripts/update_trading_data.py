import os
import json
import datetime
from pybit.unified_trading import HTTP

def main():
    API_KEY = os.getenv("BYBIT_API_KEY")
    API_SECRET = os.getenv("BYBIT_API_SECRET")

    session = HTTP(
        testnet=False,
        api_key=API_KEY,
        api_secret=API_SECRET,
    )

    total_equity = session.get_wallet_balance(accountType="UNIFIED", currency="USDT")['result']['list'][0]['totalEquity']

    all_future_position = session.get_positions(category='linear', settleCoin='USDT')['result']['list']

    if not os.path.exists('images/crypto-trading-history.json'):
        equity_history = {'history': []}
    else:
        equity_history = json.load(open('images/crypto-trading-history.json', 'r'))

    equity_history['history'].append({
        'total_equity': total_equity,
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'all_future_position': [{
            'symbol': position['symbol'],
            'leverage': position['leverage'],
            'ROI': float(position['unrealisedPnl']) * int(position['leverage']) / float(position['positionValue']) if position['positionValue'] != 0 else 0,
        } for position in all_future_position],
    })

    with open('images/crypto-trading-history.json', 'w') as f:
        json.dump(equity_history, f, indent=2)

if __name__ == "__main__":
    main()