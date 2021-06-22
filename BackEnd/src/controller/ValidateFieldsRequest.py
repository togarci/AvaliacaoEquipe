class ValidateFieldsRequest:

    def validateAll(self, arrayOfValidationNames, request):
        listToReturn = {}
        for name in arrayOfValidationNames:
            if not name in request.json.keys():
                listToReturn[name] = 'This field is required'

        if len(listToReturn) > 0:
            return { "status": False, "dataField": listToReturn }
        else:
            return { "status": True }
