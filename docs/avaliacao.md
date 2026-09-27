# 📊 Avaliação do Azure Buddy

## Objetivo

A avaliação do Azure Buddy foi realizada para verificar se o assistente consegue:

* identificar perguntas relacionadas aos temas presentes na base de conhecimento;
* retornar a informação correspondente;
* lidar corretamente com perguntas sobre assuntos que não estão disponíveis na base.

---

## 🧪 Casos de teste

### Teste 1 — Microsoft Azure

**Pergunta:**

> O que é Azure?

**Informação disponível na base:** Sim.

**Resultado esperado:**
Encontrar a seção relacionada ao Microsoft Azure e apresentar sua definição.

**Resultado obtido:**
O assistente encontrou a seção **Microsoft Azure** e apresentou a explicação e o exemplo disponíveis na base.

**Status:** ✅ Aprovado

---

### Teste 2 — Azure Virtual Machines

**Pergunta:**

> O que é uma máquina virtual?

**Informação disponível na base:** Sim.

**Resultado esperado:**
Encontrar a seção relacionada ao Azure Virtual Machines.

**Resultado obtido:**
O assistente encontrou a seção **Azure Virtual Machines** e apresentou a explicação e o exemplo disponíveis na base.

**Status:** ✅ Aprovado

---

### Teste 3 — Assunto não disponível

**Pergunta:**

> O que é Kubernetes?

**Informação disponível na base:** Não.

**Resultado esperado:**
O assistente deve informar que não possui informações suficientes sobre o assunto.

**Resultado obtido:**

> Não encontrei informações suficientes sobre esse assunto na minha base de conhecimento.

**Status:** ✅ Aprovado

---

## 📈 Resultado da avaliação

Foram realizados **3 testes**.

| Métrica              | Resultado |
| -------------------- | --------: |
| Testes realizados    |         3 |
| Testes aprovados     |         3 |
| Testes não aprovados |         0 |
| Taxa de aprovação    |  **100%** |

### Interpretação

Nos testes realizados, o Azure Buddy apresentou o comportamento esperado nos três cenários avaliados:

1. identificação de um conceito presente na base;
2. identificação de outro conceito presente na base;
3. tratamento de uma pergunta sobre um assunto ausente da base.

A avaliação representa apenas os casos de teste realizados durante o desenvolvimento e não representa uma avaliação completa de todos os possíveis tipos de perguntas que podem ser feitas ao assistente.

---

## 🔎 Critérios avaliados

A avaliação considerou três aspectos principais:

### 1. Recuperação da informação

Verificar se uma pergunta relacionada a um conteúdo existente consegue localizar a seção correspondente.

### 2. Correspondência da resposta

Verificar se o conteúdo retornado corresponde ao assunto identificado.

### 3. Tratamento de informações ausentes

Verificar se o assistente evita apresentar uma resposta quando não possui informações suficientes na base de conhecimento.

---

## 🚀 Possíveis melhorias

Em versões futuras, a avaliação pode ser ampliada com:

* maior quantidade de perguntas;
* perguntas formuladas de maneiras diferentes;
* testes de perguntas ambíguas;
* testes de conceitos semelhantes;
* avaliação da clareza das respostas;
* criação de uma métrica mais ampla de precisão.
