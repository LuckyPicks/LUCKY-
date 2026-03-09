import asyncio
from apis.odds_api import fetch_nba_props
from logic.bump_detector import detect_line_movement

async def start_scanner():

    while True:

        print("Scanning odds...")

        data = fetch_nba_props()

        if data:
            print("Odds received")

        await asyncio.sleep(180)
