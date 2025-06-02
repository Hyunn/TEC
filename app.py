from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing user to workspaces mapping
USER_WORKSPACES = {
    "1": [
        {"id": "w1", "name": "Workspace 1"},
        {"id": "w2", "name": "Workspace 2"}
    ],
    "2": [
        {"id": "w3", "name": "Workspace 3"}
    ]
}

@app.route('/workspaces', methods=['GET'])
def get_workspaces():
    """Return all workspaces for a given user."""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id query parameter is required"}), 400

    workspaces = USER_WORKSPACES.get(user_id, [])
    return jsonify({"user_id": user_id, "workspaces": workspaces})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
