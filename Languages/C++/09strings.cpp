#include <iostream>
#include <string>
using namespace std;

/*

C++ Strings
Strings are used for storing text.
A string variable contains a collection of characters surrounded by double quotes

String Concatenation
The + operator can be used between strings to add them together to make a new string. This is called concatenation

Append
A string in C++ is actually an object, which contain functions that can perform certain operations on strings.

It is up to you whether you want to use + or append(). 
The major difference between the two, is that the append() function is much faster. 
However, for testing and such, it might be easier to just use +.


WARNING!
C++ uses the + operator for both addition and concatenation.
Numbers are added. Strings are concatenated.
If you try to add a number to a string, an error occurs

String Length
To get the length of a string, use the length() function

Access Strings
You can access the characters in a string by referring to its index number inside square brackets [].

Change String Characters
To change the value of a specific character in a string, refer to the index number, and use single quotes

User Input Strings
It is possible to use the extraction operator >> on cin to display a string entered by a user
However, cin considers a space (whitespace, tabs, etc) as a terminating character
, which means that it can only display a single word (even if you type many words)
That's why, when working with strings, we often use the getline() function to read a line of text. 
It takes cin as the first parameter, and the string variable as second

Omitting Namespace
You might see some C++ programs that runs without the standard namespace library. 
The 'using namespace std line' can be omitted and replaced with the std keyword, 
followed by the :: operator for string (and cout) objects:
    #include <iostream>
    #include <string>

    int main() {
    std::string greeting = "Hello";
    std::cout << greeting;
    return 0;
    }
It is up to you if you want to include the standard namespace library or not.
*/


int main(){

    // Create a string variable
    string greeting = "Hello";

    string firstName = "John ";
    string lastName = "Doe";
    string fullName = firstName + lastName;
    cout << fullName;

// In the example above, we added a space after firstName to create a space between John and Doe on output. 
// However, you could also add a space with quotes (" " or ' ')

    string firstName = "John";
    string lastName = "Doe";
    string fullName = firstName + " " + lastName;
    cout << fullName;

    string firstName = "John ";
    string lastName = "Doe";
    string fullName = firstName.append(lastName);
    cout << fullName;

    string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    cout << "The length of the txt string is: " << txt.length();

// Tip: You might see some C++ programs that use the size() function to get the length of a string.
// This is just an alias of length(). It is completely up to you if you want to use length() or size()

    string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    cout << "The length of the txt string is: " << txt.size();

    string myString = "Hello";
    cout << myString[0];        // Outputs H
// Note: String indexes start with 0: [0] is the first character. [1] is the second character, etc.

    string myString = "Hello";
    cout << myString[1];        // Outputs e

    string myString = "Hello";
    myString[0] = 'J';
    cout << myString;           // Outputs Jello instead of Hello

    string firstName;
    cout << "Type your first name: ";
    cin >> firstName; // get user input from the keyboard
    cout << "Your name is: " << firstName;

    string fullName;
    cout << "Type your full name: ";
    getline (cin, fullName);
    cout << "Your name is: " << fullName;

    return 0;
}