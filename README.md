# ☁️ Azure Buddy

### Assistente de Azure para iniciantes

O **Azure Buddy** é um assistente virtual educacional desenvolvido como projeto para o desafio da DIO **“Construa Seu Assistente Virtual Com Inteligência Artificial”**.

O projeto tem como objetivo ajudar pessoas que estão começando a estudar **Microsoft Azure** a compreender conceitos fundamentais de computação em nuvem de forma simples e didática.

---

## 🎯 Objetivo

Criar uma aplicação simples que permita ao usuário fazer perguntas sobre conceitos básicos do Azure e receber respostas baseadas em uma **base de conhecimento previamente definida**.

O projeto também demonstra conceitos importantes de desenvolvimento de aplicações com:

* Python;
* Streamlit;
* organização de conhecimento;
* criação de prompts;
* processamento de perguntas;
* interação com o usuário;
* avaliação de respostas.

---

## 👥 Público-alvo

O Azure Buddy foi desenvolvido principalmente para:

* pessoas iniciantes em computação em nuvem;
* estudantes de tecnologia;
* pessoas que estão começando a estudar Microsoft Azure;
* estudantes que desejam compreender conceitos básicos antes de avançar para conteúdos mais técnicos.

---

## 🤖 Como funciona

O funcionamento do projeto é baseado em uma base de conhecimento em Markdown.

O fluxo principal é:

```text
Usuário
   ↓
Interface Streamlit
   ↓
Pergunta
   ↓
Busca na Base de Conhecimento
   ↓
Seção relacionada encontrada
   ↓
Resposta
```

Quando o assunto não está disponível na base de conhecimento, o Azure Buddy informa que não possui informações suficientes para responder.

Isso evita que o assistente invente informações que não fazem parte do conhecimento definido para o projeto.

---

## 📚 Base de Conhecimento

A base de conhecimento está localizada em:

```text
data/azure_basico.md
```

Atualmente, ela contém informações sobre:

* Microsoft Azure;
* Computação em Nuvem;
* IaaS;
* PaaS;
* SaaS;
* Azure Virtual Machines;
* Azure App Service;
* Azure Blob Storage;
* Azure Files;
* Microsoft Entra ID;
* Azure Monitor;
* Azure Virtual Network.

---

## 🧠 Prompt do Agente

As instruções de comportamento do assistente estão documentadas em:

```text
docs/prompt_agente.md
```

O prompt define características como:

* público do assistente;
* objetivo;
* fonte principal de conhecimento;
* forma de explicar os conceitos;
* comportamento quando uma informação não está disponível;
* tom de comunicação;
* regras para evitar informações inventadas.

---

## 💻 Tecnologias utilizadas

* **Python**
* **Streamlit**
* **Markdown**
* **Git**
* **GitHub**

---

## 📁 Estrutura do projeto

```text
assistente-azure-iniciantes/
│
├── data/
│   └── azure_basico.md
│
├── docs/
│   └── prompt_agente.md
│
├── src/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

### Descrição dos diretórios

**`data/`**

Contém a base de conhecimento utilizada pelo assistente.

**`docs/`**

Contém a documentação relacionada ao comportamento e às instruções do agente.

**`src/`**

Contém o código da aplicação e as dependências necessárias para executá-la.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd assistente-azure-iniciantes
```

### 3. Instalar as dependências

```bash
python -m pip install -r src/requirements.txt
```

### 4. Executar a aplicação

```bash
streamlit run src/app.py
```

Após executar o comando, o Streamlit abrirá a aplicação no navegador.

---

## 🧪 Testes realizados

Foram realizados testes com perguntas relacionadas e não relacionadas à base de conhecimento.

### Teste 1 — Azure

**Pergunta:**

> O que é Azure?

**Resultado:**
O assistente encontrou a seção **Microsoft Azure** e apresentou sua definição e exemplo.

### Teste 2 — Máquina virtual

**Pergunta:**

> O que é uma máquina virtual?

**Resultado:**
O assistente encontrou a seção **Azure Virtual Machines** e apresentou a explicação correspondente.

### Teste 3 — Informação fora da base

**Pergunta:**

> O que é Kubernetes?

**Resultado:**

> Não encontrei informações suficientes sobre esse assunto na minha base de conhecimento.

Esse comportamento demonstra que o assistente não apresenta uma resposta quando não possui informação suficiente na base definida para o projeto.

---

## 📊 Avaliação

A avaliação inicial foi realizada utilizando perguntas de teste.

| Pergunta                     | Informação disponível | Resultado                       |
| ---------------------------- | --------------------- | ------------------------------- |
| O que é Azure?               | Sim                   | Respondeu                       |
| O que é uma máquina virtual? | Sim                   | Respondeu                       |
| O que é Kubernetes?          | Não                   | Informou ausência de informação |

A avaliação considera principalmente:

* identificação correta do assunto;
* recuperação da informação correspondente;
* comportamento adequado quando não existe informação suficiente.

---

## 🎤 Pitch

### Problema

Pessoas que estão começando a estudar computação em nuvem podem encontrar dificuldade para compreender termos e serviços do Microsoft Azure.

### Solução

O Azure Buddy apresenta uma forma simples de consultar conceitos fundamentais do Azure por meio de uma interface de conversa.

### Valor

O projeto busca facilitar o primeiro contato com conceitos de computação em nuvem, utilizando explicações objetivas e uma base de conhecimento organizada.

---

## 🔮 Próximos passos

Algumas possibilidades de evolução do projeto são:

* ampliar a base de conhecimento;
* adicionar mais perguntas e respostas;
* melhorar a busca por conceitos;
* adicionar novos conteúdos sobre Azure;
* aprimorar a interface;
* ampliar a avaliação do assistente.

---

## 👨‍💻 Projeto

Projeto desenvolvido como parte do desafio da **DIO — Construa Seu Assistente Virtual Com Inteligência Artificial**.

**Azure Buddy — Assistente de Azure para Iniciantes**
