# 0x03. Unittests and Integration Tests

## Unittest
The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

## unittest.mock — mock object library
unittest.mock is a Python library designed specifically for testing purposes. It provides a convenient way to replace components of your system under test with mock objects, allowing you to make assertions about their usage.

The library includes a core Mock class, which eliminates the need to create multiple stubs throughout your test suite. With Mock, you can perform actions and then verify which methods and attributes were used, along with the arguments they were called with. You can also define return values and set necessary attributes in a straightforward manner.

Additionally, mock offers a patch() decorator, which simplifies the process of patching module and class level attributes within the scope of a test. It also provides the sentinel feature for creating unique objects. The included quick guide provides examples showcasing the usage of Mock, MagicMock, and patch().

It's important to note that Mock is designed to be used with the unittest framework and follows the 'action -> assertion' pattern, as opposed to the 'record -> replay' pattern used by other mocking frameworks.

For Python versions prior to the availability of unittest.mock, a backport called mock can be found on PyPI.

## Parametrized Testing
Parametrized testing is a technique that allows you to write concise and reusable test cases by providing test data as parameters. It enables you to easily test your code against various inputs and expected outputs without duplicating test code.

## Memoization
Memoization is a technique used to optimize the performance of functions by caching their results for specific input parameters. By storing previously computed values, subsequent function calls with the same inputs can be returned from the cache, avoiding redundant computations.
