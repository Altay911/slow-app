from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    birth_year: Mapped[Optional[int]]
    death_year: Mapped[Optional[int]]
    bio: Mapped[Optional[str]]

    books: Mapped[list["Book"]] = relationship(back_populates="author")
    quotes: Mapped[list["Quote"]] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("authors.id"))
    published_year: Mapped[Optional[int]]
    description: Mapped[Optional[str]]

    author: Mapped[Optional["Author"]] = relationship(back_populates="books")
    quotes: Mapped[list["Quote"]] = relationship(back_populates="book")


class Quote(Base):
    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("authors.id"))
    book_id: Mapped[Optional[int]] = mapped_column(ForeignKey("books.id"))
    created_at: Mapped[Optional[datetime]]

    author: Mapped[Optional["Author"]] = relationship(back_populates="quotes")
    book: Mapped[Optional["Book"]] = relationship(back_populates="quotes")