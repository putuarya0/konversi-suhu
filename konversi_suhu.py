def konversi():
  print("Pilih menu konversi suhu \n 1.celesius \n 2.fahrenheit \n 3.kelvin \n 4.reamur")
  pilihan = int(input("Masukan pilihan : "))
  if pilihan == 1:
    print("Pilihan menu konversi suhu ke celesius \n 1.fahrenheit \n 2.kelvin \n 3.reamur")
    pilihan = int(input("Masukan pilihan : "))
    if pilihan == 1:
      fahrenheit = float(input("Masukan suhu fahrenheit : "))
      hasil = (fahrenheit-32)*5/9
      return hasil
    elif pilihan == 2:
      kelvin = float(input("Masukan suhu kelvin : "))
      hasil = kelvin - 273
      return hasil
    elif pilihan == 3:
      reamur = float(input("Masukan suhu reamur : "))
      hasil = reamur*5/4
      return hasil
    else:
      return "Inputan anda salah"
  elif pilihan == 2:
    print("Pilihan menu konversi suhu ke fahrenheit \n 1.celesius \n 2.kelvin \n 3.reamur ")
    pilihan = int(input("Masukan pilihan : "))
    if pilihan == 1:
      celesius = float(input("Masukan suhu celesius : "))
      hasil = (celesius * 9/5) + 32
      return hasil
    elif pilihan == 2:
      kelvin = float(input("Masukan suhu kelvin : "))
      hasil = (kelvin - 273) * 9/5 + 32
      return hasil
    elif pilihan == 3:
      reamur = float(input("Masukan suhu reamur : "))
      hasil = (reamur * 9/4) + 32
      return hasil
    else:
      return "Inputan anda salah"
  elif pilihan == 3:
    print("Pilihan menu konversi suhu ke Kelvin \n 1.celesius \n 2.fahrenheit \n 3.reamur ")
    pilihan = int(input("Masukan pilihan : "))
    if pilihan == 1:
      celesius = float(input("Masukan suhu celesius : "))
      hasil = celesius + 273
      return hasil
    elif pilihan == 2:
      fahrenheit = float(input("Masukan suhu fahrenheit : "))
      hasil = (fahrenheit - 32) * 5/9 + 273
      return hasil
    elif pilihan == 3:
      reamur = float(input("Masukan suhu reamur : "))
      hasil = reamur * 5/4 + 273
      return hasil
    else:
      return "Inputan anda salah"
  elif pilihan == 4:
    print("Pilihan menu konversi suhu ke reamur \n 1.celesius \n 2.fahrenheit \n 3.kelvin ")
    pilihan = int(input("Masukan pilihan : "))
    if pilihan == 1:
      celesius = float(input("Masukan suhu celesius : "))
      hasil = celesius * 4/5
      return hasil
    elif pilihan == 2:
      fahrenheit = float(input("Masukan suhu fahrenheit : "))
      hasil = (fahrenheit - 32) * 4/9
      return hasil
    elif pilihan == 3:
      kelvin = float(input("Masukan suhu kelvin : "))
      hasil = (kelvin - 273) * 4/5
      return hasil
    else:
      return "Inputan anda salah"
  else:
    return "Inputan anda salah"
konversi()