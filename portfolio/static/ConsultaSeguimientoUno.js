var ordenes= [
  {nombre:"Plato pequeño" , estado:"ENTREGADO", clase:"estadoVerde"},
  {nombre:"Chaleco perro pequeño" , estado:"EN CAMINO",clase:"estadoAzul"},
  {nombre:"Vitaminas reconstructivas" , estado:"PROCESANDO COMPRA",clase:"estadoPurpura"},
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
    $("#ConsultaSeguimientoUno").html( acomulador_texto )
});