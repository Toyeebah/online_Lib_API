<h1> Creating a Simple API for Managing an Online Library System </h1>

<h3> Description </h3>
<p>
The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books.
</p>

<h4> User: Represents a user of the library </h4>

- id: Unique identifier for the user.
- name: Name of the user.
- email: Email address of the user.
- is_active: Indicates if the user account is active (defaults to True).


<h4>Book: Represents a book in the library</h4>

- id: Unique identifier for the book.
- title: Title of the book.
- author: Author of the book.
- is_available: Indicates if the book is available for borrowing (defaults to True).


<h4>BorrowRecord: Represents a borrowing record</h4>

- id: Unique identifier for the record.
- user_id: ID of the user who borrowed the book.
- book_id: ID of the borrowed book.
- borrow_date: Date the book was borrowed.
- return_date: Date the book was returned (if applicable).


<h3>Project Requirements</h3>

<h5>User Endpoints</h5>

- CRUD operations for User.
- Endpoint to deactivate a user, setting is_active to False.


<h5>Book Endpoints</h5>

- CRUD operations for Book.
- Endpoint to mark a book as unavailable (e.g., if it’s lost or under maintenance).


<h5>Borrow Operations</h5>
<h5>Borrow a Book</h5>

- Allows an active user to borrow an available book.
- A user cannot borrow a book if it’s unavailable or if they have already borrowed the same book.
- If the book is successfully borrowed, update its is_available status to False.
- If the book cannot be borrowed, return an appropriate response and status code.


<h5>Return a Book</h5>

- Marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting the book’s is_available status to True.


<h5>Borrow Record Management</h5>

- Endpoint to view borrowing records for a specific user.
- Endpoint to view all borrowing records.


<h4>Additional Requirements</h4>
<h5>Database</h5>
<p>Use in-memory data structures (list or dict) for storage.</p>

<h5>Validation</h5>
<p>Use Pydantic models to validate inputs for all endpoints.</p>

<h5>Code Structure</h5>

- Follow a modular structure for better readability and maintainability.
- Use separate files for models, routes, and application configuration.


<h5>Status Codes</h5>
<p> Use appropriate HTTP status codes for success and error scenarios.</p>

<h5>Constraints</h5>

- Users must be active to perform any operations. 
- Books must be available to be borrowed. 
- Each borrowing operation should have a unique BorrowRecord.


<h4>Steps to Run FastAPI</h4>

- Clone the repository:
```
git clone https://github.com/Toyeebah/online_Lib_API.git
``` 


- Create a virtual environment:
```
python -m venv venv 
source venv/Scripts/activate
``` 


- Install dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```


- Run the FastAPI server:
```uvicorn main:app --reload
```


- View the Swagger documentation in your web browser.



<h4>Summary of Endpoints</h4>
<h5>User Routes</h5>

- GET /users/: Retrieve all users
- GET /users/{id}/: Retrieve a user by ID
- POST /users/: Create a new user
- PUT /users/{id}/: Update user details
- DELETE /users/{id}/: Delete a user
- PATCH /users/{id}/deactivate/: Deactivate a user

<h5>Book Routes</h5>

- GET /books/: Retrieve all books
- GET /books/{id}/: Retrieve a book by ID
- POST /books/: Add a new book
- PUT /books/{id}/: Update book details
- DELETE /books/{id}/: Delete a book
- PATCH /books/{id}/mark-unavailable/: Mark a book as unavailable

<h5>Borrow Routes</h5>

- POST /borrow/: Borrow a book
- POST /return/: Return a book
- GET /records/user/{user_id}/: View borrowing records for a user
- GET /records/: View all borrowing records



 <p> Tests for books and users were attempted </p>