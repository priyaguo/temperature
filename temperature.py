question = input('請輸入1華氏溫度/2攝氏溫度:')

if question == 2:
    temperature_c = input('請輸入攝氏溫度:')
    temperature_c = int(temperature_c)
    temperature_f = temperature_c * 9 / 5 + 32
    print('華氏溫度為:',temperature_f)
else:
    temperature_f = input('請輸入華氏溫度:')
    temperature_f = int(temperature_f)
    temperature_c = (temperature_f - 32) / 9 * 5
    print('攝氏溫度為:',temperature_c)