# Integration Tests

## Integration Test Scenario

I ran a total of 14 tests.

A temporary database was used for integration testing which will be deleted after the all test cases have been completed.

The overall scenario for integration tests are as follows:

1. Testing Homepage endpoint
2. Testing Sign-up endpoint
3. Testing Login endpoint
4. Testing Login Success
5. Testing Login failure (invalid credentials)
6. Testing Sign-up Success
7. Testing Sign-up failure (Username already exists)
8. Testing Logout endpoint
9. Testing Add Todo
10. Testing Unauthorized Add Todo
11. Testing Update Todo
12. Testing Unauthorized Update Todo
13. Testing Delete Todo
14. Testing Unauthorized Delete Todo

## Test Results

We can run these test with the following command

`coverage run -m pytest "intergatuin_test/integration_test.py`

It will give us the following output

![Integration Tests](/assets/integrationtest_result.png "Integration Tests")