import json
import uuid
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CatalogTable')

def my_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return str(obj)


def get_catalog(event, context):
    response = table.scan()
    return {
      "statusCode": 200,
      "body": json.dumps(response['Items'], default=my_default),
    }

def get_catalog_item(event, context):
    item_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': item_id})
    try:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'], default=my_default)
        }
    except KeyError:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Item not found'})
        }

def create_catalog_item(event, context):
    item = json.loads(event['body'])
    item['id'] = str(uuid.uuid4())
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def update_catalog_item(event, context):
    item_id = event['pathParameters']['id']
    try:
        table.get_item(Key={'id': item_id})['Item'] # check if item exists in dynamodb storage
        item = json.loads(event['body'])
        item['id'] = item_id
        print(table.put_item(Item=item))
        return {
            'statusCode': 200,
            'body': item
        }
    except KeyError:
        return {
            'statusCode': 404,
            'body': {'message': 'Item not found'}
        }

def delete_catalog_item(event, context):
    item_id = event['pathParameters']['id']
    try:
        table.get_item(Key={'id': item_id})['Item']
        table.delete_item(Key={'id': item_id})
        return {
            'statusCode': 200,
            'body': {'message': 'Item deleted'}
        }
    except KeyError:
        return {
            'statusCode': 404,
            'body': {'message': 'Item not found'}
        }
