<p align="center">
  <img src="./frontend/todois/src/assets/images/main-logo.png" alt="Logo">
</p>


## Project cloning SaaS Todoist using React (JavScript) and FastAPI (Python)

| This project aims to provide an intuitive and effective task management interface using modern technologies and development best practices.

## Index
1. Overview
2. Features
3. Technologies Used
4. Installation and Configuration

## Overview
Todoist Clone is a task manager that allows users to create, view, edit, and delete tasks. The application is divided into two main parts:

- Frontend: Built with React, it provides the user interface.

- Backend: Built with FastAPI and uses SQLite as the database, managing CRUD operations for tasks.

## Features
- Task Management: Add, edit, delete and view your tasks.
- Task Lists: Organize tasks into different lists.
- Filtering and Sorting: Filter and sort your tasks by date, priority and status.
- User Authentication: Register and log in users for personal access to their tasks.

## Technologies used
__Frontend:__

- React: JavaScript library for building user interfaces.
Axios: Library for making HTTP requests.
Material-UI: React component framework for modern design.

__Backend:__

- FastAPI: Framework for building fast and efficient APIs with Python.
SQLite: Lightweight, embedded database.


## Installation and Configuration
__backend__:
- clone this repository
    ```sh
    git clone git clone https://github.com/castroofelipee/todoist-clone.git
    cd todoist-clone
    ```
- Navigate to the backend directory and set up the virtual environment with Poetry:
    ```sh
    cd backend
    poetry install
    ```

- Start the FastAPI server:
    ```sh
    poetry run uvicorn main:app --reload
    ```

__frontend__:
- Navigate to the front end directory and run the following commands
    ```sh
    npm install & npm start
    ```

Access the application at http://localhost:3000.

