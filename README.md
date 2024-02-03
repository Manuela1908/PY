# Diretório de Scripts 

Este diretório contém scripts independentes que foram desenvolvidos para uso acadêmico.

## Descrição dos Scripts

#dec_e_cod

Programa que possui as funções de codificação ou decodificação de um número binário. Utiliza dicionário de funções para selecionar as opções disponiveis (1 e 2) e possui tratamento de excessões para opções não disponiveis, numeros negativos e não inteiros durante a codificação, e numeros diferentes de 0 e 1 durante a decodificação.


#Gerador_De_Receitas

Programa desenvolvido utilizando integração com inteligência artificial ChatGPT da OpenAI, utiliza requisição HTTPS baseada na entrada do usuário e possui o comando para "gerar receitas culinarias" que é enviado para API como Role System, dispensando o uso de contextos ou frases detalhadas, o que possibilita o usuário de digitar apenas produtos, sabores, ou tipos de alimentos.
Construído utilizando Flask para ser implantado em um serviço web e ser acessado através do navegador. O aplicativo também possui a função de enviar emails para reportar problemas de requisição.

#googleapi

Programa destinado para geração de tokens dos serviços Google API. Este código foi criado para ser utilizado juntamente ao agendador de tarefas e um banco de dados, para contornar a expiração de 60 minutos do token (protocolo de segurança da Google). 
Antes de utilizar este código, é necessário ter em mãos o JSON com as credenciais do seu aplicativo, gerado no Google Cloud durante sua criação e confirgurações de acesso e autenticação.
