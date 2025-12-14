- queryset always returns a list of objects
- count(): 
    - returns the number of objects returned 
- get(): 
    - returns a model of the queryset
    - should be only used when a person is certain that it would return only one object
    - if multiple objects are returned from get, we get an exception

- exists()
    - returns true or false based on if the queryset is present or not