#include <iostream>     // a header file library that lets us work with input and output objects, 
                        // Header files add functionality to C++ programs.

using namespace std;    // means that we can use names for objects and variables from the standard library

int main() {
  cout << "Hello World!"; // cout is an object used together with the insertion operator (<<) to output/print text.
  return 0;
}

/*
- main() : this is called a function. Any code inside its curly brackets {} will be executed.
- Every C++ statement ends with a semicolon(;)
- Omitting Namespace
You might see some C++ programs that runs without the standard namespace library. 
The using namespace std line can be omitted and replaced with the std keyword, followed by the :: operator for some objects:

#include <iostream>

int main() {
  std::cout << "Hello World!";
  return 0;
}

*/