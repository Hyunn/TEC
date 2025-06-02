# Workspace API

This repository contains a simple Flask-based API that returns the list of workspaces a user belongs to.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python app.py
```

The server starts on port 5000.

## Usage

Retrieve workspaces for a user by passing the `user_id` query parameter:

```bash
curl http://localhost:5000/workspaces?user_id=1
```

This returns all workspaces the specified user belongs to. If the user has no associated workspaces, the response contains an empty array.

