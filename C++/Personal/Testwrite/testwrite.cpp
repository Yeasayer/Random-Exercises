#include <iostream>
#include <fstream>
#define arraysize(ar)  (sizeof(ar) / sizeof(ar[0]))
using namespace std;

string lazywrite (string str);
string loop (string str);
int main()
{
	string text;
	string writestr = "";
	ofstream myfile ("./cooltext.txt", ios::app);
	if (myfile.is_open())
	{
		cout << "Okay, start typing sonny!" << endl;
		text = loop(text);
		cout << text;
		writestr = text;
		cout << "This is what you wrote:\n" << text << endl;
		myfile << text;
		myfile.close();
		return 0;
	}
	else
	{
		cout << "Goodbye!" << endl;
		return 0;
	}
}

string lazywrite (string str)
{
	getline(cin, str);
	return str;
}
string loop (string str)
{
	str = str;
	string addstring;
	addstring = lazywrite(addstring);
	if (addstring != "exit")
	{ 
		str += addstring + "\n";
		cout << str;
		loop(str);
	}
	else
	{
		cout << "This is what's going to be added: " << endl << str;
		cout << "Goodbye!" << endl;
	}
	return str;
}
