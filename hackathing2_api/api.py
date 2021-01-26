import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    body = json.loads(event['body'])
    print("name: " + body['name'])
    
    response = {
        'name': body['name']
    }
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(response)
    }
    raise Exception('Something went wrong')
