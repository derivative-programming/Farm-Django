
job text...
The public repo is at https://github.com/derivative-programming/Farm-Django.
You will be submitting a PR to this repository.



todo...

priority... 
lookup enums
initialize lookup tables
security
v1_0 and Farm in template paths

convert ui apps to use new /submit endpoint

signalr

model managers...  
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
  