# Sofware testing & CI/CD Pipeline for Todo App


## Introduction

This project is part of asoftware testing course in INSAT (National Institure of Applied Sciences And Technology) integrated with it is a CI/CD pipeline made with Github Actions and deployed in AWS EC2.

## How does the app work?
1. First when you open the app you will be greeted with a login screen as shown in the image below

![Login Screen](/assets/login.png "Login Screen")

2. Enter your credentials and press the submit button and if every thing works you will be redirected to the home page.

If you don't have an account already press the sign up link at the bottom of the form.

You will be greeted with a similar screen where you can enter your credentials(username and password) and account will be registered and you will be redirected to the homepage.

![Signup Screen](/assets/signup.png "Signup Screen")

3. From here on out, you can add a todo; just simply fill the input with whatever you want to mark as todo and it will be added in the todo list and marked as incomplete.

![Homepage](/assets/todo_list.png "Homepage")

4. You can either delete a todo list or update the todo list to mark it as complete or vice versa. You can also still add other todos.



## Tests

Four type of tests have been implemented in this app:

1. Unit Tests
2. Integration Tests
3. E2E(End-to-End or system) Tests
4. UAT (User Acceptance Tests)

Check the README.md file for each test to check the test cases and the code coverage

## CI/CD (Devops)
The CI/CD Pipeline is as follows: 

1. Run all tests (Unit, Integration and E2E tests)
2. Build the Docker image and push it to Docker Hub
3. Connect to running AWS EC2 instance, remove any existing running container and pull the new image and run a new container from it

You can find the steps detailed in the [devops.yml file](https://github.com/YoussefJJ/software-testing-devops/blob/main/.github/workflows/devops.yaml)

The overall Pipeline Schema is shown in Github Actions as follows

![CI/CD Pipeline](/assets/cicd.png "CI/CD Pipeline")

## Where to find the app?

If the EC2 instance is still running, you can use the simple app in [this link](http:\\54.249.164.48:5000)

