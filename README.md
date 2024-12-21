# online_Lib_API
<h1> Creating a simple API for managing an online library system.</h1>

<h3> Description</h3>


<p>
    The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books.

    The system includes the following entities:


<h4> User: Represents a user of the library. <h4>
    <ul>
        <li> id: Unique identifier for the user. </li>
        <li> name: Name of the user.</li>
        <li> email: Email address of the user.</li>
        <li> is_active: Indicates if the user account is active (defaults to True).</li>
    </ul>

<h4> Book: Represents a book in the library. </h4>
    <ul>
        <li> id: Unique identifier for the book.</li>
        <li>title: Title of the book. </li>
        <li>author: Author of the book. </li>
        <li>is_available: Indicates if the book is available for borrowing (defaults to True). </li>
    </ul>

<h4> BorrowRecord: Represents a borrowing record.</h4> 
    <ul>
        <li> id: Unique identifier for the record. </li>
        <li> user_id: ID of the user who borrowed the book. </li>
        <li> book_id: ID of the borrowed book. </li>
        <li> borrow_date: Date the book was borrowed. </li>
        <li> return_date: Date the book was returned (if applicable). </li>
    </ul>

<h3> The project requirements were to create
<p> 
   <ol> <h5>User Endpoints: </h5>
        <li> CRUD operations for User.</li>
        <li> Endpoint to deactivate a user, setting is_active to False. </li>
    </ol>

    <ol> <h5> Book Endpoints: </h5>

        <li>CRUD operations for Book. </li>
        <li>Endpoint to mark a book as unavailable (e.g., if it’s lost or under maintenance).</li>
    </ol>


    <h5> Borrow Operations: </h5>
    <ol> <h5> Borrow a book: </h5>
        <li> Allows an active user to borrow an available book. </li>
        <li> A user cannot borrow a book if it’s unavailable or if they have already borrowed the same book.</li>
        <li> If the book is successfully borrowed, update its is_available status to False. </li>
        <li> If the book cannot be borrowed, return an appropriate response and status code. </li>

    </ol>

    <ol> <h5> Return a book: </h5>
        <li> Marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting  the book’s is_available status to True.</li>
        </ol>

    <h5> Borrow Record Management:</h5>
    <ol>
    <li> Endpoint to view borrowing records for a specific user. </li>
    <li> Endpoint to view all borrowing records. </li>

    <h4> Additional Requirements:
    <h5> Database: </h5>
        <p> Use in-memory data structures (list or dict) for storage.</p>
    <h5> Validation:</h5>
        <p>Use Pydantic models to validate inputs for all endpoints.</p>
    <h5> Code Structure: </h5>
        <p> Follow a modular structure for better readability and maintainability.
        <br>
        Use separate files for models, routes, and application configuration. </p>
    <h5> Status Codes: </h5>
        <p> Use appropriate HTTP status codes for success and error scenarios. </p>
    <h5> Constraints: </h5>
    <p> Users must be active to perform any operations. 
    <br> 
    Books must be available to be borrowed.
    <br>
    Each borrowing operation should have a unique BorrowRecord.
    </p>

</p>

<div>
    <p>
        To run the FastAPI, the following steps should be taken
        <ol>
            <li> Clone the repository.
                ```
                git clone https://github.com/Toyeebah/online_Lib_API.git

                ``` </li>
            <li> Create a virtual environment.
                ```
                python -m venv venv
                source venv/Scripts/activate

                ```
 </li>
            <li> Install dependencies from the requiremnts.txt file 
                ```
                pip install -r requirements.txt 

                ```
            </li>
            <li> Run the FastAPI server 
                ```
                uvicorn main:app --reload

                ```
            </li>
            <li> To view the documentation using swagger, open your web browser,and type localhost or the url displayed after your server starts running on uvicorn  </li>
        </ol>
    </p>
</div>

<div>
<p>
    <h4> Summary of endpoints created </h4>
    <h5> User Routes</h5>
    <ul>
        <li> GET /users/: Retrieve all users </li>
        <li> GET /users/{id}/: Retrieve a user by ID </li>
        <li> POST /users/: Create a new user </li>
        <li> PUT /users/{id}/: Update user details </li>
        <li> DELETE /users/{id}/: Delete a user </li>
        <li>PATCH /users/{id}/deactivate/: Deactivate a user</li>
    </ul>
    <h5> Book Routes</h5>
    <ul>
        <li> GET /books/: Retrieve all books </li>
        <li> GET /books/{id}/: Retrieve a book by ID </li>
        <li> POST /books/: Add a new book </li>
        <li> PUT /books/{id}/: Update book details </li>
        <li> DELETE /books/{id}/: Delete a book </li>
        <li> PATCH /books/{id}/mark-unavailable/: Mark a book as unavailable</li>
    </ul>
    <h5> Borrow Routes </h5>
    <ul>
        <li> POST /borrow/: Borrow a book </li>
        <li> POST /return/: Return a book </li>
        <li> GET /records/user/{user_id}/: View borrowing records for a user </li>
        <li> GET /records/: View all borrowing records</li>
        
    </ul>




</p>

</div>