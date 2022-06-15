var ordenes= [
  {nombre:"Collar antipulgas perro mediano" , estado:"EN CAMINO", clase:"estadoAzul"},
  {nombre:"Vitaminas reconstructivas" , estado:"EN CAMINO",clase:"estadoAzul"},
  {nombre:"Purina pro plan adulto" , estado:"EN CAMINO",clase:"estadoAzul"},
  {nombre:"Adorno navideño" , estado:"ENTREGADO",clase:"estadoVerde"},
  {nombre:"Plato pequeño" , estado:"ENTREGADO",clase:"estadoVerde"},
  {nombre:"Chaleco perro pequeño" , estado:"EN CAMINO",clase:"estadoAzul"},
]


var acomulador_texto=""

ordenes.forEach((element, index) => {

    var html_producto = `
    <tr>
      <th scope="row">${index}</th>
      <td>${element.nombre}</td>
      <td class="${element.clase}">${element.estado}</td>
    </tr>`
    
    acomulador_texto += html_producto
    $("#ConsultaSeguimientoTres").html( acomulador_texto )
});