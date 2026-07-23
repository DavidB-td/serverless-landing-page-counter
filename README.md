<!-- Badges do Topo do README -->
<p align="left">
  <img src="https://shields.io" alt="Status"/>
  <img src="https://shields.io" alt="Licença"/>
</p>

### 🛠️ Tecnologias e Infraestrutura Utilizadas

<p align="left">
  <!-- Plataforma & IaC -->
  <img src="https://shields.io" alt="AWS"/>
  <img src="https://shields.io" alt="AWS CloudFormation"/>
  <!-- Back-end & Scripts -->
  <img src="https://shields.io" alt="Node.js"/>
  <img src="https://shields.io" alt="Python"/>
  <img src="https://shields.io" alt="Boto3"/>
</p>

<p align="left">
  <!-- Serviços AWS Serverless -->
  <img src="https://shields.io" alt="Amazon S3"/>
  <img src="https://shields.io" alt="Amazon API Gateway"/>
  <img src="https://shields.io" alt="AWS Lambda"/>
  <img src="https://shields.io" alt="Amazon DynamoDB"/>
</p>

<p align="left">
  <!-- Front-end -->
  <img src="https://shields.io" alt="HTML5"/>
  <img src="https://shields.io" alt="CSS3"/>
  <img src="https://shields.io" alt="JavaScript"/>
</p>


---


# AWS Serverless Landing Page Counter

Solução **serverless** para rastreamento e contabilização em tempo real de cliques em landing pages. O projeto foi desenvolvido com foco em **alta escalabilidade**, **baixa latência** e **baixo custo operacional**, utilizando o modelo **pay-per-use** da Amazon Web Services (AWS).

---

# 📋 Sumário

* [Sobre o Projeto](#-sobre-o-projeto)
* [O Problema e a Solução](#-o-problema-e-a-solução)
* [Arquitetura do Sistema](#-arquitetura-do-sistema)
* [Funcionamento](#-funcionamento)
* [Tecnologias Utilizadas](#%EF%B8%8F-tecnologias-utilizadas)
* [Principais Características](#-principais-características)
* [Otimização Financeira](#-otimização-financeira)
* [Como Executar o Projeto](#-como-executar-o-projeto)
* [Grupo 4 (AWS re/Start)](#-grupo-4-aws-restart)
* [Licença](#-licença)

---

# 📖 Sobre o Projeto

O **AWS Contador Serverless** é uma aplicação desenvolvida para registrar e contabilizar cliques de usuários em landing pages de forma segura, escalável e totalmente serverless. A arquitetura elimina a necessidade de gerenciamento de servidores, permitindo que a infraestrutura escale automaticamente conforme a demanda. O contador é atualizado em tempo real por meio de operações atômicas no banco de dados, garantindo consistência mesmo sob alto volume de acessos simultâneos.

---

# 🎯 O Problema e a Solução

O projeto simula o cenário de uma startup lançando uma campanha inédita com tráfego imprevisível. Como métricas indicam que 53% dos visitantes abandonam páginas que demoram mais de três segundos para carregar, a performance é crítica. 

Para evitar gargalos de lentidão e travamentos sob demanda repentina, desenvolvemos essa arquitetura 100% serverless. Ela garante resiliência e tempos de resposta na casa dos milissegundos, escalando instantaneamente para absorver desde dezenas até milhões de acessos.

---

# 🏗️ Arquitetura do Sistema

A solução utiliza uma arquitetura **100% Serverless** na AWS composta pelos seguintes serviços:

### Amazon S3
* Hospedagem estática do front-end.
* Alta disponibilidade.
* Baixo custo.

### Amazon API Gateway
* Endpoint público HTTPS.
* Gerenciamento de requisições.
* Configuração de políticas CORS.

### AWS Lambda
* Execução da lógica de negócio.
* Atualização do contador sob demanda.
* Escalabilidade automática.

### Amazon DynamoDB
* Banco de dados NoSQL.
* Persistência do contador.
* Incremento atômico do valor armazenado.

### AWS IAM
* Controle de permissões.
* Execution Roles.
* Aplicação do princípio do menor privilégio (Least Privilege).

---

# 🔄 Funcionamento

1. O usuário acessa a landing page hospedada no Amazon S3.
2. Ao clicar no botão monitorado, uma requisição HTTPS é enviada ao Amazon API Gateway.
3. O API Gateway aciona uma função AWS Lambda.
4. A função Lambda incrementa o contador no Amazon DynamoDB utilizando atualização atômica.
5. O novo valor é retornado para o front-end e exibido ao usuário em tempo real.

---

# 🛠️ Tecnologias Utilizadas

## Front-end
* HTML5
* CSS3
* JavaScript (ES6)

## Back-end
* AWS Lambda
* Node.js

## Banco de Dados
* Amazon DynamoDB

## Infraestrutura como Código (IaC)
* AWS CloudFormation

## Plataforma
* Amazon Web Services (AWS)

---

# ✨ Principais Características

* Arquitetura 100% Serverless.
* Escalabilidade horizontal automática.
* Baixa latência.
* Modelo de cobrança pay-per-use.
* Alta disponibilidade.
* Incremento atômico do contador.
* Segurança baseada em políticas IAM.
* Fácil implantação utilizando Infraestrutura como Código (IaC).

---

# 💰 Otimização Financeira

O modelo serverless adotado elimina qualquer custo com capacidade ociosa de servidores. A arquitetura tira máximo proveito do Free Tier (nível gratuito) da AWS, resultando em um custo operacional projetado próximo a zero, onde a cobrança ocorre estritamente pelo milissegundo de processamento e pelas requisições efetuadas.

---

# 🚀 Como Executar o Projeto

### Pré-requisitos

* **Python 3.x** instalado.
* **AWS CLI** instalada e configurada com suas credenciais (`aws configure`).
* **Boto3** (SDK da AWS para Python).

### Passo a Passo (Deploy Automatizado)

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Instale a dependência do script:**
   ```bash
   pip install boto3
   ```

3. **Execute o pipeline de deploy:**
   ```bash
   python deploy.py
   ```

O script fará todo o fluxo pesado automaticamente:
* Provisionamento/atualização da infraestrutura na AWS via CloudFormation (`iac/template.yaml`).
* Extração dinâmica do endpoint da API e das configurações do S3.
* Injeção automática da URL gerada no arquivo `frontend/script.js`.
* Sincronização e upload dos arquivos web (`index.html`, `style.css`, `script.js`) para o bucket S3.

4. **Acesse o projeto:**
   Ao final da execução, o terminal exibirá a URL pública do site no S3 para você acessar e testar o contador em tempo real.

---

# 👥 Grupo 4 (AWS re/Start)

* **Bruno Ruan Lima Da Silva** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
* **Christopher Bernardes Viana** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
* **David Bezerra Da Silva** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
* **Natan Ferreira Dos Santos** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
* **Gustavo Ramalho Matioli** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)
* **Leticia Mikaeli Alves dos Santos** – [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais durante o programa **AWS re/Start**.
