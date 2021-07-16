#include <iostream>
using namespace std;
    
// Include the string library
#include <string>

/*
Basic Data Types
The data type specifies the size and type of information the variable will store:

int	    : 4 bytes	Stores whole numbers, without decimals
float	: 4 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 7 decimal digits
double	: 8 bytes	Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits
boolean	: 1 byte	Stores true or false values
char	: 1 byte	Stores a single character/letter/number, or ASCII values

Numeric Types
Use int when you need to store a whole number without decimals, like 35 or 1000, 
and float or double when you need a floating point number (with decimals), like 9.99 or 3.14515.

float vs. double
The precision of a floating point value indicates how many digits the value can have after the decimal point. 
The precision of float is only six or seven decimal digits, while double variables have a precision of about 15 digits. 
Therefore it is safer to use double for most calculations.

Scientific Numbers
A floating point number can also be a scientific number with an "e" to indicate the power of 10

Boolean Types
A boolean data type is declared with the bool keyword and can only take the values true or false. 
When the value is returned, true = 1 and false = 0.

Character Types
The char data type is used to store a single character. The character must be surrounded by single quotes, like 'A' or 'c'
Alternatively, you can use ASCII values to display certain characters

String Types
The string type is used to store a sequence of characters (text). 
This is not a built-in type, but it behaves like one in its most basic usage. String values must be surrounded by double quotes
To use strings, you must include an additional header file in the source code, the <string> library
*/

int main() {

    int myNum = 5;               // Integer (whole number)
    float myFloatNum = 5.99;     // Floating point number
    double myDoubleNum = 9.98;   // Floating point number
    char myLetter = 'D';         // Character
    bool myBoolean = true;       // Boolean
    string myText = "Hello";     // String

    int myNum = 1000;
    cout << myNum;

    float myNum = 5.75;
    cout << myNum;

    double myNum = 19.99;
    cout << myNum;

    float f1 = 35e3;
    double d1 = 12E4;
    cout << f1;
    cout << d1;

    bool isCodingFun = true;
    bool isFishTasty = false;
    cout << isCodingFun;  // Outputs 1 (true)
    cout << isFishTasty;  // Outputs 0 (false)

    char myGrade = 'B';
    cout << myGrade;
    char a = 65, b = 66, c = 67;
    cout << a;
    cout << b;
    cout << c;

    string greeting = "Hello";
    cout << greeting;

    // Create a string variable
    string greeting = "Hello";

    // Output string value
    cout << greeting;

    return 0;
}