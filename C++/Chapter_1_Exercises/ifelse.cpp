//Congrats on your first program dude!!!

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int getValue()
{
	cout << "Type in 100!";
	int a;
	std::cin >> a;
	return a;
}

int main()
{
	int x = getValue();
	string mystr;

	if (x == 100)
	{
		cout << x << " equals 100!\n";
		return 0;
	}
	else
	{
		cout << x << " does not equal 100!\n";
		main();
	}
}
