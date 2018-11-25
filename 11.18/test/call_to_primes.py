#----- Incorporación de código Fortran

# se usa un script denominado F2PY (Fortran 2 PYthon)
# se "compilan" los archivos Fortran con el script f2py

import primes # importo las funciones de 'primes' (Fortran)

# defino el intervalo sobre la que quiero obtener numeros primos
sieve_array = primes.sieve(150) 

# obtengo los numeros primos para dicho rango
prime_numbers = primes.logical_to_integer(sieve_array, sum(sieve_array))

print("Numeros Primos del 1 al 100: \n",prime_numbers)

#------ Incorporación de código C

from ctypes import *

mylib = CDLL("./libflags.so")

primes_digits_sum=[] # listados donde se almacenaran numeros primos cuyos digitos sumen x

for prime in prime_numbers:	
	if mylib.digits_sum(int(prime), 5) != 0: # se llama a una de las funciones de la librería de C 
		primes_digits_sum.append(prime) # se agrega el resultado a la lista
		

print ("Listado de Numeros primos cuyos dígitos suman 5\n", primes_digits_sum)