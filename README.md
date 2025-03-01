# 📌 SIGAA Activity Checker

Este projeto é uma API Flask que autentica no SIGAA e retorna as atividades pendentes do usuário, filtrando aquelas que já foram concluídas.

## 🚀 Tecnologias Utilizadas
- Python
- Flask
- Selenium
- WebDriver (Chrome)
- Regex (para análise de datas)
- HTML/CSS (para renderizar a interface inicial)

## 📌 Requisitos
Antes de rodar o projeto, certifique-se de ter instalado:
- Python 3.8+
- Google Chrome
- ChromeDriver compatível com sua versão do Chrome

Para instalar as dependências necessárias, execute:
```bash
pip install -r requirements.txt
```

## 🔧 Configuração

### 1️⃣ Instalar o ChromeDriver
Baixe e instale o [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com sua versão do Google Chrome. Certifique-se de adicionar o caminho do ChromeDriver às variáveis de ambiente do sistema.

### 2️⃣ Clonar o Repositório
```bash
git clone https://github.com/seuusuario/sigaa-activity-checker.git
cd sigaa-activity-checker
```

### 3️⃣ Rodar o Projeto
No terminal, execute:
```bash
python app.py
```
O servidor Flask será iniciado em `http://127.0.0.1:5000/`.

## 🔑 Como Usar

### 📄 Endpoints

#### `GET /`
Exibe a página inicial com o formulário de login.

#### `POST /login`
Autentica no SIGAA e retorna as atividades pendentes do usuário.

##### Exemplo de Requisição
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

##### Resposta de Sucesso
```json
{
  "atividades_pendentes": [
    "Atividade 1 - 05/03",
    "Atividade 2 - Hoje",
    "Atividade 3 - Em breve"
  ]
}
```

Se houver um erro, a resposta retornará:
```json
{
  "erro": "Descrição do erro"
}
```

## 🎯 Funcionalidades
✅ Coleta as atividades pendentes diretamente do SIGAA.
✅ Filtra atividades já concluídas.
✅ Identifica prazos e exibe apenas atividades ainda relevantes.
✅ Integração com Flask para fácil utilização via API.
✅ Suporte para execução em background com Selenium Headless.

## 🛠 Possíveis Melhorias Futuras
- Criar uma interface web mais interativa.
- Implementar autenticação segura para proteger os dados do usuário.
- Adicionar suporte a notificações para alertar sobre prazos de atividades.
- Criar um banco de dados para armazenar as atividades pendentes e permitir histórico de consultas.

## 🏗 Estrutura do Projeto
```
📂 sigaa-activity-checker
├── 📄 app.py          # Código principal da API
├── 📂 templates       # HTML para renderizar a página inicial
│   ├── index.html
├── 📄 requirements.txt # Dependências do projeto
├── 📄 README.md       # Documentação do projeto
```

## 📜 Licença
Este projeto é de uso pessoal. Caso queira contribuir ou utilizá-lo, entre em contato! 😊

