import boto3


# function definition
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    # table name
    table = dynamodb.Table('documents')
    # inserting values into table
    response = table.put_item(
        Item={
          "ID": event["ID"],
          "LastEditDate": event["LastEditDate"],
          "FileName": event["FileName"],
          "BucketFileLocation": event["BucketFileLocation"],
          "Name": event["Name"],
          "UploadDate": event["UploadDate"]
        }
    )
    return response
