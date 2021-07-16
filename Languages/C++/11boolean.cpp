#include <iostream>
#include <string>
using namespace std;


/*
C++ Booleans
Very often, in programming, you will need a data type that can only have one of two values, like:

- YES / NO
- ON / OFF
- TRUE / FALSE

For this, C++ has a bool data type, which can take the values true (1) or false (0).

Boolean Values
A boolean variable is declared with the bool keyword and can only take the values true or false

Boolean Expression
A Boolean expression is a C++ expression that returns a boolean value: 1 (true) or 0 (false).
You can use a comparison operator, such as the greater than (>) operator to find out if an expression (or a variable) is true


*/



int main(){

    bool isCodingFun = true;
    bool isFishTasty = false;
    cout << isCodingFun;  // Outputs 1 (true)
    cout << isFishTasty;  // Outputs 0 (false)

// From the example above, you can read that a true value returns 1, and false returns 0.
// However, it is more common to return boolean values from boolean expressions (see next page).

    int x = 10;
    int y = 9;
    cout << (x > y); // returns 1 (true), because 10 is higher than 9

    cout << (10 > 9);

    int x = 10;
    cout << (x == 10);  // returns 1 (true), because the value of x is equal to 10

    cout << (10 == 15);  // returns 0 (false), because 10 is not equal to 15

    
    return 0;
}