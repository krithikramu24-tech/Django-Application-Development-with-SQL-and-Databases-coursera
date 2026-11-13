# Django Application Development with SQL and Databases (Coursera)

Final Capstone Project: **Add a New Assessment Feature to an Online Course Application**

## Overview
This repository contains the completed final capstone project for the Coursera course *Django Application Development with SQL and Databases* by IBM Developer Skills Network.

### Key Implementations
- **Assessment Models (`onlinecourse/models.py`)**: Implemented `Question` (with scoring calculation helper `is_get_score`), `Choice` (with boolean correctness indicator), and `Submission` (with many-to-many choices relation) models.
- **Django Admin Interface (`onlinecourse/admin.py`)**: Registered `Question`, `Choice`, and `Submission` models with stacked `QuestionInline` and tabular `ChoiceInline` nested under `CourseAdmin` and `QuestionAdmin`.
- **Exam Assessment Views & URLs (`onlinecourse/views.py`, `onlinecourse/urls.py`)**: Implemented `extract_answers`, `submit`, and `show_exam_result` views handling submission grading, score percentage computation, and result presentation.
- **Responsive Templates (`course_detail_bootstrap.html`, `exam_result_bootstrap.html`)**: Interactive Bootstrap 4 exam forms with accordion collapse, question choice checkboxes, passing/failing alerts (>=80% passing grade), and detailed answer reviews.
- **Verification Deliverables**: Added full test suite, pre-populated database fixtures, and verified UI screenshots (`02-admin-site.png` and `07-final.png`).

---

## General Notes
An `onlinecourse` app has been provided in this repo upon which the new assessment feature is implemented.

- Developed and tested with Django 3.x/4.x and Python 3.10+
- Database: SQLite3 (compatible with PostgreSQL and MySQL)

## ER Diagram
![Onlinecourse ER Diagram](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database/blob/master/static/media/course_images/onlinecourse_app_er.png)
