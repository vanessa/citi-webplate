# CITi Webplate

1. Crie um diretório configurado com um ambiente virtual, em seguida `pip install django`

2. `django-admin startproject your_project_name . --extension py,json --name gulpfile.js --template=https://github.com/citiufpe/citi-webplate/archive/master.zip`

3. `pip install -r requirements.txt`

4. `npm install`

5. Crie um arquivo `project_config.json` que contenha pares de chave/valor das seguintes variáveis de configuração: `SECRET_KEY` (você pode gerar uma chave neste [link](www.miniwebtool.com/django-secret-key-generator/))

6. `export YOUR_PROJECT_NAME_CONFIG="/path/to/project_config.json"` (no Windows use `set YOUR_PROJECT_NAME_CONFIG=\path\to\project_config.json`)

7. `python manage.py makemigrations --settings=your_project_name.settings.development`

8. `python manage.py migrate --settings=your_project_name.settings.development`

9. Para rodar em ambiente de desenvolvimento: `gulp runserver`
