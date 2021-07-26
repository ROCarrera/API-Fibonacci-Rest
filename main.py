""" Simple View API Fibonacci """

""" FastAPI """
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

# App Instance
app = FastAPI()


# Fibonacci Function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


# View for Render HTML and View for Results
@app.get("/")
async def root(request: Request):
    """ Here we get the index value of the user """
    params = dict(request.query_params)
    if 'n' in params:
        """ Exist Parameter """
        array = []
        n = int(params['n'])
        if n <= 0:
            """ N must be >= 0 """
            return HTMLResponse("""
            You must enter a number greater than 0
            <script>setTimeout(function(){
                window.location = window.location.href.split("?")[0];
            }, 5000);
            </script>
            """)
        else:
            """ Fibonacci sequence """
            for i in range(n+1):
                array.append(fibonacci(i))
        return JSONResponse({
                'value': str(array[n])
            }
        )
    
    else:
        """ Return HTML """
        return HTMLResponse("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Insert Value</title>
        </head>
        <body>
            <form action="">
                <label>Insert <strong>INDEX</strong> Value</label>
                <input name="n" type="number">
            </form>
            <span>This App returns the Fibonacci value 
                that corresponds to the given index
            </span>
            <footer>
                Made by <strong>ROCarrera</strong>
            </footer>
        </body>
        </html>
        """)