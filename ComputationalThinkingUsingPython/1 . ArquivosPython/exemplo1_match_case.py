linguagem = input('Linguagem: ')

match linguagem:
    case 'JavaScript':
        print('Desenvolver Web')
    case 'Python' | 'python':
        print('Cientista de dados')
    case 'PHP':
        print('Desenvolvedor backend')
    case 'Java' | 'java' | 'JAVA':
        print('Desenvolvedor backend ou mobile')
    case 'Solidity':
        print('Desenvolvedor Blockchain')
    case _:
        print('Linguagem não encontrada!')
