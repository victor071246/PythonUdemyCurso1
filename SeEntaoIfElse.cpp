#include <iostream>
#include <string>
#include <locale.h>

int main()
{
	setlocale(LC_ALL, "portuguese");
	bool bFezSol, bCarroPronto, bSalarioDepositado;
	bool bAcesso;
	std::string SenhaDeAcesso = "cmaismais";
	std::string SenhaDigitada;

	std::cout << "Digite a senha de Acesso: ";
	std::cin >> SenhaDigitada;

	/*Se a senha digitada pelo usuário e armazenada na variável SenhaDigitada for igual a senha de acesso as instruções após o if serão executadas pois a condição foi verdadeira true 1*/
	if (SenhaDigitada == SenhaDeAcesso)
	{
		std::cout << "\nAcesso Permitido!" << "\n";
		//aqui aproveitamos para indicar que o acesso foi concedido através de outra variável booleana
		bAcesso = true;
		system("PAUSE");
	}
	/*Se a condição for falsa então as instruções do else serão executadas*/
	else
	{
		std::cout << "\n Acesso Negado!!!";
		exit(0); //sai do programa, força o fechamento da aplicação
		system("PAUSE");
	}

	bFezSol = false;
	bCarroPronto = false;
	bSalarioDepositado = false;
	//Aqui podemos deixar apenas a variável
	//Não é necessário == true pois será buscado o valor de bAcesso e ficará assim:
	//if (true) ou if(false)
	if (bAcesso)
	{
		if (bFezSol && bCarroPronto && bSalarioDepositado)
		{
			std::cout << "\nVai dar Praia!!!" << std::endl;
		}
		//Aqui será executado se a condição do if falhar e se bSalarioDepositado for false
		//Da mesma forma aqui
		//Como bSalarioDepositado é falso!(não) Falso dará True e ai entra no else if
		else if (!bSalarioDepositado)
		{
			std::cout << "\nNão vai dar Praia, mas o salário foi depositado" << "\n";
		}
	}

}