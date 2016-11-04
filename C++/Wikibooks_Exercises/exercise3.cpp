#include <iostream>
using namespace std;

int coolwhileloop(int startingnum)
{
	int mynum;
	while (startingnum < 24)
	{
		cout << "Type the number: " << startingnum << endl;
		cin >> mynum;
		if (mynum == startingnum)
		{
			cout << "Great Job!" << endl;
			startingnum = startingnum + 1;
		}
		else
		{
			cout << "Whoops! You didn't type the number " << startingnum << endl; 
		}
	}
	cout << "You did it!" << endl;
	return 0;
}

int main()
{
	int startingnum = 8;
	cout << "Type the numbers 8 through 23" << endl;
	coolwhileloop(startingnum);
	return 0;
}