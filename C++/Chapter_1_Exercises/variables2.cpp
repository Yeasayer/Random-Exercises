#include <iostream>
using namespace std;

int main ()
{
	int a=5;
	int b(3);
	int c(2);
	int result;

	a = a + b;
	result = a - c;
	
	cout << "The result is " << result << endl;
	cout << "Yay, it worked! ^_^" << endl;
	return 0;
}
