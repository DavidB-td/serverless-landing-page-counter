# AWS Serverless Landing Page Counter

Solução **serverless** para rastreamento e contabilização em tempo real de cliques em landing pages. O projeto foi desenvolvido com foco em **alta escalabilidade**, **baixa latência** e **baixo custo operacional**, utilizando o modelo **pay-per-use** da Amazon Web Services (AWS).

---

# 📋 Sumário

* [Sobre o Projeto](#-sobre-o-projeto)
* [Arquitetura](#-arquitetura-do-sistema)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Funcionamento](#-funcionamento)
* [Principais Características](#-principais-características)
* [Grupo 4 (AWS re/Start)](#-grupo-4-aws-restart)

---

# 📖 Sobre o Projeto

O **AWS Contador Serverless** é uma aplicação desenvolvida para registrar e contabilizar cliques de usuários em landing pages de forma segura, escalável e totalmente serverless.

A arquitetura elimina a necessidade de gerenciamento de servidores, permitindo que a infraestrutura escale automaticamente conforme a demanda. O contador é atualizado em tempo real por meio de operações atômicas no banco de dados, garantindo consistência mesmo sob alto volume de acessos simultâneos.

---

# 🎯 O Problema e a Solução

O projeto simula o cenário de uma startup lançando uma campanha inédita com tráfego imprevisível. Como métricas indicam que 53% dos visitantes abandonam páginas que demoram mais de três segundos para carregar, a performance é crítica. Para evitar gargalos de lentidão e travamentos sob demanda repentina, desenvolvemos essa arquitetura 100% serverless. Ela garante resiliência e tempos de resposta na casa dos milissegundos, escalando instantaneamente para absorver desde dezenas até milhões de acessos.  

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
* Python

## Banco de Dados

* Amazon DynamoDB

## Infraestrutura

* Amazon S3
* Amazon API Gateway
* AWS IAM

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

Pré-requisitos:
- AWS CLI instalada e configurada com suas credenciais.

Passo a Passo (Deploy Automatizado):
1. Clone o repositório.
2. Pelo terminal, execute o script de automação (deploy.sh ou deploy.bat) localizado na raiz do projeto. O pipeline do script fará o seguinte trabalho pesado:
- Provisionamento do back-end e S3 via CloudFormation.
- Extração dinâmica da URL da API gerada.
- Injeção automática do endpoint no script.js do front-end.
- Sincronização e upload dos arquivos web para o bucket S3.

3. Acesse a URL pública do site que será exibida no console ao final da execução.

---

# 👥 Grupo 4 (AWS re/Start)

* **Bruno Ruan Lima Da Silva** – GitHub | LinkedIn
* **Christopher Bernardes Viana** – GitHub | LinkedIn
* **David Bezerra Da Silva** – GitHub | LinkedIn
* **Natan Ferreira Dos Santos** – GitHub | LinkedIn
* **Gustavo Ramalho Matioli** – GitHub | LinkedIn
* **Leticia Mikaeli Alves dos Santos** – GitHub | LinkedIn

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais durante o programa **AWS re/Start**.