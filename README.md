# TDE 2 - Máquinas de Estado Finito e Gramáticas

**Aluno:** Gabriel Barbosa Fernandes de Oliveira  
**Disciplina:** Linguagens Formais e Autômatos  
**Tema:** Máquinas de Estado Finito e Gramáticas  

---

## Descrição

Este repositório contém a resolução do **TDE 2 - Máquinas de Estado Finito e Gramáticas**.

O trabalho tem como objetivo praticar conceitos relacionados a **Máquinas de Estados Finitos Determinísticas (MEFD)** e estudar a **Hierarquia de Chomsky**, relacionando linguagens formais, gramáticas e modelos computacionais.

---

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- `Exercicio1_TDE2.jpg`  
  Contém os diagramas de transição das Máquinas de Estados Finitos Determinísticas para as linguagens propostas no exercício 1.

- `Exercicio2_TDE2.py`  
  Contém a implementação, em Python, das máquinas de estado solicitadas no exercício 2.

- `Exercicio3_TDE2.pdf`  
  Contém a explicação teórica sobre a Hierarquia de Chomsky, abordando os tipos de gramáticas e suas regras de produção.

- `README.md`  
  Arquivo de documentação do repositório.

---

## Exercício 1

No exercício 1, foram construídos os diagramas de transição das seguintes linguagens:

- **L0:** strings em que cada `0` é seguido por pelo menos um `1`;
- **L1:** strings que terminam com `00`;
- **L2:** strings que contêm exatamente 3 zeros;
- **L3:** strings que iniciam com `1`;
- **L4:** strings que não começam com `1`.

---

## Exercício 2

No exercício 2, foi implementado um programa em **Python** capaz de simular cada uma das máquinas de estado.

O código contém as seguintes funções:

- `mefd_l0`: reconhece strings em que cada `0` é seguido por pelo menos um `1`;
- `mefd_l1`: reconhece strings que terminam com `00`;
- `mefd_l2`: reconhece strings que contêm exatamente 3 zeros;
- `mefd_l3`: reconhece strings que iniciam com `1`;
- `mefd_l4`: reconhece strings que não começam com `1`.

A simulação foi feita usando estados e transições, representando o funcionamento das máquinas de estado.

---

## Como Executar o Código

Para executar o código do exercício 2, é necessário ter o **Python** instalado no computador.

### 1. Baixar o repositório

Você pode baixar o repositório pelo GitHub clicando em:

```bash
Code > Download ZIP
```

Depois, extraia a pasta do projeto.

---

### 2. Abrir o terminal na pasta do projeto

No Windows, você pode abrir a pasta do projeto, clicar na barra de endereço, digitar:

```bash
cmd
```

E pressionar **Enter**.

---

### 3. Executar o arquivo Python

Com o terminal aberto na pasta do projeto, execute:

```bash
python Exercicio2_TDE2.py
```

Caso o comando `python` não funcione, tente:

```bash
python3 Exercicio2_TDE2.py
```

---

## Exemplo de Saída

Ao executar o arquivo, o programa testa algumas strings aceitas e rejeitadas por cada máquina.

Exemplo:

```bash
=== L0 - cada 0 seguido de 1 ===
Aceitos:
  '010111' -> True
  '1111' -> True
  '01110111011' -> True
Rejeitados:
  '00' -> False
  '010' -> False
  '0' -> False
  '1001' -> False
```

O valor `True` significa que a string foi aceita pela máquina.  
O valor `False` significa que a string foi rejeitada.

---

## Exercício 3

No exercício 3, foi feita uma explicação sobre a **Hierarquia de Chomsky**, destacando as quatro classes principais de gramáticas:

- **Tipo 0:** Gramáticas Irrestritas;
- **Tipo 1:** Gramáticas Sensíveis ao Contexto;
- **Tipo 2:** Gramáticas Livres de Contexto;
- **Tipo 3:** Gramáticas Regulares.

Também foram apresentados exemplos práticos de regras de produção para cada tipo de gramática.

---

## Tecnologias Utilizadas

- Python;
- GitHub;
- Markdown;
- PDF;
- Editor de texto/IDE.

---

## Autor

Gabriel Barbosa Fernandes de Oliveira
