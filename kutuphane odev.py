film_koleksiyonu=dict()
while True:
    print("Film Koleksiyonu Programi\n1-Film ekle\n2-Film guncelle\n3-Film sil\n4-Koleksyonu goruntule")

    secim = int(input("Seçiminiz: "))

    if secim == 1:
        film_adi = input("Film adı: ")
        yonetmen = input("Yoetmen: ")
        cikis_yili = input("Çıkış yılı: ")
        tur = input("Tur: ")

        film_koleksiyonu[film_adi] = {
            "Yonetmen": yonetmen,
            "Çıkış Yılı": cikis_yili,
            "Tur": tur
        }
        print(f"{film_adi} filmi koleksiyona eklendi.")

    elif secim == 2:
        film_adi = input("Düzenlemek istediğiniz filmin adı: ")
        if film_adi in film_koleksiyonu:
            print("Hangi bilgiyi düzenlemek istiyorsunuz?\n1- Yönetmen\n2- Çıkış Yılı\n3- Tür")
            duzenleme_secim = int(input("Seçiminiz: "))
            if duzenleme_secim == 1:
                yeni_yonetmen = input("Yeni yönetmen: ")
                film_koleksiyonu[film_adi]["Yönetmen"] = yeni_yonetmen
            elif duzenleme_secim == 2:
                yeni_cikis_yili = input("Yeni çıkış yılı: ")
                film_koleksiyonu[film_adi]["Çıkış Yılı"] = yeni_cikis_yili
            elif duzenleme_secim == 3:
                yeni_tur = input("Yeni tür: ")
                film_koleksiyonu[film_adi]["Tür"] = yeni_tur
            else:
                print("Geçersiz seçim.")
            print(f"{film_adi} filmi güncellendi.")
        else:
            print("Bu film koleksiyonda bulunmuyor.")

    elif secim == 3:
        film_adi = input("Silmek istediğiniz filmin adı: ")
        if film_adi in film_koleksiyonu:
            del film_koleksiyonu[film_adi]
            print(f"{film_adi} filmi koleksiyondan silindi.")
        else:
            print("Bu film koleksiyonda bulunmuyor.")

    elif secim == 4:
        print("1- Tüm koleksiyonu görüntüle\n2- Filtrele")
        goruntuleme_secim = int(input("Seçiminiz: "))
        if goruntuleme_secim == 1:
            for film, bilgiler in film_koleksiyonu.items():
                print(f"\nFilm: {film}")
                for bilgi, deger in bilgiler.items():
                    print(f"{bilgi}: {deger}")
        elif goruntuleme_secim == 2:
            print("1- Türe göre\n2- Çıkış yılına göre")
            filtre_secim = input("Filtreleme türü: ")
            if filtre_secim == 1:
                tur = input("Tür: ")
                for film, bilgiler in film_koleksiyonu.items():
                    if bilgiler["Tür"] == tur:
                        print(f"\nFilm: {film}")
                        for bilgi, deger in bilgiler.items():
                            print(f"{bilgi}: {deger}")
            elif filtre_secim == 2:
                cikis_yili = input("Çıkış yılı: ")
                for film, bilgiler in film_koleksiyonu.items():
                    if bilgiler["Çıkış Yılı"] == cikis_yili:
                        print(f"\nFilm: {film}")
                        for bilgi, deger in bilgiler.items():
                            print(f"{bilgi}: {deger}")
            else:
                print("Geçersiz seçim.")
        else:
            print("Geçersiz seçim.")

    else:
        print("Geçersiz seçim.")