# Books and Reviews Service

This microservice is responsible for all the books and reviews

## Features

- Swagger documentation
- Docker support for easy deployment

### Prerequisites

- Python 3.9 or higher
- Django
- Docker (optional)

### Steps for Installation and Run Project

#### Without Docker
1. Clone the repository
```bash
git clone https://github.com/rajiv1027/books_reviews.git .
```
2. Create Virtual Environment
   1. Virtual Environment on Windows
        ```bash
        python -m venv myenv 
        pip install virtualenv
        virtualenv myenv
        myenv\Scripts\activate
      ```
   2. Virtual Environment on mac
    ```bash
      python3 -m venv myenv
      pip install virtualenv
      virtualenv myenv
      source myenv/bin/activate
   ```
        

3. Install dependency inside Virtual Environment from requirements.txt
```bash
pip install -r requirements.txt
```
4. Run Database Migrations
```bash
python manage.py migrate
```
5. Run Project
```bash
python manage.py runserver
```
6. Visit below URL to see the swagger documentation
```bash
Visit http://127.0.0.1:8000/swagger to access the API with Documentation
```

