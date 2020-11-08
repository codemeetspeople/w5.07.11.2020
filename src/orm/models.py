from orm.db import (
    get_connection,
    SELECT_QUERY,
    INSERT_QUERY,
    UPDATE_QUERY
)


class Book:
    connection = get_connection()

    def __init__(self, _id=None):
        self._id = None
        self._title = None
        self._author = None

        self._changes = False

        if _id:
            self.__load(_id)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @title.setter
    def title(self, value):
        self._title = value
        self._changes = True

    @author.setter
    def author(self, value):
        self._author = value
        self._changes = True

    def __load(self, _id):
        cursor = self.connection.cursor()
        row = cursor.execute(SELECT_QUERY, (_id,))
        book = row.fetchone()

        self._author = book[0]
        self._title = book[1]
        self._id = _id

    def save(self):
        if not self._changes:
            return

        cursor = self.connection.cursor()
        if not self.id:
            self._id = cursor.execute(
                INSERT_QUERY, (self.title, self.author)
            ).lastrowid
        else:
            cursor.execute(
                UPDATE_QUERY, (self.title, self.author, self.id)
            )
        self._changes = False
