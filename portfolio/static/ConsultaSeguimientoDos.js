var ordenes= [
  {nombre:"Adorno navideño" , estado:"ENTREGADO", clase:"estadoVerde"},
  {nombre:"Collar antipulgas perro mediano" , estado:"EN CAMINO",clase:"estadoAzul"},
  {nombre:"Purina pro plan adulto" , estado:"ENTREGADO",clase:"estadoVerde"},
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
    $("#ConsultaSeguimientoDos").html( acomulador_texto )
});