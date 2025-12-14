# queryset always returns a list of objects
- count(): 
    - returns the number of objects returned 
- get(): 
    - returns a model of the queryset
    - should be only used when a person is certain that it would return only one object
    - if multiple objects are returned from get, we get an exception
- exists()
    - returns true or false based on if the queryset is present or not
- multiple filter()
    - many filter options can be executed by using just a comma(name=xd, type=abc)


# lookups
- __startswith = checks if a string starts with a certain char or substring
- __in = used to check if a value is in a array or no