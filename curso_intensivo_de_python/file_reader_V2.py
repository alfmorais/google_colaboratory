with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Linha de comando para Linux e OS X
# with open('text_files/nome_do_arquivo.txt') as file_object:

# Linha de comando para Windows
# with open('text_files\nome_do_arquivo.txt') as file_object:


# No Linux e no OS X paths absolutos tem o seguinte aspecto
# file_path = '/home/ehmatthes/other_files/text_files/nome_do_arquivo.txt'
# with open(file_path) as file_object:


# paths absolutos no windows
# file_path = 'C:\Users\ehmatthes\other_files\text_files\nome_do_chiclete.txt'
# with open(file_path) as file_objects:

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line)

# Criando uma lista de linhas de um arquivo
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Trabalhando com o conteudo de um arquivo
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

print('String com espaços ao invés da quebra de linha')
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print('Eliminando os espaços da string')
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

