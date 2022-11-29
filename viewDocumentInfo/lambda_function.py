import boto3

# function definition
def lambda_handler(event, context):

    response = {}
    #get meta data from dynamodb
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('documents')
    
    dynamodbResponse = table.get_item(Key={"ID": event["ID"]})
    meta = dynamodbResponse['Item']

    data = meta["Annotations"]
    del meta["Annotations"]

    response = {
        "Annotations": data,
        "Meta": meta
    }

    return response
