
def handle(event, context):
    import requests 
    headers = {}

    url = "https://api.loyal.guru/customers/authorize"
    params = {
      "email": event["queryStringParameters"]["email"].replace(" ","+"),
      "authentication_token": event["queryStringParameters"]["authentication_token"],
      "company_id": "92"
    }
    r = requests.post(url, data=params, headers=headers)
    if (r.status_code != 201):
      return {
        "statusCode": 200, 
        "headers": {"Access-Control-Allow-Origin" :"*"},   
        "body": {"status": "error"}
      }



    url = "https://ws.pyrenees.ad/Home"
    credentials = {
      "ClientID": "loyal.guru",
      "token": "c0905085ddc4e9761b89f30f58cd4fdc096307c1"
    }
    credentials["targeta"] = event["queryStringParameters"]["targeta"]

    url = url + event["resource"]
    if ((event["resource"] == "/venda") or (event["resource"] == "/pdf")):
      credentials["periode"] = event["queryStringParameters"]["periode"]

    r = requests.post(url, data=credentials, headers=headers)

    response = r.text.replace("'", "\\\"")
    if (event["resource"] == "/pdf"):
      response = '{"jsonData": "'+response+'"}'

    return {
      "statusCode": 200,    
      "headers": {"Access-Control-Allow-Origin" :"*"},   
      "body": response
    }