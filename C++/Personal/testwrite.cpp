#include <iostream>
#include <fstream>
#include "testwrite.h"
using namespace std;

int main()
{
	string write;
	ofstream myfile ("cooltext.txt");
	if (myfile.is_open())
	{
		cout << "Okay, start typing sonny!" << endl;
		myfile << WRITE_H(write);
	}
	else
	{
		cout << "Goodbye!" << endl;
		return 0;
	}
}