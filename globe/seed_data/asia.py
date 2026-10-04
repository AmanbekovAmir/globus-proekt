"""Города Африки и Азии: Каир, Пекин, Дели, Сеул, Дубай, Астана, Самарканд."""

CITIES = [
    {
        "country": "EG",
        "name": ("Каир", "Qohira", "Qahira"),
        "lat": 30.0444, "lng": 31.2357, "population": 10000000, "capital": True,
        "desc": (
            "Каир — столица Египта и крупнейший город арабского мира, раскинувшийся на берегах Нила. Рядом с ним, в Гизе, стоят великие пирамиды, а старый город хранит сотни мечетей — за это Каир называют городом тысячи минаретов.",
            "Qohira — Misr poytaxti va arab dunyosining eng yirik shahri, Nil daryosi boʻyida joylashgan. Uning yonida, Gizada, buyuk piramidalar turibdi, eski shaharda esa yuzlab masjidlar saqlanib qolgan — shu bois Qohirani ming minorali shahar deb ataydilar.",
            "Qahira — Mısırdıń paytaxtı hám arab dúnyasınıń eń úlken qalası, Nil dáryasınıń boyında jaylasqan. Onıń janında, Gizada, ullı piramidalar turadı, eski qalada bolsa júzlegen meshitler saqlanıp qalǵan — sol sebepli Qahiranı mıń minaralı qala dep ataydı.",
        ),
        "history": (
            [
                "969 — Династия Фатимидов основывает Каир как новую столицу.",
                "970 — Заложена мечеть аль-Азхар, при которой вырос один из старейших университетов мира.",
                "1798 — Наполеон Бонапарт входит в Каир во время египетского похода.",
                "2011 — На площади Тахрир проходят массовые протесты, приведшие к отставке президента.",
            ],
            [
                "969 — Fotimiylar sulolasi Qohirani yangi poytaxt sifatida barpo etdi.",
                "970 — Al-Azhar masjidi qurila boshlandi; uning qoshida dunyodagi eng qadimgi universitetlardan biri vujudga keldi.",
                "1798 — Napoleon Bonapart Misr yurishi chogʻida Qohiraga kirdi.",
                "2011 — Tahrir maydonida ommaviy namoyishlar boʻlib oʻtdi va prezident iste'foga chiqdi.",
            ],
            [
                "969 — Fatimiyler dinastiyası Qahiranı jańa paytaxt retinde tiykarladı.",
                "970 — Al-Azhar meshiti salına basladı; onıń janında dúnyadaǵı eń áyyemgi universitetlerden biri payda boldı.",
                "1798 — Napoleon Bonapart Mısır júrisi waqtında Qahiraǵa kirdi.",
                "2011 — Tahrir maydanında jámáátlik namoyıslar ótti hám prezident iste'faǵa shıqtı.",
            ],
        ),
        "industry": (
            [
                "Banque Misr — Первый банк с египетским капиталом, основан в 1920 году в Каире.",
                "Commercial International Bank (CIB) — Один из крупнейших частных банков Египта со штаб-квартирой в Каире.",
                "Telecom Egypt — Национальный оператор связи Египта, штаб-квартира в Каире.",
            ],
            [
                "Banque Misr — Misr kapitali bilan tuzilgan birinchi bank, 1920-yilda Qohirada asos solingan.",
                "Commercial International Bank (CIB) — Misrning eng yirik xususiy banklaridan biri, bosh ofisi Qohirada.",
                "Telecom Egypt — Misrning milliy aloqa operatori, bosh ofisi Qohirada.",
            ],
            [
                "Banque Misr — Mısır kapitalı menen dúzilgen birinshi bank, 1920-jılı Qahirada tiykarlanǵan.",
                "Commercial International Bank (CIB) — Mısırdıń eń iri jeke banklarınan biri, bas ofisi Qahirada.",
                "Telecom Egypt — Mısırdıń milliy baylanıs operatorı, bas ofisi Qahirada.",
            ],
        ),
    },
    {
        "country": "CN",
        "name": ("Пекин", "Pekin", "Pekin"),
        "lat": 39.9042, "lng": 116.4074, "population": 21900000, "capital": True,
        "desc": (
            "Пекин — столица Китая, политический и культурный центр страны. Здесь находятся Запретный город, площадь Тяньаньмэнь и Храм Неба, а в окрестностях проходят участки Великой китайской стены.",
            "Pekin — Xitoyning poytaxti, mamlakatning siyosiy va madaniy markazi. Bu yerda Taqiqlangan shahar, Tyananmen maydoni va Osmon ibodatxonasi joylashgan, atrofida esa Buyuk Xitoy devorining boʻlaklari oʻtadi.",
            "Pekin — Qıtaydıń paytaxtı, eldiń siyasiy hám mádeniy orayı. Bul jerde Tıyım salınǵan qala, Tyananmen maydanı hám Aspan ibadatxanası jaylasqan, átirapında bolsa Ullı Qıtay diywalınıń bólekleri ótedi.",
        ),
        "history": (
            [
                "1267 — Хубилай-хан закладывает в этих местах столицу монгольской империи Юань — Ханбалык (Даду).",
                "1420 — Завершено строительство Запретного города — императорского дворца династий Мин и Цин.",
                "1 октября 1949 — Мао Цзэдун с трибуны Тяньаньмэнь провозглашает образование Китайской Народной Республики.",
                "2008 — Пекин принимает летние Олимпийские игры; в 2022 году становится первым городом, принявшим и летние, и зимние Игры.",
            ],
            [
                "1267 — Xubilay xon bu yerda Yuan mongol imperiyasining poytaxti — Xanbalik (Dadu)ga asos soldi.",
                "1420 — Min va Sin sulolalarining imperator saroyi — Taqiqlangan shahar qurilishi yakunlandi.",
                "1949-yil 1-oktabr — Mao Szedun Tyananmen minbaridan Xitoy Xalq Respublikasi tashkil etilganini eʼlon qildi.",
                "2008 — Pekin yozgi Olimpiya oʻyinlarini qabul qildi; 2022-yilda yozgi va qishki oʻyinlarni oʻtkazgan birinchi shahar boʻldi.",
            ],
            [
                "1267 — Xubilay xan bul jerde Yuan mongol imperiyasınıń paytaxtı — Xanbalik (Dadu)ǵa tiykar saldı.",
                "1420 — Min hám Sin dinastiyalarınıń imperator sarayı — Tıyım salınǵan qala qurılısı tamamlandı.",
                "1949-jıl 1-oktyabr — Mao Szedun Tyananmen minberinen Qıtay Xalıq Respublikası dúzilgenin járiyaladı.",
                "2008 — Pekin jazǵı Olimpiada oyınların qabıllady; 2022-jılı jazǵı hám qısqı oyınlardı ótkergen birinshi qala boldı.",
            ],
        ),
        "industry": (
            [
                "Lenovo — Один из крупнейших в мире производителей персональных компьютеров; основана в Пекине в 1984 году.",
                "Xiaomi — Производитель смартфонов и умной электроники, основана в Пекине в 2010 году.",
                "Baidu — Крупнейшая китайская поисковая система и разработчик технологий искусственного интеллекта; штаб-квартира в Пекине.",
            ],
            [
                "Lenovo — Dunyodagi eng yirik shaxsiy kompyuter ishlab chiqaruvchilardan biri; 1984-yilda Pekinda asos solingan.",
                "Xiaomi — Smartfonlar va aqlli elektronika ishlab chiqaruvchi, 2010-yilda Pekinda asos solingan.",
                "Baidu — Xitoyning eng yirik qidiruv tizimi va sunʼiy intellekt texnologiyalari ishlab chiqaruvchisi; bosh ofisi Pekinda.",
            ],
            [
                "Lenovo — Dúnyadaǵı eń iri jeke kompyuter shıǵarıwshılardan biri; 1984-jılı Pekinde tiykarlanǵan.",
                "Xiaomi — Smartfonlar hám aqıllı elektronika shıǵarıwshı, 2010-jılı Pekinde tiykarlanǵan.",
                "Baidu — Qıtaydıń eń iri izlew sisteması hám jasalma intellekt texnologiyaların islep shıǵarıwshı; bas ofisi Pekinde.",
            ],
        ),
    },
    {
        "country": "IN",
        "name": ("Дели", "Dehli", "Dehli"),
        "lat": 28.6139, "lng": 77.2090, "population": 16800000, "capital": True,
        "desc": (
            "Дели — столица Индии, один из старейших непрерывно населённых городов мира, стоящий на реке Ямуна. Старый город с Красным фортом соседствует с широкими проспектами Нью-Дели, построенного в начале XX века.",
            "Dehli — Hindistonning poytaxti, dunyodagi eng qadimgi uzluksiz yashab kelayotgan shaharlardan biri, Yamuna daryosi boʻyida joylashgan. Qizil qalʼali eski shahar XX asr boshida qurilgan Nyu-Dehlining keng xiyobonlari bilan yonma-yon turadi.",
            "Dehli — Hindstannıń paytaxtı, dúnyadaǵı eń áyyemgi úzliksiz jasap kiyatırǵan qalalardan biri, Yamuna dáryasınıń boyında jaylasqan. Qızıl qorǵanlı eski qala XX ásir basında qurılǵan Nyu-Dehliniń keń kósheleri menen qatar jaylasqan.",
        ),
        "history": (
            [
                "1206 — Основан Делийский султанат; Дели на несколько веков становится столицей его правителей.",
                "1648 — Император Шах-Джахан завершает строительство Шахджаханабада — нынешнего Старого Дели с Красным фортом.",
                "1911 — Британская Индия объявляет о переносе столицы из Калькутты в Дели; Нью-Дели торжественно открывается в 1931 году.",
                "15 августа 1947 — Индия обретает независимость; Дели становится столицей суверенного государства.",
            ],
            [
                "1206 — Dehli sultonligi tashkil topdi; Dehli bir necha asr davomida uning hukmdorlari poytaxti boʻldi.",
                "1648 — Imperator Shohjahon Shohjahonobodni — Qizil qalʼali hozirgi Eski Dehlini — qurib bitkazdi.",
                "1911 — Britaniya Hindistoni poytaxtni Kalkuttadan Dehliga koʻchirishni eʼlon qildi; Nyu-Dehli 1931-yilda tantanali ochildi.",
                "1947-yil 15-avgust — Hindiston mustaqillikka erishdi; Dehli mustaqil davlatning poytaxtiga aylandi.",
            ],
            [
                "1206 — Dehli sultanlıǵı dúzildi; Dehli bir neshe ásir dawamında onıń húkimdarları paytaxtı boldı.",
                "1648 — Imperator Shahjahan Shahjahanabadtı — Qızıl qorǵanlı házirgi Eski Dehlini — qurıp pitkerdi.",
                "1911 — Britaniya Hindstanı paytaxtı Kalkuttadan Dehliǵe kóshiriw haqqında járiyaladı; Nyu-Dehli 1931-jılı saltanatlı ashıldı.",
                "1947-jıl 15-avgust — Hindstan ǵárezsizlikke eristi; Dehli ǵárezsiz mámleketiniń paytaxtına aylandı.",
            ],
        ),
        "industry": (
            [
                "Maruti Suzuki — Крупнейший индийский производитель легковых автомобилей; штаб-квартира в Нью-Дели.",
                "Bharti Airtel — Одна из крупнейших телекоммуникационных компаний мира, штаб-квартира в Нью-Дели.",
                "Indian Oil Corporation — Крупнейшая нефтяная компания Индии, штаб-квартира в Нью-Дели.",
            ],
            [
                "Maruti Suzuki — Hindistonning eng yirik yengil avtomobil ishlab chiqaruvchisi; bosh ofisi Nyu-Dehlida.",
                "Bharti Airtel — Dunyodagi eng yirik telekommunikatsiya kompaniyalaridan biri, bosh ofisi Nyu-Dehlida.",
                "Indian Oil Corporation — Hindistonning eng yirik neft kompaniyasi, bosh ofisi Nyu-Dehlida.",
            ],
            [
                "Maruti Suzuki — Hindstannıń eń iri jeńil avtomobil shıǵarıwshısı; bas ofisi Nyu-Dehlide.",
                "Bharti Airtel — Dúnyadaǵı eń iri telekommunikaciya kompaniyalarınan biri, bas ofisi Nyu-Dehlide.",
                "Indian Oil Corporation — Hindstannıń eń iri neft kompaniyası, bas ofisi Nyu-Dehlide.",
            ],
        ),
    },
    {
        "country": "KR",
        "name": ("Сеул", "Seul", "Seul"),
        "lat": 37.5665, "lng": 126.9780, "population": 9400000, "capital": True,
        "desc": (
            "Сеул — столица Южной Кореи, раскинувшаяся по обе стороны реки Хан и окружённая горами. Футуристичные небоскрёбы и технопарки соседствуют здесь с дворцами династии Чосон.",
            "Seul — Janubiy Koreyaning poytaxti, Xan daryosining ikki tomonida joylashgan va togʻlar bilan oʻralgan. Bu yerda futuristik osmonoʻparlar va texnoparklar Choson sulolasi saroylari bilan yonma-yon turadi.",
            "Seul — Qubla Koreyanıń paytaxtı, Xan dáryasınıń eki tárepinde jaylasqan hám taw menen qorshalǵan. Bul jerde futuristik kóp qabatlı imaratlar hám texnoparklar Choson dinastiyası saraylarına qatar turadı.",
        ),
        "history": (
            [
                "1394 — Основатель династии Чосон Тхэджо переносит столицу в Ханян — нынешний Сеул.",
                "1446 — Король Седжон обнародует корейский алфавит хангыль.",
                "1950 — Начинается Корейская война; за три года боёв Сеул четыре раза переходит из рук в руки.",
                "1988 — Сеул принимает летние Олимпийские игры.",
            ],
            [
                "1394 — Choson sulolasi asoschisi Taejo poytaxtni Xanyangga — hozirgi Seulga koʻchirdi.",
                "1446 — Qirol Sejong koreys alifbosi — xangulni eʼlon qildi.",
                "1950 — Koreya urushi boshlandi; uch yillik janglar davomida Seul toʻrt marta qoʻldan-qoʻlga oʻtdi.",
                "1988 — Seul yozgi Olimpiya oʻyinlarini qabul qildi.",
            ],
            [
                "1394 — Choson dinastiyasınıń tiykarlawshısı Taejo paytaxtı Xanyangǵa — házirgi Seulge kóshirdi.",
                "1446 — Patsha Sejong koreys álipbesi — xangıldı járiyaladı.",
                "1950 — Koreya urısı baslandı; úsh jıllıq urıslar dawamında Seul tórt ret qoldan-qolǵa ótti.",
                "1988 — Seul jazǵı Olimpiada oyınların qabıllady.",
            ],
        ),
        "industry": (
            [
                "Samsung — Крупнейший южнокорейский конгломерат (электроника, строительство, финансы); штаб-квартира группы в Сеуле.",
                "Hyundai Motor Company — Один из крупнейших автопроизводителей мира, штаб-квартира в Сеуле.",
                "LG — Производитель бытовой техники, электроники и аккумуляторов; штаб-квартира в Сеуле.",
            ],
            [
                "Samsung — Janubiy Koreyaning eng yirik konglomerati (elektronika, qurilish, moliya); guruhning bosh ofisi Seulda.",
                "Hyundai Motor Company — Dunyodagi eng yirik avtomobil ishlab chiqaruvchilardan biri, bosh ofisi Seulda.",
                "LG — Maishiy texnika, elektronika va akkumulyatorlar ishlab chiqaruvchi; bosh ofisi Seulda.",
            ],
            [
                "Samsung — Qubla Koreyanıń eń iri konglomerati (elektronika, qurılıs, finans); toparınıń bas ofisi Seulde.",
                "Hyundai Motor Company — Dúnyadaǵı eń iri avtomobil shıǵarıwshılardan biri, bas ofisi Seulde.",
                "LG — Turmıs texnikası, elektronika hám akkumulyatorlar shıǵarıwshı; bas ofisi Seulde.",
            ],
        ),
    },
    {
        "country": "AE",
        "name": ("Дубай", "Dubay", "Dubay"),
        "lat": 25.2048, "lng": 55.2708, "population": 3600000, "capital": False,
        "desc": (
            "Дубай — крупнейший город Объединённых Арабских Эмиратов на берегу Персидского залива. Из небольшого торгового порта он за полвека вырос в мировой центр авиации, торговли и туризма с небоскрёбами, включая Бурдж-Халифу.",
            "Dubay — Birlashgan Arab Amirliklarining eng yirik shahri, Fors koʻrfazi sohilida joylashgan. Kichik savdo portidan yarim asr ichida aviatsiya, savdo va turizmning jahon markaziga, Burj Xalifa kabi osmonoʻparlar shahriga aylandi.",
            "Dubay — Birlesken Arab Ámirliklerınıń eń úlken qalası, Pars qoltıǵınıń jaǵasında jaylasqan. Kishi sawda portınan yarım ásir ishinde aviaciya, sawda hám turizmniń dúnyalıq orayına, Burj Xalifa sıyaqlı kóp qabatlı imaratlar qalasına aylandı.",
        ),
        "history": (
            [
                "1833 — Клан Аль Мактум из племени бани яс поселяется у бухты Дубай-Крик и основывает самостоятельное шейхство.",
                "2 декабря 1971 — Дубай входит в состав образованных Объединённых Арабских Эмиратов.",
                "1979 — Открыт порт Джебель-Али — крупнейший искусственный порт мира.",
                "2010 — Открыта Бурдж-Халифа — самое высокое здание мира (828 м).",
            ],
            [
                "1833 — Bani Yos qabilasidan boʻlgan Al Maktum urugʻi Dubay-Krik koʻrfazi yonida joylashib, mustaqil shayxlik asos soldi.",
                "1971-yil 2-dekabr — Dubay tashkil etilgan Birlashgan Arab Amirliklari tarkibiga kirdi.",
                "1979 — Dunyodagi eng yirik sunʼiy port — Jabal Ali porti ochildi.",
                "2010 — Dunyodagi eng baland bino — Burj Xalifa (828 m) ochildi.",
            ],
            [
                "1833 — Bani Yos qáwiminen bolǵan Al Maktum urıwı Dubay-Krik qoltıǵı janında jaylasıp, óz aldına shayxlıqqa tiykar saldı.",
                "1971-jıl 2-dekabr — Dubay dúzilgen Birlesken Arab Ámirlikleri quramına kirdi.",
                "1979 — Dúnyadaǵı eń iri jasalma port — Jabal Ali portı ashıldı.",
                "2010 — Dúnyadaǵı eń biyik imarat — Burj Xalifa (828 m) ashıldı.",
            ],
        ),
        "industry": (
            [
                "Emirates — Крупнейшая авиакомпания Ближнего Востока с хабом в международном аэропорту Дубая.",
                "DP World — Один из крупнейших в мире операторов морских портов и логистики; штаб-квартира в Дубае.",
                "Emaar Properties — Девелопер, построивший Бурдж-Халифу и торговый центр Dubai Mall.",
            ],
            [
                "Emirates — Yaqin Sharqdagi eng yirik aviakompaniya; tayanch aeroporti Dubay xalqaro aeroporti.",
                "DP World — Dunyodagi eng yirik dengiz portlari va logistika operatorlaridan biri; bosh ofisi Dubayda.",
                "Emaar Properties — Burj Xalifa va Dubai Mall savdo markazini qurgan dasturchi kompaniya.",
            ],
            [
                "Emirates — Jaqın Shıǵıstaǵı eń iri aviakompaniya; tayanısh aeroportı Dubay xalıqaralıq aeroportı.",
                "DP World — Dúnyadaǵı eń iri teńiz portları hám logistika operatorlarınan biri; bas ofisi Dubayda.",
                "Emaar Properties — Burj Xalifa hám Dubai Mall sawda orayın qurǵan qurılıs kompaniyası.",
            ],
        ),
    },
    {
        "country": "KZ",
        "name": ("Астана", "Ostona", "Astana"),
        "lat": 51.1694, "lng": 71.4491, "population": 1350000, "capital": True,
        "desc": (
            "Астана — столица Казахстана, расположенная на реке Ишим посреди степей. Современный город с футуристичной архитектурой почти целиком построен после переноса столицы в 1997 году.",
            "Ostona — Qozogʻistonning poytaxti, dasht oʻrtasida Esil daryosi boʻyida joylashgan. Futuristik meʼmorchilikka ega zamonaviy shahar poytaxt 1997-yilda koʻchirilgach, deyarli butunlay qaytadan qurilgan.",
            "Astana — Qazaqstannıń paytaxtı, dala ortasında Esil dáryasınıń boyında jaylasqan. Futuristik arxitekturalı zamanagóy qala paytaxt 1997-jılı kóshirilgennen keyin derlik pútkilley qaytadan qurılǵan.",
        ),
        "history": (
            [
                "1830 — Основано казачье укрепление Акмолинское, позднее ставшее городом.",
                "1961 — Город получает название Целиноград в связи с освоением целинных земель.",
                "1997 — Столица Казахстана переносится из Алма-Аты в Акмолу; в 1998 году город получает название Астана.",
                "2022 — После переименования в Нур-Султан городу возвращено название Астана.",
            ],
            [
                "1830 — Akmola kazak istehkomi asos solindi, keyinchalik u shaharga aylandi.",
                "1961 — Choʻl yerlarini oʻzlashtirish munosabati bilan shahar Selinograd deb atala boshladi.",
                "1997 — Qozogʻiston poytaxti Almatidan Akmolaga koʻchirildi; 1998-yilda shahar Ostona nomini oldi.",
                "2022 — Nur-Sulton deb qayta nomlangan shaharga Ostona nomi qaytarildi.",
            ],
            [
                "1830 — Akmola kazak bekinisi tiykarlandı, keyinirek ol qalaǵa aylandı.",
                "1961 — Tıń jerlerdi ózlestiriw munasábeti menen qala Selinograd dep atala basladı.",
                "1997 — Qazaqstan paytaxtı Almatıdan Akmolaǵa kóshirildi; 1998-jılı qala Astana atın aldı.",
                "2022 — Nur-Sultan dep qayta atalǵan qalaǵa Astana atı qaytarıldı.",
            ],
        ),
        "industry": (
            [
                "Самрук-Казына — Национальный фонд благосостояния, управляющий крупнейшими государственными компаниями Казахстана.",
                "КазМунайГаз — Национальная нефтегазовая компания Казахстана, штаб-квартира в Астане.",
                "Международный финансовый центр «Астана» (AIFC) — Финансовая площадка со своей правовой системой на основе английского права; открыта в 2018 году.",
            ],
            [
                "Samruk-Qozina — Qozogʻistonning yirik davlat kompaniyalarini boshqaradigan milliy farovonlik jamgʻarmasi.",
                "QozMunayGaz — Qozogʻistonning milliy neft-gaz kompaniyasi, bosh ofisi Ostonada.",
                "«Ostona» xalqaro moliya markazi (AIFC) — Ingliz huquqi asosidagi oʻz huquqiy tizimiga ega moliyaviy maydon; 2018-yilda ochilgan.",
            ],
            [
                "Samruk-Qazına — Qazaqstannıń iri mámleketlik kompaniyaların basqaratuǵın milliy abadanshılıq qorı.",
                "QazMunayGaz — Qazaqstannıń milliy neft-gaz kompaniyası, bas ofisi Astanada.",
                "«Astana» xalıqaralıq finans orayı (AIFC) — Ingliz huqıqı tiykarındaǵı óz huqıqıy sistemasına iye finans maydanı; 2018-jılı ashılǵan.",
            ],
        ),
    },
    {
        "country": "UZ",
        "name": ("Самарканд", "Samarqand", "Samarqand"),
        "lat": 39.6542, "lng": 66.9597, "population": 550000, "capital": False,
        "desc": (
            "Самарканд — один из древнейших городов Центральной Азии, возраст которого превышает 2500 лет. Жемчужина Великого шёлкового пути: площадь Регистан, мавзолей Гур-Эмир и ансамбль Шахи-Зинда входят в число главных памятников региона.",
            "Samarqand — Markaziy Osiyoning eng qadimgi shaharlaridan biri, yoshi 2500 yildan ortiq. Buyuk ipak yoʻlining injusi: Registon maydoni, Gʻur Amir maqbarasi va Shohi Zinda ansambli mintaqaning eng muhim yodgorliklari qatoriga kiradi.",
            "Samarqand — Orta Aziyanıń eń áyyemgi qalalarınan biri, jası 2500 jıldan asadı. Ullı Jipek jolınıń injusi: Registan maydanı, Gúr Amir maqbarası hám Shohi Zinda ansamblı aymaqtıń eń áhmiyetli estelikleri qatarına kiredi.",
        ),
        "history": (
            [
                "329 до н. э. — Александр Македонский берёт Мараканду — так греки называли Самарканд.",
                "1370 — Амир Темур делает Самарканд столицей своей империи и украшает его великолепными постройками.",
                "1428 — Мирзо Улугбек завершает строительство обсерватории, где создан один из лучших звёздных каталогов Средневековья.",
                "1925 — Самарканд становится первой столицей Узбекской ССР; в 1930 году столица переносится в Ташкент.",
                "2001 — Исторический центр Самарканда включён в список Всемирного наследия ЮНЕСКО.",
            ],
            [
                "Miloddan avvalgi 329-yil — Iskandar Zulqarnayn Marakandani — yunonlar Samarqandni shunday atagan — egalladi.",
                "1370 — Amir Temur Samarqandni imperiyasi poytaxtiga aylantirdi va uni mahobatli binolar bilan bezadi.",
                "1428 — Mirzo Ulugʻbek rasadxona qurilishini yakunladi; oʻrta asrlarning eng yaxshi yulduzlar katalogidan biri shu yerda yaratildi.",
                "1925 — Samarqand Oʻzbekiston SSRning birinchi poytaxti boʻldi; 1930-yilda poytaxt Toshkentga koʻchirildi.",
                "2001 — Samarqandning tarixiy markazi YuNESKOning Butunjahon merosi roʻyxatiga kiritildi.",
            ],
            [
                "Miladdan aldınǵı 329-jıl — Iskandar Zulqarnayn Marakandanı — greklar Samarqandtı usılay atap kelgen — iyeledi.",
                "1370 — Ámir Temur Samarqandtı imperiyasınıń paytaxtına aylandırdı hám onı kórkem imaratlar menen bezedi.",
                "1428 — Mırza Ulıǵbek rasadxana qurılısın tamamladı; orta ásirlerdiń eń jaqsı juldızlar katalogınan biri usı jerde jaratıldı.",
                "1925 — Samarqand Ózbekstan SSR-diń birinshi paytaxtı boldı; 1930-jılı paytaxt Tashkentke kóshirildi.",
                "2001 — Samarqandtıń tariyxıy orayı YuNESKO-nıń Dúnyalıq miyras dizimine kirgizildi.",
            ],
        ),
        "industry": (
            [
                "SamAuto — Автомобильный завод, выпускающий автобусы и грузовики; один из крупнейших промышленных предприятий региона.",
                "Konigil — Мастерская шёлковой бумаги, возрождающая древнюю самаркандскую технологию ручного производства бумаги.",
                "Туризм и ремёсла — Регистан, Шахи-Зинда и мастерские керамики, ковров и шёлка ежегодно принимают миллионы туристов.",
            ],
            [
                "SamAuto — Avtobus va yuk mashinalari ishlab chiqaradigan avtomobil zavodi; mintaqadagi yirik sanoat korxonalaridan biri.",
                "Konigil — Qadimiy Samarqand qogʻoz tayyorlash texnologiyasini qayta tiklayotgan ipak qogʻoz ustaxonasi.",
                "Turizm va hunarmandchilik — Registon, Shohi Zinda hamda kulolchilik, gilam va ipak ustaxonalari yiliga millionlab sayyohlarni qabul qiladi.",
            ],
            [
                "SamAuto — Avtobus hám júk mashinaların shıǵaratuǵın avtomobil zavodı; aymaqtaǵı iri ónerkásip kárxanalarınan biri.",
                "Konigil — Áyyemgi Samarqand qaǵaz tayarlaw texnologiyasın qayta tiklep atırǵan jipek qaǵaz ustaxanası.",
                "Turizm hám ónermentshilik — Registan, Shohi Zinda hám kulalshılıq, gilem hám jipek ustaxanaları jılına millionlaǵan sayaxatshını qabıllaydı.",
            ],
        ),
    },
]
