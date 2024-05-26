console.log('Hola mundo');
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('opciones').addEventListener('change', function() {
    let seleccionado = this.value;
    console.log(seleccionado);
    let get = 'http://localhost:8000/consultas?tabla=';
    fetch(get + this.value) 
      .then( res => {
        if (!res.ok) 
          throw new Error('Problema al obtener datos');
        return res.json();
      } )
      .then ( datos => {
        for (let key in datos[0])
          console.log(key);
      } )
      .catch(err => {
        console.log('Capturé:\n', err);
      });

  });
});
