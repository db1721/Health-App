import time

import boto3
from boto3.dynamodb.conditions import Key, Attr

PORT_DYNAMODB = 4566
dynamodb = boto3.client("dynamodb", endpoint_url="http://localhost:%s" % PORT_DYNAMODB)
dynamodb = boto3.resource('dynamodb')
blackjackTable = dynamodb.Table('exercise')
playerName = "Test name"
playerID = 1

def connect():
    return boto3.client("dynamodb", endpoint_url="http://localhost:%s" % PORT_DYNAMODB)


def create():
    client = connect()
    client.create_table(
        TableName="customers",
        BillingMode="PAY_PER_REQUEST",
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
    )


def insert(count):
    client = connect()
    start = time.time()
    for i in range(count):
        if i > 0 and i % 100 == 0:
            delta = time.time() - start
            print("%s sec for %s items = %s req/sec" % (delta, i, i / delta))
        client.put_item(
            TableName="customers",
            Item={
                "id": {"S": str(i)},
                "name": {"S": "Test name"},
                "zip_code": {"N": "12345"},
            },
        )

def getPlayerChips():
    """Searches database for player's chip count"""
    client = connect()
    fe = Key('id').between(1,100) & Attr('name').eq(playerName)
    pe = "id, name"

    response = blackjackTable.scan(
        FilterExpression=fe,
        ProjectionExpression=pe
        )
    
    dbList = response['Items']
    a_dictionary = dbList[0]
    
    for p in dbList:
        print(p['name'])
    
def main():
    # create()
    # insert(10000)
    getPlayerChips()