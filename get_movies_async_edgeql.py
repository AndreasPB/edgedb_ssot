# AUTOGENERATED FROM 'get_movies.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetMoviesResult(NoPydanticValidation):
    id: uuid.UUID
    title: str
    actors: list[GetMoviesResultActorsItem]


@dataclasses.dataclass
class GetMoviesResultActorsItem(NoPydanticValidation):
    id: uuid.UUID
    name: str


async def get_movies(
    executor: edgedb.AsyncIOExecutor,
) -> list[GetMoviesResult]:
    return await executor.query(
        """\
        select Movie { id,
                       title,
                       actors: { id,
                                 name}
                     }\
        """,
    )
