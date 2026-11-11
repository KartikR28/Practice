# TODO (plan for tomorrow - Lesson 1 remaining tasks):
# 1. Rename this file to "app.py" (it has no .py extension yet)
# 2. Create helper find_user(user_id) and use it in GET, PUT, DELETE
# 3. Create helper validate_name(name) and use it in POST, PUT
#    - reject names with no letters, e.g. "!!!" -> any(c.isalpha() for c in name)
# 4. Add JSON error handlers for 404, 405 and 500 (@app.errorhandler)
# 5. Test with Postman/curl: name "!!!", missing user, PATCH /users/1 (expect 405)
# 6. Answer interview questions: 400 vs 401 vs 403 vs 404, PUT vs PATCH, what is a decorator

from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "amit"},
    {"id": 2, "name": "riya"},
    {"id": 3, "name": "rahul"},
    {"id": 4, "name": "sneha"},
    {"id": 5, "name": "vikram"},
    {"id": 6, "name": "pooja"},
    {"id": 7, "name": "arjun"},
    {"id": 8, "name": "neha"},
    {"id": 9, "name": "karan"},
    {"id": 10, "name": "anjali"},
]

# The id the next new user will get. It only goes up, so a deleted
# user's id is never given to someone else. Worked out once at startup.
next_id = max((user["id"] for user in users), default=0) + 1


def find_user(user_id):
    """Return the user with this id, or None if there is no such user."""
    return next((user for user in users if user["id"] == user_id), None)


def validate_name(name):
    """Return an error message if the name is not valid, otherwise None."""
    if not isinstance(name, str) or not any(char.isalpha() for char in name):
        return "Name must be a string with at least one letter"
    return None


@app.route("/")
def home():
    return jsonify({"message": "Flask API is running"})


@app.route("/users", methods=["GET"])
def get_users():
    
    return jsonify({
        "data": users
    }), 200



@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object"
        }), 400

    name = data.get("name")

    error = validate_name(name)
    if error:
        return jsonify({"error": error}), 400

    new_user = {
        "id": next_id,
        "name": name.strip()
    }
    next_id += 1

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "data": new_user
    }), 201




@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = find_user(user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    users.remove(user)

    return jsonify({
        "message": "User deleted successfully"
    }), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    user = find_user(user_id)

    if user is None:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "data": user
    }), 200



@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json(silent=True)

    # 1. Validate the request body
    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object"
        }), 400

    # 2. Validate the name
    name = data.get("name")

    error = validate_name(name)
    if error:
        return jsonify({"error": error}), 400

    # 3. Find the user
    user = find_user(user_id)

    # 4. Check whether the user exists
    if user is None:
        return jsonify({
            "error": "User not found"
        }), 404

    # 5. Update the user
    user["name"] = name.strip()

    # 6. Return the response
    return jsonify({
        "message": "User updated successfully",
        "data": user
    }), 200


# Without these, Flask answers unknown routes with an HTML page.
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    app.run()
