function Condicion(){

if (document.getElementById("seguimiento_text").value == 2792902){
    location.href="ConsultaSeguimientoUno.html";
}
else if(document.getElementById("seguimiento_text").value == 123456){
    location.href="ConsultaSeguimientoDos.html";
    
}
else if(document.getElementById("seguimiento_text").value == 456789){
    location.href="ConsultaSeguimientoTres.html";
    
}
else if (document.getElementById("seguimiento_text").value !== 2792902 || 123456||456789){
    alert("Su numero de seguimiento no existe, Intentelo otra vez");
    
}
}
document.getElementById("boton_seguimiento").onclick = function(){
    Condicion();
}
