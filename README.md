# openapi-client
### This is pymetrics's public API for assessments, usually as part of a job application workflow.
The typical use case for this is to support an externally initiated assessment for a candidate job application.
This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application.

The expected sequence of API calls is:
* `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided
* `Get Assessment Configurations` to determine which configured assessment templates are available
* `Create Assessment Order` for a selected Assessment and candidate job application
* `Get Assessment Order` to receive the recommendation results, once they are available

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    authorization = 'authorization_example' # str | Standard Bearer token request, from `Generate OAuth Token`. Formatted `Bearer {token}` (optional)
x_api_key = 'x_api_key_example' # str | Mandatory API Key that pymetrics will provide (optional)
order_request = openapi_client.OrderRequest() # OrderRequest | Candidate, assessment, and job application details (optional)

    try:
        # Create Assessment Order
        api_response = api_instance.mercury_create_order(authorization=authorization, x_api_key=x_api_key, order_request=order_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->mercury_create_order: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://staging.api.pymetrics.com* or *http://api.pymetrics.com* 

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**mercury_create_order**](docs/DefaultApi.md#mercury_create_order) | **POST** /mercury/order | Create Assessment Order
*DefaultApi* | [**mercury_get_config**](docs/DefaultApi.md#mercury_get_config) | **GET** /mercury/configuration | Get Assessment Configurations
*DefaultApi* | [**mercury_list_orders**](docs/DefaultApi.md#mercury_list_orders) | **POST** /mercury/orders | List Assessment Orders
*DefaultApi* | [**mercury_o_auth**](docs/DefaultApi.md#mercury_o_auth) | **POST** /mercury/oauth/token | Generate OAuth Token
*DefaultApi* | [**mercury_retrieve_order**](docs/DefaultApi.md#mercury_retrieve_order) | **GET** /mercury/getOrder/{uuid} | Get Assessment Order


## Documentation For Models

 - [AssessmentType](docs/AssessmentType.md)
 - [AtsType](docs/AtsType.md)
 - [Configuration](docs/Configuration.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ListOrdersRequest](docs/ListOrdersRequest.md)
 - [ListOrdersResponse](docs/ListOrdersResponse.md)
 - [MercuryAssessment](docs/MercuryAssessment.md)
 - [MercuryAssessmentOrder](docs/MercuryAssessmentOrder.md)
 - [MercuryCandidate](docs/MercuryCandidate.md)
 - [MercuryReport](docs/MercuryReport.md)
 - [MercuryResult](docs/MercuryResult.md)
 - [OAuthRequest](docs/OAuthRequest.md)
 - [OAuthResponse](docs/OAuthResponse.md)
 - [OrderCreateResponse](docs/OrderCreateResponse.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [PontemOrderStatuses](docs/PontemOrderStatuses.md)


## Documentation For Authorization

You will need to call 

## Author




