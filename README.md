A. This microservice takes a list of tasks and does three types of data
    processing: stats (calculate completion rate and task counts), tagging (
    extracts keywords from task names), and priority scoring (assigns an
    urgency score of 1 - 10 to each task).
B. How to run this:
    1. pip install flask requests
    2. python app.py
    3. server runs at http://localhost:5000
C. To request data, send a POST request to one of the endpoints with a JSON
    body with a tasks array. Each task must have a name which is a string, and
    a completed which is a boolean.
    Example call (Endpoint 1, task statistics):
        POST https://localhost:5000/process/stats

        python:
        import requests

        response = requests.post("POST writtten above", json={"tasks": [
            {"name": "Fix login bug", "completed": False},
            {"name": "Write tests", "completed": True},
            {"name": "Deploy app", "completed": False}
        ]
        })
        print(response.json())
D. <img width="785" height="398" alt="Screenshot 2026-05-20 at 4 06 01 PM" src="https://github.com/user-attachments/assets/7567bfa7-1922-45ff-805b-1be997750237" />
