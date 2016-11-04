#include <iostream>
using namespace std;

int add(int x, int y)
{
	return x + y;
}
int multiply(int z, int w)
{
	return z * w;
}

int main()
{
	cout << add(4,5) << endl;
	cout << multiply(2,3) << endl;

	//You can pass values of expressions.
	cout << add(1+2,3*4) << endl;

	//You can also pass variables, which is awesome!
	int a = 5;
	cout << add(a,a) << endl;

	//You can also do this kooky thing and pass functions as parameters.
	cout << add(1,multiply(2,3)) << endl;
	cout << add(1, add(2,3)) << endl;

	//Personal test
	cout << add(multiply(42,42),add(multiply(2,2),multiply(8,7))) << endl;
	cout << "That really was kooky!" << endl;
	return 0;
}