import requests

BASE = "http://localhost:5000"

# placeholder task list
tasks = [
    {"name": "Login Bug", "completed": False},
    {"name": "Write tests", "completed": True},
    {"name": "Deploy the app", "completed": False},
    {"name": "Resolve web-app crash", "completed": False},
    {"name": "Update README.md", "completed": True},
]

print("\nTesting Data Processing Microservice\n")

# stats test
print("\n[1] POST /process/stats")
response = requests.post(f"{BASE}/process/stats", json={"tasks": tasks})
print("Response:", response.json())

# tags test
print("\n[2] POST /process/tags")
response = requests.post(f"{BASE}/process/tags", json={"tasks": tasks})
print("Response:", response.json())

# priority test
print("\n[3] POST /process/priority")
response = requests.post(f"{BASE}/process/priority", json={"tasks": tasks})
print("Response:", response.json())
 
print("\nAll tests complete!\n")