#include <iostream>
#include <string>

using namespace std;

/*
C++ Loops
Loops can execute a block of code as long as a specified condition is reached.
Loops are handy because they save time, reduce errors, and they make code more readable.

C++ While Loop
The while loop loops through a block of code as long as a specified condition is true:
    while (condition) {
    // code block to be executed
    }

The Do/While Loop
The do/while loop is a variant of the while loop. 
This loop will execute the code block once, before checking if the condition is true, 
then it will repeat the loop as long as the condition is true:

    do {
    // code block to be executed
    }
    while (condition);

C++ For Loop
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop:
    for (statement 1; statement 2; statement 3) {
    // code block to be executed
    }

Statement 1 is executed (one time) before the execution of the code block.
Statement 2 defines the condition for executing the code block.
Statement 3 is executed (every time) after the code block has been executed.

C++ Break
You have already seen the break statement used in an earlier chapter of this tutorial. 
It was used to "jump out" of a switch statement.
The break statement can also be used to jump out of a loop.

C++ Continue
The continue statement breaks one iteration (in the loop), 
if a specified condition occurs, and continues with the next iteration in the loop.
*/


int main(){

    // In the example below, the code in the loop will run, over and over again, as long as a variable (i) is less than 5:
    int i = 0;
        while (i < 5) {
        cout << i << "\n";
        i++;
    }
    // Note: Do not forget to increase the variable used in the condition, otherwise the loop will never end!

    int i = 0;
    do {
        cout << i << "\n";
        i++;
    }
    while (i < 5);
    // Do not forget to increase the variable used in the condition, otherwise the loop will never end!

    for (int i = 0; i < 5; i++) {
        cout << i << "\n";
    }

    for (int i = 0; i <= 10; i = i + 2) {
        cout << i << "\n";
    }

    for (int i = 0; i < 10; i++) {
        if (i == 4) {
            break;
        }
        cout << i << "\n";
    }

    for (int i = 0; i < 10; i++) {
        if (i == 4) {
            continue;
        }
        cout << i << "\n";
    }

    int i = 0;
    while (i < 10) {
        cout << i << "\n";
        i++;
        if (i == 4) {
            break;
        }
    }

    int i = 0;
    while (i < 10) {
        if (i == 4) {
            i++;
            continue;
        }
        cout << i << "\n";
        i++;
    }
    return 0;
}