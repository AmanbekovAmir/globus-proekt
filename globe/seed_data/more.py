"""Дополнительные страны и города: Центральная Азия и Кавказ, Испания, Канада,
Аргентина, ЮАР, Саудовская Аравия, Таиланд, Индонезия, а также Бухара и Санкт-Петербург.

Формат тот же, что в europe.py / asia.py: тексты — кортежи (ru, uz, qr).
"""

CITIES = [
    {
        "country": "KG",
        "name": ("Бишкек", "Bishkek", "Bishkek"),
        "lat": 42.8746, "lng": 74.5698, "population": 1100000, "capital": True,
        "desc": (
            "Бишкек — столица Кыргызстана, зелёный город у подножия хребта Ала-Тоо, где улицы обсажены тополями. Это политический, научный и торговый центр страны, а рядом лежат горные ущелья и курорты.",
            "Bishkek — Qirgʻizistonning poytaxti, Ala-Too tizmasi etagidagi yam-yashil shahar; koʻchalari terak daraxtlari bilan oʻralgan. Bu mamlakatning siyosiy, ilmiy va savdo markazi, atrofida esa togʻ daralari va kurortlar joylashgan.",
            "Bishkek — Qırǵızstannıń paytaxtı, Ala-Too dizbegi etegindegi jasıl qala; kóshelerin terek aǵashları qorshap turadı. Ol eldiń siyasiy, ilimiy hám sawda orayı, átirapında bolsa taw saylar hám kurortlar jaylasqan.",
        ),
        "history": (
            [
                "1825 — Кокандские правители строят в долине Чуя крепость Пишпек.",
                "1926 — Город переименован во Фрунзе в честь революционера Михаила Фрунзе, уроженца этих мест.",
                "1991 — Городу возвращают название Бишкек; в том же году Кыргызстан объявляет независимость.",
            ],
            [
                "1825 — Qoʻqon hukmdorlari Chu vodiysida Pishpak qalʼasini qurdilar.",
                "1926 — Shahar shu yerlik inqilobchi Mixail Frunze sharafiga Frunze deb oʻzgartirildi.",
                "1991 — Shaharga Bishkek nomi qaytarildi; xuddi shu yili Qirgʻiziston mustaqilligini eʼlon qildi.",
            ],
            [
                "1825 — Qoqan húkimdarları Shu alabında Pishpek qalasın qurdı.",
                "1926 — Qala usı jerden shıqqan revolyuciyashı Mixail Frunze húrmetine Frunze dep ataldı.",
                "1991 — Qalaǵa Bishkek ataması qaytarıldı; sol jılı Qırǵızstan ǵárezsizligin járiyaladı.",
            ],
        ),
        "industry": (
            [
                "Дордой — Один из крупнейших оптовых рынков Центральной Азии на окраине Бишкека, куда поступают товары из Китая и других стран.",
                "Кумтор — Одно из крупнейших золотых месторождений Центральной Азии в горах Тянь-Шаня; с 2021 года контролируется государством.",
            ],
            [
                "Dordoy — Markaziy Osiyodagi eng yirik ulgurji bozorlardan biri, Bishkek chekkasida joylashgan; Xitoy va boshqa mamlakatlardan tovarlar keladi.",
                "Kumtor — Tyan-Shan togʻlaridagi Markaziy Osiyoning eng yirik oltin konlaridan biri; 2021-yildan davlat nazoratida.",
            ],
            [
                "Dordoy — Orta Aziyadaǵı eń úlken ulıwma bazarlardan biri, Bishkektiń shetinde jaylasqan; Qıtay hám basqa elatlardan tovarlar keledi.",
                "Kumtor — Tyan-Shan tawlarındaǵı Orta Aziyanıń eń úlken altın kenlerinen biri; 2021-jıldan baslap mámleket qadaǵalawında.",
            ],
        ),
    },
    {
        "country": "TJ",
        "name": ("Душанбе", "Dushanbe", "Dushanbe"),
        "lat": 38.5598, "lng": 68.7870, "population": 1000000, "capital": True,
        "desc": (
            "Душанбе — столица Таджикистана в долине реки Варзоб, окружённая горами Гиссарского хребта. Название означает «понедельник»: когда-то здесь работал базар по понедельникам.",
            "Dushanbe — Tojikistonning poytaxti, Varzob daryosi vodiysida, Hisor tizmasi togʻlari bilan oʻralgan. Nomi «dushanba» degan maʼnoni bildiradi: bir paytlar bu yerda dushanba kunlari bozor ishlagan.",
            "Dushanbe — Tájikstannıń paytaxtı, Varzob dáryası alabında, Hisar dizbegi tawları menen qorshalǵan. Atamasınıń mánisi «dúysenbi»: burın bul jerde dúysenbi kúnleri bazar islegen.",
        ),
        "history": (
            [
                "1924 — Душанбе становится столицей Таджикской АССР; с 1929 по 1961 год город носит имя Сталинабад.",
                "1961 — Городу возвращают историческое название Душанбе.",
                "1991 — Таджикистан провозглашает независимость, Душанбе становится столицей суверенного государства.",
            ],
            [
                "1924 — Dushanbe Tojikiston ASSRning poytaxtiga aylandi; 1929–1961-yillarda shahar Stalinobod deb atalgan.",
                "1961 — Shaharga tarixiy Dushanbe nomi qaytarildi.",
                "1991 — Tojikiston mustaqilligini eʼlon qildi, Dushanbe suveren davlat poytaxtiga aylandi.",
            ],
            [
                "1924 — Dushanbe Tájik AKSRiniń paytaxtına aylandı; 1929–1961-jıllarda qala Stalinabad dep atalǵan.",
                "1961 — Qalaǵa tariyxıy Dushanbe ataması qaytarıldı.",
                "1991 — Tájikstan ǵárezsizligin járiyaladı, Dushanbe suveren mámleket paytaxtına aylandı.",
            ],
        ),
        "industry": (
            [
                "Таджикская алюминиевая компания (TALCO) — Крупнейшее промышленное предприятие страны; завод находится в Турсунзаде к западу от Душанбе.",
                "Нурекская ГЭС — Одна из самых высоких плотин мира (около 300 м) на реке Вахш, примерно в 70 км от столицы; даёт значительную часть электроэнергии страны.",
            ],
            [
                "Tojikiston alyuminiy kompaniyasi (TALCO) — Mamlakatning eng yirik sanoat korxonasi; zavodi Dushanbening gʻarbidagi Tursunzodada joylashgan.",
                "Norak GES — Vahsh daryosidagi dunyodagi eng baland toʻgʻonlardan biri (taxminan 300 m), poytaxtdan qariyb 70 km uzoqlikda; mamlakat elektr energiyasining katta qismini beradi.",
            ],
            [
                "Tájikstan alyuminiy kompaniyası (TALCO) — Eldiń eń úlken sanaat kárxanası; zavodı Dushanbeniń batısındaǵı Tursunzodada jaylasqan.",
                "Nurek GES — Vahsh dáryasındaǵı dúnyanıń eń biyik bendlerinen biri (shama menen 300 m), paytaxttan qarıyb 70 km qashıqlıqta; eldiń elektr energiyasınıń úlken bólegin beredi.",
            ],
        ),
    },
    {
        "country": "TM",
        "name": ("Ашхабад", "Ashxobod", "Ashxabad"),
        "lat": 37.9601, "lng": 58.3261, "population": 1030000, "capital": True,
        "desc": (
            "Ашхабад — столица Туркменистана у подножия Копетдага, на краю пустыни Каракум. Город известен белым мрамором зданий: в 2013 году он попал в Книгу рекордов Гиннесса как город с самой большой концентрацией таких построек.",
            "Ashxobod — Turkmanistonning poytaxti, Kopetdogʻ etagida, Qoraqum choʻli chekkasida joylashgan. Shahar oq marmar binolari bilan mashhur: 2013-yilda u shunday binolar eng koʻp toʻplangan shahar sifatida Ginnes rekordlar kitobiga kiritilgan.",
            "Ashxabad — Túrkmenstannıń paytaxtı, Kopetdag etegindegi, Qaraqum shóliniń shetinde jaylasqan. Qala aq mramor imaratları menen tanılǵan: 2013-jılı ol sonday imaratlar eń kóp toplanǵan qala retinde Ginnes rekordlar kitabına kirgizilgen.",
        ),
        "history": (
            [
                "1881 — Русские войска основывают крепость Ашхабад близ древнего поселения.",
                "1948 — Разрушительное землетрясение 6 октября почти полностью уничтожает город.",
                "1991 — Туркменистан провозглашает независимость, Ашхабад становится столицей суверенного государства.",
            ],
            [
                "1881 — Rus qoʻshinlari qadimiy aholi punkti yaqinida Ashxobod qalʼasiga asos soldi.",
                "1948 — 6-oktabrdagi vayronkor zilzila shaharni deyarli butunlay yoʻq qildi.",
                "1991 — Turkmaniston mustaqilligini eʼlon qildi, Ashxobod suveren davlat poytaxtiga aylandi.",
            ],
            [
                "1881 — Rus áskerleri áyyemgi turaqjay janında Ashxabad qalasına tiykar saldı.",
                "1948 — 6-oktyabrdegi qıran salǵan jer silkiniw qalanı derlik pútkilley joq etti.",
                "1991 — Túrkmenstan ǵárezsizligin járiyaladı, Ashxabad suveren mámleket paytaxtına aylandı.",
            ],
        ),
        "industry": (
            [
                "Туркменгаз — Государственный концерн, отвечающий за добычу и экспорт природного газа; Туркменистан входит в число стран с крупнейшими запасами газа.",
                "Туркменнебит — Государственный нефтяной концерн страны.",
            ],
            [
                "Turkmengaz — Tabiiy gaz qazib olish va eksport qilish uchun masʼul davlat konserni; Turkmaniston gaz zaxiralari eng katta mamlakatlar qatoriga kiradi.",
                "Turkmenneft — Mamlakatning davlat neft konserni.",
            ],
            [
                "Túrkmengaz — Tábiyiy gaz qazıp alıw hám eksport etiw ushın juwapker mámleket konserni; Túrkmenstan gaz qorları eń úlken elatlar qatarına kiredi.",
                "Túrkmenneft — Eldiń mámleket neft konserni.",
            ],
        ),
    },
    {
        "country": "AZ",
        "name": ("Баку", "Boku", "Baku"),
        "lat": 40.4093, "lng": 49.8671, "population": 2300000, "capital": True,
        "desc": (
            "Баку — столица Азербайджана на берегу Каспия, на Апшеронском полуострове. Старый город Ичеришехер с Девичьей башней входит в список ЮНЕСКО, а рядом поднимаются небоскрёбы Flame Towers; Баку — один из старейших центров мировой нефтедобычи.",
            "Boku — Ozarbayjonning poytaxti, Kaspiy boʻyida, Absheron yarim orolida joylashgan. Icherishahar eski shahri Qiz minorasi bilan YuNESKO roʻyxatiga kiritilgan, yonida esa Flame Towers osmonoʻpar binolari koʻtarilgan; Boku dunyodagi eng qadimgi neft qazib olish markazlaridan biri.",
            "Baku — Ázerbayjannıń paytaxtı, Kaspiy boyında, Absheron yarım atawında jaylasqan. Icherisheher eski qalası Qız minarası menen YuNESKO dizimine kirgizilgen, janında Flame Towers kóp qabatlı imaratları kóterilgen; Baku dúnyadaǵı eń áyyemgi neft qazıp alıw orayların biri.",
        ),
        "history": (
            [
                "1846 — В Биби-Эйбате близ Баку пробурена одна из первых в мире нефтяных скважин.",
                "1918 — Баку становится столицей Азербайджанской Демократической Республики, первой светской республики на мусульманском Востоке.",
                "2000 — Старый город с Дворцом ширваншахов и Девичьей башней включён в список Всемирного наследия ЮНЕСКО.",
            ],
            [
                "1846 — Boku yaqinidagi Bibiheybatda dunyodagi dastlabki neft quduqlaridan biri burgʻulandi.",
                "1918 — Boku Ozarbayjon Demokratik Respublikasining poytaxtiga aylandi; bu musulmon Sharqidagi birinchi dunyoviy respublika edi.",
                "2000 — Shirvonshohlar saroyi va Qiz minorasi joylashgan eski shahar YuNESKO Jahon merosi roʻyxatiga kiritildi.",
            ],
            [
                "1846 — Baku janındaǵı Bibiheybatta dúnyadaǵı dáslepki neft quduqlarınan biri burǵılandı.",
                "1918 — Baku Ázerbayjan Demokratiyalıq Respublikasınıń paytaxtına aylandı; bul musılman Shıǵısındaǵı birinshi dúnyalıq respublika edi.",
                "2000 — Shirvanshahlar saraylı hám Qız minarası jaylasqan eski qala YuNESKO Dúnyalıq miyras dizimine kirgizildi.",
            ],
        ),
        "industry": (
            [
                "SOCAR — Государственная нефтегазовая компания Азербайджана, штаб-квартира в Баку.",
                "Азери–Чираг–Гюнешли — Крупнейший нефтяной проект Азербайджана на Каспии; нефть идёт по трубопроводу Баку–Тбилиси–Джейхан к турецкому побережью.",
            ],
            [
                "SOCAR — Ozarbayjonning davlat neft-gaz kompaniyasi, bosh ofisi Bokuda.",
                "Azeri–Chiroq–Guneshli — Ozarbayjonning Kaspiydagi eng yirik neft loyihasi; neft Boku–Tbilisi–Jeyhan quvuri orqali Turkiya sohiliga yetkaziladi.",
            ],
            [
                "SOCAR — Ázerbayjannıń mámleket neft-gaz kompaniyası, bas ofisi Bakude.",
                "Azeri–Shıraq–Guneshli — Ázerbayjannıń Kaspiydegi eń úlken neft joybarı; neft Baku–Tbilisi–Jeyxan tútigi arqalı Túrkiya jaǵalawına jetkeriledi.",
            ],
        ),
    },
    {
        "country": "ES",
        "name": ("Мадрид", "Madrid", "Madrid"),
        "lat": 40.4168, "lng": -3.7038, "population": 3300000, "capital": True,
        "desc": (
            "Мадрид — столица Испании и одна из самых высоко расположенных столиц Европы (около 650 м над уровнем моря). Здесь находится «золотой треугольник искусства»: музеи Прадо, Рейны Софии и Тиссена-Борнемисы.",
            "Madrid — Ispaniyaning poytaxti va Yevropaning eng baland joylashgan poytaxtlaridan biri (dengiz sathidan taxminan 650 m). Bu yerda «sanʼatning oltin uchburchagi» — Prado, Reyna Sofiya va Tissen-Bornemisa muzeylari bor.",
            "Madrid — Ispaniyanıń paytaxtı hám Evropanıń eń biyik jaylasqan paytaxtlarınan biri (teńiz dárejesinen shama menen 650 m). Bul jerde «óner altın úshmúyeshligi» — Prado, Reyna Sofiya hám Tissen-Bornemisa muzeyleri bar.",
        ),
        "history": (
            [
                "1561 — Король Филипп II переносит двор в Мадрид; с коротким перерывом (1601–1606) город остаётся столицей Испании.",
                "1819 — Открывается музей Прадо, одна из величайших картинных галерей мира.",
                "1936 — Начинается Гражданская война; Мадрид почти три года обороняется от наступающих войск Франко.",
            ],
            [
                "1561 — Qirol Filipp II saroyni Madridga koʻchirdi; qisqa tanaffus (1601–1606) bilan shahar Ispaniya poytaxti boʻlib qoldi.",
                "1819 — Dunyoning eng buyuk rasm galereyalaridan biri — Prado muzeyi ochildi.",
                "1936 — Fuqarolar urushi boshlandi; Madrid deyarli uch yil davomida Franko qoʻshinlaridan mudofaa qildi.",
            ],
            [
                "1561 — Patsha Filipp II sarayın Madridke kóshirdi; qısqa úzilis (1601–1606) menen qala Ispaniya paytaxtı bolıp qaldı.",
                "1819 — Dúnyanıń eń ullı súwret galereyalarınan biri — Prado muzeyi ashıldı.",
                "1936 — Puqaralıq urısı baslandı; Madrid derlik úsh jıl dawamında Franko áskerlerinen qorǵandı.",
            ],
        ),
        "industry": (
            [
                "Telefónica — Один из крупнейших телекоммуникационных операторов мира, штаб-квартира в Мадриде.",
                "Repsol — Энергетическая и нефтегазовая компания, штаб-квартира в Мадриде.",
            ],
            [
                "Telefónica — Dunyodagi eng yirik telekommunikatsiya operatorlaridan biri, bosh ofisi Madridda.",
                "Repsol — Energetika va neft-gaz kompaniyasi, bosh ofisi Madridda.",
            ],
            [
                "Telefónica — Dúnyadaǵı eń úlken telekommunikaciya operatorlarınan biri, bas ofisi Madridte.",
                "Repsol — Energetika hám neft-gaz kompaniyası, bas ofisi Madridte.",
            ],
        ),
    },
    {
        "country": "ES",
        "name": ("Барселона", "Barselona", "Barselona"),
        "lat": 41.3874, "lng": 2.1686, "population": 1640000, "capital": False,
        "desc": (
            "Барселона — столица Каталонии на берегу Средиземного моря, город Гауди, морского порта и футбола. Саграда Фамилия, парк Гуэль и дом Бальо входят в архитектурное наследие Гауди.",
            "Barselona — Kataloniyaning poytaxti, Oʻrta dengiz boʻyidagi Gaudi, dengiz porti va futbol shahri. Sagrada Familiya, Gvel bogʻi va Batlyo uyi Gaudi meʼmoriy merosining bir qismi.",
            "Barselona — Kataloniyanıń paytaxtı, Orta teńiz boyındaǵı Gaudi, teńiz porti hám futbol qalası. Sagrada Familiya, Gvel baǵı hám Batlyo úyi Gaudi arxitekturalıq miyrasınıń bir bólegi.",
        ),
        "history": (
            [
                "Около 10 г. до н. э. — Римляне основывают колонию Барсино.",
                "1882 — Закладывается Саграда Фамилия; с 1883 года проект ведёт Антонио Гауди.",
                "1992 — Барселона принимает летние Олимпийские игры, после которых преображаются её набережная и районы.",
            ],
            [
                "Miloddan avvalgi taxminan 10-yil — Rimliklar Barsino mustamlakasiga asos soldilar.",
                "1882 — Sagrada Familiya poydevori qoʻyildi; 1883-yildan loyihani Antoni Gaudi olib bordi.",
                "1992 — Barselona yozgi Olimpiya oʻyinlarini oʻtkazdi; shundan keyin sohil va mahallalar oʻzgarib ketdi.",
            ],
            [
                "Miladdan aldınǵı shama menen 10-jıl — Rimliler Barsino koloniyasına tiykar saldı.",
                "1882 — Sagrada Familiya irgetası qoyıldı; 1883-jıldan joybardı Antoni Gaudi alıp bardı.",
                "1992 — Barselona jazǵı Olimpiada oyınların ótkerdi; usıdan keyin jaǵalaw hám mahallalar ózgerip ketti.",
            ],
        ),
        "industry": (
            [
                "SEAT — Испанский автопроизводитель; главный завод находится в Мартореле близ Барселоны.",
                "Порт Барселоны — Один из важнейших грузовых и круизных портов Средиземноморья.",
            ],
            [
                "SEAT — Ispaniya avtomobil ishlab chiqaruvchisi; asosiy zavodi Barselona yaqinidagi Martorelda joylashgan.",
                "Barselona porti — Oʻrta dengizdagi eng muhim yuk va kruiz portlaridan biri.",
            ],
            [
                "SEAT — Ispaniya avtomobil islep shıǵarıwshısı; tiykarǵı zavodı Barselona janındaǵı Martorelde jaylasqan.",
                "Barselona porti — Orta teńizdegi eń áhmiyetli júk hám kruiz portlarınan biri.",
            ],
        ),
    },
    {
        "country": "CA",
        "name": ("Торонто", "Toronto", "Toronto"),
        "lat": 43.6532, "lng": -79.3832, "population": 2800000, "capital": False,
        "desc": (
            "Торонто — крупнейший город Канады на северном берегу озера Онтарио, финансовый и деловой центр страны. Почти половина жителей родилась за пределами Канады, а на улицах звучат сотни языков.",
            "Toronto — Kanadaning eng yirik shahri, Ontario koʻlining shimoliy sohilida joylashgan, mamlakatning moliyaviy va ishbilarmonlik markazi. Aholining deyarli yarmi Kanadadan tashqarida tugʻilgan, koʻchalarda yuzlab tillar yangraydi.",
            "Toronto — Kanadanıń eń úlken qalası, Ontario kóliniń arqa jaǵalawında jaylasqan, eldiń finans hám isbilermenlik orayı. Xalıqtıń derlik yarımı Kanadadan sırtta tuwılǵan, kóshelerde júzlegen tiller esitiledi.",
        ),
        "history": (
            [
                "1793 — Британцы основывают поселение Йорк на месте будущего Торонто.",
                "1834 — Йорк получает статус города и возвращает название Торонто.",
                "1976 — Достроена Си-Эн Тауэр, надолго ставшая самым высоким свободно стоящим сооружением мира.",
            ],
            [
                "1793 — Britaniyaliklar kelajakdagi Toronto oʻrnida York posyolkasiga asos soldilar.",
                "1834 — York shahar maqomini oldi va Toronto nomini qaytarib oldi.",
                "1976 — Si-En Tauer qurib bitkazildi; u uzoq vaqt dunyoning eng baland mustaqil turuvchi inshooti boʻlib turdi.",
            ],
            [
                "1793 — Britaniyalılar keleshektegi Toronto ornında York turaqjayına tiykar saldı.",
                "1834 — York qala mártebesin aldı hám Toronto atamasın qaytarıp aldı.",
                "1976 — Si-En Tauer qurıp pitkerildi; ol uzaq waqıt dúnyanıń eń biyik óz aldına turatuǵın imaratı bolıp turdı.",
            ],
        ),
        "industry": (
            [
                "TD Bank Group — Один из крупнейших банков Канады, штаб-квартира в Торонто.",
                "Toronto Stock Exchange — Крупнейшая биржа Канады и мировой лидер по числу листингов горнодобывающих компаний.",
            ],
            [
                "TD Bank Group — Kanadaning eng yirik banklaridan biri, bosh ofisi Torontoda.",
                "Toronto fond birjasi — Kanadaning eng yirik birjasi va togʻ-kon kompaniyalari roʻyxatga olinishi boʻyicha jahon yetakchisi.",
            ],
            [
                "TD Bank Group — Kanadanıń eń úlken banklarınan biri, bas ofisi Torontoda.",
                "Toronto fond birjası — Kanadanıń eń úlken birjası hám taw-ken kompaniyaların dizimge alıw boyınsha dúnya jetekshisi.",
            ],
        ),
    },
    {
        "country": "AR",
        "name": ("Буэнос-Айрес", "Buenos-Ayres", "Buenos-Ayres"),
        "lat": -34.6037, "lng": -58.3816, "population": 3100000, "capital": True,
        "desc": (
            "Буэнос-Айрес — столица Аргентины на берегу реки Ла-Плата, «Париж Южной Америки» с широкими проспектами, театрами и кофейнями. Это родина танго.",
            "Buenos-Ayres — Argentinaning poytaxti, Laplata daryosi boʻyida joylashgan, keng xiyobonlari, teatrlari va qahvaxonalari bilan «Janubiy Amerika Pariji». Bu tangoning vatani.",
            "Buenos-Ayres — Argentinanıń paytaxtı, Laplata dáryasınıń boyında jaylasqan, keń kóshelerı, teatrları hám kofexanaları menen «Qubla Amerika Parijı». Bul tangonıń watanı.",
        ),
        "history": (
            [
                "1536 — Педро де Мендоса закладывает первое поселение на берегу Ла-Платы; в 1580 году город основывает заново Хуан де Гарай.",
                "1810 — Майская революция: начало борьбы Аргентины за независимость от Испании.",
                "1880 — Буэнос-Айрес окончательно получает статус федеральной столицы.",
            ],
            [
                "1536 — Pedro de Mendosa Laplata sohilida birinchi posyolkaga asos soldi; 1580-yilda shaharni Xuan de Garay qaytadan barpo etdi.",
                "1810 — May inqilobi: Argentinaning Ispaniyadan mustaqillik uchun kurashi boshlandi.",
                "1880 — Buenos-Ayres yakuniy ravishda federal poytaxt maqomini oldi.",
            ],
            [
                "1536 — Pedro de Mendosa Laplata jaǵalawında birinshi turaqjayǵa tiykar saldı; 1580-jılı qalanı Xuan de Garay qaytadan payda etti.",
                "1810 — May revolyuciyası: Argentinanıń Ispaniyadan ǵárezsizlik ushın gúresi baslandı.",
                "1880 — Buenos-Ayres juwmaqlawshı túrde federal paytaxt mártebesin aldı.",
            ],
        ),
        "industry": (
            [
                "YPF — Крупнейшая нефтегазовая компания Аргентины, штаб-квартира в Буэнос-Айресе.",
                "Mercado Libre — Крупнейшая торговая платформа Латинской Америки, основанная в Буэнос-Айресе в 1999 году.",
            ],
            [
                "YPF — Argentinaning eng yirik neft-gaz kompaniyasi, bosh ofisi Buenos-Ayresda.",
                "Mercado Libre — Lotin Amerikasidagi eng yirik savdo platformasi, 1999-yilda Buenos-Ayresda tashkil etilgan.",
            ],
            [
                "YPF — Argentinanıń eń úlken neft-gaz kompaniyası, bas ofisi Buenos-Ayresta.",
                "Mercado Libre — Latın Amerikasındaǵı eń úlken sawda platforması, 1999-jılı Buenos-Ayresta shólkemlestirilgen.",
            ],
        ),
    },
    {
        "country": "ZA",
        "name": ("Кейптаун", "Keyptaun", "Keyptaun"),
        "lat": -33.9249, "lng": 18.4241, "population": 4000000, "capital": True,
        "desc": (
            "Кейптаун — законодательная столица ЮАР у подножия Столовой горы на побережье Атлантики. Один из красивейших городов мира: отсюда рукой подать до мыса Доброй Надежды и винных долин.",
            "Keyptaun — JARning qonunchilik poytaxti, Atlantika sohilidagi Stol togʻi etagida joylashgan. Dunyoning eng goʻzal shaharlaridan biri: bu yerdan Yaxshi Umid burni va vino vodiylariga yaqin.",
            "Keyptaun — QAR-dıń nızam shıǵarıwshı paytaxtı, Atlantika jaǵalawındaǵı Stol tawı etegindegi jaylasqan. Dúnyanıń eń kórkem qalalarınan biri: bunnan Jaqsı Úmit murnına hám vino alaplarına jaqın.",
        ),
        "history": (
            [
                "1652 — Ян ван Рибек основывает у Столовой бухты станцию снабжения Голландской Ост-Индской компании.",
                "1806 — Британская империя занимает Капскую колонию и позднее закрепляет её за собой.",
                "1990 — 11 февраля Нельсон Мандела, выйдя на свободу, обращается к толпе с балкона ратуши Кейптауна.",
            ],
            [
                "1652 — Yan van Ribek Stol koʻrfazi yonida Gollandiya Ost-Hind kompaniyasining taʼminot stansiyasiga asos soldi.",
                "1806 — Britaniya imperiyasi Keyp mustamlakasini egalladi va keyinchalik uni oʻzida mustahkamladi.",
                "1990 — 11-fevralda Nelson Mandela ozodlikka chiqib, Keyptaun shahar hokimiyati balkonidan olomonga murojaat qildi.",
            ],
            [
                "1652 — Yan van Ribek Stol qoltıǵı janında Gollandiya Ost-Hind kompaniyasınıń támiynat stanciyasına tiykar saldı.",
                "1806 — Britaniya imperiyası Keyp koloniyasın iyeledi hám keyin ózinde bekkemledi.",
                "1990 — 11-fevralda Nelson Mandela azatlıqqa shıǵıp, Keyptaun qala húkimeti balkonınan xalıqqa shıǵıp sóyledi.",
            ],
        ),
        "industry": (
            [
                "Naspers — Медиа- и технологический холдинг, штаб-квартира в Кейптауне.",
                "Woolworths Holdings — Крупная розничная группа ЮАР, штаб-квартира в Кейптауне.",
            ],
            [
                "Naspers — Media va texnologiya xoldingi, bosh ofisi Keyptaunda.",
                "Woolworths Holdings — JARning yirik chakana savdo guruhi, bosh ofisi Keyptaunda.",
            ],
            [
                "Naspers — Media hám texnologiya xoldingi, bas ofisi Keyptaunda.",
                "Woolworths Holdings — QAR-dıń úlken bólshek sawda toparı, bas ofisi Keyptaunda.",
            ],
        ),
    },
    {
        "country": "SA",
        "name": ("Эр-Рияд", "Ar-Riyod", "Er-Riyad"),
        "lat": 24.7136, "lng": 46.6753, "population": 7000000, "capital": True,
        "desc": (
            "Эр-Рияд — столица Саудовской Аравии в центре Аравийского плато и самый большой город страны. Быстро растущий мегаполис, где соседствуют старый глинобитный квартал Диръия и небоскрёбы вроде Кингдом-центра.",
            "Ar-Riyod — Saudiya Arabistonining poytaxti, Arabiston platosi markazida joylashgan va mamlakatning eng katta shahri. Tez oʻsayotgan megapolisda qadimiy gʻishtin Diriya mahallasi va Kingdom Centre kabi osmonoʻpar binolar yonma-yon turadi.",
            "Er-Riyad — Saudiya Arabstanınıń paytaxtı, Arabstan platosınıń ortasında jaylasqan hám eldiń eń úlken qalası. Tez ósip atırǵan megapolista áyyemgi sawıt Diriya mahallesi hám Kingdom Centre sıyaqlı kóp qabatlı imaratlar qatar turadı.",
        ),
        "history": (
            [
                "1744 — В соседней Диръии союз Мухаммада ибн Сауда и Мухаммада ибн Абд аль-Ваххаба закладывает основу первого Саудовского государства.",
                "1902 — Абдул-Азиз ибн Сауд берёт Эр-Рияд, начиная объединение Аравии.",
                "1932 — Провозглашено Королевство Саудовская Аравия со столицей в Эр-Рияде.",
            ],
            [
                "1744 — Qoʻshni Diriyada Muhammad ibn Saud va Muhammad ibn Abdulvahhob ittifoqi birinchi Saudiya davlatining asosini qoʻydi.",
                "1902 — Abdulaziz ibn Saud Ar-Riyodni egallab, Arabistonni birlashtirishni boshladi.",
                "1932 — Poytaxti Ar-Riyod boʻlgan Saudiya Arabistoni Qirolligi eʼlon qilindi.",
            ],
            [
                "1744 — Qońsı Diriyada Muhammad ibn Saud hám Muhammad ibn Abdulvahhab awqamı birinshi Saudiya mámleketiniń tiykarın qoydı.",
                "1902 — Abdulaziz ibn Saud Er-Riyadtı iyelep, Arabstandı birlestiriwdi basladı.",
                "1932 — Paytaxtı Er-Riyad bolǵan Saudiya Arabstanı Patshalıǵı járiyalandı.",
            ],
        ),
        "industry": (
            [
                "SABIC — Одна из крупнейших химических компаний мира, штаб-квартира в Эр-Рияде.",
                "Saudi Telecom Company (stc) — Крупнейший оператор связи страны, штаб-квартира в Эр-Рияде.",
            ],
            [
                "SABIC — Dunyodagi eng yirik kimyo kompaniyalaridan biri, bosh ofisi Ar-Riyodda.",
                "Saudi Telecom Company (stc) — Mamlakatning eng yirik aloqa operatori, bosh ofisi Ar-Riyodda.",
            ],
            [
                "SABIC — Dúnyadaǵı eń úlken ximiya kompaniyalarınan biri, bas ofisi Er-Riyadta.",
                "Saudi Telecom Company (stc) — Eldiń eń úlken baylanıs operatorı, bas ofisi Er-Riyadta.",
            ],
        ),
    },
    {
        "country": "TH",
        "name": ("Бангкок", "Bangkok", "Bangkok"),
        "lat": 13.7563, "lng": 100.5018, "population": 5500000, "capital": True,
        "desc": (
            "Бангкок — столица Таиланда на реке Чаопрайя, шумный мегаполис с королевским дворцом, храмами Ват Пхо и Ват Арун и плавучими рынками. Полное церемониальное название города — одно из самых длинных в мире.",
            "Bangkok — Tailandning poytaxti, Chaopraya daryosi boʻyidagi gavjum megapolis; qirol saroyi, Vat Pxo va Vat Arun ibodatxonalari hamda suzuvchi bozorlari bor. Shaharning toʻliq tantanali nomi dunyodagi eng uzun nomlardan biri.",
            "Bangkok — Tailandtıń paytaxtı, Chaopraya dáryası boyındaǵı gúbirlegen megapolis; patsha saraylı, Vat Pxo hám Vat Arun ibadatxanaları hám suwda júziwshi bazarları bar. Qalanıń tolıq ráwishli atı dúnyadaǵı eń uzın atlardan biri.",
        ),
        "history": (
            [
                "1782 — Король Рама I переносит столицу на восточный берег Чаопрайи, основывая Бангкок.",
                "1932 — Бескровная революция вводит конституционную монархию вместо абсолютной.",
                "1967 — В Бангкоке подписана декларация о создании АСЕАН.",
            ],
            [
                "1782 — Qirol Rama I poytaxtni Chaoprayaning sharqiy sohiliga koʻchirib, Bangkokka asos soldi.",
                "1932 — Qonsiz inqilob mutlaq monarxiya oʻrniga konstitutsiyaviy monarxiyani joriy etdi.",
                "1967 — Bangkokda ASEAN tuzilishi toʻgʻrisidagi deklaratsiya imzolandi.",
            ],
            [
                "1782 — Patsha Rama I paytaxtı Chaoprayanıń shıǵıs jaǵalawına kóshirip, Bangkokqa tiykar saldı.",
                "1932 — Qansız revolyuciya mutlaq monarxiya ornına konstituciyalıq monarxiyanı engizdi.",
                "1967 — Bangkokta ASEAN dúziliwi haqqındaǵı deklaraciya qol qoyıldı.",
            ],
        ),
        "industry": (
            [
                "PTT — Государственная нефтегазовая компания Таиланда, штаб-квартира в Бангкоке.",
                "Charoen Pokphand (CP Group) — Один из крупнейших агропромышленных конгломератов Азии, штаб-квартира в Бангкоке.",
            ],
            [
                "PTT — Tailandning davlat neft-gaz kompaniyasi, bosh ofisi Bangkokda.",
                "Charoen Pokphand (CP Group) — Osiyodagi eng yirik agrosanoat konglomeratlaridan biri, bosh ofisi Bangkokda.",
            ],
            [
                "PTT — Tailandtıń mámleket neft-gaz kompaniyası, bas ofisi Bangkokta.",
                "Charoen Pokphand (CP Group) — Aziyadaǵı eń úlken agrosanaat konglomeratlarınan biri, bas ofisi Bangkokta.",
            ],
        ),
    },
    {
        "country": "ID",
        "name": ("Джакарта", "Jakarta", "Jakarta"),
        "lat": -6.2088, "lng": 106.8456, "population": 10500000, "capital": True,
        "desc": (
            "Джакарта — столица Индонезии на северном побережье острова Ява и один из самых густонаселённых городов мира. По закону 2022 года столица государства должна со временем перейти в новый город Нусантара на Калимантане.",
            "Jakarta — Indoneziyaning poytaxti, Yava orolining shimoliy sohilida joylashgan va dunyodagi eng gavjum shaharlardan biri. 2022-yilgi qonunga koʻra, davlat poytaxti keyinchalik Kalimantandagi yangi Nusantara shahriga koʻchirilishi kerak.",
            "Jakarta — Indoneziyanıń paytaxtı, Yava atawınıń arqa jaǵalawında jaylasqan hám dúnyadaǵı eń adamlı qalalardan biri. 2022-jılǵı nızamǵa kóre, mámleket paytaxtı keyinirek Kalimantandaǵı jańa Nusantara qalasına kóshiriliwi kerek.",
        ),
        "history": (
            [
                "1527 — Порт Сунда-Келапа переименован в Джаякарту — так начинается история нынешней Джакарты.",
                "1619 — Голландская Ост-Индская компания захватывает город и называет его Батавия.",
                "1945 — 17 августа в Джакарте провозглашена независимость Индонезии.",
            ],
            [
                "1527 — Sunda-Kelapa porti Jayakarta deb nomlandi — hozirgi Jakarta tarixi shunday boshlandi.",
                "1619 — Gollandiya Ost-Hind kompaniyasi shaharni egallab, uni Batavia deb atadi.",
                "1945 — 17-avgustda Jakartada Indoneziya mustaqilligi eʼlon qilindi.",
            ],
            [
                "1527 — Sunda-Kelapa porti Jayakarta dep ataldı — házirgi Jakarta tariyxı usılay baslandı.",
                "1619 — Gollandiya Ost-Hind kompaniyası qalanı iyelep, onı Batavia dep atadı.",
                "1945 — 17-avgustta Jakartada Indoneziya ǵárezsizligi járiyalandı.",
            ],
        ),
        "industry": (
            [
                "Pertamina — Государственная нефтегазовая компания Индонезии, штаб-квартира в Джакарте.",
                "GoTo — Технологическая группа, объединившая сервис Gojek и маркетплейс Tokopedia; штаб-квартира в Джакарте.",
            ],
            [
                "Pertamina — Indoneziyaning davlat neft-gaz kompaniyasi, bosh ofisi Jakartada.",
                "GoTo — Gojek xizmati va Tokopedia marketpleysini birlashtirgan texnologik guruh; bosh ofisi Jakartada.",
            ],
            [
                "Pertamina — Indoneziyanıń mámleket neft-gaz kompaniyası, bas ofisi Jakartada.",
                "GoTo — Gojek xızmeti menen Tokopedia marketpleysın birlestirgen texnologiyalıq topar; bas ofisi Jakartada.",
            ],
        ),
    },
    {
        "country": "UZ",
        "name": ("Бухара", "Buxoro", "Buxara"),
        "lat": 39.7747, "lng": 64.4286, "population": 280000, "capital": False,
        "desc": (
            "Бухара — один из древнейших городов Центральной Азии, более 2000 лет стоящий на Великом шёлковом пути. Исторический центр с минаретом Калян, медресе Мири-Араб и торговыми куполами включён в список ЮНЕСКО.",
            "Buxoro — Markaziy Osiyoning eng qadimiy shaharlaridan biri, 2000 yildan ortiq vaqtdan beri Buyuk ipak yoʻlida turibdi. Kalon minorasi, Mir Arab madrasasi va savdo gumbazlari joylashgan tarixiy markaz YuNESKO roʻyxatiga kiritilgan.",
            "Buxara — Orta Aziyanıń eń áyyemgi qalalarınan biri, 2000 jıldan artıq waqıttan beri Ullı jibek jolında turıptı. Kalon minarası, Mir Arab medresesi hám sawda gúmbezleri jaylasqan tariyxıy orayı YuNESKO dizimine kirgizilgen.",
        ),
        "history": (
            [
                "IX–X века — Бухара становится столицей государства Саманидов и центром науки; здесь учился Ибн Сина (Авиценна).",
                "1220 — Город захвачен и разорён войсками Чингисхана.",
                "1993 — Исторический центр Бухары включён в список Всемирного наследия ЮНЕСКО.",
            ],
            [
                "IX–X asrlar — Buxoro Somoniylar davlatining poytaxti va ilm markaziga aylandi; bu yerda Ibn Sino (Avitsenna) taʼlim olgan.",
                "1220 — Shahar Chingizxon qoʻshinlari tomonidan bosib olinib, vayron qilindi.",
                "1993 — Buxoroning tarixiy markazi YuNESKO Jahon merosi roʻyxatiga kiritildi.",
            ],
            [
                "IX–X ásirler — Buxara Samaniyler mámleketiniń paytaxtı hám ilim orayına aylandı; bul jerde Ibn Sino (Avicenna) bilim alǵan.",
                "1220 — Qala Shıńǵısxan áskerleri tárepinen basıp alınıp, qıran saldı.",
                "1993 — Buxaranıń tariyxıy orayı YuNESKO Dúnyalıq miyras dizimine kirgizildi.",
            ],
        ),
        "industry": (
            [
                "Бухарский нефтеперерабатывающий завод — Один из ключевых нефтеперерабатывающих заводов Узбекистана.",
                "Золотое шитьё (зардузи) — Традиционное бухарское ремесло: вышивка золотой нитью по бархату и шёлку.",
            ],
            [
                "Buxoro neftni qayta ishlash zavodi — Oʻzbekistonning asosiy neftni qayta ishlash zavodlaridan biri.",
                "Zardoʻzlik — Anʼanaviy buxoroliklar hunari: baxmal va ipakka oltin ip bilan tikish.",
            ],
            [
                "Buxara neftti qayta islew zavodı — Ózbekstannıń tiykarǵı neftti qayta islew zavodlarınan biri.",
                "Zardozlıq — Buxaralılardıń dástúriy kásibi: baxmal hám jipekke altın jip penen tigiw.",
            ],
        ),
    },
    {
        "country": "RU",
        "name": ("Санкт-Петербург", "Sankt-Peterburg", "Sankt-Peterburg"),
        "lat": 59.9343, "lng": 30.3351, "population": 5600000, "capital": False,
        "desc": (
            "Санкт-Петербург — второй по величине город России, основанный Петром I в устье Невы на берегу Балтики. «Северная столица» хранит Эрмитаж, Петергоф и разводные мосты, а исторический центр входит в список ЮНЕСКО.",
            "Sankt-Peterburg — Rossiyaning ikkinchi yirik shahri, Pyotr I tomonidan Boltiq boʻyida Neva daryosi quyilishida asos solingan. «Shimoliy poytaxt»da Ermitaj, Peterhof va koʻtariladigan koʻprikler bor, tarixiy markazi YuNESKO roʻyxatiga kiritilgan.",
            "Sankt-Peterburg — Rossiyanıń ekinshi úlken qalası, Pyotr I tárepinen Baltika boyında Neva dáryasınıń quyılısında tiykar salınǵan. «Arqa paytaxt»ta Ermitaj, Peterhof hám kóterilmeli kópirler bar, tariyxıy orayı YuNESKO dizimine kirgizilgen.",
        ),
        "history": (
            [
                "1703 — Пётр I закладывает Петропавловскую крепость; с неё начинается история города.",
                "1712 — Столица Российской империи переносится в Петербург; она останется здесь до 1918 года.",
                "1941 — Начинается блокада Ленинграда, продлившаяся около 900 дней.",
            ],
            [
                "1703 — Pyotr I Pyotr va Pavel qalʼasiga asos soldi; shahar tarixi shundan boshlandi.",
                "1712 — Rossiya imperiyasi poytaxti Peterburgga koʻchirildi; 1918-yilgacha shu yerda qoldi.",
                "1941 — Leningrad qamali boshlandi, u qariyb 900 kun davom etdi.",
            ],
            [
                "1703 — Pyotr I Pyotr hám Pavel qalasına tiykar saldı; qala tariyxı usıdan baslandı.",
                "1712 — Rossiya imperiyası paytaxtı Peterburgke kóshirildi; 1918-jılǵa shekem sol jerde qaldı.",
                "1941 — Leningrad qamalı baslandı, ol qarıyb 900 kún dawam etti.",
            ],
        ),
        "industry": (
            [
                "Кировский завод — Один из старейших машиностроительных заводов России, основан в 1801 году.",
                "Адмиралтейские верфи — Старейшее судостроительное предприятие России, основано в 1704 году.",
            ],
            [
                "Kirov zavodi — Rossiyaning eng qadimgi mashinasozlik zavodlaridan biri, 1801-yilda asos solingan.",
                "Admiralteyskiye verflari — Rossiyaning eng qadimgi kemasozlik korxonasi, 1704-yilda asos solingan.",
            ],
            [
                "Kirov zavodı — Rossiyanıń eń áyyemgi mashinasozlıq zavodlarınan biri, 1801-jılı tiykar salınǵan.",
                "Admiralteyskiye verfleri — Rossiyanıń eń áyyemgi kemasozlıq kárxanası, 1704-jılı tiykar salınǵan.",
            ],
        ),
    },
]
