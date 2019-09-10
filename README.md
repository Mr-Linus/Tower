# Tower
A Machine Learning Task Management Platform Based on Kubernetes.
## Features
- View cluster status, tasks.
- Manage deep learning tasks.
- Use namespaces for task isolation.
## Overview
- Dashboard
![Dash](https://github.com/NJUPT-ISL/Tower/blob/master/images/dash.png)
- Task Management
![Task](https://github.com/NJUPT-ISL/Tower/blob/master/images/task.png)
- Add Task
![Add](https://github.com/NJUPT-ISL/Tower/blob/master/images/create.png)
- Task Details
![Details](https://github.com/NJUPT-ISL/Tower/blob/master/images/details.png)
- Namespace Management
![NS](https://github.com/NJUPT-ISL/Tower/blob/master/images/ns.png)

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
