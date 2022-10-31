class Drinkable
{
    ##Atributos##
    
    name=""               #nombre del bebestible
    code=0                #codigo de barra del bebestible
    sale_price=0          #valor del bebestible
    expiration_date=0     #fecha de expiracion del bebestible
    ML=0                  #la cantidad de Mililitros que contiene el embase
    stock=0               #stock del bebestible en la tienda
    sale_restriction=0    #la edad necesaria para la compra del bebestible
    type=""               #si es alcoholica y/o fantasia 
    brand=""              #marca del bebestible
    material=""           #material del embase
    seals=                #manda un True o False segun si contiene sellos o no 
    
    
    ##Fin seccion de Atributos##
    
    ##Metodos##
    
    update_stock()            #actualizacion stock del bebestible que hay en la botilleria
    order_expiration_date()   #ordenar en estantes segun fecha de vencimiento
    total_sales()             #las ventas totales de un dia 
    selling_price_update()    #actualizacion precio del bebestible
    payment_method()          #el metodo por el cual se pago el bebestible
    
    ##Fin seccion de Metodos##
}
