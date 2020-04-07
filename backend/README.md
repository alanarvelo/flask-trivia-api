# Full Stack Trivia API Backend


## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 



## API Reference

### Getting Started
- Base URL: currently the server runs locally on `http://127.0.0.1:5000/`.
- Authentication: not yet configured. 

### Error Handling
Flask's `@app.errorhandler` decorators are implemented for:
- 404: Resource not found
- 405: Method not allowed
- 422: Unprocessable entity

Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Resource not found"
}
```


### Endpoints 

### Categories

#### GET /categories
- General:
    - Returns the list of categories, success value, and the current category.
- Sample: `curl http://127.0.0.1:5000/categories`

```{
    "categories": {
        "1":"Science",
        "2":"Art",
        "3":"Geography",
        "4":"History",
        "5":"Entertainment",
        "6":"Sports"},
    "current_category":null,
    "success":true
}
```

#### GET /categories/{cat_id}/questions
- General:
    - Returns a list of questions that belong to the request category. Also returns a success value, the total number of questions, and the current category.
    - The list of questions is paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/categories/2/questions`
```
{
   "current_category":2,
   "questions":[
      {
         "answer":"Escher",
         "category":2,
         "difficulty":1,
         "id":16,
         "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      },
      {
         "answer":"Mona Lisa",
         "category":2,
         "difficulty":3,
         "id":17,
         "question":"La Giaconda is better known as what?"
      },
      {
         "answer":"One",
         "category":2,
         "difficulty":4,
         "id":18,
         "question":"How many paintings did Van Gogh sell in his lifetime?"
      },
      {
         "answer":"Jackson Pollock",
         "category":2,
         "difficulty":2,
         "id":19,
         "question":"Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
      },
      {
         "answer":"well",
         "category":2,
         "difficulty":5,
         "id":28,
         "question":"Who I am?"
      }
   ],
   "success":true,
   "total_questions":5
}
```

### Questions

#### GET /questions
- General:
    - Returns the list of categories, the current category, a list of questions, the total number of questions, and a success value. 
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions`
```
{
   "categories":{
      "1":"Science",
      "2":"Art",
      "3":"Geography",
      "4":"History",
      "5":"Entertainment",
      "6":"Sports"
   },
   "current_category":null,
   "questions":[
      {
         "answer":"Maya Angelou",
         "category":4,
         "difficulty":2,
         "id":5,
         "question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
         "answer":"Edward Scissorhands",
         "category":5,
         "difficulty":3,
         "id":6,
         "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
         "answer":"Muhammad Ali",
         "category":4,
         "difficulty":1,
         "id":9,
         "question":"What boxer's original name is Cassius Clay?"
      },
      {
         "answer":"Brazil",
         "category":6,
         "difficulty":3,
         "id":10,
         "question":"Which is the only team to play in every soccer World Cup tournament?"
      },
      {
         "answer":"Uruguay",
         "category":6,
         "difficulty":4,
         "id":11,
         "question":"Which country won the first ever soccer World Cup in 1930?"
      },
      {
         "answer":"George Washington Carver",
         "category":4,
         "difficulty":2,
         "id":12,
         "question":"Who invented Peanut Butter?"
      },
      {
         "answer":"Lake Victoria",
         "category":3,
         "difficulty":2,
         "id":13,
         "question":"What is the largest lake in Africa?"
      },
      {
         "answer":"The Palace of Versailles",
         "category":3,
         "difficulty":3,
         "id":14,
         "question":"In which royal palace would you find the Hall of Mirrors?"
      },
      {
         "answer":"Agra",
         "category":3,
         "difficulty":2,
         "id":15,
         "question":"The Taj Mahal is located in which Indian city?"
      },
      {
         "answer":"Escher",
         "category":2,
         "difficulty":1,
         "id":16,
         "question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      }
   ],
   "success":true,
   "total_questions":19
}
```
#### DELETE /questions/{question_id}
- General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question and a success value. 
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/3?page=2`
```
{
    "id":3,
    "success":true
}
```
#### POST /questions/
- General:
    - Creates a new question resource using the submitted question, answer, difficulty, and category. Returns a success value.
- Sample: `curl http://127.0.0.1:5000/questions? -X POST -H "Content-Type: application/json" -d '{"question": "Are tests working?", "answer": "Yes", "difficulty": 1, "category": 3}'`
```
{
  "success": true
}
```

#### POST /questions/search
- General:
    - Searches for questions based on the `searchTerm` provided in the request body. Retunrs a list of matching questions, the number of matching questions, the current category, and a success value.
- Sample: `curl http://127.0.0.1:5000/questions/search? -X POST -H "Content-Type: application/json" -d '{"searchTerm": "largest lake in Africa"}'`
```
{
   "current_category":null,
   "questions":[
      {
         "answer":"Lake Victoria",
         "category":3,
         "difficulty":2,
         "id":13,
         "question":"What is the largest lake in Africa?"
      }
   ],
   "success":true,
   "total_questions":1
}
```

#### POST /quizzes
- General:
    - The body of this request contains a category value (can be null) and a list of previously asked questions. The response contains a random question from the provided category that is not in the previous questions list. Returns a question and a success value.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Science", "id": 5}}'`
```
{
   "question":{
      "answer":"Edward Scissorhands",
      "category":5,
      "difficulty":3,
      "id":6,
      "question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
   },
   "success":true
}
```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```