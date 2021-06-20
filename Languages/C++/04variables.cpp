/*
Variables are containers for storing data values.

In C++, there are different types of variables (defined with different keywords), for example:

- int - stores integers (whole numbers), without decimals, such as 123 or -123
- double - stores floating point numbers, with decimals, such as 19.99 or -19.99
- char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
- string - stores text, such as "Hello World". String values are surrounded by double quotes
- bool - stores values with two states: true or false

To create a variable, you must specify the type and assign it a value

> type variable = value;
: Where type is one of C++ types (such as int), and variable is the name of the variable (such as x or myName). 
The equal sign is used to assign values to the variable.

You can also declare a variable without assigning the value, and assign the value later

Note that if you assign a new value to an existing variable, it will overwrite the previous value

The cout object is used together with the << operator to display variables.
To combine both text and a variable, separate them with the << operator

All C++ variables must be identified with unique names.
These unique names are called identifiers.
Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).
Note: It is recommended to use descriptive names in order to create understandable and maintainable code

The general rules for constructing names for variables (unique identifiers) are:
- Names can contain letters, digits and underscores
- Names must begin with a letter or an underscore (_)
- Names are case sensitive (myVar and myvar are different variables)
- Names cannot contain whitespaces or special characters like !, #, %, etc.
- Reserved words (like C++ keywords, such as int) cannot be used as names
*/

#include <iostream>
using namespace std;

int main(){

    //int myNum = 15;

    int myNum;
    myNum = 15;
    cout << myNum;

    int myAge = 35;
    cout << "I am " << myAge << " years old.";
    
    // To add a variable to another variable, you can use the + operator
    int x = 5;
    int y = 6;
    int sum = x + y;
    cout << sum;

    // To declare more than one variable of the same type, use a comma-separated list
    int x = 5, y = 6, z = 50;
    cout << x + y + z;

    return 0;
}