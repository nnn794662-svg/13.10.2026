login = {'login': 'Nodirbek', 'password': '12345'}
a = input("Loginni kiriting: ")
b = input("Parolni kiriting: ")
if a == login['login'] and b == login['password']:
    print('Parol va login togri!')
else:
    print("Parol yoki login xato!")


otam = {
    'ismi': input("Otangizning ismini kiriting: "),
    'tugilgan_yili': input("Tug'ilgan yilini kiriting: "),
    'shahri': input("Tug'ilgan shahrini ( viloyatini) kiriting: ")
}

print(f'Otamning ismi {otam['ismi']}, {otam['tugilgan_yili']}-yilda, {otam['shahri']} shahrida tug\'ilgan.')





