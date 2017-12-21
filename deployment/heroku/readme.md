# Deployment no Heroku

1. Crie uma nova aplicação através da Dashboard do Heroku;

2. Na aba `Resources` da página do projeto, adicione os seguintes add-ons ao seu projeto:
    * `Heroku Postgres`, para adicionar um banco de dados PostgreSQL;
    * `SendGrid`, (opcional, caso não seja adicionado, e-mails serão enviados para o console da aplicação) para adicionar as funcionalidades de e-mail via SendGrid (necessário ter um cartão de crédito cadastrado);

3. Na aba `Settings` do projeto, clique no botão `Reveal Config Vars` para poder adicionar variáveis de ambiente ao projeto. Adicione as seguintes:
    * `DJANGO_SETTINGS_MODULE` (obrigatória, deve conter o valor `{{ project_name }}.settings.production`);
    * `SECRET_KEY` (obrigatória, a mesma que você gerou em ambiente de desenvolvimento);
    * `RECIPIENT_EMAIL` (opcional, indica para qual endereço de e-mail serão enviadas as mensagens via formulário na app `contact` e tem como valor padrão `recipient@{{ project_name }}.com`);
    * `AWS_REGION` (obrigatória para usar o Amazon S3, representa a região onde está localizado o seu repositório do DigitalOcean Spaces);
    * `AWS_S3_ACCESS_KEY_ID` (obrigatória para usar o Amazon S3, representa a chave pública do seu repositório do DigitalOcean Spaces);
    * `AWS_S3_SECRET_ACCESS_KEY` (obrigatória para usar o Amazon S3, representa a chave privada do seu repositório do DigitalOcean Spaces);
    * `AWS_STORAGE_BUCKET_NAME` (obrigatória para usar o Amazon S3, representa o bucket do seu repositório do DigitalOcean Spaces);

4. Na mesma aba, adicione o buildpack de `Python`;

5. Na aba `Deploy`, escolha o método de deployment através do GitHub, fornecendo o nome do repositório do seu projeto no GitHub;

6. Escolha uma branch para deployments automáticos em cada modificação no repositório do GitHub (você também pode optar por só efetuar o deployment após as realizações do teste da Integração Contínua, caso seu repositório tenha essa funcionalidade habilitada);

7. Clique em `Deploy Branch` para realizar seu primeiro deploy. Caso tudo tenha sido realizado corretamente, sua aplicação já estará executando no endereço criado pelo Heroku para o projeto.
