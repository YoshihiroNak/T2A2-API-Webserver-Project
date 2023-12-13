# GroupJournal_T2A2

# Table of Contents:

- [R1 - Identification of the problem you are trying to solve by building this particular app.](#anchor1)
- [R2 - Why is it a problem that needs solving?](#anchor2)
- [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#anchor3)
- [R4 - Identify and discuss the key functionalities and benefits of an ORM
](#anchor4)
- [R5 - Document all endpoints for your API](#anchor5)
- [R6 - An ERD for your app
](#anchor6)
- [R7 - Detail any third party services that your app will use](#anchor7)
- [R8 - Describe your projects models in terms of the relationships they have with each other](#anchor8)
- [R9 - Discuss the database relations to be implemented in your application
](#anchor9)
- [R10 - Describe the way tasks are allocated and tracked in your project
](#anchor10)


<a id="anchor1"></a>

## R1 - Identification of the problem you are trying to solve by building this particular app.
I am building this particular app to address the problem of a large retail sales company with an ineffcient new employee training system. The problem is that a mentor and new employees use a group journal which is a notebook to exchange feedback, which is inefficient and unsuitable for storing and sharing information.<br>
By developing this app, manual information exchage is no longer necessary, and feedback between a mentor and new employees can be smoothly conducted on the app.,<br>
Other employees can view the conversation on a unified platform, so when they comment on a new employee, they can communicate with them while understanding the corrent situation. This app will improve the efficiency of training new employees and also make data management easier.


<a id="anchor2"></a>

## R2 - Why is it a problem that needs solving?
There are several problems with managing group journals in notebooks. the problems that require solutions are:<br>

- Inefficiency: Exchanging feedback using a notebook is inefficient because only the person who owns the notebook can write and view it. Manual work is time-consuming and limits the opportunity for other employees to view it.

- Data Management: It is inefficient for a company to keep multiple notebooks, and searching for past information becomes manual and time-consuming.　By managing data, a campany can quickly search for past information and use it for training new empolyees　in the next period.

- Limited collaboration: The current method is inefficient as oppotunities for other employees to view the group journal are limited. Additionally, it is difficult to grasp the status of new employee training for all employees. By having a unified platform, all employees can view the group journal, and there is the advantage that they can communicate after understanding the situation.

<a id="anchor3"></a>

## R3 - Why have you chosen this database system. What are the drawbacks compared to others?
I have chosen PostgreSQL as the database for this app because it is a powful and reliable open source relational database management system(RDBMS) and it ishighly scalable.
Moreover, PostgeSQL has rich query optimization features and can efficiently process complex queries. <br>
When comparing PostgreSQL and MongoDB which is one of the other database management system, there are the following drawbacks: <br>
#### PostgeSQL drawbacks compared MongoDB

- Performance: When we handle large amounts of data or high traffic, PostgeSQL might not suitable.
- Schema Flexiblity: PostgeSQL is not a flexible schema such as  MongoDB, so it doesn't allow for easy modification or adaptation to changing data requirements.

#### MongoDB drawbacks compared PostgeSQL

- Consistency and Transactions: MongoDB sacrifices some of the ACID properties in favar of performance and scalability. It may not be the best choice for applications that require strict consistency and complex.
- Administration: The administaration comes with its own set of difficulities and complexities.

The choice between PostgreSQL and MongoDB depends on the specific requirements of the project, including the nature of data, scalability needs and the importance of transactional consistency.


<a id="anchor4"></a>

## R4 - Identify and discuss the key functionalities and benefits of an ORM
ORM stands for Object_Relational Mapping. It is a programing technique userd in software development that involves the conversion of data between incompatible type systems in relational databases and object-oriented programming languages The primary goal of ORM is to bridge the gap between the relatiomal model of a database and the object-oriented model used in application code.<br>

A key function of ORM is to facilitate the seamless interaction between an application's object-oriented code and the underlying relational database. <br>
Here are the key functions of ORM:<br>

#### 1. Mapping Objects to Tables: 

- ORM enables developers to define mappings between the objects in their application code and the tables in the relational database. Each class in the code corresponds to a table in the database, and instances of these classes represent rows in the  table.

#### 2. Abstraction of Database Operations:

- Developers can interact with the database using object-oriented syntax and methods, abstracting away the need to write raw SQL queries. ORM frameworks provide methods for common database operations(e.g., `insert`, `update`)that can be called from the application code.

Here are the benefits of ORM:<br>

#### 1. Abstraction:

- Developers can work with objects and classes in their code, abstracting away the complexities of SQL queries and database schema.

#### 2. Portability:

- ORM frameworks often provide a level of abstraction that makes it easier to switch between different database systems without significant cade changes.

#### 3. Productivity:

- ORM can lead to increased productivity as developers can focus more on the application logic rather than writing raw SQL queries.

In summary, the key function of ORM is to simplify and streamline the interaction between object-oriented code and relational database, providing a higher level of abstraction, improving code maintainability, and facilitating a more natural and intuitive way for developers to work with database in their applications.

<a id="anchor5"></a>

## R5 - Document all endpoints for your API

### 1. /users/register

- HTTP Request Verb: POST
- Required data: name, email, password
- Expected response Data: Expected '201 CREATED' response with return of data including is_admin and journals but excluding password
- Authentication methods: Autentication required for new users to register as a user to the app. It allows only admin
- Description: Allows user to register. This information is stored in the database

![register](/docs/images/register.png)

### 2. /users/login

- HTTP Request Verb: POST
- Required data: email, password
- Expected response Data: Expected '200 OK' response with return of data and JWT token generation excluding password
- Authentication methods: email, password
- Description: Allows users to login if email and password are matching in the database. It then generates a JWT token required for authorisation to enable user to use the app

![login](/docs/images/login.png)

### 3. /users

- HTTP Request Verb: GET
- Required data:N/A
- Expected response Data: Expected '200 OK' response with return of all users data excluding passwords
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to get all users information

![all_users](/docs/images/all_users.png)

### 4./users/＜int:user_id＞

- HTTP Request Verb: DELETE
- Required data: N/A
- Expected response Data:Expected '200 OK' response with return of empty JSON response
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to delete a specific user from the database and users can delete themselves as well

![delete_user](/docs/images/delete_user.png)

### 5. /journals

- HTTP Request Verb: GET
- Required data: N/A
- Expected response Data: Expected '200 OK' response with return of all journals
- Authentication methods: Valid JWT token
- Description: Allows users to get all journals

![all_journals](/docs/images/all_journals.png)

### 6. /journals/＜id＞

- HTTP Request Verb: GET
- Required data:N/A
- Expected response Data: Expected '200 OK' response with return of a specific journal
- Authentication methods: Valid JWT token
- Description: Allows users to get a specific journal

![one_journal](/docs/images/one_journal.png)

### 7. /journals

- HTTP Request Verb: POST
- Required data: title, description
- Expected response Data: Expected '201 CREATED' response with return of journal information
- Authentication methods: Valid JWT token
- Description: Allows users to add a journal

![post_journal](/docs/images/post_journal.png)

### 8./journals/＜id＞

- HTTP Request Verb: PUT/PATCH
- Required data: title, description
- Expected response Data: Expected '200 OK' response with return of journal information
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to update a specific journal and users can update themselves as well

![put_journal](/docs/images/put_journal.png)

### 9./journals/＜id＞

- HTTP Request Verb: DELETE
- Required data: N/A
- Expected response Data:Expected '200 OK' response with return of empty JSON response
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to delete a specific journal

![delete_journal](/docs/images/delete_journal.png)

### 10./journals/<journal_id>/feedbacks

- HTTP Request Verb: POST
- Required data: message
- Expected response Data: Expected '201 CREATED' response with return of a specific journal information with message
- Authentication methods: Valid JWT token
- Description: Allows users to add message

![post_feedback](/docs/images/post_feedback.png)

### 11./journals/<journal_id>/feedbacks/<feedback_id>

- HTTP Request Verb: PUT/PATCH
- Required data: message
- Expected response Data: Expected '200 OK' response with return of a specific journal information with message
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to update a specific feedback and users can update themselves as well

![put_feedback](/docs/images/put_feedback.png)

### 12./journals/<journal_id>/feedbacks/<feedback_id>

- HTTP Request Verb: DELETE
- Required data: N/A
- Expected response Data::Expected '200 OK' response with return of empty JSON response
- Authentication methods: Valid JWT token, authorize()
- Description: Allows an admin to delete a specific feedback and users can delete themselves as well

![delete_feedback](/docs/images/delete_feedback.png)

### Endpoint Error Handling
![error_handling1](/docs/images/error_handling1.png)
![error_handling1](/docs/images/error_handling2.png)
![error_handling1](/docs/images/error_handling3.png)
![error_handling1](/docs/images/error_handling4.png)
![error_handling1](/docs/images/error_handling5.png)
![error_handling1](/docs/images/error_handling6.png)
![error_handling1](/docs/images/error_handling7.png)
![error_handling1](/docs/images/error_handling8.png)
![error_handling1](/docs/images/error_handling9.png)

<a id="anchor6"></a>

## R6 - An ERD for your app

Enttities are users, jounals and feedbacks. The table of users is associated with multiple journals and feedbacks. The table of journals is associated with multiple feedbacks.
![ERD](/docs/images/ERD.png)

<a id="anchor7"></a>

## R7 - Detail any third party services that your app will use

### SQL Alchemy

- ORM library allows developers to interact with database using high-level programming language constructs, abstracting away much of the SQL code.

### PostgreSQL

- A DBMS is essential for storing and managing data. The choice of database depends on factors such as scalability, data complexity and application requirements.

### Marshmallow

- Marshmallow is a Python library that provides a simple way to convert complex data types, such as objects, to and from Python data types. 

### Psycopg2

- Psycopg2 is a PostgreSQL adapter for the Python programming language. It allows Python programs to connect to and interact with PostgreSQL databases. 

### Bcrypt

- Bcrypt is a password-hashing library for Python (and other languages) that is designed to securely hash passwords. It is specifically designed to be slow and computationally intensive, making it resistant to brute-force attacks, rainbow table attacks, and other common password-cracking techniques.

### Flask JWT Extended

- Flask JWT Extended is an extension for the Flask web framework that adds support for JSON Web Tokens (JWT) in Flask applications.
The Flask JWT Extended extension provides tools to easily implement JWT-based authentication and authorization in your Flask applications. 

<a id="anchor8"></a>

## R8 - Describe your projects models in terms of the relationships they have with each other

### User model

- The User model represents a user and has a one-to-many relationship with Journal and Feedback, allowing a user to have multiple associated journals and feedbacks.
 The User model has a foreign key user_id in the Journal model, which establishes the relationship between the two models. And also the User model has a foreign key user_id in the Feedback model, which establishes the relationship between the two models. The relationship is defined using "jounals = db.relationship('Journal', back_populates='user')" and "feedbacks = db.relationship('Feedback', back_populates='user')" in the User model.

![user_model](/docs/images/user_model.png)

### Journal model

- The Journal model represents a journal and has a one-to-many relationship with Feedback and many-to-one relationships with user.
The Journal model has a foreign key journal_id in the Feedback model, which establishes the relationship between the two models.
 The relationship is defined using "user = db.relationship('User', back_populates='journals')" and
 "feedbacks = db.relationship('Feedback', back_populates='journal')" in the Journal model.

![journal_model](/docs/images/journal_model.png)

### Feedback model

- The Feedback model represents a feedback and has a many-to-one relationship with User and Journal.
The relationship is defined using "user = db.relationship('User', back_populates='feedbacks')" and "journal = db.relationship('Journal', back_populates='feedbacks')" in the Feedback model.


![feedback_model](/docs/images/feedback_model.png)

<a id="anchor9"></a>


## R9 - Discuss the database relations to be implemented in your application

My API app has a database called "journal" which has 3 tables: users, journals, feedbacks.
The users table represents the users in the system. Each item in the table represents a column.
Esch user has a unique ID. If the name is not entered, it defaults to "Annoymous". The email column has to be filled in. The password column stores encrypted and hashed passwords. This column also cannot be NULL. A JWT token will be generated when the user log in with a valid email and password.<br>

The journals table represents the journals in the system. It has an id, title, description and date columns. The title of the company training will be entered in the title column. The training content will be entered in the description column.<br>

The feedbacks table represents the feedbacks in the system. It has an id, message columns. New employees receive company training and record their impressions as feedback in the journal. Other employees and an admin who see the feedback also writhe messages to the feedback.
To establish the relationship between users and journals, the "feedbacks" table acts as a join table. It contains foreign keys that reference the "users" and "journals" tables. Using join tables allows for the efficient handling of the one-to-many and many-to-one relationships.


<a id="anchor10"></a>

## R10 - Describe the way tasks are allocated and tracked in your project

I used Trello to manage my daily tasks. First, I exported all the tasks for this project to Trello. Trello allows to assign tasks visually and easily to understand, and organizes tasks into four categories: To Do, Doing, Testing and Done. I was able to track the prosess of tasks on Trello every day and work systematically and efficiently.<br>
The task management method is simple and all tasks are initially placed in To Do. Tasks that are being worked on are assigned in Doing, and then tasks that need testing are moved to Testing. Once all tasks have been completed, they will be moved to Done.<br>
By recording my progress daily in standups in Discord, I was able to divide the flow of tasks into 3 days( yesterday, today, tomorrow) which helped me work more efficiently.<br>
By looking at the records of my daily commits to Github, I was able to grasp the current status of the entire task, objectively analyze the progress of my work, and this helped me work far more efficiently.

![trello1](/docs/images/trello1.png)
![trello2](/docs/images/trello2.png)
![trello3](/docs/images/trello3.png)
![trello4](/docs/images/trello4.png)
![trello5](/docs/images/trello5.png)
![trello6](/docs/images/trello6.png)
![trello7](/docs/images/trello7.png)
![trello8](/docs/images/trello8.png)
![standup1](/docs/images/standup1.png)
![standup2](/docs/images/standup2.png)
![standup3](/docs/images/standup3.png)
![github_commits](/docs/images/github_commits.png)






