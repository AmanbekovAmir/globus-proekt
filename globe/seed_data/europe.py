"""Города Европы и Турции: Париж, Лондон, Берлин, Рим, Стамбул."""

CITIES = [
    {
        "country": "FR",
        "name": ("Париж", "Parij", "Parij"),
        "lat": 48.8566, "lng": 2.3522, "population": 2100000, "capital": True,
        "desc": (
            "Париж — столица Франции, расположенная на берегах Сены. Один из главных мировых центров культуры, моды, науки и финансов: здесь находятся Лувр, Эйфелева башня и штаб-квартира ЮНЕСКО.",
            "Parij — Fransiyaning poytaxti, Sena daryosi boʻyida joylashgan. Jahonning madaniyat, moda, fan va moliya markazlaridan biri: bu yerda Luvr, Eyfel minorasi va YuNESKO bosh qarorgohi joylashgan.",
            "Parij — Franciyanıń paytaxtı, Sena dáryasınıń boyında jaylasqan. Dúnyanıń mádeniyat, moda, ilim hám finans orayların biri: bul jerde Luvr, Eyfel minarası hám YuNESKO bas shtab-páteri jaylasqan.",
        ),
        "history": (
            [
                "52 до н. э. — Римляне разбивают племя паризиев; на берегах Сены вырастает римская Лютеция.",
                "987 — Гуго Капет становится королём Франции, и Париж превращается в столицу королевства.",
                "14 июля 1789 — Штурм Бастилии: начало Великой французской революции.",
                "1889 — К Всемирной выставке построена Эйфелева башня — тогда самое высокое сооружение мира.",
                "1948 — На Генеральной Ассамблее ООН в Париже принята Всеобщая декларация прав человека.",
            ],
            [
                "Miloddan avvalgi 52-yil — Rimliklar parizi qabilasini magʻlub etdi; Sena boʻyida Rim Lyutetsiyasi paydo boʻldi.",
                "987 — Gugo Kapet Fransiya qiroli boʻldi va Parij qirollik poytaxtiga aylandi.",
                "1789-yil 14-iyul — Bastiliyaning bosib olinishi: Buyuk Fransuz inqilobining boshlanishi.",
                "1889 — Butunjahon koʻrgazmasi uchun Eyfel minorasi qurildi — u paytda dunyodagi eng baland inshoot.",
                "1948 — Parijdagi BMT Bosh Assambleyasida Inson huquqlari umumjahon deklaratsiyasi qabul qilindi.",
            ],
            [
                "Miladdan aldınǵı 52-jıl — Rimliler parizi qáwimin jeńdi; Sena boyında Rim Lyuteciyası payda boldı.",
                "987 — Gugo Kapet Franciya patshası boldı hám Parij patshalıq paytaxtına aylandı.",
                "1789-jıl 14-iyul — Bastiliyanıń alınıwı: Ullı Franciya revolyuciyasınıń baslanıwı.",
                "1889 — Pútkil dúnyalıq kórgeme ushın Eyfel minarası qurıldı — ol waqıtta dúnyadaǵı eń biyik imarat.",
                "1948 — Parijdegi BMT Bas Assambleyasında Insan huqıqları ulıwma deklaraciyası qabıl etildi.",
            ],
        ),
        "industry": (
            [
                "LVMH — Крупнейшая в мире группа компаний в сфере предметов роскоши (Louis Vuitton, Dior, Moët & Chandon); штаб-квартира в Париже.",
                "BNP Paribas — Один из крупнейших банков Европы со штаб-квартирой в Париже.",
                "TotalEnergies — Международная энергетическая компания, штаб-квартира в деловом районе Дефанс близ Парижа.",
            ],
            [
                "LVMH — Dunyodagi eng yirik hashamatli buyumlar guruhi (Louis Vuitton, Dior, Moët & Chandon); bosh ofisi Parijda.",
                "BNP Paribas — Yevropaning eng yirik banklaridan biri, bosh ofisi Parijda.",
                "TotalEnergies — Xalqaro energetika kompaniyasi, bosh ofisi Parij yaqinidagi Defans biznes tumanida.",
            ],
            [
                "LVMH — Dúnyadaǵı eń iri sánlilik buyımları toparı (Louis Vuitton, Dior, Moët & Chandon); bas ofisi Parijde.",
                "BNP Paribas — Evropanıń eń iri banklerinen biri, bas ofisi Parijde.",
                "TotalEnergies — Xalıqaralıq energetika kompaniyası, bas ofisi Parij janındaǵı Defans biznes rayonında.",
            ],
        ),
    },
    {
        "country": "GB",
        "name": ("Лондон", "London", "London"),
        "lat": 51.5074, "lng": -0.1278, "population": 9000000, "capital": True,
        "desc": (
            "Лондон — столица Великобритании, стоящая на Темзе. Один из ведущих мировых финансовых центров: древний Сити соседствует с королевскими парками и музеями, среди которых Британский музей и галерея Тейт.",
            "London — Buyuk Britaniyaning poytaxti, Temza daryosi boʻyida joylashgan. Dunyoning yetakchi moliya markazlaridan biri: qadimiy Siti qirollik bogʻlari va muzeylar, jumladan Britaniya muzeyi va Teyt galereyasi bilan yonma-yon turadi.",
            "London — Ullı Britaniyanıń paytaxtı, Temza dáryasınıń boyında jaylasqan. Dúnyanıń jetekshi finans orayların biri: áyyemgi Siti patshalıq baǵları hám muzeyler, sonıń ishinde Britaniya muzeyi hám Teyt galereyası menen qatar jaylasqan.",
        ),
        "history": (
            [
                "43 — Римляне основывают на Темзе торговый город Лондиний.",
                "1666 — Великий лондонский пожар уничтожает большую часть средневекового города; собор Святого Павла перестраивает Кристофер Рен.",
                "1863 — Открыта первая в мире линия метрополитена.",
                "2012 — Лондон становится первым городом, трижды принявшим летние Олимпийские игры.",
            ],
            [
                "43 — Rimliklar Temza boʻyida Londiniy savdo shahriga asos soldi.",
                "1666 — Buyuk London yongʻini oʻrta asr shaharining katta qismini yoqib yubordi; Avliyo Pavel soborini Kristofer Ren qayta qurdi.",
                "1863 — Dunyodagi birinchi metro liniyasi ochildi.",
                "2012 — London yozgi Olimpiya oʻyinlarini uch marta oʻtkazgan birinchi shaharga aylandi.",
            ],
            [
                "43 — Rimliler Temza boyında Londiniy sawda qalasına tiykar saldı.",
                "1666 — Ullı London órti orta ásir qalasınıń úlken bólegin joq etti; Aziz Pavel soborın Kristofer Ren qayta qurdı.",
                "1863 — Dúnyadaǵı birinshi metro liniyası ashıldı.",
                "2012 — London jazǵı Olimpiada oyınların úsh ret ótkergen birinshi qalaǵa aylandı.",
            ],
        ),
        "industry": (
            [
                "HSBC — Один из крупнейших банковских групп мира со штаб-квартирой в Лондоне.",
                "BP — Нефтегазовая компания, штаб-квартира в Лондоне.",
                "London Stock Exchange Group — Оператор Лондонской фондовой биржи, одной из старейших в мире.",
            ],
            [
                "HSBC — Dunyodagi eng yirik bank guruhlaridan biri, bosh ofisi Londonda.",
                "BP — Neft-gaz kompaniyasi, bosh ofisi Londonda.",
                "London Stock Exchange Group — Dunyodagi eng qadimgi birjalardan biri — London fond birjasining operatori.",
            ],
            [
                "HSBC — Dúnyadaǵı eń iri bank toparlarınan biri, bas ofisi Londonda.",
                "BP — Neft-gaz kompaniyası, bas ofisi Londonda.",
                "London Stock Exchange Group — Dúnyadaǵı eń áyyemgi birjalardan biri — London fond birjasınıń operatorı.",
            ],
        ),
    },
    {
        "country": "DE",
        "name": ("Берлин", "Berlin", "Berlin"),
        "lat": 52.5200, "lng": 13.4050, "population": 3700000, "capital": True,
        "desc": (
            "Берлин — столица и крупнейший город Германии на реке Шпрее. Город с бурной историей сегодня стал центром политики, науки, искусства и стартапов.",
            "Berlin — Germaniyaning poytaxti va eng yirik shahri, Shpree daryosi boʻyida joylashgan. Voqealarga boy tarixga ega shahar bugun siyosat, fan, sanʼat va startaplar markaziga aylangan.",
            "Berlin — Germaniyanıń paytaxtı hám eń úlken qalası, Shpree dáryasınıń boyında jaylasqan. Waqıyalarǵa baı tariyxqa iye qala búgin siyasat, ilim, óner hám startaplar orayına aylanǵan.",
        ),
        "history": (
            [
                "1237 — Первое упоминание Кёльна — одного из двух поселений, давших начало Берлину.",
                "1871 — Берлин становится столицей объединённой Германской империи.",
                "13 августа 1961 — Начинается строительство Берлинской стены, разделившей город на две части.",
                "9 ноября 1989 — Падение Берлинской стены.",
                "3 октября 1990 — Объединение Германии; Берлин вновь становится её столицей.",
            ],
            [
                "1237 — Berlinga asos solgan ikki aholi punktidan biri — Kyoln birinchi marta tilga olindi.",
                "1871 — Berlin birlashgan Germaniya imperiyasining poytaxtiga aylandi.",
                "1961-yil 13-avgust — Shaharni ikkiga boʻlgan Berlin devori qurilishi boshlandi.",
                "1989-yil 9-noyabr — Berlin devori qulaydi.",
                "1990-yil 3-oktabr — Germaniya birlashdi; Berlin yana uning poytaxti boʻldi.",
            ],
            [
                "1237 — Berlinge tiykar salǵan eki eldi mekennen biri — Kyoln dáslep tilge alındı.",
                "1871 — Berlin birlesken Germaniya imperiyasınıń paytaxtına aylandı.",
                "1961-jıl 13-avgust — Qalanı eki bólekke bólgen Berlin diywalı qurılısı baslandı.",
                "1989-jıl 9-noyabr — Berlin diywalı qulaydı.",
                "1990-jıl 3-oktyabr — Germaniya birlesti; Berlin qaytadan onıń paytaxtı boldı.",
            ],
        ),
        "industry": (
            [
                "Siemens — Основана в Берлине в 1847 году Вернером фон Сименсом; сегодня одна из крупнейших технологических и промышленных корпораций мира.",
                "Deutsche Bahn — Национальная железнодорожная компания Германии со штаб-квартирой в Берлине.",
                "Zalando — Европейская онлайн-платформа моды, основанная в Берлине в 2008 году.",
            ],
            [
                "Siemens — 1847-yilda Berlinda Verner fon Simens tomonidan asos solingan; bugun dunyodagi eng yirik texnologiya va sanoat korporatsiyalaridan biri.",
                "Deutsche Bahn — Germaniyaning milliy temir yoʻl kompaniyasi, bosh ofisi Berlinda.",
                "Zalando — 2008-yilda Berlinda asos solingan Yevropa onlayn moda platformasi.",
            ],
            [
                "Siemens — 1847-jılı Berlinde Verner fon Simens tárepinen tiykarlanǵan; búgin dúnyadaǵı eń iri texnologiya hám ónerkásip korporaciyalarınan biri.",
                "Deutsche Bahn — Germaniyanıń milliy temir jol kompaniyası, bas ofisi Berlinde.",
                "Zalando — 2008-jılı Berlinde tiykarlanǵan Evropa onlayn moda platforması.",
            ],
        ),
    },
    {
        "country": "IT",
        "name": ("Рим", "Rim", "Rim"),
        "lat": 41.9028, "lng": 12.4964, "population": 2800000, "capital": True,
        "desc": (
            "Рим — столица Италии, «Вечный город» на реке Тибр. Здесь сохранились Колизей, Форум и Пантеон, а в самом городе расположено независимое государство Ватикан.",
            "Rim — Italiyaning poytaxti, Tibr daryosi boʻyidagi «Abadiy shahar». Bu yerda Kolizey, Forum va Panteon saqlanib qolgan, shahar ichida esa mustaqil Vatikan davlati joylashgan.",
            "Rim — Italiyanıń paytaxtı, Tibr dáryasınıń boyındaǵı «Máńgilik qala». Bul jerde Kolizey, Forum hám Panteon saqlanıp qalǵan, qala ishinde ǵárezsiz Vatikan mámleketi jaylasqan.",
        ),
        "history": (
            [
                "753 до н. э. — По преданию, Ромул основывает Рим.",
                "27 до н. э. — Октавиан получает титул Августа: начало Римской империи.",
                "1871 — Рим становится столицей объединённого Итальянского королевства.",
                "25 марта 1957 — В Риме подписан договор об учреждении Европейского экономического сообщества.",
            ],
            [
                "Miloddan avvalgi 753-yil — Rivoyatga koʻra, Romul Rimga asos soldi.",
                "Miloddan avvalgi 27-yil — Oktavian Avgust unvonini oldi: Rim imperiyasining boshlanishi.",
                "1871 — Rim birlashgan Italiya qirolligining poytaxtiga aylandi.",
                "1957-yil 25-mart — Rimda Yevropa iqtisodiy hamjamiyatini tashkil etish toʻgʻrisidagi shartnoma imzolandi.",
            ],
            [
                "Miladdan aldınǵı 753-jıl — Rawayatqa kóre, Romul Rimge tiykar saldı.",
                "Miladdan aldınǵı 27-jıl — Oktavian Avgust ataǵın aldı: Rim imperiyasınıń baslanıwı.",
                "1871 — Rim birlesken Italiya patshalıǵınıń paytaxtına aylandı.",
                "1957-jıl 25-mart — Rimde Evropa ekonomikalıq birlespesin dúziw haqqındaǵı shártnama imzalandı.",
            ],
        ),
        "industry": (
            [
                "Eni — Одна из крупнейших нефтегазовых компаний Европы со штаб-квартирой в Риме.",
                "Enel — Крупнейшая итальянская энергетическая компания, штаб-квартира в Риме.",
                "Cinecittà — Киностудия, основанная в 1937 году; здесь снимали «Бен-Гур» и фильмы Федерико Феллини.",
            ],
            [
                "Eni — Yevropaning eng yirik neft-gaz kompaniyalaridan biri, bosh ofisi Rimda.",
                "Enel — Italiyaning eng yirik energetika kompaniyasi, bosh ofisi Rimda.",
                "Cinecittà — 1937-yilda asos solingan kinostudiya; bu yerda «Ben-Gur» va Federiko Fellini filmlari suratga olingan.",
            ],
            [
                "Eni — Evropanıń eń iri neft-gaz kompaniyalarınan biri, bas ofisi Rimde.",
                "Enel — Italiyanıń eń iri energetika kompaniyası, bas ofisi Rimde.",
                "Cinecittà — 1937-jılı tiykarlanǵan kinostudiya; bul jerde «Ben-Gur» hám Federiko Fellini filmleri túsirilgen.",
            ],
        ),
    },
    {
        "country": "TR",
        "name": ("Стамбул", "Istanbul", "Istanbul"),
        "lat": 41.0082, "lng": 28.9784, "population": 15500000, "capital": False,
        "desc": (
            "Стамбул — крупнейший город Турции, раскинувшийся на двух континентах по обе стороны пролива Босфор. Бывшая столица Византийской и Османской империй сегодня — главный торговый, культурный и транспортный центр страны.",
            "Istanbul — Turkiyaning eng yirik shahri, Bosfor boʻgʻozining ikki tomonida, ikki qitʼada joylashgan. Vizantiya va Usmonlilar imperiyalarining sobiq poytaxti bugun mamlakatning asosiy savdo, madaniyat va transport markazi.",
            "Istanbul — Túrkiyanıń eń úlken qalası, Bosfor boǵazınıń eki tárepinde, eki qıtada jaylasqan. Vizantiya hám Osman imperiyalarınıń burınǵı paytaxtı búgin eldiń tiykarǵı sawda, mádeniyat hám transport orayı.",
        ),
        "history": (
            [
                "Ок. 660 до н. э. — Греческие колонисты основывают на Босфоре город Византий.",
                "330 — Император Константин Великий делает город столицей Римской империи — Константинополем.",
                "537 — Освящён собор Святой Софии (Айя-София).",
                "29 мая 1453 — Войска султана Мехмеда II берут Константинополь; он становится столицей Османской империи.",
            ],
            [
                "Miloddan avvalgi taxminan 660-yil — Yunon koloniyachilari Bosforda Vizantiy shahriga asos soldi.",
                "330 — Imperator Buyuk Konstantin shaharni Rim imperiyasining poytaxti — Konstantinopolga aylantirdi.",
                "537 — Ayasofya (Avliyo Sofiya) sobori muqaddas qilindi.",
                "1453-yil 29-may — Sulton Mehmed II qoʻshinlari Konstantinopolni egalladi; u Usmonlilar imperiyasining poytaxtiga aylandi.",
            ],
            [
                "Miladdan aldınǵı shama menen 660-jıl — Grek koloniyashıları Bosforda Vizantiy qalasına tiykar saldı.",
                "330 — Imperator Ullı Konstantin qalanı Rim imperiyasınıń paytaxtı — Konstantinopolge aylandırdı.",
                "537 — Ayasofya (Aziz Sofiya) soboru muqaddeslendi.",
                "1453-jıl 29-may — Sultan Mehmed II áskerleri Konstantinopoldi iyeledi; ol Osman imperiyasınıń paytaxtına aylandı.",
            ],
        ),
        "industry": (
            [
                "Turkish Airlines — Национальный авиаперевозчик; главный хаб — аэропорт Стамбула, один из крупнейших в мире.",
                "Koç Holding — Крупнейший промышленный конгломерат Турции со штаб-квартирой в Стамбуле.",
                "Borsa Istanbul — Единственная фондовая биржа Турции.",
            ],
            [
                "Turkish Airlines — Milliy aviakompaniya; asosiy tayanch aeroporti — dunyodagi eng yirik aeroportlardan biri boʻlgan Istanbul aeroporti.",
                "Koç Holding — Turkiyaning eng yirik sanoat konglomerati, bosh ofisi Istanbulda.",
                "Borsa Istanbul — Turkiyaning yagona fond birjasi.",
            ],
            [
                "Turkish Airlines — Milliy aviakompaniya; tiykarǵı tayanısh aeroportı — dúnyadaǵı eń iri aeroportlardan biri bolǵan Istanbul aeroportı.",
                "Koç Holding — Túrkiyanıń eń iri ónerkásip konglomerati, bas ofisi Istanbulda.",
                "Borsa Istanbul — Túrkiyanıń jalǵız fond birjası.",
            ],
        ),
    },
]
