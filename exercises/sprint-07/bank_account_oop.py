from datetime import datetime


"""
1. Crea una clase Account() que represente una cuenta bancaria con los siguientes
atributos:

bank para el nombre del banco.
acc_id para la ID de la cuenta.
holder_id para la ID del titular.
balance para el saldo inicial de la cuenta.
start_date para la fecha y hora en que se abrió la cuenta.
Asegúrate de que balance sea del tipo float y tenga un valor predeterminado de 0.0.. 
Para establecer un valor y tipo de 'balance' predeterminados, pasa la información
dentro de __init__(). Este es un ejemplo donde establecemos un valor inicial de 32 y
el tipo int en strength:

def __init__(self, strength:int=32):
Cuando se inicia una instancia de la clase Account(), esta debe registrar
automáticamente la fecha y hora en que se abre la cuenta y almacenar estos datos como
start_date. Para hacerlo, deberás importar el módulo datetime del paquete datetime:

from datetime import datetime
Una vez que lo hayas importado, puedes utilizar su método de clase now() para crear
una marca temporal a partir de la fecha y la hora reales como esta:

from datetime import datetime

datetime.now()

2. Agrega dos métodos, deposit() (depositar) y withdraw() (retirar), los cuales toman
argumentos flotantes y afectan el balance en consecuencia. El método deposit()
aumenta el balance, mientras que el método withdraw() lo disminuye; ambos métodos
esperan que la entrada amount sea del tipo float.

3. Agrega un método para obtener el número de teléfono de un banco determinado. Por
ejemplo, este método puede conectarse online, obtener el número de teléfono del banco
e imprimirlo. Por motivos de simplicidad, te pedimos que implementes esta
funcionalidad creando un método estático bankphone. Este método debe tomar un nombre
de banco e imprimir siempre 1-000-1234567 como salida.

Observa que en el precódigo agregamos alguna descripción para el método estático que
te pedimos que crees con el siguiente texto: imprimir el número del banco.

4. Supongamos que necesitamos una forma rápida de añadir una cuenta utilizando una
cadena que almacene las ID de la cuenta y del titular, por ejemplo, tenemos una
cadena "001/2406".

Para lograrlo, debes crear el método de clase quick(). Este método debe esperar una
cadena con las ID de cuenta y titular, separarlas y almacenar cada valor
correspondiente en las variables acc_id y holder_id.

Luego, el método debe devolver la clase, donde bank siempre es default_bank, seguido
de acc_d, holder_id y, finalmente, un balance de 0.0, en ese orden.

5. Es hora de usar la clase. Crea una instancia llamada first (primera) usando la
forma predeterminada con la siguiente información: el nombre del banco es
old_trusty, la identificación de la cuenta es 001, la identificación del titular es
10043 y la suma inicial es 500. Luego deposita 250 unidades más y retira 400. Imprime
el saldo 'balance'.

Posteriormente, crea otra instancia llamada second utilizando el método quick()
pasando '002/10123' como entrada. Imprime el año de creación de la cuenta (para ello,
es importante recordar que las instancias datetime tienen un atributo year).
"""

class Account:
    def __init__(self, bank, acc_id, holder_id, balance:float=0.0):
        self.bank = bank
        self.acc_id = acc_id
        self.holder_id = holder_id
        self.balance = balance
        self.start_date = datetime.now()
    def deposit(self, amount:float):
        self.balance += amount        
        
    def withdraw(self, amount:float):
        self.balance -= amount
    
    @staticmethod
    def bankphone(bank: str):
        '''
        imprime el número del banco
        '''
        print("1-000-1234567")
    
    @classmethod
    def quick(cls, string):
        '''
        crea una cuenta a partir de una cadena
        usando solo las identificaciones de cuenta y titular
        separadas por una barra
        '''
        acc_id, holder_id = string.split("/")
        return cls("default_bank", acc_id, holder_id, 0.0)
    
first = Account("old_trusty", "001", "10043", 500)  # crea la primera cuenta
first.deposit(250) # llama al método deposit
first.withdraw(400) # llama al método withdraw
print(first.balance) # imprime el saldo

second = Account.quick('002/10123') # crea la segunda cuenta
print(second.start_date.year) # imprime el año
