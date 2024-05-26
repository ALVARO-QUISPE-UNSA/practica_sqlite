echo "en el buscador, ingresar a: http://localhost:8000/"
echo "Documento de explicación: https://drive.google.com/open?id=161P63cHeII1AbDA0agc5uEo0OrmYNZlfBA7FE180TSo&usp=drive_copy"
echo "Vídeo: https://drive.google.com/file/d/18y674BYt1fDlhRNDYeCozHwLVEstbBc6/view?usp=sharing"

source bin/activate
cd peliculas/
python manage.py runserver
