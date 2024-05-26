document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('opciones').addEventListener('change', function() {
    let get = 'http://localhost:8000/consultas?tabla=';
    fetch(get + this.value) 
      .then( res => {
        if (!res.ok) 
          throw new Error('Problema al obtener datos');
        return res.json();
      } )
      .then ( datos => {
        let contenido = encabezado(datos) + cuerpo(datos);
        document.getElementById('tabla_contenido').innerHTML = contenido;
      } )
      .catch(err => {
        console.log('Capturé:\n', err);
      });

  });
});

function encabezado(data) {
  let str='';
  for (key in data[0])
    str+=`<th>${key}</th>`

  return `<thead><tr>${str}</tr></thead>`
}

function cuerpo(data) {
  str = '';
  data.forEach((dato) => {
    let tr = '<tr>';
    Object.values(dato).forEach((value) => {
      tr+=`<td>${value}</td>`;
    });
    str += tr + '<tr>';
  });
  return str;
}
