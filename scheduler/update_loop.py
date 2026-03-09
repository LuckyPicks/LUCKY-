import asyncio
from apis.odds_api import fetch_nba_props

async def start_scanner():

    while True:

        print("Scanning odds...")

        data = fetch_nba_props()

        if data:
            print("Odds received")

        await asyncio.sleep(180)
