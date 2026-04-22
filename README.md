Aqui está uma sugestão de **README.md** para o seu projeto de calculadora interativa, destacando o uso de funções e o laço de repetição contínuo.

---

# 🧮 Calculadora Interativa em Python

Este é um projeto de uma calculadora funcional que opera via terminal. Diferente de versões simples, esta versão utiliza um laço de repetição (`while`) que permite ao usuário realizar múltiplos cálculos sem precisar reiniciar o programa manualmente.

## 📝 Descrição

O script define uma função lógica para as quatro operações aritméticas básicas e utiliza uma estrutura de controle para interagir com o usuário, validando a operação desejada e perguntando se ele deseja realizar um novo cálculo.

## 🚀 Funcionalidades

O programa aceita os seguintes comandos de operação:
* `soma`
* `subtração`
* `multiplicação`
* `divisão`

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Funções (`def`)**: Para modularizar a lógica do cálculo.
* **Estruturas Condicionais (`if/elif/else`)**: Para seleção da operação.
* **Laço de Repetição (`while True`)**: Para manter o programa rodando até que o usuário decida parar.

## 💻 Como Funciona o Fluxo

1. O usuário insere dois números inteiros.
2. O usuário escreve o nome da operação (ex: "soma").
3. O resultado é exibido na tela.
4. O programa pergunta: *"Deseja continuar? (s/n)"*.
   - Se digitar `s`, o ciclo reinicia.
   - Se digitar `n`, o programa é encerrado via comando `break`.

## 📂 Como Executar

1. Tenha o Python instalado em seu computador.
2. Salve o código em um arquivo `calculadora_interativa.py`.
3. No terminal, execute:
   ```bash
   python calculador.py
   ```

---
*Projeto desenvolvido para praticar a integração entre funções e fluxos de repetição de entrada de dados.*
