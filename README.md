# Todo App

A simple todo application built with FastAPI and NeonDB (PostgreSQL).

## Features

- Add, edit, and delete tasks
- Get tasks by ID, title, or all tasks
- Automatic created_at timestamp

## Installation

1. Install uv: `pip install uv`
2. Install dependencies: `uv sync`

## Running the App

`uv run uvicorn app.main:app --reload`

## API Endpoints

- GET /tasks/{id} - Get task by ID
- GET /tasks/?title=... - Get tasks by title
- GET /tasks/ - Get all tasks
- POST /tasks/ - Create a new task
- PUT /tasks/{id} - Update task by ID
- DELETE /tasks/{id} - Delete task by ID
- DELETE /tasks/ - Delete all tasks