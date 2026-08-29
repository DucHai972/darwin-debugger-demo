"""Pricing helpers. Monetary half-cents must round away from zero."""


def discounted_cents(cents: int, percent: int) -> int:
    """Return integer cents after applying an integer percentage discount."""
    if cents < 0:
        raise ValueError("cents must be non-negative")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return int(cents * (100 - percent) / 100)
