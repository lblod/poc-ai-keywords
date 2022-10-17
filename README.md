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


keyword extraction api by ML2Grow
