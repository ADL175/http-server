# http-server

<h1>Socket Server Step 2</h1>

<h2>Task</h2>

Implemented a function called parse_request
  The function takes a single argument which is the request from the client.
  The function only accepts GET requests. Any other request method raises an appropriate Python exception.
  The function only accepts HTTP/1.1 requests. A request of any other HTTP version raises an appropriate Python exception.
  The function validates that a proper Host header was included in the request and if not, raises an appropriate Python exception.
  The function validates that the request is well-formed. If the request is malformed in some way, it raises an appropriate Python exception.
  If none of the conditions above arise, the function should return the URI from the request.


If none of the conditions above arise, the function should return the URI from the request.

Updated response_error function to parameterize the error code and reason phrase.
The return value is a well-formed HTTP error response, built using the provided error code and reason phrase.

Updated the server loop:

passes the request you accumulate into your new parse_request function
handles any Python exceptions raised by building a meaningful HTTP error response
if no errors are raised, builds an HTTP 200 OK response.
returns the response you built to the client
