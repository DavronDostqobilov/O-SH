# Shajara

## Installation

**Clone the repository:**

```
bash git clone https://github.com/DavronDostqobilov/O-SH.git
```

**Create a virtual environment and activate it:**

```
python -m venv env
```
```
source env\Scripts\activate
```

**Install dependencies:**
```
pip install -r requirements.txt
```
**Apply migrations:**
```
python manage.py migrate
```
**Run the development server:**
```
python manage.py runserver
```

**Person Model Schema**

|name |type |description|
|-----|------|----------|
|id   |int   | primary key|
|name | str  |person's name|
|birth_date | date person's |birth date|
|photo | image | person's photo|
|father| ForeignKey| ID of father (optional)|
|mother| ForeignKey| ID of mother (optional)|
## API Endpoints

### Persons Endpoints:

|Method | Endpoint | Description |
|-------|----------|-------------|
|GET    |/persons/ | Get all persons |
|POST   |/persons/ | Create a new person|
|GET    |/persons/{id}/| Get a person by ID|
|PUT    |/persons/{id}/| Update a person by ID|
|DELETE |/persons/{id}/| Delete a person by ID|

**Responses**

- 200 OK: Successful retrieval or update.

- 201 Created: Successful creation.

- 204 No Content: Successful deletion.

- 400 Bad Request: Invalid input.

- 404 Not Found: Person not found.
