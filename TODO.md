
job text...
The public repo is at https://github.com/derivative-programming/Farm-Django.
You will be submitting a PR to this repository.



todo...


priority...   
security
v1_0 and Farm in template paths  

convert ui apps to use new /submit endpoint

signalr
 
- expose build on parent object model.  def build_[child_object]   

implement django-seed to generate seed data.  add to readme doc on how to use.
- getting error on seeding. only 3 are being populated.
   

site templates have farm in file path

version number folder name replacement not working...
calculatedCodeSafeVersionNumber > calculatedCodeSafeVersionNumberText
add a view sub folder?

add roles to token. check roles in flow?

implement security checks in base flows

If report is custom, create txt file 

Signalr 

multiple project settings files. one for each env 

async workflow processing....
- celery? 
    - requires redis?
- dj background tasks?
- tasks subfolder containing all dynaflow tasks?


low priority....

on parent object...build_[child object name]...
- need a sub array on object... childObjects
- childObject array exist, but not being populated?


Change farm land parent to customer? Tac?

need view post (no id), get (no id), delete, and put examples 

tests...
- check all object props  

 apis and flows should be async
 
add to admin models...
search_fields = ['name', 'email', 'related_model__related_field']. what the admin search textbox will search.  do all varchar and nvarchar fields.

list_filter = ('is_active', 'created_at', 'related_model__related_field'). filter controls show on sidebar.
all boolean, all dates? all datetimes?
  