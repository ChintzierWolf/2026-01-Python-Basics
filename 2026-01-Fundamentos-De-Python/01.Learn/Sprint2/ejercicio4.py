usuario = input('ingresa tu usuario: ')
password = input('ingresa tu contraseña: ')

if usuario == 'Admin':
    print('usuario correcto')
    if password == '1234':
        print('Contraseña correcta. Bienvenido al sistema')
    else:
        print('Contraseña incorrecta. Acceso denegado')
else:
    print('Intruso detectado. Acceso denegado')