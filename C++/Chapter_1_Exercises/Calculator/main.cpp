#include <iostream>
using namespace std;

int getUserInput()
{
	
	cout << "Please enter an interger!";
	int num;
	cin >> num;
	return num;
}

int getMathOperation()
{
	cout << "Pick an operation:\n" << "(1 = +)\t" <<
	"(2 = -)\t(3 = *)\t(4 = /)" << endl;
	int oper;
	cin >> oper;
	if ((oper > 0) && (oper < 5))
	{
		return oper;
	}
	else
	{
		cout << "That's not a valid number!" << endl;
		getMathOperation();
	}
}
int calculate(int num1, int operation, int num2)
{
	if (operation == 1)
	{
		return num1 + num2;
	}
	else if (operation == 2)
	{
		return num1 - num2;
	}
	else if (operation == 3)
	{
		return num1 * num2;
	}
	else if (operation == 4)
	{
		return num1 / num2;
	}
}

void printResult(int result)
{
	cout << "You got " << result << " Awesome!" << endl;
}
int main()
{
	int num1 = getUserInput();

	int operation = getMathOperation();

	int num2 = getUserInput();

	int result = calculate(num1, operation, num2);

	printResult(result);
}