# BlackKnight-Innovation-Lab
Interview challenge

This was a fun challenge really put some of my skills to the test.

I didn't have the time to do everything the best practices way. I am actually on vacation and have been working on this a couple of hours a night. I did quite a bit in console, so there won't be any code for some things but I will describe how I did them in my video. 


# Architecture

The architecture of this solution is as follows:
  Client -> API Gateway -> Lambda -> Sagemaker Endoint

## Client

I didn't have time to build a website but you can use CURL or Postman to send api calls. You will need the API key to make calls. I am aware that is not best practices to put your API key on get hub. "fIBJsF1YV07Iw5F6GQKGbmlFlVyGiw2AfRp5h5f0"

Example Curl:
curl -d @data.json -H "Content-Type: application/json" -H "X-API-KEY:fIBJsF1YV07Iw5F6GQKGbmlFlVyGiw2AfRp5h5f0" -X POST https://ncng9rt3f4.execute-api.us-east-1.amazonaws.com/prod/model

you can add and subtract data to the data.json files to test in batches. The configuration {"K"} allows you to return the TOP K classes based on probability 


## API

The api is using a POST method for a resource named "Model" within a "prod" stage. Don't worry about the API Key I have throttled the API with limits. Only 3 request per seconds and only 400 requests per month are allowed by this API Key. Hopefully thats enough for you to test. This Solution will be deleted on June 26 2020 at 5 pm eastern. If you finish testing before then please contact me at mureese.javon@gmail.com so I can terminate resources early and save my self a few nickles. 

## Lambda

The Lambda takes the request parses the data out and sends it to the model endpoint. It takes the response from the model endpoint and formats it.

## Sagemaker Endpoint 

Sits infront of a Blazingtext text classifier model. The model was trained with a automatic Hyperparmeter tuning job. The objective was to maximize validation accuracy. The best Model it produced had 85.7% accuracy on testing set while having 87% on training set. 

