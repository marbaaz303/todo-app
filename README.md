# 📝 To-Do List Web App

A simple Flask-based To-Do List web application with full CI/CD automation using GitHub Actions and deployment on Render.

---

## 🚀 Live Demo
👉 [Click to View App](https://todo-app-h18x.onrender.com/)

---

## 🧩 Features

- ✅ Add and delete tasks in real time
- ✅ Built with Python and Flask
- ✅ Fully tested with white-box and black-box unit tests
- ✅ Includes Boundary Value Analysis (BVA) and Equivalence Class Partitioning (ECP)
- ✅ Continuous Integration (CI) using GitHub Actions
- ✅ Deployed to the cloud via Render

---

## 🧪 Testing

Tests are located in the `testcases/` directory and cover:

- `test_homepage_loads` – homepage renders successfully
- `test_add_task` – valid task is added
- `test_delete_task` – tasks can be deleted
- `test_bva_empty_task` – empty task input (BVA)
- `test_ecp_invalid_delete` – invalid task index deletion (ECP)

To run tests locally:

```bash
python testcases/test_app.py
