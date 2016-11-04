#include <iostream>
using namespace std;

int doubleNumber(int a)
{
	return a + a;
}


int main()
{
	cout << "Give me a number and I'll give you double!" << endl;
	int x = 0;
	cin >> x;
	cout << "I have taken your " << x << " and given you " << doubleNumber(x) << " ain't that cool!" << endl;
	return 0;
}