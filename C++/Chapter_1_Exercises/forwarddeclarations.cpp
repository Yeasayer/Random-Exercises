#include <iostream>


//We're declaring the function multiply() before we hit main. This is very
//useful and important!
int multiply(int x, int y);

int main()
{
	using namespace std; //You can also put this inside functions.
	cout << "The product of 10 & 12 is...\t" << multiply(10, 12) << 
	"!" << endl;
	return 0;
}

int multiply(int x, int y)
{
	return x * y;
}