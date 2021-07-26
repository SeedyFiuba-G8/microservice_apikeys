from __future__ import annotations  # Necessary for Config type hinting
from dataclasses import dataclass, asdict, field
from os import getenv
from typing import Dict


def default_openapi() -> Dict[str, str]:
    return {
        "title": "APIKeys Microservice",
        "version": "0.1.0",
        "description": "Part of the **Seedy FIUBA Project** "
        "([view it on GitHub](https://github.com/orgs/SeedyFiuba-G8))",
        "hello": 'debug'
    }


@dataclass
class Config:
    ENV: str = getenv('FASTAPI_ENV', default='default')
    DB_USER: str = None
    DB_PASSWORD: str = None
    DB_DATABASE: str = None

    OPENAPI_SETTINGS: Dict[str, str] = field(default_factory=default_openapi)

    def update(self, other: Config):
        other_dict = asdict(other)
        for key, value in other_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return


config = Config()
