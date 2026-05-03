import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client

load_dotenv()

app = Flask(__name__)
CORS(app)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# GET posts + replies
@app.route('/posts', methods=['GET'])
def get_posts():
    response = supabase.table("posts").select("*,replies(*)").execute()
    return jsonify(response.data)

# ADD post
@app.route('/posts', methods=['POST'])
def add_post():
    data = request.json

    response = supabase.table("posts").insert({
        "name": data.get("name"),
        "contact": data.get("contact"),
        "email": data.get("email"),
        "description": data.get("description"),  # ✅ FIXED
        "image": data.get("image")
    }).execute()

    return jsonify(response.data), 201

#UPDATE POST
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json

    update_data = {
        "name": data.get("name"),
        "description": data.get("description")
    }

    if data.get("image"):
        update_data["image"] = data.get("image")

    # Update main post
    supabase.table("posts") \
        .update(update_data) \
        .eq("id", post_id) \
        .execute()

    # Save update history
    supabase.table("post_updates").insert({
        "post_id": post_id,
        "name": update_data.get("name"),
        "description": update_data.get("description"),
        "image": update_data.get("image")
    }).execute()

    return jsonify({"message": "Updated successfully"})

# ADD reply
@app.route('/posts/<int:post_id>/reply', methods=['POST'])
def add_reply(post_id):
    data = request.json

    response = supabase.table("replies").insert({
        "post_id": post_id,
        "name": data.get("name"),
        "text": data.get("text")
    }).execute()

    return jsonify(response.data), 201

if __name__ == '__main__':
    app.run(debug=True)