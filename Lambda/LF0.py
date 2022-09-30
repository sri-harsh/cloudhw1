import json

def lambda_handler(event, context):
    # TODO implement
    message = "Application under development. Search functionality will be implemented in Assignment 2"
    return {
        'statusCode': 200,
        "messages": [{"type": "unstructured","unstructured": { "text": message }}]
    }
