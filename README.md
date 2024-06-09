# FastAPI Animal Factory

Welcome to the FastAPI Animal Factory project! This project demonstrates the use of the Factory Design Pattern to create animal objects and expose them through a FastAPI API.

## Features

- Create different types of animals (dogs and cats) through HTTP requests.
- Each animal can "speak", providing its characteristic sound.
- Error handling for unknown animal types.

## Installation

1. Clone the repository:

`git clone https://github.com/your_username/fastapi-animal-factory.git`

2. Navigate to the project directory:

`cd fastapi-animal-factory`

3. Set up a virtual environment:

`python3 -m venv venv`
`source venv/bin/activate`

4. Install dependencies:

`pip install -r requirements.txt`

## Usage

1. Run the FastAPI application:

`uvicorn app.main:app --reload`

2. Open your web browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API documentation using Swagger UI.

3. Use the provided endpoints to create animals and make them speak!

## Endpoints

- GET /animal/{animal_type}: Retrieve an animal of the specified type.
Examples

- To create a dog:

`curl -X GET "http://127.0.0.1:8000/animal/dog"`

- To create a cat:

`curl -X GET "http://127.0.0.1:8000/animal/cat"`

## Testing

To run the tests, use the following command:

bash
Copy code
pytest
## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
