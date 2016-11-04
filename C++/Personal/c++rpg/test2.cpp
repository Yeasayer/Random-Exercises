#include <iostream>
#include <string>
using namespace std;

int main()
{
	std::cout << "Please enter your first name: \t";
	std::string name;
	std::cin >> name;
	const std::string greeting = ("Hello, " + name + "!");

	const std::string spaces(greeting.size(), 'x');
	const std::string second = "*x" + spaces + "x*";

	const std::string first(second.size(), '*');

	std::cout << first << std::endl << second << std::endl << "*x" << greeting << "x*" << endl << second << endl << first << endl;

	return 0; 
}