
import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    print(event)
    #Invoking Endpoint to get response
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=json.dumps(event))
    

    result = json.loads(response['Body'].read().decode())
    
    #Place holder for reformatted response
    holder = {}
   
    # Map to decode labels
    map = {'__label__0': 'DELETION OF INTEREST', '__label__1': 'RETURNED CHECK', '__label__2': 'BILL', '__label__3': 'POLICY CHANGE', '__label__4': 'CANCELLATION NOTICE', '__label__5': 'DECLARATION', '__label__6': 'CHANGE ENDORSEMENT', '__label__7': 'NON-RENEWAL NOTICE', '__label__8': 'BINDER', '__label__9': 'REINSTATEMENT NOTICE', '__label__10': 'EXPIRATION NOTICE', '__label__11': 'INTENT TO CANCEL NOTICE', '__label__12': 'APPLICATION', '__label__13': 'BILL BINDER'}
    
    #Logic to map multiple responses in case of multi batch
    for i in range(len(result)):
        label_list = []
        prob_list = []
        for ii in result[i]['label']:
            label_list.append(map[ii])
        for iii in result[i]['prob']:
            prob_list.append(iii)
        
        holder['response ' + str(i)] = dict(zip(label_list,prob_list))
        
        
    
    return holder
    
    #Function can return Top K classifications
