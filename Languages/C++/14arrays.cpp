#include <iostream>
#include <string>

using namespace std;

/*
C++ Arrays
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

To declare an array, 
define the variable type, 
specify the name of the array followed by square brackets and specify the number of elements it should store:
    
    string cars[4];

We have now declared a variable that holds an array of four strings. 
To insert values to it, we can use an array literal - place the values in a comma-separated list, inside curly braces:

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};

To create an array of three integers, you could write:

    int myNum[3] = {10, 20, 30};

Access the Elements of an Array
You access an array element by referring to the index number.
Note: Array indexes start with 0: [0] is the first element. [1] is the second element, etc.

Change an Array Element
To change the value of a specific element, refer to the index number:
    
    cars[0] = "Opel";

Loop Through an Array
You can loop through the array elements with the for loop.

Omit Array Size
You don't have to specify the size of the array. But if you don't, it will only be as big as the elements that are inserted into it:

    string cars[] = {"Volvo", "BMW", "Ford"}; // size of array is always 3

his is completely fine. However, the problem arise if you want extra space for future elements. 
Then you have to overwrite the existing values:

    string cars[] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};

If you specify the size however, the array will reserve the extra space:
    string cars[5] = {"Volvo", "BMW", "Ford"}; 
    // size of array is 5, even though it's only three elements inside it

Now you can add a fourth and fifth element without overwriting the others:

    cars[3] = "Mazda";
    cars[4] = "Tesla";

Omit Elements on Declaration
It is also possible to declare an array without specifying the elements on declaration, and add them later:

    string cars[5];
    cars[0] = "Volvo";
    cars[1] = "BMW";
*/

int main(){

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
    cout << cars[0];
    // Outputs Volvo

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
    cars[0] = "Opel";
    cout << cars[0];
    // Now outputs Opel instead of Volvo

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
    for(int i = 0; i < 4; i++) {
        cout << cars[i] << "\n";
    }

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
    for(int i = 0; i < 4; i++) {
        cout << i << ": " << cars[i] << "\n";
    }

    return 0;
}