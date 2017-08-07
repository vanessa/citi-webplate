# CITi Webplate

0. É necessário ter instalado o [npm](https://www.npmjs.com/get-npm) no seu computador. Feito isso, execute `npm install -g gulp-cli` para instalar o `gulp` global em seu ambiente

1. Crie um diretório configurado com um ambiente virtual, em seguida `pip install django`

2. `django-admin startproject your_project_name . --extension py,json --name gulpfile.js --template=https://github.com/citiufpe/citi-webplate/archive/master.zip`

3. `pip install -r requirements.txt`

4. `npm install`

5. Crie variáveis de ambiente para configurar o seu ambiente utilizando o comando `export VARIABLE_NAME="value"` (no Windows use `set VARIABLE_NAME=value`). Lembre-se de subsituir `VARIABLE_NAME` pelo nome da variável e `value` pelo respectivo valor. As variáveis que devem ser criadas são as seguintes:

* `SECRET_KEY` (você pode gerar uma chave neste [link](http://www.miniwebtool.com/django-secret-key-generator/), certifique-se de que a chave gerada não começa com o caractere `!`)

* `EMAIL_HOST_USER` (representa o seu e-mail)

* `EMAIL_HOST_PASSWORD` (representa a senha do seu e-mail)

* `EMAIL_HOST` (representa o provedor do e-mail, use `smtp.gmail.com` para o Gmail)

* `EMAIL_PORT` (representa a porta de envio do e-mail, use `587` para o Gmail)

Caso você use o Gmail, é necessário realizar algumas configurações a mais no próprio site do serviço. Clique [aqui](https://www.codingforentrepreneurs.com/blog/use-gmail-for-email-in-django/#allow-less-secure-apps) para ver mais detalhes.

6. `python manage.py makemigrations --settings=your_project_name.settings.development`

7. `python manage.py migrate --settings=your_project_name.settings.development`

8. Para rodar em ambiente de desenvolvimento: `gulp runserver`
