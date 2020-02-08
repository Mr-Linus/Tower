# Tower
A machine learning task management 
platform based on Kubernetes that implements the management of the Machine 
Learning tasks life cycle by Breakfast.
## Features
- View cluster status, tasks.
- Manage Machine Learning tasks.
- Use namespaces for task isolation.
## Overview
- Dashboard
![Dash](https://github.com/NJUPT-ISL/Tower/blob/master/img/dash.png)
- Task Management
![Task](https://github.com/NJUPT-ISL/Tower/blob/master/img/task.png)
- Add Task
![Add](https://github.com/NJUPT-ISL/Tower/blob/master/img/create.png)
- Task Details
![Details](https://github.com/NJUPT-ISL/Tower/blob/master/img/details.png)
- Namespace Management
![NS](https://github.com/NJUPT-ISL/Tower/blob/master/img/ns.png)

## Quick Start 
### Development Test Environment
- Python 3.7 (Recommend)
- Django 2.2 (Necessary)
- Kubernetes 1.15+ (Recommend)

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
