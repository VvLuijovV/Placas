import re
import platform
import os

#----------------------------------------------------------------
# Limpia la pantalla antes de iniciar el programa
if( platform.system() == "Windows" ):
    os.system( "cls" ) # Comando para Windows
else:
    os.system( "clear" ) # Comando en caso de que la maquina sea Linux o Mac
    
#----------------------------------------------------------------

# Funcion encargada de mostrar el resultado segun lo ingresado por el usuario

def Resultado( tipo_de_placa ):
	if ( tipo_de_placa != "__ERROR__" ):
		print( "\nLa placa pertenece a", tipo_de_placa, "\n" )
	else:
		print("\nPlaca irreconocida")

#----------------------------------------------------------------

class Placa: #Clase Placas aqui se procesa el resultado final

    def ProcesoPlaca(self):
        placa_beta = input( "\nIngresar placa: " ) # <--------Entrada de texto para el usuario----
        placa_alfa = placa_beta.upper()		# <----- En caso de que el usuario introduzca letras minusculas las lleva a mayuscula-----
        if re.match( "(^([A-Z]){2}|[0-9]{2})[0-9]{4}$", placa_alfa ): # Condicion para que se valide la entrada del usuario de la siguiente manera:
            print( "\nEntrada correcta" )					   # Si empieza con dos Letras o dos numeros y luego cuatro numeros pasa,
            											   # sino, enviara el mensaje de error
            if re.match( "^MA([A-Z]|[0-9])+$", placa_alfa ):
                tipo_de_placa="una motocicleta"
            
            elif re.match( "^MB[0-9]+", placa_alfa ):
                tipo_de_placa=( "un MetroBus" )
            
            elif re.match( "^T([A-Z]|[0-9])+", placa_alfa ):
                tipo_de_placa=( "un taxi" )
            
            elif re.match( "^E[A-Z][0-9]+", placa_alfa ):
                typtipo_de_placae=( "un vehiculo fiscal o judicial" )
                
            elif re.match( "^CP[0-9]+", placa_alfa ):
                tipo_de_placa=( "un vehiculo del canal" )
            
            elif re.match( "^B[0-9]+$", placa_alfa ):
                tipo_de_placa=( "un Bus" )
            
            elif re.match( "^HP[0-9]+", placa_alfa ):
                tipo_de_placa=( "un radioaficionado" )
            
            elif re.match( "^A[A-G][0-9]+$", placa_alfa ):
                tipo_de_placa=( "un auto regular" )
            
            elif re.match( "^CC[0-9]+$", placa_alfa ):
                tipo_de_placa=( "un cuerpo consular" )
            
            elif re.match( "[0-9]+$", placa_alfa ):
                tipo_de_placa = ( "una serie antigua..." )
            
            elif re.match( "^PR[0-9]+", placa_alfa ):
                tipo_de_placa = ( "un auto de prensa" )
                
            else:
                tipo_de_placa = ( "__ERROR__" ) # En caso de que la placa ingresada cumpla con la sintaxis pero no pertenezca a ninguna serie valida
            Resultado( tipo_de_placa )
        else:
            print( "\nLa serie ingresada no es correcta, por favor verifique\n" ) # Mensaje de error

placa=Placa()

#----------------------------------------------------------------

if __name__=="__main__":
	# Justo despues de limpiar la pantalla se imprimira esta pequeña ayuda
    print("\nEl formato para las placas a ingresar son los siguientes")
    print("\n\nMoto:            MA####\nAuto Regular:    (A-G)(A-G)####")
    print("Autos de prensa: PR####\nCuerpo Consular: CC####")
    print("Radioaficionado: HP####\nBus:             B(A-Z)####")
    print("Fiscal :         E(A-Z)####\nTaxi:            T(A-Z)####\nMetroBus:        MB####")
    print("Las series de placas antiguas se conforman de 6 numeros.")
    print("\n\n")
    placa.ProcesoPlaca()
