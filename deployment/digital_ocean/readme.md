# Deployment no DigitalOcean

1. Após acessar o droplet escolhido via SSH, é necessário inicialmente instalar algumas dependências. Para isso, crie um arquivo `dependencies.sh` contendo o seguinte [conteúdo](https://raw.githubusercontent.com/citiufpe/citi-webplate/master/deployment/digital_ocean/dependencies.sh) e execute `sudo -H dependencies.sh`;

2. Feito isso, acesse o usuário `postgres` do servidor usando `su - postgres`. Neste momento você realizará a configuração do banco de dados. Execute os seguintes comandos:
  ```bash
  createuser POSTGRES_DB_USER
  createdb POSTGRES_DB_NAME --owner POSTGRES_DB_USER
  psql -c "ALTER USER u_urban WITH PASSWORD 'POSTGRES_DB_PASSWORD'"
  exit
  ```
Lembre-se de substituir `POSTGRES_DB_USER`, `POSTGRES_DB_NAME` e `POSTGRES_DB_PASSWORD` pelos valores apropriados (nome do usuário do banco de dados, nome do banco de dados e senha do banco de dados, respectivamente). Guarde bem esses valores, pois serão necessários no futuro;

3. De volta ao usuário `root`, está na hora de criar o usuário responsável pela aplicação. Para isso, execute `adduser USER_NAME`, substituindo `USER_NAME` pelo valor apropriado. Quando solicitado, crie uma senha (e a guarde em local seguro) e em seguida preencha os dados solicitados (ou aperte ENTER para deixá-los vazios) e confirme a criação do mesmo;

4. Adicione o novo usuário ao grupo `sudo` usando `gpasswd -a USER_NAME sudo` e em seguida troque de usuário usando `su - USER_NAME`;

5. Logado no novo usuário, execute `virtualenv .` para criar um ambiente virtual e ative-o usando `source bin/activate`;

6. Clone o repositório do seu projeto para o diretório atual e acesse a pasta do mesmo usando `cd PROJECT_DIR`, substituindo `PROJECT_DIR` pelo nome da pasta do projeto;

7. Instale as dependências do projeto usando `pip install -r requirements.txt`;

8. Crie um arquivo `.env` na pasta atual contendo as seguintes variáveis, seguindo as mesmas especificações da versão de desenvolvimento:
  * `DJANGO_SETTINGS_MODULE` (obrigatória, deve conter o valor `{{ project_name }}.settings.production`);
  * `SECRET_KEY` (obrigatória, a mesma que você gerou em ambiente de desenvolvimento);
  * `RECIPIENT_EMAIL` (opcional, indica para qual endereço de e-mail serão enviadas as mensagens via formulário na app `contact` e tem como valor padrão `recipient@{{ project_name }}.com`);
  * `POSTGRES_DB_NAME` (obrigatória, é o mesmo valor usado no passo 2);
  * `POSTGRES_DB_USER` (obrigatória, idem acima);
  * `POSTGRES_DB_PASSWORD` (obrigatória, idem acima);
  * `SENDGRID_API_KEY` (obrigatória para usar o serviço [SendGrid](https://sendgrid.com/) para enviar e-mails);
  * `AWS_REGION` (obrigatória para usar o Amazon S3, representa a região onde está localizado o seu repositório do DigitalOcean Spaces);
  * `AWS_S3_ACCESS_KEY_ID` (obrigatória para usar o Amazon S3, representa a chave pública do seu repositório do DigitalOcean Spaces);
  * `AWS_S3_SECRET_ACCESS_KEY` (obrigatória para usar o Amazon S3, representa a chave privada do seu repositório do DigitalOcean Spaces);
  * `AWS_STORAGE_BUCKET_NAME` (obrigatória para usar o Amazon S3, representa o bucket do seu repositório do DigitalOcean Spaces);

9. Realize as migrações utilizando `python manage.py migrate`;

10. Execute o `collectstatic` utilizando `python manage.py collectstatic --noinput`;

11. Em seguida, vá para o diretório `deployment/digital_ocean` e lá execute `sudo bash setup.sh PROJECT_DIR USER_NAME IP_ADDRESS`, onde `PROJECT_DIR` é o nome da pasta onde está o arquivo `manage.py`, `USER_NAME` é o nome do usuário atual e `IP_ADDRESS` é o endereço de IP onde o servidor está rodando;

12. Ao fim do passo anterior, você deverá estar deslogado do servidor acessado via SSH. No seu browser, acesse a URL composta pelo `IP_ADDRESS` do projeto. Caso o site esteja no ar, parabéns, o deployment foi concluído com sucesso;

13. Caso deseje realizar alguma atualização futura no código, basta acessar o servidor, alterar o usuário para `USER_NAME` e mudar o diretório para `PROJECT_DIR`. Lá, realize um `pull` no seu projeto, execute o `collectstatic` e o `migrate` novamente e por fim, `sudo supervisorctl restart PROJECT_DIR`.
