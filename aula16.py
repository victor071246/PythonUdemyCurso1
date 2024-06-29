# if / elif / else
entrada = input('Você quer entrar ou sair? ')


if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você escolheu sair do sistema')
else:
    print('Nenhuma das escolhas possíveis foi detectada, por favor, insira "entrar" ou "sair"')