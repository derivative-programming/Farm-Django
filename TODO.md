
job text...
The public repo is at https://github.com/derivative-programming/Farm-Django.
You will be submitting a PR to this repository.



todo...

implement django-seed to generate seed data.  add to readme doc on how to use.
- getting error on seeding. only 3 are being populated.

change name of app from 'Api' to 'Core'

running:job...implement factory_boy and faker in pac, tac, and customer unit tests

move model out of farm repos. put in harvest repo. 
 
models...
- blank=true
- add indexes
- set table name explicitly. no plurals
- set col name explicitly
- override update to verify that lastchangecode matches

tests...
- check all object props
- api call tests !!!gpt
- expand factory_boy and faker logic from job to test all objects

multiple project settings files. one for each env

populate flavor table with lookup values...
- dont create a migration
- use a fixture?  what happens if it runs twice?
- generate a migration to create lookup recs?

job to create register endpoint....
-  should also encrypt a string 
 


flows...      
- make async     
- https://github.com/phalt/django-api-domains/blob/master/example_domain/services.py

reports...
- separate classes to generate reports
- dir structure
    - [app root]
        - models
        - flows
        - reports
            - [modelName]
                - [reportname] file
                    - Generate function 
                        call provider class
                        optionally just return json instead of report item array?
                    - report item class
                - reader folder
                - writer folder
                - provider folder
                    report provider class
                        - this contains the custom sql. it may be generated but overridden later
                        - return json? have a reader loat it?
- use custom sql
- use dataclasses to define request and response objects
- select_related?
    no. not using models
- use functional views?
- paginator 
    - offset? cursor\keyset?

api...
- create instance of flow or report and execute
- folder struct
    - [approot]
        - models
        - reports
        - flows
        - api
            - /V##/
                - views
                    - [endpointname] file
                        - contains all functions. creates flows or generates reports
                - data-models
- use dataclasses to define request and response of api endpoints
- views.  class or function? what do dataclass examples use?
- https://copyprogramming.com/howto/django-reporting-options
    - custom sql example
- https://stackoverflow.com/questions/26015851/django-rest-framework-passing-raw-query
    - endpoint with custom sql to json example
        queryset = MyModel.objects.raw('... your SQL here...')
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)
- https://www.scaler.com/topics/django/django-running-raw-queries/
    - custom sql
- https://djangostars.com/blog/rest-apis-django-development/
    - api test
    - browsable api
    - openapi web -  drf-yasg
- https://stackoverflow.com/questions/59361772/using-custom-query-to-return-json-in-django-rest-framework
    - custom sql
        - execute to dict
- https://medium.com/roivant-technology/faster-api-development-with-django-dataclasses-5d33c366f23c
    - django_dataclasses<<< best???
        - request and response defined
            - https://pypi.org/project/django-dataclasses/
- https://www.errietta.me/blog/django-dataclass-serializer-openapi-swagger/  
    - djangorestframework-dataclasses
    - swagger
- https://opensource.com/article/21/9/unit-test-python
    - dataclass and testing
- https://aws.amazon.com/blogs/compute/generating-rest-apis-from-data-classes-in-python/
    - dataclass and dataclass_json
- https://fabiorosado.dev/blog/python-dataclasses/
                    - 

async workflow processing....
- celery? 
    - requires redis?
- dj background tasks?
- tasks subfolder containing all dynaflow tasks?


api auth...
- rest framework... DEFAULT_AUTHENTICATION_CLASSES 
- allauth?
  
admin...
- can create Admin versions of models with props
    - list_display
    - list_filter
    - search_fields
    - raw_id_fields




choices?
- create a json dict of all possible values a column can have?
- dont use. stick to lookup tables
