#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  cout << "I am learning C++";

  cout << "Hello World! \n";

  cout << "Hello World! \n\n";

  
  return 0;
}

/*
The cout object, together with the << operator, is used to output values/print text
You can add as many cout objects as you want. 
However, note that it does not insert a new line at the end of the output

To insert a new line, you can use the \n character

Another way to insert a new line, is with the endl manipulator

cout << "Hello World!" << endl;

Both \n and endl are used to break lines. However, \n is used more often and is the preferred way.
*/