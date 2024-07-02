# Disponibilizando no servidor linux

## Necessidade de serviços instalados:
1) nginx
2) gunicorn
3) mysql
4) ssh liberado
5) python
6) git

## Primeiros passos:
1) acessar o servidor via ssh
2) criar a pasta para receber o repositorio
    - Políticas ou boas praticas da Infraestruturas UFN
    1) sistemas devem estar em var/www
    2) nome da pasta do sistema deve ser saoa.labinf.ufn.edu.br
3) clonar o projeto do github no servidor
4) criar a venv
    - usar virtualenv:-p python3.10 venv (pois o servidor contem python2.7)
5) ativa venv:source venv/bomd/activate (pois é em linux)
6) instala pacotes

## Passos de configuração

# Passos para disponibilizar sistema em servidor linux

Acesso remoto via SSH

Necessário a instalação e configuração do:
    - Gunicorn - https://gunicorn.org/ - is a Python WSGI HTTP Server for UNIX.
    - Nginx - https://www.nginx.com/ - is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.

Clonar o projeto na pasta desejada, em geral, uma boa prática é em /var/www/urlCriada/saoaClonado

Criar e levantar a venv, e instalar os requirements.txt

### GUNICORN 

- criar o arquivo /etc/systemd/system/saoa.service
```ini
[Unit]
Description=saoa daemon
After=network.target

[Service]
User=usuarioServidor
Group=www-data
WorkingDirectory=/var/www/saoa.labin.ufn.edu.br/saoa/projeto
ExecStart=/var/www/saoa.labin.ufn.edu.br/saoa/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/saoa.labin.ufn.edu.br/saoa/projeto/saoa.sock projeto.wsgi:application
```

- Iniciar o parser gunicorn:
    - sudo systemctl start saoa

    - Adicionar o sistema como serviço reconhecido no sistema:
        - sudo systemctl enable saoa

### Nginx

Esse é o roteiro para criar outros serviços virtuais, ai e só substituir saoa.labin.ufn.edu.br pelo  domínio que tu vai utilizar sem www (por exemplo, comic.labinf.ufn.edu.br)
 
Crie o diretório para examplo.com como a seguir, usando o flag -p para criar qualquer diretório pai necessário:
 
- sudo mkdir -p /var/www/saoa.labin.ufn.edu.br/examplo.com/
  
Para que o Nginx sirva esse conteúdo, é necessário criar um bloco de servidor com as diretivas corretas. 
Em vez de modificar o arquivo de configuração padrão diretamente, vamos criar um novo em 

- /etc/nginx/sites-available/saoa.labin.ufn.edu.br:
 
- sudo vim /etc/nginx/sites-available/saoa.labin.ufn.edu.br
Cole dentro o seguinte bloco de configuração, que é similar ao padrão, mas atualizado para nosso novo diretório e nome de domínio:
 
- /etc/nginx/sites-available/saoa.labin.ufn.edu.br
```ini
server {
        server_name comic.lapinf.ufn.edu.br www.comic.lapinf.ufn.edu.br;
        client_body_in_file_only clean;
        client_body_buffer_size 32K;
        client_max_body_size 2512M;


        #aceitar arquivos grande via get
        client_header_buffer_size 3232k;
        large_client_header_buffers 4 3232k;
        sendfile on;
        send_timeout 900s;
        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                expires 30d;
                access_log off;
                break;
                alias /var/www/comic.lapinf.ufn.edu.br/comic/projeto/projeto/static;
        }

        location / {
                client_max_body_size 2048M;
                include proxy_params;
                proxy_pass http://unix:/var/www/comic.lapinf.ufn.edu.br/comic/comic.sock;
        }
} 
```
Observe que atualizamos a configuração root para corresponder ao nosso novo diretório e 
server_name ao nosso nome de domínio.
 
A seguir, vamos ativar o arquivo através da criação de um link dele para o diretório sites-enabled, 
a partir do qual o Nginx lê durante a inicialização:
 
- sudo ln -s /etc/nginx/sites-available/saoa.labin.ufn.edu.br /etc/nginx/sites-enabled/
 
Depois, teste para certificar-se de que não existem erros de sintaxe em quaisquer de seus arquivos do Nginx:
 
- sudo nginx -t
Salve e feche o arquivo quando tiver terminado.
 
Se não houver problemas, reinicie o Nginx para ativar suas alterações:
 
- sudo systemctl restart nginx

### Obtendo um Certificado SSL
 
- sudo certbot --nginx -d saoa.labin.ufn.edu.br -d www.saoa.labin.ufn.edu.br
 
Se isso for bem sucedido, o certbot perguntará como você gostaria de definir suas configurações de HTTPS.
Usa 2 para sempre redirecionar para SSL

```markdown
Output
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
-------------------------------------------------------------------------------
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
-------------------------------------------------------------------------------
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
Selecione a sua escolha e pressione ENTER. A configuração será atualizada, e o Nginx irá recarregar para pegar as novas configurações. O certbot irá terminar com uma mensagem informando que o processo foi bem-sucedido e onde os seus certificados estão armazenados:
```
```markdown
Output
IMPORTANT NOTES:
- Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/saoa.labin.ufn.edu.br/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/saoa.labin.ufn.edu.br/privkey.pem
   Your cert will expire on 2018-07-23. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
- Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
- If you like Certbot, please consider supporting our work by:
 
   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
  Donating to EFF:                    https://eff.org/donate-le
```
### Criando esquema de BD no MYSQL

PARA VISUALIZAR, SE NECESSÁRIO, OS USUÁRIOS DO MYSQL
```sql
SELECT user FROM mysql.user;

CREATE DATABASE nomeDoSistema_db;

CREATE USER saoa@‘localhost' IDENTIFIED BY ‘senhaDesejada’;

GRANT ALL PRIVILEGES ON saoa_db.* TO saoa@‘localhost' IDENTIFIED BY 'senhaDesejada';

-- Criando o primeiro usuário

--na pasta projeto do sistema, com a venv ativa,
-- rodar migrate
-- python projeto/manage.py shell

from usuario.models import Usuario
u = Usuario()
u.nome = 'Nome do usuario'
u.tipo = 'ADMINISTRADOR'
u.email = 'projetos@ufn.edu.br'
u.is_active = True
u.cpf = '99999999999'
u.save()
u.set_password('projetos@ufn.edu.br')
u.save()

-------------------------------------------
-- Configurar .env o driver do MYSQL
    -- No arquivo .env adicionar:
--.env
DATABASE_URL=mysql://saoa:senhaEscolhida$@127.0.0.1:3306/saoa_db
```
## comandos

```bash
# Conectar ao servidor via SSH
ssh alexz@labinf.ufn.edu.br

# Digitar a senha quando solicitado
password

# Navegar até o diretório /var/www
cd /var/www

# Listar os arquivos e diretórios no diretório atual
ls

# Criar um novo diretório para o projeto saoa.labinf.ufn.edu.br
sudo mkdir saoa.labinf.ufn.edu.br

# Digitar a senha de superusuário (sudo) quando solicitado
password

# Entrar no diretório recém-criado
cd saoa.labinf.ufn.edu.br/

# Clonar o repositório do projeto (se a permissão for negada, tentar com sudo)
git clone : link

# Caso seja necessário usar sudo para clonar o repositório
sudo git clone : link

# Entrar no diretório do projeto clonado
cd saoa

# Verificar a versão do Python instalada
python --version

# Iniciar o interpretador Python
python

# Criar um ambiente virtual usando Python 3.10
sudo python3.10 -m venv venv 

# Navegar de volta ao diretório raiz
cd .. 

# Mudar a propriedade dos arquivos para o usuário alexz e grupo www-data
sudo chown alexz:www-data

# Verificar o histórico para comandos relacionados a `chown`
history | grep chown

# Mudar recursivamente a propriedade dos arquivos do projeto
sudo chown alexz:www-data -R saoa.labinf.ufn.edu.br

# Entrar no diretório do projeto
cd saoa.labinf.ufn.edu.br

# Listar os arquivos detalhadamente
ls -l

# Remover o ambiente virtual `venv`
rm -r venv

# Listar os arquivos após a remoção do ambiente virtual
ls

# Criar um novo ambiente virtual especificando Python 3.10
virtualvenv -p python3.10 venv

# Ativar o ambiente virtual
source venv/bin/activate

# Atualizar o pip no ambiente virtual
python -m pip install --upgrade pip

# Desativar o ambiente virtual
deactivate

# Remover completamente o ambiente virtual
rm -r venv/

# Criar um novo ambiente virtual usando Python 3.10 com sudo
virtualvenv -p python3.10 venv

# Atualizar/Atualizar pacotes no repositório do Ubuntu
sudo apt-get upgrade/update (repositorio do ubunto, la onde ele busca)

# Instalar o Python 3.11
sudo apt-get install python3.11

# Instalar as dependências do projeto listadas no arquivo requirements.txt
pip install -r requirements.txt

# Parar ou iniciar o serviço "projeto"
sudo service projeto stop/start

```
