# Digimons-BE

## Project: Digimons-BE

### Author: Amani M AL-Zoubi
 

### Links and Resources

- [Django REST framework](https://www.django-rest-framework.org/)

### Setup

- use python version 3.10.7


#### How to initialize/run your application (where applicable)
- clone Repo 
- Create environment `python -m venv .venv`
- active env `source .venv/bin/activate`
- install requirement `pip install requirements.txt `
- make migrations and migrate  `python manage.py makemigrations`
    `python manage.py migrate`
- run server `python manage.py runserver`
- Use `http://127.0.0.1:<PORT>/api/v1/favDigimons/` to get favDigimons API 
- for specific Card add it's id to your path like `http://127.0.0.1:<PORT>/api/v1/favDigimons/1`

### Authentication and Permission for models


| API end-points        | HTTP Method   | Authentication  | Permission  | Result                                       |
|---------------------- |-------------  |------------   |------------  |------------------------------------------     |
| /favDigimons                 | GET           | AnyOne          | AnyOne        |  view all the favDigimons that are retrieved                  |
| /favDigimons                 | POST          | AnyOne          | AnyOne         | Create new favDigimons                                |
| /favDigimons/{favDigimons_pk}       | GET           | AnyOne          | AnyOne         | Retrieve details of a particular favDigimons         |
| /favDigimons/{favDigimons_pk}       | PUT           | AnyOne          | AnyOne         | Update a particular favDigimons's info               |
| /favDigimons/{favDigimons_pk}       | DELETE        | AnyOne          | AnyOne         | Delete a particular favDigimons's details from DB    |
