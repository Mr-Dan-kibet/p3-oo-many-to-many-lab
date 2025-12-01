# lib/many_to_many.py

class Book:
    all = []
    
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        """Return a list of contracts for this book."""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return a list of authors for this book."""
        return [contract.author for contract in self.contracts()]

class Author:
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        """Return a list of contracts for this author."""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Return a list of books for this author."""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object between the author and book."""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        
        # Validate book
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        
        # Validate date
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        
        # Validate royalties
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date as the specified date."""
        return [contract for contract in cls.all if contract.date == date]