import asyncio

import edgedb

from get_people_async_edgeql import get_people
from get_movies_async_edgeql import get_movies


client = edgedb.create_async_client()


async def main():
    people = await get_people(client)
    movies = await get_movies(client)
    
    print(people, "\n")
    print(movies, "\n")

    for person in people:
        print(person.name)

    await client.aclose()


asyncio.run(main())
