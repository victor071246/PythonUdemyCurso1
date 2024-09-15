#include <iostream>

int main()
{
	int Num1 = 10, Num2 = 20, Num3, Num4;
	Num3 = Num1++;
	Num4 = ++Num2;
	std::cout << "Num1 = " << Num1 << std::endl;
	std::cout << "Num2 = " << Num2 << "\n";
	std::cout << "Num3 = " << Num3 << std::endl;
	std::cout << "Num4 = " << Num4 << "\n";
}

