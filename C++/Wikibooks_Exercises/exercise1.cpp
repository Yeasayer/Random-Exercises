#include <iostream>
using namespace std;

int main()
{
	int myinput;
	cout << "Pick a number:\t" << endl;
	cin >> myinput;
	if ((myinput < 56) || (myinput > 78))
	{
		cout << "That's not right" << endl;
		main();
	}
	else
	{
		cout << "YOU WIN!" << endl;
		return 0;
	}
}