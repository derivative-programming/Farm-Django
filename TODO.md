
job text...
The public repo is at https://github.com/derivative-programming/Farm-Django.
You will be submitting a PR to this repository.



todo...

priority...
>>>>>>create managers for all models.  create enums for all lookups. create on manager get_by_code, get_by_enum

initialize lookup tables
security
v1_0 and Farm in template paths

convert ui apps to use new /submit endpoint

signalr

model managers...
- /models/managers folder
- one for each model
- initialize function: create any recs, like lookups
- build function: initializes all props and sets all lookups to unknown

currentRuntime class
- static fn Get[modelName]ByEnum(enum) for each lookup
- static fn Get[Modelname]ByCode(code) 



implement django-seed to generate seed data.  add to readme doc on how to use.
- getting error on seeding. only 3 are being populated.
   

site templates have farm in file path

version number folder name replacement not working...
calculatedCodeSafeVersionNumber > calculatedCodeSafeVersionNumberText
add a view sub folder?

add roles to token. check roles in flow?

implement security checks in base flows

Change land parent to customer? Tac?

If report is custom, create txt file

Init lookups

need view post (no id), get (no id), delete, and put examples 

Signalr 

tests...
- check all object props  

multiple project settings files. one for each env

populate flavor table with lookup values...
- dont create a migration
- use a fixture?  what happens if it runs twice?
- generate a migration to create lookup recs?

 apis and flows should be async

async workflow processing....
- celery? 
    - requires redis?
- dj background tasks?
- tasks subfolder containing all dynaflow tasks?
 
add to admin models...
search_fields = ['name', 'email', 'related_model__related_field']. what the admin search textbox will search.  do all varchar and nvarchar fields.

list_filter = ('is_active', 'created_at', 'related_model__related_field'). filter controls show on sidebar.
all boolean, all dates? all datetimes?
 
---------------------------------------------

flavor manager...............
 In this scenario, you can create a custom manager for the Flavor model, define a method in that manager to get an instance based on the LookupEnumName, and define an Enum to represent the possible LookupEnumName values.

First, you would need to import the necessary modules and define the Enum:

python
Copy code
from enum import Enum
from django.db import models

class FlavorEnum(Enum):
    SWEET = 'Sweet'
    SOUR = 'Sour'
    UNKNOWN = 'Unknown'
Next, you would define the custom manager. In the manager, you would define a method that takes a FlavorEnum value and returns the corresponding Flavor instance:

python
Copy code
class FlavorManager(models.Manager):
    def from_enum(self, flavor_enum):
        return self.get(LookupEnumName=flavor_enum.value)
Finally, you would define the Flavor model, using the custom manager and LookupEnumName field:

python
Copy code
class Flavor(models.Model):
    LookupEnumName = models.CharField(max_length=50)

    objects = FlavorManager()
Now, you can get a Flavor instance using a FlavorEnum value like this:

python
Copy code
sweet_flavor = Flavor.objects.from_enum(FlavorEnum.SWEET)
This will return the Flavor instance with LookupEnumName equal to 'Sweet'. If no such instance exists, it will raise a Flavor.DoesNotExist exception.

You should handle this exception in your application code and decide what to do if the Flavor instance doesn't exist.

Also, please ensure that the Flavor instances for all FlavorEnum values are created in the database.