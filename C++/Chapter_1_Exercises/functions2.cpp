#include <iostream>
using namespace std;

void returnNothing()
{

}

int return5()
{
	return 5;
}

int main()
{
	cout << return5() << endl;
	cout << return5() + 2 << endl;

	returnNothing();
	return5();

	//cout << returnNothing()

	return 0;
}