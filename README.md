# English Instructions

# LITReview: Minimum viable product for a django based application

SoftAPI is a django rest API that has to be executed locally for demonstration purpose.
It allow testing of the functionalities required to be developped in the context of openclassroom python programmer formation.
With it, you can create projects, issues linked to project, comments linked to issues.

## Installation

This locally-executable django application can be executed from [http://localhost:8000/api](http://localhost:8000/api) using the following steps.

Installation and execution using venv and pip

1. Clone this repository using `$ git clone https://github.com/Yohz78/Projet_10`
2. Move to the LITReview root folder with `$ cd Projet_10\backend`
3. Create a virtual environment for the project with `$ py -m venv env` on windows or `$ python3 -m venv env` on macos or linux.
4. Activate the virtual environment with `$ env\Scripts\activate` on windows or `$ source env/bin/activate` on macos or linux.
5. Install project dependencies with `$ pip install -r requirements.txt`
6. Run the server with `$ python manage.py runserver`

When the server is running after step of the procedure, the API can be accessed at [http://localhost:8000/api](http://localhost:8000/api)

Steps 1-5 are only required for initial installation. For subsequent launches of the Django app, you only have to execute step 6 from the root folder of the project.

## Usage

The API is used for project issues management. It is a secure environnement in which you can create project, issues on a specific project, comments on a specific issues. Permissions has been setup and only owner can update or destroy an instance of a model. Other user will be able to read instance if they are part of a contributor object linking their ID to a project_id. Contributors can create issues and comments for a given project environnement. They can also read instance of models linked to that specific project.

First, a user should register using the signup URL.

Then, he should log in and save his token. This authentication token allow securization of the API with token authentication. It should be added in the header of any request except for login and signup. The API will then adapt user permission depending on his profile : Owner of an item or not, contributor of a project or not.

Please find the extensive documentation of the API and all its endpoints here [https://documenter.getpostman.com/view/23138448/VUxRPmDz](https://documenter.getpostman.com/view/23138448/VUxRPmDz)
