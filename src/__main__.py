import asyncio

from .games import ultra_sun_ultra_moon
from .wild_pokemon import Move, PokeAPIClient


async def main():
    async with PokeAPIClient(ultra_sun_ultra_moon) as poke_client:
        moveset: list[Move] = await poke_client.get_wild_moveset('rattata-alola', 19)
        max_pp: int = sum(move['pp'] for move in moveset)

        print(f'This is a test! Alolan Rattata at level 19 should have a max of {max_pp} pp!')


asyncio.get_event_loop().run_until_complete(main())
