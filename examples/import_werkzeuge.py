"""Kleine Hilfsfunktionen fuer Import-Beispiele."""


def begruessung(name: str) -> str:
    return f"Hallo {name}!"


def quadrat(x: int | float) -> int | float:
    return x * x


def tags_liste(tags: list[str]) -> str:
    return " | ".join(tag.upper() for tag in tags)
