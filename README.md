# Tower
A Machine Learning Task Management Platform Based on Kubernetes.
## Features
- View cluster status, tasks.
- Manage deep learning tasks.
- Use namespaces for task isolation.
## Overview
- Dashboard
![Dash](images/dash.png)
- Task Management
![Task](images/task.png)
- Task Details
![Details](images/details.png)
- Namespace Management
![NS](images/ns.png)

## Quick Start 
### Development Test Environment
- Python 3.6 (Recommend)
- Django 2.1 (Necessary)
- Kubernetes 1.15 (Recommend)

### Install dependencies
```shell script
pip install -r requirements.txt
```
### Initialize the Tower
- Refresh & Synchronize the database(Step 1):
```shell script
python manage.py makemigrations
python manage.py migrate
```
- Create Superuser(Step 2):
```shell script
python manage.py createsuperuser
```
- Run the website(Step 3):
```shell script
python manage.py runserver
```