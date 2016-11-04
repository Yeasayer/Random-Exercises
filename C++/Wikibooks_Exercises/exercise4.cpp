#include <iostream>
using namespace std;

	

int tenarray()
{
	int ten [] = {};
	int input;
	int arraysum;
	int i = 0;
	while (i < 11)
	{
		if (i == 0)
		{
			cout << "Type the 1st number:\t";
		}
		else if (i == 1)
		{
			cout << "Type the " << i << "nd number:\t";
		}
		else if (i == 2)
		{
			cout << "Type the " << i << "rd number:\t";
		}
		else if (i > 2 && i < 10)
		{
			cout << "Type the " << i << "th number:\t";
		} 
		else
		{
			cout << "Type the last number:";
		}
		cin >> input;
		if (!isdigit(input))
		{
			cout << "Alright, adding " << input << " to the array." << endl;
			ten[i] = input;
			i = i + 1;
		}
		else
		{
			cout << "Sorry! " << input << " is not a number!" << endl; 
		}
	}
	for (int j = 0; j < (sizeof(ten)/sizeof(int)); ++j)
	{
		cout << ten[j] << endl;
		arraysum += ten[j];
	}
	cout << "Okay now we're going to add those numbers up." << endl;
	return arraysum;
}

int main()
{
	int sum;
	cout << "Alright, I'm going to ask you for ten numbers..." << endl;
	sum = tenarray();
	cout << "The sum of all those values you put in is " << sum << endl;
	return 0;
}