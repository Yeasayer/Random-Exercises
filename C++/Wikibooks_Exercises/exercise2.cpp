#include <iostream>
using namespace std;

int coolforloop()
{
	int userinput;
	for (int num = 8; num <= 23; num = num + 1)
	{
		cin >> userinput;
		if (userinput == num)
		{
			if (num + 1 < 24)
			{
			cout << "Great Job! Now Type " << num + 1 << endl;
			}
		}
		else
		{
			cout << "OOPS! You have to start over!" << endl;
			coolforloop();
		}
	}
	cout << "Great Job! See Ya' Later!" << endl;
	return 0;
}

int main()
{
	int userinput;
	cout << "You're going to type every number from 8 to 23\t" << endl;
	cout << "Let's go!" << endl;
	coolforloop();
	return 0;
}