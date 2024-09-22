# Project Instructions

This repository contains solutions to various coding challenges, implemented in Python and Django. Below is a summary of each question and the setup instructions.

## Table of Contents

1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
3. [Solutions](#solutions)
   - [Q1: Web Scraping with BeautifulSoup](#q1-web-scraping-with-beautifulsoup)
   - [Q2: Cleaning User Data from CSV](#q2-cleaning-user-data-from-csv)
   - [Q3: Django Top Customers View](#q3-django-top-customers-view)
   - [Q4: Rate Limiter Implementation](#q4-rate-limiter-implementation)
   - [Q5: Data Aggregation Function](#q5-data-aggregation-function)
   - [Q6: Find Duplicate in Array with O(1) Extra Space](#q6-find-duplicate-in-array-with-o1-extra-space)

## Requirements

- Python 3.x
- Django 3.x or higher
- Django Rest Framework
- BeautifulSoup4
- requests
- pandas (for CSV handling)

Make sure to include a `requirements.txt` file to install the necessary dependencies:

Django>=3.x
djangorestframework>=3.x
beautifulsoup4
requests
pandas

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bphariharan1301/VD-SE-Assignment
   cd VD-SE-Assignment

   ```

2. **Install Dependencies**:
   Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows use venv\Scripts\activate

   ```

Install the required packages:

- Inside each Q's folder there's a requirements.txt file. You've to run this command before within all virtual environments testing the program results and codes.

```bash
pip install -r requirements.txt
```

3. **Run Migrations**:
   After installing the dependencies, run the following command to create the necessary database tables:

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   Start the server with:

   ```bash
   python manage.py runserver
   ```

   For normal python programs run

   ```bash
   python <python_file_name>.py
   ```

5. **Access the API**:

   - Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.
   - To access the `top-customers` endpoint, you'll need to authenticate using a token. Follow these steps to set up the token:

     1. **Create Users**: Use the `create_users_view` endpoint to create multiple users. Send a POST request to `http://127.0.0.1:8000/api/create-users` with the following JSON payload:

        ```json
        [
        	{
        		"username": "user1",
        		"password": "password1",
        		"email": "user1@example.com",
        		"first_name": "User",
        		"last_name": "One"
        	},
        	{
        		"username": "user2",
        		"password": "password2",
        		"email": "user2@example.com",
        		"first_name": "User",
        		"last_name": "Two"
        	},
        	{
        		"username": "user3",
        		"password": "password3",
        		"email": "user3@example.com",
        		"first_name": "User",
        		"last_name": "Three"
        	},
        	{
        		"username": "user4",
        		"password": "password4",
        		"email": "user4@example.com",
        		"first_name": "User",
        		"last_name": "Four"
        	},
        	{
        		"username": "user5",
        		"password": "password5",
        		"email": "user5@example.com",
        		"first_name": "User",
        		"last_name": "Five"
        	},
        	{
        		"username": "user6",
        		"password": "password6",
        		"email": "user6@example.com",
        		"first_name": "User",
        		"last_name": "Six"
        	},
        	{
        		"username": "user7",
        		"password": "password7",
        		"email": "user7@example.com",
        		"first_name": "User",
        		"last_name": "Seven"
        	}
        ]
        ```

     2. **Obtain Token**: After creating a user, use the following endpoint to get the token:

        - Send a POST request to `http://127.0.0.1:8000/api/token-auth` with the following JSON payload:
          ```json
          {
          	"username": "user1", // Replace with the actual username
          	"password": "password1" // Replace with the actual password
          }
          ```

     3. **Use Curl Command**: Once you have the token, you can access the `top-customers` endpoint using the following curl command:
        ```bash
        curl -H "Authorization: Token your_token_here" http://127.0.0.1:8000/api/top-customers
        ```

## Solutions

### Q1: Web Scraping with BeautifulSoup

- **Setup**: Run the script to scrape titles from a specified news website. Make sure to have BeautifulSoup and requests installed.

### Q2: Cleaning User Data from CSV

- **Setup**: Ensure you have a CSV file with user data. Run the cleaning function to remove duplicates and invalid emails.

### Q3: Django Top Customers View

- **Setup**: This view requires the Django application to be running. Ensure you have the `Order` model set up and token authentication enabled.

### Q4: Rate Limiter Implementation

- **Setup**: Integrate the rate limiter into your Django views. Ensure it handles user requests properly.

### Q5: Data Aggregation Function

- **Setup**: Call the aggregation function with a list of dictionaries and a specified key to aggregate data.

### Q6: Find Duplicate in Array with O(1) Extra Space

- **Setup**: Given an array of n+1 integers where each integer is between 1 and n, find all duplicate numbers. The solution must not use extra space.

**Time Complexity**: O(n)

**Space Complexity**: O(1)
