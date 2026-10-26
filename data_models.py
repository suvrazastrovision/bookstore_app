"""SQLAlchemy database and model definitions for the book catalog."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    """Represent an author and their associated books."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    date_of_death = db.Column(db.Date, nullable=True)
    books = db.relationship(
        "Book", back_populates="author", cascade="all, delete-orphan"
    )

    def __repr__(self):
        """Return a concise representation of the author."""
        return f"Author(id={self.id}, name={self.name!r})"


class Book(db.Model):
    """Represent a book and its catalog metadata."""

    __table_args__ = (
        db.CheckConstraint(
            "rating IS NULL OR rating BETWEEN 1 AND 10",
            name="ck_book_rating_range",
        ),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    author_id = db.Column(
        db.Integer, db.ForeignKey("author.id"), nullable=False
    )
    author = db.relationship("Author", back_populates="books")

    def __repr__(self):
        """Return a concise representation of the book."""
        return f"Book(id={self.id}, title={self.title!r})"
