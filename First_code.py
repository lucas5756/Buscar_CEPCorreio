#Importar Biblioteca de Requests
import requests

#cabeçalho 
def main():
    print('### Consulta CEP ###')
    print()

# Início

#Peça ao usuário para digitar o CEP
cep_input = input('Digite o CEP para consulta: ')

if len(cep_input) !=8:
    print('CEP inválido')
    exit()

#Fazendo a requisição e formatação do CEP digitado pelo usuário:
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

#Realiza uma busca na API Via CEP

#Busca na API Viacep os dados condizentes com as variavéis explicito em []
if 'erro' not in address_data:
    print('CEP: {}'.format(address_data['cep']))
    print('Rua/Avenida: {}'.format(address_data['logradouro']))
    print('Complemento: {}'.format(address_data['complemento']))
    print('Bairro: {}'.format(address_data['bairro']))
    print('Cidade: {}'.format(address_data['localidade']))
    print('Estado: {}'.format(address_data['uf']))
 

#se ocorrer erro na busca exibir erro de CEP
else:
    print('{}: CEP INÁLIDO!.'.format(cep_input))
    option = int(input('Deseja realizar uma nova busca? \n1. Sim\n2 Sair\n'))


if option == 1:
    main()
else:
    print('Saindo...')

#Nome do ambiente de nível superior do programa
if __name__ == '__main__':
    main()
