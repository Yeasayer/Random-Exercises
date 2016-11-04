#include <iostream>
using namespace std;

void doPrint()
{
	cout << "In doPrint()" << endl;
}

int main()
{
	cout << "Starting main()" << endl;
	doPrint();
	cout << "Ending main ()" << endl;
	return 0;
}