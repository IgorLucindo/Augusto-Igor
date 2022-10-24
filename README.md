# **Bug Hunter Hub**


## Aluno Augusto - 3º Ano - Engenharia de Comunicações
## Aluno Igor - 3º Ano - Engenharia Eletrônica

---

1. [Conceito](#conceito)
1. [Proposta](#proposta)
1. [Função](#função)
    1. [Domínios](#domínios)
    1. [Mapa](#mapa)
    1. [Usuário](#usuário)


# **Conceito**

Bug Bounty denomina a atividade de testar aplicações Web de Empresas as quais permitem que hackers, indivíduos com capacidade de burlar sistemas de segurança de programas pela internet, possam testar a segurança de suas aplicações e, caso consigam achar uma vulnerabilidade ao testá-la, ganhar uma recompensa em dinheiro ao reportá-la à empresa.
O trabalho de Bug Bounty requer paciência, diligência e organização para poder gerar resultados. Saber organizar o escopo do alvo, subdomínios, diretórios e tecnologias dos sites testados é de extrema importância para um bom Bug Bounty, mas vêm se mostrando um trabalho árduo para os iniciantes no ramo.

# **Proposta**

Esta aplicação visa a solucionar este problema. O Bug Hunter Hub é um website local, rodando em Flask, que possibilita ao hacker ter mais organização de seu trabalho, agilizar os testes da aplicação e retomar de onde parou a sessão de hacking após salvar os dados analisados no BHH.

# **Função**

Na aplicação é possível criar projetos, denominando os sites que serão testados, e dentro do projeto haverão 3 abas: domínios, diretórios e usuário. As abas deverão ser preenchidas com informações do website à medida que for analisado pelo usuário.

## **Domínios**
Nesta aba, cada domínio do site analisado terá um dos marcadores quanto aos serviços que responde.
- Desconhecido
> Valor padrão. Indica que o usuário ainda não analisou o domínio. O domínio com essa opção marcada não aparecerá na aba "Mapeamento"
- Web
> O domínio apresenta serviço web respondendo e operando.
- Não Web
> O domínio não tem serviço web, mas tem outros serviços em portas distintas.
- Não Responde
> O domínio não tem serviço web, nem outros serviços após um escaneamento com um programa como o nmap. O domínio com essa opção marcada não aparecerá na aba "Mapeamento"

Cada domínio poderá ter mais os seguintes marcadores em relação às análises que está submetido.
- Em análise
> O usuário está em meio a uma análise detalhada do serviço web.
- Analisado
> O usuário não encontrou vulnerabilidades ao analisar o domínio
- Não analisado
> O usuário não testou o domínio. O domínio com essa opção marcada não aparecerá na aba "Mapeamento"
- Análise adiada
> O usuário ainda não analisou o domínio

## **Mapeamento**

Nesta aba, cada domínio analisado na aba anterior será apresentado aqui nesta aba como um mapeamento da aplicação com cada diretório e funcionalidades embutidas neles.
O hacker, então, poderá organizar as requisições, funcionalidades, cookies e muito mais para cada diretório da aplicação de cada domínio do alvo analisado.

## **Usuário**

Para utilizar a aplicação, será necessário criar um login e senha. Na aba "usuário", este poderá ver informações mais abrangentes dos projetos analisados, escolher o projeto o qual vai focar agora e começar o hacking. 
Além disso terá um campo para deletar a conta, remover projetos.

## **Tutorial de execução**

A aplicação tem como requisitos possuir o python 3 instalado e executar os comandos no arquivo ``requirements.txt`` conforme com o seguinte comando:
<font size='4'>
 ```
$ pip install -r requirements.txt
 ```
 </font>

E em seguida, para iniciar o programa basta executar o arquivo ``run.py`` através do seguinte comando:
<font size='4'>
 ```
$ python3 run.py
 ```
</font>

Após isso você verá no terminal a linha de comando com URL ``http://127.0.0.1:5000`` da aplicação:
<font size='4'>
 ```
 * Serving Flask app 'bughunter'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 534-739-443
127.0.0.1 - - [24/Oct/2022 15:13:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Oct/2022 15:13:42] "GET /favicon.ico HTTP/1.1" 404 -
 ```
</font>