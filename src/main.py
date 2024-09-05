from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from Passiv import buy_passiv

app = FastAPI()


@app.get("/")
def read_root():
    html_content = """
    <html>
      <head>
        <title>Passiv buyer</title>
        <script type="text/javascript">
          function disableButton(event) {
            event.target.disabled = true;
            event.target.innerText = 'Running...';
          }
        </script>
      </head>
      <body>
        <h1>Hello</h1>
        <p>This is a simple page to run Passiv buyer</p>
        <form action="/passiv">
          <button type="submit" onClick="disableButton(event)">Run Passiv</button>
        </form>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/passiv")
def run_passiv():
    buy_passiv()
    return {"status": "success"}
