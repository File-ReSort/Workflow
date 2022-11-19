import boto3

ID = "ID"
NAME = "Name"

# function definition
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('documents')

    response = table.scan(AttributesToGet=[ID, NAME])
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data

