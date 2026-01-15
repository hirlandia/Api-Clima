# 🌤️ Monitor de Clima: Conectando Python ao Mundo Real via API

Neste projeto, desenvolvi um script em Python que vai além do processamento de dados estáticos: ele busca informações em tempo real. Utilizei a API pública **Open-Meteo** para consultar previsões de temperatura baseadas em coordenadas geográficas e transformei esses dados brutos em um gráfico visual de fácil compreensão.

---

### 💡 O Desafio
O objetivo foi entender na prática como as aplicações modernas se comunicam. Em vez de usar uma base de dados pronta, eu queria que o usuário pudesse informar uma localização e o sistema respondesse: *"Aqui está a flutuação da temperatura para estas coordenadas agora"*.

---

### 🔍 O que eu aprendi e apliquei

#### 1. Comunicação via API (A ponte de dados)
Aprendi a usar a biblioteca `requests` para "conversar" com servidores externos de forma eficiente:
* **Endpoints e Parâmetros:** Entendi que o `endpoint` é o endereço digital dos dados e usei dicionários (`chave: valor`) para personalizar a requisição com latitude, longitude e fuso horário.
* **Método GET:** Pratiquei o comando fundamental para solicitar informações de um servidor.

#### 2. Tradução de Dados (JSON)
As APIs respondem em uma linguagem chamada **JSON**. Minha tarefa foi converter essa resposta para um formato que o Python entenda, permitindo "navegar" dentro da base de dados e extrair apenas o que importava: as horas e as temperaturas.

#### 3. Visualização de Dados (DataViz)
Para tornar o resultado amigável, utilizei a biblioteca `matplotlib`:
* **Plotagem de Gráficos:** Transformei listas de números em um gráfico de linhas intuitivo.
* **Organização Visual:** Configurei os eixos X (tempo) e Y (temperatura) e adicionei títulos para garantir que a informação fosse lida sem esforço.

---

### 🛠️ Tecnologias e Bibliotecas
* **Python 3**: Linguagem base do projeto.
* **Requests**: Para realizar a "ponte" entre meu computador e a API.
* **Matplotlib**: Para transformar números em visão estratégica (gráficos).
* **Open-Meteo API**: Minha fonte confiável de dados meteorológicos reais.

---

### 🚀 Como executar o projeto
1. Instale as bibliotecas necessárias:
   ```bash
   pip install requests matplotlib
