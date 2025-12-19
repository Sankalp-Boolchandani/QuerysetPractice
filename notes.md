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
- exclude 
    - returns all the the data in the queryset excluding the one condition specified - opposite of filter()
- order_by()
    - order_by is used to order the queryset based on the param passed
    - by default django orders based on the primary key of the model
    - ordering can be done either using queryset or the model itself. 
        - queryset - Restaurant.objects.order_by('xd')
        - mode - introducing ordering in the meta class of the model
    - Functions like Lower, Upper are also used for ordering
    - Lower: what this does is sorted the order by first converting the string into lower case and then sorting to avoid any ordering ambiguity based on ord(ascii) values of the alphabets


# lookups
- __startswith = checks if a string starts with a certain char or substring
- __in = used to check if a value is in a array or no
- __lt/lte = less than/less than equal to: for filtering out values less than specified condition
- __gt/gte = greater than/greater than equal to: for filtering out values greater than specified condition
- __range = used to get results in the given range of the specified field, takes lower and upper limits respectively as args field__range=(lower, upper)