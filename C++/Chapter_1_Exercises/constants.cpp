#include <iostream>
using namespace std;

const double pi = 3.14159;
const char newline = '\n';
const char tab = '\t';

int main ()
{
	double r=5.0;
	double circle;

	circle = 2 * pi * r;
	cout << "The area of the circle is: " << tab << circle;
	cout << newline;
	return 0;
}