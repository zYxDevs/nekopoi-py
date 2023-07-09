import typing as t
import dateparser
from datetime import datetime
from slugify import slugify


def slugified(title: str) -> str:
    return slugify(title)


def slugified_web_url(title: str, slug: t.Optional[str] = None) -> str:
    slugified = slugify(slug) if slug else slugify(title)
    return f"https://nekopoi.care/{slugified}"


def parse_date(date: str) -> datetime:
    return dateparser.parse(date)
