#include <iostream>
#include <string>
using namespace std;

/*
C++ Operators
Operators are used to perform operations on variables and values.

C++ divides the operators into the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Bitwise operators

Arithmetic Operators
Arithmetic operators are used to perform common mathematical operations:
+	Addition	Adds together two values	x + y	
-	Subtraction	Subtracts one value from another	x - y	
*	Multiplication	Multiplies two values	x * y	
/	Division	Divides one value by another	x / y	
%	Modulus	Returns the division remainder	x % y	
++	Increment	Increases the value of a variable by 1	++x	
--	Decrement	Decreases the value of a variable by 1	--x

Assignment Operators
Assignment operators are used to assign values to variables.
The addition assignment operator (+=) adds a value to a variable
These are used in the similar way: =, +=, -=, *=, /=, %=, &=, |=, ^=, >>=, <<=, 

Comparison Operators
Comparison operators are used to compare two values.
Note: The return value of a comparison is either true (1) or false (0).
: ==, !=, >, <, >=, <=

Logical Operators
Logical operators are used to determine the logic between variables or values
- && 	: Logical and	: Returns true if both statements are true	                : x < 5 &&  x < 10	
- || 	: Logical or	: Returns true if one of the statements is true	            : x < 5 || x < 4	
- !	    : Logical not	: Reverse the result, returns false if the result is true	: !(x < 5 && x < 10)
*/



int main(){

    int x = 100 + 50;

    int sum1 = 100 + 50;        // 150 (100 + 50)
    int sum2 = sum1 + 250;      // 400 (150 + 250)
    int sum3 = sum2 + sum2;     // 800 (400 + 400)

    int x = 10;
    x += 5;

    int x = 5;
    int y = 3;
    cout << (x > y); // returns 1 (true) because 5 is greater than 3

    return 0;
}