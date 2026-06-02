from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process/stats', methods = ['POST'])

# Endpoint 1, task statistics
def stats():
    data =request.get_json()
    tasks = data.get('tasks', [])

    total = len(tasks)
    completed = 0
    for t in tasks:
        if t.get('completed') == True:
            completed += 1
    
    active = total - completed

    if total > 0:
        rate = str(int((completed / total) * 100)) + "%"
    else:
        rate = "0%"

    return jsonify({
        "completionRate": rate,
        "totalTasks": total,
        "totalCompleted": completed,
        "totalActive": active
    })

# Endpoint 2, automated tagging
@app.route('/process/tags', methods = ['POST'])

def tags():
    data = request.get_json()
    tasks = data.get('tasks', [])

    skip = {"a", "an", "the", "to", "and", "or", "is", "in", "on", "at",
            "for", "of", "so", "that", "i", "my", "it", "with", "from"}
    
    keywords = []

    for task in tasks:
        words = task.get('name', '').lower().split()
        for word in words:
            clean = word.strip('.,!?')
            if len(clean) > 2 and clean not in skip and clean not in keywords:
                keywords.append(clean)

    keywords.sort()

    return jsonify({"tags": keywords})

# Endpoint 3, priority sorting
# for the scoring system there couldve been more in depth variables
# instead of score, it couldve been a defined constant that said why 
# and when this would be subtracted or added
@app.route('/process/priority', methods=['POST'])

def priority():
    data = request.get_json()
    tasks = data.get('tasks', [])

    priority_words = {"fix", "bug", "urgent", "asap", "critical", "crash",
                    "broken", "error", "fail", "deploy", "hotfix", "issue"}
    results = []
    for task in tasks:
        name = task.get('name', '').lower()
        score = 5
        for word in priority_words:
            if word in name:
                score += 2
        if task.get('completed'):
            score -= 3
        score = max(1, min(10, score))
        results.append({"name": task.get('name'), "score": score})

    return jsonify ({"priorities": results})


# Run server
if __name__ == '__main__':
    app.run(port=5000, debug = True)

