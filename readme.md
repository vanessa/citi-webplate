# CITi Webplate

## Ambiente de Desenvolvimento

0. É necessário ter instalado o [npm](https://www.npmjs.com/get-npm) no seu computador. Feito isso, execute `npm install -g gulp-cli` para instalar o `gulp` global em seu ambiente;

1. Crie um diretório configurado com um ambiente virtual, em seguida `pip install Django==1.11.3`;

2. Dentro do ambiente virtual, execute `django-admin startproject your_project_name . --extension py,json --name gulpfile.js --template=https://github.com/citiufpe/citi-webplate/archive/master.zip`;

3. Execute `pip install -r requirements/development.txt` e em seguida `npm install`;

4. Crie um arquivo `environment.py` na pasta raiz do seu projeto (lembre-se de manter o arquivo fora do controle de versão), contendo as seguintes variáveis:
  * `SECRET_KEY` (obrigatória, você pode gerar uma chave neste [link](http://www.miniwebtool.com/django-secret-key-generator/), certifique-se de que a chave gerada não começa com o caractere !);
  * `SENDER_EMAIL` (opcional, indica qual endereço de e-mail será usado para enviar mensagens na app `contact` e tem como valor padrão `no-reply@your_project_name.com`);

5. Execute `python manage.py makemigrations` e `python manage.py migrate`;

6. Para rodar, execute `gulp runserver`.

## Testando

Em breve...

## Deployment

Em breve...
