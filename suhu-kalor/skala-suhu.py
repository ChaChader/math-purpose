#skala
print('program ini dijalankan untuk mengkonversikan suhu')
def cr() -> str:
    celsius = float(input('masukan celsius: '))
    print('oR = (4/5) *', celsius)
    reamur = (4/5) * celsius
    hasil = f'suhu dalam reamur adalah:  {reamur} oR'
    return hasil

def ck()-> str:
    celsius = float(input('masukan celsius: '))
    print('oK =', celsius, '+ 273')
    kelvin = celsius + 273
    hasil = f'suhu dalam kelvin adalah:  {kelvin} oK'
    return hasil

def cf()-> str:
    celsius = float(input('masukan celsius: '))
    print('oF = (9/5) *', celsius, '+ 32')
    fahrenheit = (9/5) * celsius + 32
    hasil = f'suhu dalam fahrenheit adalah: {fahrenheit} oF'
    return hasil

def rc()-> str:
    reamur = float(input('masukan reamur: '))
    print('oC = (5/4) *', reamur)
    celsius = (5/4) * reamur
    hasil = f'suhu dalam celsius adalah:  {celsius} oC'
    return hasil
 
def rk()-> str:
    reamur = float(input('masukan reamur: '))
    print('oK = (4/5) *', reamur, '+ 273')
    kelvin = (5/4) * reamur + 273
    hasil = f'suhu dalam kelvin adalah: {kelvin} oK'
    return hasil

def rf()-> str:
    reamur = float(input('masukan reamur: '))
    print('oF = (9/4) *', reamur, '+ 32')
    fahrenheit = (9/4) * reamur + 32
    hasil = f'suhu dalam fahrenheit adalah: {fahrenheit} oF'
    return hasil

def fc()-> str:
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oC = (5/9) *', fahrenheit, '- 32')
    celsius = (5/9) * (fahrenheit - 32)
    hasil = f'suhu dalam celsius adalah: {celsius} oC'
    return hasil

def fr():
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oR = (4/9) *', fahrenheit, '- 32')
    reamur = (4/9) * (fahrenheit - 32)
    hasil = f'suhu dalam reamur adalah: {reamur} oR'
    return hasil

def fk()-> str:
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oK = (5/9) *', fahrenheit, '- 32')
    kelvin = (5/9) * (fahrenheit - 32) + 273
    hasil = f'suhu dalam kelvin adalah:  {kelvin} oK'
    return hasil

def kc()-> str:
    kelvin = float(input('masukan kelvin: '))
    print('oC =', kelvin, '- 273')
    celsius = kelvin - 273
    hasil = f'suhu dalam celsius adalah:  {celsius} oC'
    return hasil

def kr()-> str:
    kelvin = float(input('masukan kelvin: '))
    print('oR = (4/5) *', kelvin, '- 273')
    reamur = (4/5) * (kelvin - 273)
    hasil = f'suhu dalam reamur adalah: {reamur} oR'
    return hasil

def kf()-> str:
    kelvin = float(input('masukan kelvin: '))
    print('oF = (9/5) *', kelvin, '- 32')
    fahrenheit = (9/5) * (kelvin - 273) + 32
    hasil = f'suhu dalam fahrenheit adalah: {fahrenheit} oF'
    return hasil


doks ="""celcius - > reamur = cr        |  reamur - > celsius = rc       |  kelvin - > celsius = kc      |  fahrenheit - > celsius = fc  |
celcius - > kelvin = ck        |  reamur - > kelvin = rk        |  kelvin - > reamur = kr       |  fahrenheit - > reamur = fr   |
celcius - > fahrenheit = cf    |  reamur - > fahrenheit = rf    |  kelvin - > fahrenheit = kf   |  fahrenheit - > kelvin = fk   |\n"""

print(doks)

while (sat := str(input('masukan satuan yang ingin dikonversikan: '))) != "exit" :
    try :
        if sat == 'cr':
            print(cr())
            
        elif sat == 'ck':
            print(ck())
            
        elif sat == 'cf':
            print(cf())
            
        elif sat == 'rc':
            print(rc())
            
        elif sat == 'rk':
            print(rk())
            
        elif sat == 'rf':
            print(rf())
            
        elif sat == 'kc':
            print(kc())
            
        elif sat == 'kr':
            print(kr())
            
        elif sat == 'kf':
            print(kf())
            
        elif sat == 'fc':
            print(fc())
            
        elif sat == 'fr':
            print(fr())
            
        elif sat == 'fk':
            print(fk())
            
        else:
            print('satuan yang kamu masukan salah')

        print("\nGunakan 'exit' untuk keluar")
           
    except ValueError :
        print("Input tidak Valid!!")
        break
