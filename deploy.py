import boto3
import time
import os
import re
import mimetypes
from botocore.exceptions import ClientError

# ---------------- CONFIGURAÇÕES ---------------- #
REGION = 'us-east-1'
STACK_NAME = 'contador-serverless-grupo4'
TEMPLATE_PATH = 'iac/template.yaml'
FRONTEND_DIR = 'frontend'
# ----------------------------------------------- #

def main():
    print("="*50)
    print("🚀 INICIANDO PIPELINE DE DEPLOY SERVERLESS")
    print("="*50)

    # 1. Instanciando os clientes boto3
    cf_client = boto3.client('cloudformation', region_name=REGION)
    s3_client = boto3.client('s3', region_name=REGION)

    # 2. Lendo o template CloudFormation
    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            template_body = f.read()
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado em '{TEMPLATE_PATH}'.")
        return

    # 3. Executando o Deploy da Infraestrutura
    print(f"\n[1/4] Avaliando a stack CloudFormation '{STACK_NAME}'...")
    waiter = None
    try:
        cf_client.create_stack(
            StackName=STACK_NAME,
            TemplateBody=template_body,
            Capabilities=['CAPABILITY_NAMED_IAM']
        )
        print("Criando nova infraestrutura...")
        waiter = cf_client.get_waiter('stack_create_complete')
    except ClientError as e:
        if 'AlreadyExistsException' in str(e):
            try:
                cf_client.update_stack(
                    StackName=STACK_NAME,
                    TemplateBody=template_body,
                    Capabilities=['CAPABILITY_NAMED_IAM']
                )
                print("Atualizando infraestrutura existente...")
                waiter = cf_client.get_waiter('stack_update_complete')
            except ClientError as update_e:
                if 'No updates are to be performed' in str(update_e):
                    print("Nenhuma alteração na infraestrutura necessária.")
                else:
                    raise update_e
        else:
            raise e

    if waiter:
        print("⏳ Aguardando a AWS provisionar os recursos (isso pode levar alguns minutos)...")
        waiter.wait(StackName=STACK_NAME)
        print("✅ Infraestrutura provisionada/atualizada com sucesso!")

    # 4. Extração dos Outputs diretamente da Stack
    print("\n[2/4] Extraindo Outputs e metadados da nuvem...")
    response = cf_client.describe_stacks(StackName=STACK_NAME)
    outputs = response['Stacks'][0].get('Outputs', [])
    
    api_endpoint = None
    website_url = None
    bucket_name = None

    for out in outputs:
        if out['OutputKey'] == 'ApiEndpoint':
            api_endpoint = out['OutputValue']
        elif out['OutputKey'] == 'WebsiteURL':
            website_url = out['OutputValue']
        elif out['OutputKey'] == 'BucketName':
            bucket_name = out['OutputValue']

    print(f"🔗 API Endpoint gerado: {api_endpoint}")
    print(f"🪣 Bucket S3 de destino: {bucket_name}")

    # 5. Injeção Dinâmica Idempotente da URL no Front-end (Regex)
    print("\n[3/4] Injetando variáveis no ambiente local...")
    script_path = os.path.join(FRONTEND_DIR, 'script.js')
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()

        # Isso funciona perfeitamente mesmo que o script seja executado 100 vezes seguidas.
        padrao_regex = r"const API_URL = '.*?';"
        nova_linha_url = f"const API_URL = '{api_endpoint}/contador';"
        
        script_content_updated = re.sub(padrao_regex, nova_linha_url, script_content)

        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(script_content_updated)
        print(f"✅ Arquivo {script_path} atualizado via Regex com sucesso.")
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo {script_path} não encontrado na pasta local.")
        return

    # 6. Upload dos Arquivos (S3 Sync)
    print("\n[4/4] Sincronizando arquivos com o S3...")
    for root, dirs, files in os.walk(FRONTEND_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, FRONTEND_DIR).replace('\\', '/')

            content_type, _ = mimetypes.guess_type(file_path)
            if content_type is None:
                content_type = 'application/octet-stream'

            print(f"Enviando {s3_key} ({content_type})...")
            s3_client.upload_file(
                file_path,
                bucket_name,
                s3_key,
                ExtraArgs={'ContentType': content_type}
            )
    print("✅ Sincronização concluída.")

    # 7. Finalização
    print("\n" + "="*50)
    print("🎉 DEPLOY CONCLUÍDO COM SUCESSO!")
    print(f"🌐 Acesse a aplicação na web: {website_url}")
    print("="*50 + "\n")

if __name__ == '__main__':
    main()
