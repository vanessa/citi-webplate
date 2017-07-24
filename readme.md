# CITi Webplate

1. Crie um diretório configurado com um ambiente virtual e instale o Django nele

2. `django-admin startproject your_project_name . --extension py,json --name gulpfile.js --template=/path/to/citi-webplate/`

3. `npm install`

4. Crie um arquivo `project_config.json` que contenha pares de chave/valor das seguintes variáveis de configuração: SECRET_KEY

5. `export PROJECT_CONFIG="/path/to/project_config.json"`

6. Para rodar em ambiente de desenvolvimento: `gulp runserver`
