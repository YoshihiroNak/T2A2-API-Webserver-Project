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

- [](#anchor11)


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


<a id="anchor6"></a>

## R6 - An ERD for your app


<a id="anchor7"></a>

## R7 - Detail any third party services that your app will use

<a id="anchor8"></a>

## R8 - Describe your projects models in terms of the relationships they have with each other

<a id="anchor9"></a>


## R9 - Discuss the database relations to be implemented in your application

<a id="anchor10"></a>

## R10 - Describe the way tasks are allocated and tracked in your project




