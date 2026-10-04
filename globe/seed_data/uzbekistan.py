"""Города Узбекистана: областные центры и другие крупные города.

Областные центры Узбекистана. Ташкент и Нукус продублированы из fixtures.json, чтобы
seed_world добавлял их, даже если fixtures не загружали (дублей не будет: поиск по названию).
Формат тот же, что в extra.py: тексты — тройки (ru, uz, qr).
"""
from .extra import _city

CITIES = [
    _city(
        "UZ", ('Ташкент', 'Toshkent', 'Tashkent'), 41.2995, 69.2401, 3000000, True,
        (
            'Ташкент — столица Узбекистана и крупнейший город Центральной Азии. Он лежит в предгорьях Западного Тянь-Шаня, на реке Чирчик, на пересечении древних торговых путей. Сегодня это административный, финансовый и научный центр страны: здесь расположены правительство, крупнейшие банки, университеты и большинство национальных компаний.',
            'Toshkent — Oʻzbekistonning poytaxti va Markaziy Osiyodagi eng yirik shahar. U Gʻarbiy Tyan-Shan togʻ etaklarida, Chirchiq daryosi boʻyida, qadimiy savdo yoʻllari kesishgan joyda joylashgan. Bugungi kunda bu mamlakatning maʼmuriy, moliyaviy va ilmiy markazi: bu yerda hukumat, yirik banklar, universitetlar va koʻpchilik milliy kompaniyalar joylashgan.',
            'Tashkent — Ózbekstannıń paytaxtı hám Orta Aziyadaǵı eń úlken qala. Ol Batıs Tyan-Shan taw etegindegi, Shırshıq dáryasınıń boyında, áyyemgi sawda jolları kesilisken jerde jaylasqan. Búgingi kúnde ol eldiń ákimshilik, finans hám ilim orayı: bul jerde húkimet, iri bankler, universitetler hám kóplegen milliy kompaniyalar jaylasqan.',
        ),
        [
            ('Древность и Средневековье — Город известен как Чач, а затем как Шаш: он стоял на ответвлениях Великого шёлкового пути и славился ремёслами и торговлей.', 'Qadimgi davr va oʻrta asrlar — Shahar Choch, keyinroq Shosh nomi bilan mashhur boʻlgan: u Buyuk ipak yoʻlining tarmoqlarida joylashib, hunarmandchilik va savdosi bilan dovruq qozongan.', 'Áyyemgi dáwir hám orta ásirler — Qala dáslep Chach, keyinirek Shash atı menen belgili bolǵan: ol Ullı Jipek jolınıń tarmaqlarında jaylasıp, ónermentshilik hám sawdası menen dańqı shıqqan.'),
            ('1865 — Ташкент занят российскими войсками под командованием генерала Михаила Черняева; позднее город становится центром Туркестанского генерал-губернаторства.', '1865 — Toshkentni general Mixail Chernyaev boshchiligidagi Rossiya qoʻshinlari egalladi; keyinchalik shahar Turkiston general-gubernatorligining markaziga aylandi.', '1865 — Tashkentti general Mixail Chernyaev basshılıǵındaǵı Rossiya áskerleri iyeledi; keyin qala Túrkstan general-gubernatorlıǵınıń orayına aylandı.'),
            ('1930 — Столица Узбекской ССР переносится из Самарканда в Ташкент.', '1930 — Oʻzbekiston SSR poytaxti Samarqanddan Toshkentga koʻchirildi.', '1930 — Ózbekstan SSR-diń paytaxtı Samarqandtan Tashkentke kóshirildi.'),
            ('Январь 1966 — Подписана Ташкентская декларация об урегулировании конфликта между Индией и Пакистаном.', '1966-yil yanvar — Hindiston va Pokiston oʻrtasidagi mojaroni tinch yoʻl bilan hal etish boʻyicha Toshkent deklaratsiyasi imzolandi.', '1966-jıl yanvar — Hindstan menen Pákstan arasındaǵı ziddiyattı tınıshlıqta sheshiw haqqındaǵı Tashkent deklaraciyası imzalandı.'),
            ('26 апреля 1966 — Мощное землетрясение разрушает значительную часть центра; отстраивать Ташкент помогают все республики СССР.', '1966-yil 26-aprel — Kuchli zilzila shahar markazining katta qismini vayron qildi; Toshkentni qayta qurishda SSSRning barcha respublikalari yordam berdi.', '1966-jıl 26-aprel — Kúshli jer silkiniwi qala orayınıń úlken bólegin buzdı; Tashkentti qayta qurıwǵa SSSR-diń barlıq respublikaları járdem berdi.'),
            ('1991 — Узбекистан обретает независимость, Ташкент становится столицей суверенного государства.', '1991 — Oʻzbekiston mustaqillikka erishdi, Toshkent mustaqil davlatning poytaxtiga aylandi.', '1991 — Ózbekstan óz aldına ǵárezsizlikke eristi, Tashkent ǵárezsiz mámleketiniń paytaxtına aylandı.'),
        ],
        [
            ('Ташкентское авиационное производственное объединение — Один из старейших авиазаводов на постсоветском пространстве; в советское время выпускал транспортные самолёты Ил-76.', 'Toshkent aviatsiya ishlab chiqarish birlashmasi — MDHning eng qadimgi aviazavodlaridan biri; sovet davrida Il-76 yuk samolyotlarini ishlab chiqargan.', 'Tashkent aviaciya óndiris birlespesi — MDH-nıń eń áyyemgi aviazavodlarınan biri; sovet dáwirinde Il-76 júk ushaqların shıǵarǵan.'),
            ('Uzbekistan Airways — Национальный авиаперевозчик; главный хаб — Ташкентский международный аэропорт.', 'Uzbekistan Airways — Milliy aviakompaniya; asosiy tayanch aeroporti — Toshkent xalqaro aeroporti.', 'Uzbekistan Airways — Milliy aviakompaniya; tiykarǵı tayanısh aeroportı — Tashkent xalıqaralıq aeroportı.'),
            ('Artel — Крупный производитель бытовой техники и электроники со штаб-квартирой в Ташкенте.', 'Artel — Maishiy texnika va elektronika ishlab chiqaruvchi yirik kompaniya; bosh ofisi Toshkentda.', 'Artel — Turmıs texnikası hám elektronika shıǵarıwshı iri kompaniya; bas ofisi Tashkentte.'),
            ('Uzum — Финтех- и маркетплейс-экосистема, первый «единорог» Узбекистана.', 'Uzum — Fintex va marketplace ekotizimi; mamlakatning birinchi «unicorn» kompaniyasi.', 'Uzum — Fintex hám marketplace ekosisteması; eldiń birinshi «unicorn» kompaniyası.'),
            ('Узбекнефтегаз — Государственный нефтегазовый холдинг, управляющий добычей и переработкой углеводородов страны.', 'Oʻzbekneftgaz — Mamlakatning uglevodorodlarini qazib olish va qayta ishlashni boshqaradigan davlat neft-gaz xoldingi.', 'Ózbekneftgaz — Eldegi uglevodorodlardı qazıp alıw hám qayta islewdi basqaratuǵın mámleketlik neft-gaz xoldingi.'),
        ],
    ),

    _city(
        "UZ", ('Нукус', 'Nukus', 'Nókis'), 42.46, 59.6166, 320000, False,
        (
            'Нукус — столица Республики Каракалпакстан в составе Узбекистана. Город стоит на правом берегу Амударьи, у края пустыни Кызылкум. Это административный, культурный и научный центр региона, известный всему миру музеем имени Игоря Савицкого с уникальной коллекцией русского авангарда и каракалпакского искусства. Отсюда отправляются экспедиции к бывшему порту Муйнак и к высохшему дну Аральского моря.',
            'Nukus — Oʻzbekiston tarkibidagi Qoraqalpogʻiston Respublikasining poytaxti. Shahar Amudaryoning oʻng qirgʻogʻida, Qizilqum choʻli chekkasida joylashgan. Bu hududning maʼmuriy, madaniy va ilmiy markazi; butun dunyoga Igor Savitskiy nomidagi muzey — rus avangardi va qoraqalpoq sanʼatining noyob toʻplami bilan mashhur. Bu yerdan sobiq Moʻynoq porti va Orol dengizining qurigan tubiga ekspeditsiyalar yoʻlga chiqadi.',
            'Nókis — Ózbekstan quramındaǵı Qaraqalpaqstan Respublikasınıń paytaxtı. Qala Ámiwdáryanıń oń jaǵasında, Qızılqum shóliniń shetinde jaylasqan. Ol aymaqtıń ákimshilik, mádeniy hám ilimiy orayı; pútkil dúnyaǵa Igor Savitskiy atındaǵı muzey — rus avangardı hám qaraqalpaq kórkem ónerdiń ózgeshe toplamı menen belgili. Bul jerden burınǵı Moynaq portına hám Aral teńiziniń qurıp qalǵan tubine ekspediciyalar jolǵa shıǵadı.',
        ),
        [
            ('1932 — Нукус получает статус города; к 1950-м годам из небольшого посёлка он превращается в современный советский город с широкими проспектами.', '1932 — Nukus shahar maqomini oldi; 1950-yillarga kelib kichik posyolkadan keng xiyobonli zamonaviy sovet shahriga aylandi.', '1932 — Nókis qala statusın aldı; 1950-jıllarǵa kelip kishi posyolkadan keń kóshelerge iye zamanagóy sovet qalasına aylandı.'),
            ('1960-е — Аральское море начинает стремительно мелеть из-за забора воды Амударьи и Сырдарьи на орошение; экологическая катастрофа затрагивает весь регион.', '1960-yillar — Amudaryo va Sirdaryo suvlarining sugʻorishga olinishi tufayli Orol dengizi tez qurib bora boshladi; ekologik falokat butun mintaqaga taʼsir qildi.', '1960-jıllar — Ámiwdárya hám Sırdárya suwınıń suwǵarıwǵa alınıwı sebepli Aral teńizi tez qurıy basladı; ekologiyalıq apat pútkil aymaqqa tásir etti.'),
            ('1966 — По инициативе Игоря Савицкого в Нукусе открывается музей; его коллекция считается одной из крупнейших в мире собраний русского авангарда.', '1966 — Igor Savitskiy tashabbusi bilan Nukusda muzey ochildi; uning toʻplami rus avangardining dunyodagi eng yirik toʻplamlaridan biri hisoblanadi.', '1966 — Igor Savitskiy baslaması menen Nókiste muzey ashıldı; onıń toplamı rus avangardınıń dúnyadaǵı eń iri toplamlarınıń biri delinedi.'),
            ('1992 — Каракалпакстан получает название и статус Республики Каракалпакстан в составе Узбекистана; Нукус остаётся её столицей.', '1992 — Qoraqalpogʻiston Oʻzbekiston tarkibidagi Qoraqalpogʻiston Respublikasi nomi va maqomini oldi; Nukus uning poytaxti boʻlib qoldi.', '1992 — Qaraqalpaqstan Ózbekstan quramındaǵı Qaraqalpaqstan Respublikası atı hám statusın aldı; Nókis onıń paytaxtı bolıp qaldı.'),
        ],
        [
            ('Хлопкопереработка и текстиль — Хлопок остаётся одной из опор экономики региона; в Нукусе работают предприятия первичной переработки хлопка.', 'Paxta tozalash va toʻqimachilik — Paxta mintaqa iqtisodiyotining asosiy tayanchlaridan biri; Nukusda paxtani dastlabki qayta ishlash korxonalari faoliyat yuritadi.', 'Paxta tazalaw hám toqımashılıq — Paxta aymaq ekonomikasınıń tiykarǵı tayanıshlarınan biri; Nókiste paxtanı dáslepki qayta islew kárxanaları isleydi.'),
            ('Пищевая промышленность — Консервирование и переработка мяса, молока и овощей из дельты Амударьи.', 'Oziq-ovqat sanoati — Amudaryo deltasida yetishtirilgan mahsulotlarni konservalash hamda goʻsht, sut va sabzavotlarni qayta ishlash.', 'Azıq-awqat ónerkásibi — Ámiwdárya deltasında jetistirilgen ónimlerdi konservalaw hám et, sút, palız ónimlerin qayta islew.'),
            ('Кунградский содовый завод — Крупное предприятие по выпуску кальцинированной соды в Каракалпакстане (город Кунград), важное звено химической отрасли страны.', 'Qoʻngʻirot soda zavodi — Qoraqalpogʻistondagi (Qoʻngʻirot shahri) kalsinatsiyalangan soda ishlab chiqaruvchi yirik korxona; mamlakat kimyo sanoatining muhim boʻgʻini.', 'Qońırat soda zavodı — Qaraqalpaqstandaǵı (Qońırat qalası) kalcinaciyalanǵan soda shıǵarıwshı iri kárxana; eldiń ximiya ónerkásibiniń áhmiyetli bólegi.'),
            ('Устюртский газохимический комплекс — Один из крупнейших проектов республики: переработка газа, производство полиэтилена и полипропилена.', 'Ustyurt gaz-kimyo majmuasi — Respublikadagi yirik loyihalardan biri: gazni qayta ishlash, polietilen va polipropilen ishlab chiqarish.', 'Ustyurt gaz-ximiya kompleksi — Respublikadaǵı iri joybarlardan biri: gazdi qayta islew, polietilen hám polipropilen shıǵarıw.'),
            ('Народные ремёсла — Каракалпакская вышивка и ковроткачество — неотъемлемая часть культурного наследия региона.', 'Xalq hunarmandchiligi — Qoraqalpoq kashtachiligi va gilamdoʻzligi hududning madaniy merosining ajralmas qismi.', 'Xalıq ónermentshiligi — Qaraqalpaq keste tigiw hám gilem toqıw ónerleri aymaqtıń mádeniy miyrasınıń ajıralmas bólegi.'),
        ],
    ),

    _city(
        "UZ", ("Андижан", "Andijon", "Andijan"), 40.7821, 72.3442, 480000, False,
        (
            "Андижан — один из крупнейших городов Ферганской долины и центр Андижанской области. Здесь в 1483 году родился Захириддин Мухаммад Бабур, основатель империи Великих Моголов.",
            "Andijon — Fargʻona vodiysining yirik shaharlaridan biri va Andijon viloyati markazi. 1483-yilda bu yerda Buyuk Mugʻullar imperiyasi asoschisi Zahiriddin Muhammad Bobur tugʻilgan.",
            "Andijan — Ferǵana alabınıń iri qalalarınan biri hám Andijan wálayatı orayı. 1483-jılı bul jerde Ullı Moǵollar imperiyasınıń tiykarshısı Zahiriddin Muhammed Babur tuwılǵan.",
        ),
        [
            ("1483 — В Андижане рождается Бабур, будущий основатель империи Великих Моголов в Индии.",
             "1483 — Andijonda Hindistondagi Buyuk Mugʻullar imperiyasining bo‘lajak asoschisi Bobur tugʻildi.",
             "1483 — Andijanda Hindstandaǵı Ullı Moǵollar imperiyasınıń keleshektegi tiykarshısı Babur tuwıldı."),
            ("1902 — Сильное землетрясение разрушает значительную часть города.",
             "1902 — Kuchli zilzila shaharning katta qismini vayron qildi.",
             "1902 — Kúshli jer silkiniwi qalanıń úlken bólegin qırattı."),
        ],
        [
            ("Автозавод в Асаке — Крупнейшее автомобильное предприятие страны (UzAuto Motors) находится в Андижанской области.",
             "Asaka avtomobil zavodi — Mamlakatning eng yirik avtomobil korxonasi (UzAuto Motors) Andijon viloyatida joylashgan.",
             "Asaka avtomobil zavodı — Eldiń eń iri avtomobil kárxanası (UzAuto Motors) Andijan wálayatında jaylasqan."),
            ("Хлопок и текстиль — Андижанская область входит в число важных аграрных и текстильных районов Ферганской долины.",
             "Paxta va toʻqimachilik — Andijon viloyati Fargʻona vodiysining muhim agrar va toʻqimachilik hududlaridan biri.",
             "Paxta hám toqımashılıq — Andijan wálayatı Ferǵana alabınıń áhmiyetli agrar hám toqımashılıq aymaqların biri."),
        ],
    ),

    _city(
        "UZ", ("Наманган", "Namangan", "Namangan"), 41.0011, 71.6726, 630000, False,
        (
            "Наманган — крупнейший город Ферганской долины по числу жителей и центр Наманганской области. Он славится садами, ремёслами и гостеприимной кухней.",
            "Namangan — Fargʻona vodiysining aholi soni boʻyicha eng yirik shahri va Namangan viloyati markazi. Bogʻlari, hunarmandchiligi va mehmondoʻst oshxonasi bilan mashhur.",
            "Namangan — Ferǵana alabınıń xalıq sanı boyınsha eń iri qalası hám Namangan wálayatı orayı. Baǵları, ónermentshiligi hám miymandos asxanası menen belgili.",
        ),
        [
            ("1876 — После упразднения Кокандского ханства Наманган входит в состав Российской империи.",
             "1876 — Qoʻqon xonligi tugatilgach, Namangan Rossiya imperiyasi tarkibiga kirdi.",
             "1876 — Qoqan xanlıǵı joq etilgennen keyin Namangan Rossiya imperiyası quramına kirdi."),
            ("1991 — Наманганская область входит в независимый Узбекистан.",
             "1991 — Namangan viloyati mustaqil Oʻzbekiston tarkibida qoldi.",
             "1991 — Namangan wálayatı ǵárezsiz Ózbekstan quramında qaldı."),
        ],
        [
            ("Текстильная промышленность — Наманган — один из центров хлопковой и текстильной отрасли Ферганской долины.",
             "Toʻqimachilik sanoati — Namangan Fargʻona vodiysidagi paxta va toʻqimachilik sanoati markazlaridan biri.",
             "Toqımashılıq sanaatı — Namangan Ferǵana alabındaǵı paxta hám toqımashılıq tarawı orayların biri."),
            ("Садоводство — Область известна фруктами и сухофруктами, которые вывозят в другие страны.",
             "Bogʻdorchilik — Viloyat mevalari va quruq mevalari bilan mashhur, ular boshqa mamlakatlarga yuboriladi.",
             "Baǵdarshılıq — Wálayat miywe hám qurǵaq miywelerı menen belgili, olar basqa mámleketlerge jiberiledi."),
        ],
    ),

    _city(
        "UZ", ("Фергана", "Fargʻona", "Ferǵana"), 40.3864, 71.7864, 300000, False,
        (
            "Фергана — центр Ферганской области, зелёный город с широкими улицами и старыми русскими кварталами. Он стал центром нефтепереработки и химической промышленности долины.",
            "Fargʻona — Fargʻona viloyati markazi, keng koʻchalari va eski rus mahallalari bilan yam-yashil shahar. U vodiydagi neftni qayta ishlash va kimyo sanoati markaziga aylangan.",
            "Ferǵana — Ferǵana wálayatı orayı, keń kóshelerı hám eski rus mahallaları menen jasıl qala. Ol alaptaǵı neftti qayta islew hám ximiya sanaatı orayına aylanǵan.",
        ),
        [
            ("1876 — Основан как Новый Маргелан — русский город рядом со старым Маргиланом.",
             "1876 — Eski Margʻilon yonida rus shahri sifatida Yangi Margʻilon nomi bilan barpo etildi.",
             "1876 — Eski Marǵılan janında rus qalası retinde Jańa Marǵılan atı menen tiykarlandı."),
            ("1907 — Город переименован в Скобелев; с 1924 года носит название Фергана.",
             "1907 — Shahar Skobelev deb qayta nomlandi; 1924-yildan Fargʻona deb ataladi.",
             "1907 — Qala Skobelev dep qayta atalǵan; 1924-jıldan Ferǵana dep ataladı."),
        ],
        [
            ("Ферганский НПЗ — Один из старейших и крупнейших нефтеперерабатывающих заводов Узбекистана.",
             "Fargʻona neftni qayta ishlash zavodi — Oʻzbekistondagi eng qadimgi va yirik neft zavodlaridan biri.",
             "Ferǵana neftti qayta islew zavodı — Ózbekstandaǵı eń áyyemgi hám iri neft zavodlarınan biri."),
            ("Ферганаазот — Предприятие по выпуску азотных удобрений и химической продукции.",
             "Fargʻonaazot — Azotli oʻgʻitlar va kimyoviy mahsulotlar ishlab chiqaruvchi korxona.",
             "Ferǵanaazot — Azotlı tóginler hám ximiyalıq ónimler islep shıǵarıwshı kárxana."),
        ],
    ),

    _city(
        "UZ", ("Карши", "Qarshi", "Qarshı"), 38.8606, 65.7891, 290000, False,
        (
            "Карши — центр Кашкадарьинской области на юге Узбекистана, на краю одноимённой степи. Рядом лежат месторождения природного газа, дающие стране значительную часть топлива.",
            "Qarshi — Oʻzbekiston janubidagi Qashqadaryo viloyati markazi, bir xil nomli choʻl chekkasida joylashgan. Yaqinida mamlakat yoqilgʻisining muhim qismini beradigan tabiiy gaz konlari bor.",
            "Qarshı — Ózbekstan qublasındaǵı Qashqadárya wálayatı orayı, birdey atlı shól shetinde jaylasqan. Jaqınında eldiń janılǵısınıń áhmiyetli bólegin beretuǵın tábiyiy gaz kánleri bar.",
        ),
        [
            ("VI век — В этих местах существует крупный город Нахшаб (Насаф).",
             "VI asr — Bu hududlarda yirik Naxshab (Nasaf) shahri mavjud edi.",
             "VI ásir — Bul aymaqlarda iri Naxshab (Nasaf) qalası bar edi."),
            ("XIV век — По преданию, хан Кебек строит здесь дворец («карши»), от которого город получил своё название.",
             "XIV asr — Rivoyatga koʻra, Kebek xon bu yerda saroy («qarshi») qurdi, shahar nomini shundan olgan.",
             "XIV ásir — Rawayatqa kóre, Kebek xan bul jerde saray («qarshı») qurdı, qala atın sodan alǵan."),
        ],
        [
            ("Шуртанский газохимический комплекс — Перерабатывает природный газ в полиэтилен и другую химическую продукцию.",
             "Shurtan gaz-kimyo majmuasi — Tabiiy gazni polietilen va boshqa kimyoviy mahsulotlarga qayta ishlaydi.",
             "Shurtan gaz-ximiya kompleksi — Tábiyiy gazdı polietilen hám basqa ximiyalıq ónimlerge qayta isleydi."),
            ("Мубарекский газоперерабатывающий завод — Один из крупнейших газоперерабатывающих заводов Узбекистана.",
             "Muborak gazni qayta ishlash zavodi — Oʻzbekistondagi eng yirik gaz zavodlaridan biri.",
             "Mubarek gazdı qayta islew zavodı — Ózbekstandaǵı eń iri gaz zavodlarınan biri."),
        ],
    ),

    _city(
        "UZ", ("Термез", "Termiz", "Termez"), 37.2242, 67.2783, 175000, False,
        (
            "Термез — самый южный город Узбекистана, порт на Амударье на границе с Афганистаном. Его возраст отсчитывают более чем с двух тысяч лет; рядом сохранились буддийские монастыри Кара-Тепа и Фаяз-Тепа.",
            "Termiz — Oʻzbekistonning eng janubiy shahri, Amudaryodagi Afgʻoniston chegarasidagi port. Uning yoshi ikki ming yildan ortiq deb hisoblanadi; yaqinida Qoratepa va Fayoztepa buddaviy monastirlari saqlangan.",
            "Termez — Ózbekstannıń eń qublalıq qalası, Amudáryadaǵı Awǵanstan shegarasındaǵı port. Onıń jası eki mıń jıldan artıq dep esaplanadı; jaqınında Qaratepe hám Fayaztepe buddalıq monastırları saqlanǵan.",
        ),
        [
            ("329 до н. э. — Через эти земли проходит войско Александра Македонского.",
             "Miloddan avvalgi 329-yil — Bu yerlar orqali Iskandar Zulqarnayn qoʻshini oʻtdi.",
             "Miladdan aldınǵı 329-jıl — Bul jerler arqalı Aleksandr Makedonskiy áskeri ótti."),
            ("1220 — Монгольские войска разрушают древний Термез.",
             "1220 — Moʻgʻul qoʻshinlari qadimgi Termizni vayron qildi.",
             "1220 — Moǵol áskerleri áyyemgi Termezdi qırattı."),
            ("1982 — Открыт мост Дружбы через Амударью, соединивший Термез с Афганистаном.",
             "1982 — Termizni Afgʻoniston bilan bogʻlagan Amudaryo ustidagi Doʻstlik koʻprigi ochildi.",
             "1982 — Termezdi Awǵanstan menen baylanıstırǵan Amudárya ústindegi Dos'lıq kópirı ashıldı."),
        ],
        [
            ("Термезский речной порт — Единственный речной порт Узбекистана, принимает грузы на Амударье.",
             "Termiz daryo porti — Oʻzbekistondagi yagona daryo porti, Amudaryoda yuklarni qabul qiladi.",
             "Termez dárya portı — Ózbekstandaǵı jalǵız dárya portı, Amudáryada júklerdi qabıllaydı."),
            ("Погранично-торговые перевозки — Через Термез идут грузы в Афганистан и обратно.",
             "Chegara savdo tashuvlari — Termiz orqali Afgʻonistonga va undan yuklar tashiladi.",
             "Shegara sawda tasıwları — Termez arqalı Awǵanstanǵa hám onnan júkler tasıladı."),
        ],
    ),

    _city(
        "UZ", ("Джизак", "Jizzax", "Jizzax"), 40.1158, 67.8422, 180000, False,
        (
            "Джизак — центр Джизакской области на дороге между Ташкентом и Самаркандом. Город лежит у края Голодной степи (Мирзачуль), на пути древних караванов.",
            "Jizzax — Toshkent bilan Samarqand oʻrtasidagi yoʻlda joylashgan Jizzax viloyati markazi. Shahar Mirzachoʻl chekkasida, qadimiy karvon yoʻllari ustida joylashgan.",
            "Jizzax — Tashkent penen Samarqand ortasındaǵı jolda jaylasqan Jizzax wálayatı orayı. Qala Mirzashól shetinde, áyyemgi karvan jolları ústinde jaylasqan.",
        ),
        [
            ("1866 — Русские войска занимают Джизак; крепость на пути в Самарканд переходит под их контроль.",
             "1866 — Rus qoʻshinlari Jizzaxni egalladi; Samarqand yoʻlidagi qalʼa ularning nazoratiga oʻtdi.",
             "1866 — Rus áskerleri Jizzaxtı iyeledi; Samarqand jolındaǵı qala olardıń qadaǵalawına ótti."),
            ("1916 — В Джизаке начинается восстание против царской мобилизации в Туркестане.",
             "1916 — Jizzaxda Turkistonda podsho safarbarligiga qarshi qoʻzgʻolon boshlandi.",
             "1916 — Jizzaxta Turkistanda patsha jumıs kúshin shaqırıwına qarsı kóterilis baslandı."),
        ],
        [
            ("Особая индустриальная зона «Джизак» — Площадка для промышленных предприятий и иностранных инвестиций.",
             "«Jizzax» maxsus industrial zonasi — Sanoat korxonalari va xorijiy investitsiyalar uchun maydon.",
             "«Jizzax» arnawlı industriallıq zonası — Sanaat kárxanaları hám shet el investiciyaları ushın maydan."),
            ("Зерно и хлопок — Область входит в число важных аграрных районов, осваивающих Голодную степь.",
             "Don va paxta — Viloyat Mirzacho‘lni o‘zlashtirayotgan muhim agrar hududlardan biri.",
             "Biyday hám paxta — Wálayat Mirzashólsi ózlestirip atırǵan áhmiyetli agrar aymaqlardan biri."),
        ],
    ),

    _city(
        "UZ", ("Гулистан", "Guliston", "Gúlistan"), 40.4897, 68.7842, 80000, False,
        (
            "Гулистан — центр Сырдарьинской области, молодой город, выросший вместе с освоением Голодной степи. Название означает «цветущий сад».",
            "Guliston — Sirdaryo viloyati markazi, Mirzacho‘lni o‘zlashtirish bilan birga oʻsib chiqqan yosh shahar. Nomi «gullar bogʻi» degan maʼnoni anglatadi.",
            "Gúlistan — Sırdárya wálayatı orayı, Mirzashólsi ózlestiriw menen birge ósip shıqqan jas qala. Atı «gúller baǵı» degen mánisti ańlatadı.",
        ),
        [
            ("1961 — Посёлок Гулистан получает статус города.",
             "1961 — Guliston posyolkasi shahar maqomini oldi.",
             "1961 — Gúlistan posyolkası qala statusın aldı."),
            ("1963 — Гулистан становится центром образованной Сырдарьинской области.",
             "1963 — Guliston yangi tashkil etilgan Sirdaryo viloyatining markaziga aylandi.",
             "1963 — Gúlistan jańadan dúzilgen Sırdárya wálayatınıń orayına aylandı."),
        ],
        [
            ("Сырдарьинская ТЭС — Одна из крупнейших тепловых электростанций страны, расположена в Сырдарьинской области.",
             "Sirdaryo IES — Mamlakatning eng yirik issiqlik elektr stansiyalaridan biri, Sirdaryo viloyatida joylashgan.",
             "Sırdárya ISES — Eldiń eń iri jıllılıq elektr stanciyaların biri, Sırdárya wálayatında jaylasqan."),
            ("Хлопок и зерно — Основа сельского хозяйства региона.",
             "Paxta va don — Mintaqa qishloq xoʻjaligining asosi.",
             "Paxta hám biyday — Aymaq awıl xojalıǵınıń tiykarı."),
        ],
    ),

    _city(
        "UZ", ("Навои", "Navoiy", "Nawayı"), 40.0844, 65.3792, 140000, False,
        (
            "Навои — молодой город в центре пустыни Кызылкум, названный в честь поэта Алишера Навои. Он вырос рядом с горнодобывающими предприятиями, добывающими золото и уран.",
            "Navoiy — Qizilqum choʻli markazidagi yosh shahar, shoir Alisher Navoiy nomi bilan atalgan. U oltin va uran qazib oluvchi togʻ-kon korxonalari yonida oʻsib chiqqan.",
            "Nawayı — Qızılqum shólinıń ortasındaǵı jas qala, shayır Álisher Nawayı atı menen atalǵan. Ol altın hám uran qazıp alıwshı taw-kán kárxanaları janında ósip shıqqan.",
        ),
        [
            ("1958 — Основан город Навои; тогда же создаётся горно-металлургическое предприятие.",
             "1958 — Navoiy shahri barpo etildi; shu yili togʻ-kon metallurgiya korxonasi tashkil etildi.",
             "1958 — Nawayı qalası tiykarlandı; sol jılı taw-kán metallurgiya kárxanası dúzildi."),
            ("2008 — Создана Навоийская свободная индустриально-экономическая зона и логистический центр на базе аэропорта.",
             "2008 — Navoiy erkin industrial-iqtisodiy zonasi va aeroport asosidagi logistika markazi tashkil etildi.",
             "2008 — Nawayı erkin industriallıq-ekonomikalıq zonası hám aeroport tiykarındaǵı logistika orayı dúzildi."),
        ],
        [
            ("Навоийский горно-металлургический комбинат (НГМК) — Один из крупнейших производителей золота и урана в Центральной Азии.",
             "Navoiy togʻ-kon metallurgiya kombinati (NKMK) — Markaziy Osiyodagi oltin va uranning eng yirik ishlab chiqaruvchilaridan biri.",
             "Nawayı taw-kán metallurgiya kombinatı (NTMK) — Orayı Aziyadaǵı altın hám urannıń eń iri islep shıǵarıwshılarınan biri."),
            ("Navoiyazot — Крупное химическое предприятие по выпуску азотных удобрений.",
             "Navoiyazot — Azotli oʻgʻitlar ishlab chiqaruvchi yirik kimyo korxonasi.",
             "Nawayıazot — Azotlı tóginler islep shıǵarıwshı iri ximiya kárxanası."),
        ],
    ),

    _city(
        "UZ", ("Ургенч", "Urganch", "Úrgenish"), 41.5500, 60.6333, 150000, False,
        (
            "Ургенч — центр Хорезмской области, зелёный город на Амударье, ворота к Хиве. Старый Ургенч (Гургандж) был столицей Хорезмшахов; нынешний город основан позже на новом месте.",
            "Urganch — Xorazm viloyati markazi, Amudaryo boʻyidagi yam-yashil shahar, Xivaga kirish darvozasi. Qadimgi Urganch (Gurganj) Xorazmshohlar poytaxti boʻlgan; hozirgi shahar keyinroq yangi joyda barpo etilgan.",
            "Úrgenish — Xorezm wálayatı orayı, Amudárya boyındaǵı jasıl qala, Xiywaǵa kirisiw dárwazası. Eski Úrgenish (Gurganj) Xorezmshahlar paytaxtı bolǵan; házirgi qala keyinirek jańa jerde tiykarlanǵan.",
        ),
        [
            ("1221 — Монгольские войска разрушают столицу Хорезмшахов Гургандж.",
             "1221 — Moʻgʻul qoʻshinlari Xorazmshohlar poytaxti Gurganjni vayron qildi.",
             "1221 — Moǵol áskerleri Xorezmshahlar paytaxtı Gurganjdı qırattı."),
            ("XVII век — После изменения русла Амударьи жители старого города основывают Новый Ургенч.",
             "XVII asr — Amudaryo oʻzani oʻzgargach, eski shahar aholisi Yangi Urganchni barpo etdi.",
             "XVII ásir — Amudárya aǵısı ózgergennen keyin, eski qala xalqı Jańa Úrgenishti tiykarladı."),
        ],
        [
            ("Хорезмский шёлк и хлопок — Традиционные отрасли региона: шелководство и хлопководство.",
             "Xorazm ipagi va paxtasi — Mintaqaning anʼanaviy tarmoqlari: ipakchilik va paxtachilik.",
             "Xorezm jipegi hám paxtası — Aymaqtıń dástúriy tarawları: jipekshilik hám paxtashılıq."),
            ("Аэропорт Ургенч — Главные воздушные ворота Хорезма и Хивы.",
             "Urganch aeroporti — Xorazm va Xivaning asosiy havo darvozasi.",
             "Úrgenish aeroportı — Xorezm hám Xiywanıń tiykarǵı hawa dárwazası."),
        ],
    ),
]
