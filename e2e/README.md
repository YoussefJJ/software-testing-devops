# End-to-End Testing

## End-to-End Tests Scenario

A total of 6 e2e tests were considered for this app that represent the following scenario:

1. Registering User
2. Logging in User
3. Logging out User
4. Add Todo
5. Update Todo (mark it as complete)
6. Delete Todo

Selenium was used to run the end-to-end tests but it needed a lot of tinkering not only to make it work locally, but also when ran as a workflow job in Github Actions.

## Test Results
To run the system tests, execute the following command:
`coverage run -m pytest e2e/e2e_test.py`

After running the tests, the following will be outputted to the console:

![End-to-End Tests](/assets/e2e_test_results.png "End-to-End Tests")

## Test Coverage
We can check the coverage by typing the following command:

`coverage report`

![End-to-End Test Coverage](/assets/e2e_coverage.png "End-to-End Test Coverage")