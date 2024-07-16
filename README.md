# CRUD Catalog App with AWS SAM

This project is a Serverless Application Model (SAM) based CRUD catalog application using AWS Lambda, Amazon API Gateway, Amazon DynamoDB, and Amazon Cognito.

## Architecture

- **AWS Lambda**: Backend logic for CRUD operations
- **Amazon API Gateway**: RESTful endpoints
- **Amazon DynamoDB**: Storage for catalog items
- **Amazon Cognito**: User authentication (admin and customer pools)

## Features

- Create, Read, Update, Delete catalog items
- Separate APIs for admin and customer users, each with different authorizers

## Prerequisites

- AWS CLI configured
- AWS SAM CLI installed
- Python 3.9
- An AWS account

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/crud-catalog-app.git
    cd crud-catalog-app
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Deploy

1. **Build the SAM application**:
    ```bash
    sam build
    ```
2. **Deploy the application**:
    ```bash
    sam deploy --guided
    ```
    Enter the parameters for `AdminUserPool` and `CustomerUserPool` when prompted.

## Usage

### Admin API

- **Create**:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "item1", "description": "desc1", "price": 100}' https://your-admin-api-url/catalog
    ```
- **Get All**:
    ```bash
    curl https://your-admin-api-url/catalog
    ```
- **Get by ID**:
    ```bash
    curl https://your-admin-api-url/catalog/{id}
    ```
- **Update**:
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "item1", "description": "desc updated", "price": 120}' https://your-admin-api-url/catalog/{id}
    ```
- **Delete**:
    ```bash
    curl -X DELETE https://your-admin-api-url/catalog/{id}
    ```

### Customer API

- **Get All**:
    ```bash
    curl https://your-customer-api-url/catalog
    ```
- **Get by ID**:
    ```bash
    curl https://your-customer-api-url/catalog/{id}
    ```

## Local Testing

To test the application locally using SAM CLI:
```bash
sam local start-api
```

## Delete

To delete the application:
```bash
sam delete
```
