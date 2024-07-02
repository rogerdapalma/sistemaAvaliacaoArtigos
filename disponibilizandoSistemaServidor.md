# Disponibilizando no servidor linux

Necessidade de serviços instalados:
1) nginx
2) gunicorn
3) mysql
4) ssh liberado
5) python
6) git

Primeiros passos:
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


#
## comandos
- ssh alexz@labinf.ufn.edu.br
- password
- cd/var/www
- ls
- sudo mkdir saoa.labinf.ufn.edu.br
- passworld
- cd saoa.labinf.ufn.edu.br/
- git clone : link (negado)
- sudo git clone : (aceito)
- cd saoa
- python --version
- python
- sudo python3.10 -m venv venv 
    - cd .. cd..
    - sudo chown alexz:www-data
    - history |grep chown
    - sudo chown alexz:www-data -R saoa.labinf.ufn.edu.br   (o dono vai ser o alexz e o grupo sera www-data)
- cd saoa.labinf.ufn.edu.br
- ls -l
- rm -r venv
- ls
- virtualvenv -p python3.10 venv
- source venv/bin/activate
- python -m pip install --upgrade pip
    - deactvate
- rm -r venv/
- virtualvenv -p python3.10 venv
- sudo apt-get upgrade/update(repositorio do ubunto, la onde ele busca)
- sudo apt-get install python3.11
- 
