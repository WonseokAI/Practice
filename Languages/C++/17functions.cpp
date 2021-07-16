#include <iostream>
#include <string>

using namespace std;

/*
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
Functions are used to perform certain actions, and they are important for reusing code: 
-> Define the code once, and use it many times.

Create a Function
C++ provides some pre-defined functions, such as main(), which is used to execute code.
But you can also create your own functions to perform certain actions.
To create (often referred to as declare) a function, specify the name of the function, followed by parentheses ():

    void myFunction() {
    // code to be executed
    }

    Example Explained
    - myFunction() is the name of the function
    - void means that the function does not have a return value. You will learn more about return values later in the next chapter
    - inside the function (the body), add code that defines what the function should do

Call a Function
Declared functions are not executed immediately. They are "saved for later use", and will be executed later, when they are called.
To call a function, write the function's name followed by two parentheses () and a semicolon ;

Function Declaration and Definition
A C++ function consist of two parts:
    - Declaration: the function's name, return type, and parameters (if any)
    - Definition: the body of the function (code to be executed)

        void myFunction() { // declaration
            // the body of the function (definition)
        }

Note: If a user-defined function, such as myFunction() is declared after the main() function, an error will occur:
    
    int main() {
        myFunction();
        return 0;
    }

    void myFunction() {
        cout << "I just got executed!";
    }

    // Error

However, it is possible to separate the declaration and the definition of the function - for code optimization.

You will often see C++ programs that have function declaration above main(), and function definition below main(). 
This will make the code better organized and easier to read:

    // Function declaration
    void myFunction();

    // The main method
    int main() {
        myFunction();  // call the function
        return 0;
    }

    // Function definition
        void myFunction() {
        cout << "I just got executed!";
    }

Parameters and Arguments
Information can be passed to functions as a parameter. Parameters act as variables inside the function.

Parameters are specified after the function name, inside the parentheses. 
You can add as many parameters as you want, just separate them with a comma:

    void functionName(parameter1, parameter2, parameter3) {
        // code to be executed
    }

The following example has a function that takes a string called fname as parameter. 
When the function is called, we pass along a first name, which is used inside the function to print the full name:

    void myFunction(string fname) {
        cout << fname << " Refsnes\n";
    }

    int main() {
        myFunction("Liam");
        myFunction("Jenny");
        myFunction("Anja");
        return 0;
    }

    // Liam Refsnes
    // Jenny Refsnes
    // Anja Refsnes
    // When a parameter is passed to the function, it is called an argument. 
    // So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.

Default Parameter Value
You can also use a default parameter value, by using the equals sign (=).
If we call the function without an argument, it uses the default value ("Norway"):

    void myFunction(string country = "Norway") {
        cout << country << "\n";
    }

    int main() {
        myFunction("Sweden");
        myFunction("India");
        myFunction();
        myFunction("USA");
        return 0;
    }

    // Sweden
    // India
    // Norway
    // USA
    // A parameter with a default value, is often known as an "optional parameter". 
    // From the example above, country is an optional parameter and "Norway" is the default value.

Multiple Parameters
Inside the function, you can add as many parameters as you want:

    void myFunction(string fname, int age) {
  cout << fname << " Refsnes. " << age << " years old. \n";
}

    int main() {
        myFunction("Liam", 3);
        myFunction("Jenny", 14);
        myFunction("Anja", 30);
        return 0;
    }

    // Liam Refsnes. 3 years old.
    // Jenny Refsnes. 14 years old.
    // Anja Refsnes. 30 years old.
    // Note that when you are working with multiple parameters, 
    // the function call must have the same number of arguments as there are parameters 
    // ,and the arguments must be passed in the same order.

Return Values
여기부터 시작
*/

void myFunction();
int main(){

    myFunction(); // call the function

    // A function can be called multiple times
    myFunction();
    myFunction();
    myFunction();



    return 0;
}

// Create a function
void myFunction() {
  cout << "I just got executed!";
}