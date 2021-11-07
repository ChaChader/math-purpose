#skala
print('program ini dijalankan untuk mengkonversikan suhu')
def cr(celsius):
    celsius = float(input('masukan celsius: '))
    print('oR = (4/5) *', celsius)
    reamurc = (4/5) * celsius
    print('suhu dalam reamur adalah: ', reamurc, 'oR')
    return reamurc

def ck(celsius):
    celsius = float(input('masukan celsius: '))
    print('oK =', celsius, '+ 273')
    kelvin = celsius + 273
    print('suhu dalam kelvin adalah: ', kelvin, 'oK')
    return kelvin

def cf(celsius):
    celsius = float(input('masukan celsius: '))
    print('oF = (9/5) *', celsius, '+ 32')
    fahrenheit = (9/5) * celsius + 32
    print('suhu dalam fahrenheit adalah: ', fahrenheit, 'oF')
    return fahrenheit

def rc(reamur):
    reamur = float(input('masukan reamur: '))
    print('oC = (5/4) *', reamur)
    celsius = (5/4) * reamur
    print('suhu dalam celsius adalah: ', celsius, 'oC')
    return celsius
 
def rk(reamur):
    reamur = float(input('masukan reamur: '))
    print('oK = (4/5) *', reamur, '+ 273')
    kelvin = (5/4) * reamur + 273
    print('suhu dalam kelvin adalah: ', kelvin, 'oK')
    return kelvin

def rf(reamur):
    reamur = float(input('masukan reamur: '))
    print('oF = (9/4) *', reamur, '+ 32')
    fahrenheit = (9/4) * reamur + 32
    print('suhu dalam fahrenheit adalah: ', fahrenheit, 'oF')
    return fahrenheit

def fc(fahrenheit):
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oC = (5/9) *', fahrenheit, '- 32')
    celsius = (5/9) * (fahrenheit - 32)
    print('suhu dalam celsius adalah: ', celsius, 'oC')
    return celsius

def fr(fahrenheit):
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oR = (4/9) *', fahrenheit, '- 32')
    reamur = (5/9) * (fahrenheit - 32)
    print('suhu dalam reamur adalah: ', reamur, 'oR')
    return reamur

def fk(fahrenheit):
    fahrenheit = float(input('masukan fahrenheit: '))
    print('oK = (5/9) *', fahrenheit, '- 32')
    kelvin = (5/9) * (fahrenheit - 32) + 273
    print('suhu dalam kelvin adalah: ', kelvin, 'oK')
    return kelvin

def kc(kelvin):
    kelvin = float(input('masukan kelvin: '))
    print('oC =', kelvin, '- 273')
    celsius = kelvin - 273
    print('suhu dalam celsius adalah: ', celsius, 'oC')
    return celsius

def kr(kelvin):
    kelvin = float(input('masukan kelvin: '))
    print('oR = (4/5) *', kelvin, '- 273')
    reamur = (5/4) * (kelvin - 273)
    print('suhu dalam reamur adalah: ', reamur, 'oR')
    return reamur

def kf(kelvin):
    kelvin = float(input('masukan kelvin: '))
    print('oF = (9/5) *', kelvin, '- 32')
    fahrenheit = (9/5) * (kelvin - 273) + 32
    print('suhu dalam fahrenheit adalah: ', fahrenheit, 'oF')
    return fahrenheit

doks = ['celcius - > reamur = cr | '
        'celcius - > kelvin = ck | '
        'celcius - > fahrenheit = cf | '
        'reamur - > celsius = rc | '
        'reamur - > kelvin = rk | '
        'reamur - > fahrenheit = rf | '
        'kelvin - > celsius = kc | '
        'kelvin - > reamur = kr | '
        'kelvin - > fahrenheit = kf | '
        'fahrenheit - > celsius = fc | '
        'fahrenheit - > reamur = fr | '
        'fahrenheit - > kelvin = fk | ']

print(doks)
sat = input('masukan satuan yang ingin dikonversikan: ')
if sat == 'cr':
    cr(1)
elif sat == 'ck':
    ck(1)
elif sat == 'cf':
    cf(1)
elif sat == 'rc':
    rc(1)
elif sat == 'rk':
    rk(1)
elif sat == 'rf':
    rf(1)
elif sat == 'kc':
    kc(1)
elif sat == 'kr':
    kr(1)
elif sat == 'kf':
    kf(1)
elif sat == 'fc':
    fc(1)
elif sat == 'fr':
    fr(1)
elif sat == 'fk':
    fk(1)
else:
    print('satuan yang kamu masukan salah')

