0-promise.js - Return a Promise using this prototype function getResponseFromAPI()

1-promise.js - Using the prototype below, return a promise. The parameter is a boolean.
    _getFullResponseFromAPI(success)_
When the argument is:
    • true
        resolve the promise by passing an object with 2 attributes:
            status: 200
            body: 'Success'
    • false
        reject the promise with an error object with the message The fake API is not working currently
Try testing it out for yourself

