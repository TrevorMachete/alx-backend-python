
# Project: 0x03 - Unittests and Integration Tests

This project focuses on writing unit tests and integration tests for various components of your application. By following the guidelines below, you'll ensure that your code is robust, reliable, and well-tested.

## Introduction

Before diving into the specific tasks, make sure you're familiar with the following functions and classes:

- `utils.access_nested_map`: Understand its purpose and play with it in the Python console to ensure comprehension.
- `utils.get_json`: Familiarize yourself with this function, which makes HTTP requests. We'll mock it later to avoid actual external calls.
- `client.GithubOrgClient`: This class interacts with the GitHub API. We'll test its methods using mocks and parameterization.

## Unit Tests

### Task 1: Parameterize a Unit Test

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`. Implement the `test_access_nested_map` method to verify that `utils.access_nested_map` returns the expected results. Decorate this method with `@parameterized.expand` to test it with various inputs.

### Task 2: Mock HTTP Calls

Define the `TestGetJson(unittest.TestCase)` class. Implement the `test_get_json` method to test that `utils.get_json` returns the expected result. Use `unittest.mock.patch` to mock the actual HTTP call and ensure it returns a known payload.

### Task 3: Parameterize and Patch

Learn about memoization and explore the `utils.memoize` decorator. Create the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method. Inside this method, define a class to test memoization behavior.

### Task 4: Parameterize and Patch as Decorators

Study the `client.GithubOrgClient` class. In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class. Implement the `test_org` method to verify that `GithubOrgClient.org` returns the correct value. Use `@patch` as a decorator to ensure `get_json` is called once with the expected argument but not executed. Parametrize the test with a couple of organization examples (e.g., "google" and "abc").

### Task 5: Mocking a Property

Memoization turns methods into properties. Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`. Use `patch` as a context manager to mock `GithubOrgClient.org` and return a known payload. Verify that the result of `_public_repos_url` matches the expected value based on the mocked payload.

### Task 6: More Patching

Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`. Mock `get_json` using `@patch` and return a payload of your choice. Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value. Verify that the list of repos matches your expectations and that the mocked property and `get_json` were called once.

### Task 7: Parameterize

Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`. Parametrize the test with different inputs.

### Task 8: Integration Test: Fixtures

Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class. Implement `setUpClass` and `tearDownClass` methods. Use `@parameterized_class` to parameterize the class with fixtures from `fixtures.py`.

### Task 9: Integration Tests (Advanced)

Implement the `test_public_repos` method to test `GithubOrgClient.public_repos`. Ensure that the method returns the expected results based on the fixtures.
