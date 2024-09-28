# Restaurant Marketplace

API implementation with Clean Architecture, Python, FastAPI and MongoDB

## AnotaAE Backend Challenge

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

This project is an API built using **Python, FastAPI, AWS Simple Queue Service, AWS Lambda, AWS Simple Storage and Mongo DB with BeanieODM**

Challenge: [AnotaAi Backend Challenge](https://github.com/githubanotaai/new-test-backend-nodejs)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ozseniorcl13/anotaae-challenge
```

2. Install dependencies with pip

```bash
cd backend/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set your runtime environment variables with your AWS Credentials at `orchrestrator/env/.dev.env`
```yaml
AWS_REGION=us-east-1
AWS_KEY_ID=${AWS_KEY_ID}
AWS_SECRET_KEY=${AWS_SECRET}
```

## Usage

1. Start the application with `orchestrator/app.sh`
2. The API will be accessible at `http://localhost:3000/docs`

## API Endpoints
The API provides the following endpoints:

**API PRODUCT**
```markdown
POST /api/product - Create a new product
GET /api/product - Retrieve all products
PUT /api/product/{id} - Updates a product
DELETE /api/product/{id} - Delete a product
```

**BODY**
```json
{
  "title": "ProductTest",
  "description": "Product test",
  "ownerId": "1234",
  "categoryId": "659d558b0304df732ddd4587",
  "price": 10000
}
```

**API CATEGORY**
```markdown
POST /api/category - Create a new category
GET /api/category - Retrieve all categories
PUT /api/category/{id} - Updates a category
DELETE /api/category/{id} - Delete a category
```

**BODY**
```json
{
  "id": "393948882828",
  "title": "CategoryTest",
  "description": "Catetory test",
  "ownerId": "1234"
}
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request to the repository.

When contributing to this project, please follow the existing code style, [commit conventions](https://www.conventionalcommits.org/en/v1.0.0/), and submit your changes in a separate branch.

