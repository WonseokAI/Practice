// Include the cmath library
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

/*
C++ Math
C++ has many functions that allows you to perform mathematical tasks on numbers.

Max and min
The max(x,y) function can be used to find the highest value of x and y
The min(x,y) function can be used to find the lowest value of x and y

C++ <cmath> Header
Other functions, such as sqrt (square root), round (rounds a number) and log (natural logarithm), 
can be found in the <cmath> header file

*/

int main(){

    cout << max(5, 10);
    cout << min(5, 10);

    cout << sqrt(64);
    cout << round(2.6);
    cout << log(2);
    return 0;
}