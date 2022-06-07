# Sofware testing & CI/CD Pipeline for Todo App


## Introduction

This project is part of asoftware testing course in INSAT (National Institure of Applied Sciences And Technology) integrated with it is a CI/CD pipeline made with Github Actions and deployed in AWS EC2.

## How does the app work?
1. First when you open the app you will be greeted with a login screen as shown in the image below

![Login Screen](/assets/login_screen.png "Login Screen")

2. Enter your credentials and press the submit button and if every thing works you will be redirected to the home page.

If you don't have an account already press the sign up link at the bottom of the form.

You will be greeted with a similar screen where you can enter your credentials(username and password) and account will be registered and you will be redirected to the homepage.

![Signup Screen](/assets/signup.png "Signup Screen")

3. From here on out, you can add a todo; just simply fill the input with whatever you want to mark as todo and it will be added in the todo list and marked as incomplete.

![Homepage](/assets/todo_list.png "Homepage")

4. You can either delete a todo list or update the todo list to mark it as complete or vice versa. You can also still add other todos.



## Tests

Four type of tests have been implemented in this app:

1. [Unit Tests](https://github.com/YoussefJJ/software-testing-devops/tree/main/unit%20test)
2. [Integration Tests](https://github.com/YoussefJJ/software-testing-devops/tree/main/intergation_test)
3. [E2E (End-to-End or system) Tests](https://github.com/YoussefJJ/software-testing-devops/tree/main/e2e)
4. [UAT (User Acceptance Tests)](https://github.com/YoussefJJ/software-testing-devops/tree/main/UAT%20test)

Check the README.md file for each test to check the test cases and the code coverage

## CI/CD (Devops)
The CI/CD Pipeline is as follows:

### First Workflow

1. Run all tests (Unit, Integration and E2E tests)
2. Build the Docker image and push it to Docker Hub
3. Deploy App to an Amazon Elastic Compute Cloud container:
    - Launch AWS EC2 instance
    - Remove any existing running container
    - Pull the new Docker image
    - Run a new container from the newly pulled docker image

You can find the steps detailed in the [devops.yml](https://github.com/YoussefJJ/software-testing-devops/blob/main/.github/workflows/devops.yaml) file.

The overall Pipeline Schema is shown in Github Actions as follows

![CI/CD Pipeline](/assets/cicd.png "CI/CD Pipeline")

### Second Workflow

The CI phase is pretty much the same as the first workflow. The deployment process is different as we use AWS ECS to deploy our app

You can find the steps detailed in the [devops-ecs.yml](https://github.com/YoussefJJ/software-testing-devops/blob/main/.github/workflows/devops-ecs.yaml) file.


## Where to find the app?

If the EC2 instance is still running, you can use the simple app by clicking [this link](http://54.249.164.48:5000/)

