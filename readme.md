# CITi Webplate

0. É necessário ter instalado o [npm](https://www.npmjs.com/get-npm) no seu computador. Feito isso, execute `npm install -g gulp-cli` para instalar o `gulp` global em seu ambiente

1. Crie um diretório configurado com um ambiente virtual, em seguida `pip install django`

2. `django-admin startproject your_project_name . --extension py,json --name gulpfile.js --template=https://github.com/citiufpe/citi-webplate/archive/master.zip`

3. `pip install -r requirements.txt`

4. `npm install`

5. Crie um arquivo `project_config.json` que contenha pares de chave/valor das seguintes variáveis de configuração: `SECRET_KEY` (você pode gerar uma chave neste [link](http://www.miniwebtool.com/django-secret-key-generator/)).

  Exemplo de arquivo:
  ```
  {
    "SECRET_KEY": "valor da chave secreta",
    "CHAVE_X": "valor da chave 2",
  }
  ```

6. `export YOUR_PROJECT_NAME_CONFIG="/path/to/project_config.json"` (no Windows use `set YOUR_PROJECT_NAME_CONFIG=\path\to\project_config.json`) (é necessário que o `YOUR_PROJECT_NAME_CONFIG` esteja com todas as letras maiúsculas)

7. `python manage.py makemigrations --settings=your_project_name.settings.development`

8. `python manage.py migrate --settings=your_project_name.settings.development`

9. Para rodar em ambiente de desenvolvimento: `gulp runserver`
