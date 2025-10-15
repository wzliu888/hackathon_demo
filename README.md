# Flask Hello World API

A simple Flask application that exposes various endpoints including a Server-Sent Events (SSE) endpoint.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:

   ```bash
   python app.py
   ```

3. Access the endpoints:

   ### Hello World

   - URL: [http://localhost:8080/hello_world](http://localhost:8080/hello_world)
   - Method: GET
   - Response: `{"message": "Hello, World!"}`

   ### Hello World with Name

   - URL: [http://localhost:8080/hello_world/YourName](http://localhost:8080/hello_world/YourName)
   - Method: GET
   - Response: `{"message": "Hello, YourName World!"}`

   ### Hello (POST)

   - URL: [http://localhost:8080/hello](http://localhost:8080/hello)
   - Method: POST
   - Request Body: `{"name": "YourName"}`
   - Response: `{"message": "Hello, YourName! This is a POST response."}`

   ### Server-Sent Events (SSE)

   - URL: [http://localhost:8080/sse](http://localhost:8080/sse)
   - Method: GET
   - Response: Continuous stream of events
   - Format: `{"count": 1, "time": "14:30:00"}` (sent every second)

## Requirements

- Python 3.6+
- Flask 2.3.3
