#include <iostream>
#include <string>
using namespace std;

/*

C++ Conditions and If Statements
C++ supports the usual logical conditions from mathematics:

- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
- Equal to a == b
- Not Equal to: a != b
You can use these conditions to perform different actions for different decisions.

C++ has the following conditional statements:

Use 'if' to specify a block of code to be executed, if a specified condition is true
Use 'else' to specify a block of code to be executed, if the same condition is false
Use 'else' if to specify a new condition to test, if the first condition is false
Use 'switch' to specify many alternative blocks of code to be executed

The if Statement
Use the if statement to specify a block of C++ code to be executed if a condition is true:
    if (condition) {
    // block of code to be executed if the condition is true
    }

Note that if is in lowercase letters. Uppercase letters (If or IF) will generate an error.

The else Statement
Use the else statement to specify a block of code to be executed if the condition is false:

    if (condition) {
    // block of code to be executed if the condition is true
    } else {
    // block of code to be executed if the condition is false
    }

The else if Statement
Use the else if statement to specify a new condition if the first condition is false:

    if (condition1) {
    // block of code to be executed if condition1 is true
    } else if (condition2) {
    // block of code to be executed if the condition1 is false and condition2 is true
    } else {
    // block of code to be executed if the condition1 is false and condition2 is false
    }

Short Hand If...Else (Ternary Operator)
There is also a short-hand if else, which is known as the ternary operator because it consists of three operands. 
It can be used to replace multiple lines of code with a single line. 
It is often used to replace simple if else statements:

    variable = (condition) ? expressionTrue : expressionFalse;


C++ Switch Statements
Use the switch statement to select one of many code blocks to be executed:

    switch(expression) {
    case x:
        // code block
        break;
    case y:
        // code block
        break;
    default:
        // code block
    }
This is how it works:

The switch expression is evaluated once
The value of the expression is compared with the values of each case
If there is a match, the associated block of code is executed
The break and default keywords are optional, and will be described later in this chapter

The break Keyword
When C++ reaches a break keyword, it breaks out of the switch block.
This will stop the execution of more code and case testing inside the block.
When a match is found, and the job is done, it's time for a break. There is no need for more testing.
A break can save a lot of execution time because it "ignores" the execution of all the rest of the code in the switch block.

The default Keyword
The default keyword specifies some code to run if there is no case match
Note: The default keyword must be used as the last statement in the switch, and it does not need a break.
*/


int main(){

    if (20 > 18) {
        cout << "20 is greater than 18";
    }

    int x = 20;
    int y = 18;
    if (x > y) {
        cout << "x is greater than y";
    }

    int time = 20;
    if (time < 18) {
        cout << "Good day.";
    } else {
        cout << "Good evening.";
    }

    int time = 22;
    if (time < 10) {
        cout << "Good morning.";
    } else if (time < 20) {
        cout << "Good day.";
    } else {
        cout << "Good evening.";
    }

    int time = 20;
    string result = (time < 18) ? "Good day." : "Good evening.";
    cout << result;

    int day = 4;
    switch (day) {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    case 3:
        cout << "Wednesday";
        break;
    case 4:
        cout << "Thursday";
        break;
    case 5:
        cout << "Friday";
        break;
    case 6:
        cout << "Saturday";
        break;
    case 7:
        cout << "Sunday";
        break;
    }
    // Outputs "Thursday" (day 4)

    int day = 4;
    switch (day) {
    case 6:
        cout << "Today is Saturday";
        break;
    case 7:
        cout << "Today is Sunday";
        break;
    default:
        cout << "Looking forward to the Weekend";
    }
    // Outputs "Looking forward to the Weekend"

    return 0;
}