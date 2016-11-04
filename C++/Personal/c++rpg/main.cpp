#include <iostream>
using namespace std;

int choice();

int main()
{
	string soda [] = {"Coke","Water","Sprite","Sweet Tea","Lemonade"};
	int count = sizeof(soda)/sizeof(soda[0]);
	cout << "Pick a soda! Your choices are:" << endl;
	for (int i = 0; i < count; ++i)
	{
		cout << i+1 << ":\t" << soda[i] << endl;
	}
	while (pick < 0 || pick > 5)
	{
		int pick = choice();
	}
	cout << "Thank you for choosing some delicious " << soda[pick-1] <<
	" have a well hydrated day!" << endl;
	return 0;
}

int choice()
{
	int x;
	cin >> x;
	if (x <= 5 or x >= 1)
	{
		return x; 
	}
	
}

