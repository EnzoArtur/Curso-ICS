usuario_correto = 'Enzo999'
senha_correta = 'Enzo123'

nome_de_usuario = input('digite seu nome de usuario: ')
senha = input('digite sua senha: ')

if nome_de_usuario == usuario_correto and senha == senha_correta:
    print('acesso concedido ')

else:
    print('acesso negado ')