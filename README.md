# poc-ai-keywords

![](https://build.redpencil.io/api/badges/lblod/poc-ai-keywords/status.svg)

This repository contains the code to get started with the keyword extraction api. This api is used to extract keywords from a given text,
but also to extract keywords from generated text (integration with poc-ai-text-generation).

## Getting started
In order to run this code, you will either have to build it localy or use our build container. Keep in mind you will have to
supply the container with our model (you can copy it from a google storage bucket).
### Pre-requisit
In order to use the full functionality of this api, you will have to make sure that you have the poc-ai-text-generation api
running aswel.

### Starting the docker container
First you pull the container (can be skipped --> will be pulled either if not present when executing the run command)
```
docker pull lblod/poc-ai-keywords
```

run command
```
docker run -it --rm  -p 8080:8080 lblod/poc-ai-keywords
```

You could also add a model_store volume mount, here you could add caching. If you restart you api you will not have to redownload the entire model.

### Swagger

```
{"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/":{"get":{"summary":"Health Check Route","operationId":"Health_check_route__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}}}}},"/get_gen_keywords":{"get":{"summary":"This Route Is To Extract Keywords From Generated Text That Is Created From A Prompt","description":"Takes a text; generates a large text body using text generation api and does keyword extraction\non this text body.\n\n:param text_prompt:str text to generate keywords for\n:return:Dict containing keywords in a list in the form of {\"result\":{\"keywords\":keywords}}","operationId":"This_route_is_to_extract_keywords_from_generated_text_that_is_created_from_a_prompt_get_gen_keywords_get","parameters":[{"required":true,"schema":{"title":"Text Prompt","type":"string"},"name":"text_prompt","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/get_text_keywords":{"get":{"summary":"This Route Is Made To Extract Keywords From A Document","description":"Takes a text generates a large text body using text generation api and does keyword extraction\non this text body.\n\n:param text_prompt:str text to generate keywords for\n:return:Dict containing keywords in a list in the form of {\"result\":{\"keywords\":keywords}}","operationId":"This_route_is_made_to_extract_keywords_from_a_document_get_text_keywords_get","parameters":[{"required":true,"schema":{"title":"Doc Text","type":"string"},"name":"doc_text","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"anyOf":[{"type":"string"},{"type":"integer"}]}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}

```

keyword extraction api by ML2Grow
