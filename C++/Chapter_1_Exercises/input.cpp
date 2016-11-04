#include <iostream>
#include <string>
using namespace std;

int main ()
{
	string mystr;
	cout << "What's your name?\t";
	getline (cin, mystr);
	cout << "Hiya" << mystr << ".\n";
	cout << "What's your favorite game?\t";
	getline (cin, mystr);
	cout << mystr << " is my favorite game too!\n";
	return 0;
}