### Local

To verify the operation you must have Python installed on your computer and then follow these steps:

- Clone this repository and install dependencies with pip install

```
$ pip install -r requirements.txt 
```

 And then,

```
$ uvicorn main:app --reload
```

You can always make improvements to any project or code.

Initially, FastAPI was used as a Python framework to obtain a single, simple and functional view.

This view has the ability to render HTML and return an API response through a validated GET request.

The decision was made to do a function called "fibonacci". This function complies with the formula to obtain the sequence of numbers.

A view based on a function called "root" was made, which is in charge of rendering a simple HTML with a form, validation and delivery of the API response, it was done in this way for a fast and functional deployment.

As soon as the parameter was valid, we set an empty array to be filled by the Fibonacci sequence under the number entered by the user. At the end, a JSON response is delivered giving a REST API functionality from the GET method.
Note: HTML rendering was done to give a user friendly feature.

For an optimization the best thing would be to make a view based on classes and not by function. The HTML separate them from the main.py script, in this way the render is separated from the code and helps the readability and structure of the code. On the other hand, a good process would be to do unit tests to verify what is the maximum number that the user can enter so as not to obtain an API timeout, this according to the computational capacity of the computer or server.

Something interesting would be, upload this project after some tests to make it an interactive application for users who want to know what results the Fibonacci sequence can give them from the data they enter.

