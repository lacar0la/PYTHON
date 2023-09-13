# Testing

Testear es un proceso de evaluación el código que se realiza y es una forma de asegurar que se haga lo que se supone que debe hacerse

> ***Tests can help make good code great***
> 

Automated testing, unit test, integration test, and test-driven development.

## Manual and automated testing

- Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing.
- Using the interpreter to try our code before putting it in a script is another form of manual testing.
- Formal software testing takes us process a step further, codifying tests into its own software and code that can be run to verify that our programs do what we expect them to do. This is called automatic testing.

The goal of automatic testing is to automate the process of checking if the returned value matches the expectations. Instead of us humans running a function over and over with different parameters and checking the results are what we expected them to be, we let the computer do this for us.

## Unit test

Unit tests are used to verify that small isolated parts of a program are correct. Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods. Unit tests help assure the developer that each piece of code does what it's meant to do. An important characteristic of a unit test is **isolation.**

Para crear una prueba unitaria en python es necesario usar el modulo FROM, que permite aislar las funciones en un archivo diferente 

## Unittest

[unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html#basic-example)

This module includes a number of classes and methods that let us easily create unit tests for our code. The first thing we'll do is import the unit test module we'll need for testing.

The unit test module provides a test case class with a bunch of testing methods ready to use. 

To access this functionality, we create our own class by inherits from test case, thus inheriting all those testing methods.

 So we're going to write our own test rearrange class that inherits from test case.  We need to include the class that we want to inherit from in the parentheses.

```python
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
def test_basic(self):
	testcase = "lovelace, Ada"
	expected = "Ada Lovelace"
	self.assertEqual(rearrange_name(testcase), expected)
```

We then use the assertEqual method provided to us by the test case class we inherited from to verify that what we expected is exactly what we got.he assertEqual method basically says both of my arguments are equal. If that statement's true, then the test passes. If it's false, the test fails and an error is printed to the screen when the test is run. Okay, we've got our first unit test. So how can we run it? In the main part of our program, we'll call the unittest.main() function, which will run the test for us.

**Edge cases** are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.

![Screen Shot 2023-09-12 at 3.56.01 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b2b7fb9e-15e2-4186-9c86-ff6fa417b245/67945bf1-03dd-4755-bb25-b95120d88bc2/Screen_Shot_2023-09-12_at_3.56.01_PM.png)

## white-box test or a black-box test

- White-box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of the software being tested to construct the test cases. With a white-box test, the test creator knows how the code works and can write test cases that use the understanding to make sure that everything is performing the way it's expected to.
- In black-box testing, the software being tested is treated like an opaque box. In other words, the tester doesn't know the internals of how the software works. Black-box tests are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it.

## Other type of test…

- **integration tests** verify that the interactions between the different pieces of code in integrated environments are working the way we expect them to.
- **test environment** runs a test version of our software that we're trying to verify.
- **Smoke test** get their name from a concept that comes from testing hardware equipment. Plug in the given piece of hardware and see if smoke starts coming out of it. When writing software smoke test serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions like, does the program run? These tests are usually run before more refined testing takes place.
- **load tests:** These tests verify that the system behaves well when it's under significant load. To actually perform these tests will need to generate traffic to our application simulating typical usage of the service.
- **Test driven development** calls for creating the test before writing the code. Writing a test first helps you think about the ways your program could fail and break which can lead to some valuable insights and even change the approach you take for the better.

### Raise

Esta es la palabra clave para definir errores en python y debe ir acompañado por el tipo de error, por ejemplo ValueError permite establecer los errores asociados al tipo de valores ingresados al programa.

[8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)

### Assert

Esta palabra clave intenta verificar que una expresión condicional es verdadera, y si es falsa, genera un error de aserción con el mensaje indicado. Podemos añadirlos en cualquier momento donde queramos asegurarnos de que las variables contengan los valores y tipos que deberían o cuando pensamos que eso es algo que no debería suceder está sucediendo.

Como regla general, deberíamos usar raise para verificar las condiciones que esperamos que ocurran durante la ejecución normal de nuestro código y afirmar para verificar situaciones que no se esperan, pero que podrían causar que nuestro código se comporte mal.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b2b7fb9e-15e2-4186-9c86-ff6fa417b245/6f14a8e9-d189-455e-bd49-e6469f8420ca/Untitled.png)

### Método assert-raise

> The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.
> 

[8. Errors and Exceptions — Python 2.7.18 documentation](https://docs.python.org/2/tutorial/errors.html#handling-exceptions)

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

## **Errores de validación**

A continuación, se presenta el código para un error de validación. La función RemoveValue elimina un número de una lista de números. ¿Qué sucede si el número que se desea eliminar no se encuentra en la lista?, deberá aparecer un error. En el código lo que se hace es establecer el tipo de error encontrado. 

```python
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError('Value must be in the given list')
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))
```

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-17c39a180301> in <module>
      6     return my_list
      7 
----> 8 print(RemoveValue(27))

<ipython-input-5-17c39a180301> in RemoveValue(myVal)
      1 def RemoveValue(myVal):
      2     if myVal not in my_list:
----> 3         raise ValueError('Value must be in the given list')
      4     else:
      5         my_list.remove(myVal)

ValueError: Value must be in the given list
```

Como puede verse, el ValueError ahora está especificado.
