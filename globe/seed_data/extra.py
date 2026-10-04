"""Ещё страны и города: Польша, Нидерланды, Греция, Португалия, Австрия, Чехия, Грузия,
Армения, Вьетнам, Малайзия, Перу, Колумбия, Кения, Марокко, а также новые города в уже
существующих странах (Лос-Анджелес, Киото, Осака, Казань, Шанхай, Мумбаи, Мюнхен, Милан,
Эдинбург, Анкара, Хива, Алматы, Мельбурн).

Формат результата тот же, что в europe.py / asia.py: тексты — кортежи (ru, uz, qr).
Для удобства события и компании здесь записаны тройками (ru, uz, qr) и собираются функцией _city.
"""

# code: (name_ru, name_uz, name_qr, широта центра, долгота центра)
COUNTRIES = {
    "PL": ("Польша", "Polsha", "Polsha", 52.0, 19.4),
    "NL": ("Нидерланды", "Niderlandiya", "Niderlandiya", 52.2, 5.3),
    "GR": ("Греция", "Gretsiya", "Greciya", 39.0, 22.0),
    "PT": ("Португалия", "Portugaliya", "Portugaliya", 39.6, -8.0),
    "AT": ("Австрия", "Avstriya", "Avstriya", 47.6, 14.1),
    "CZ": ("Чехия", "Chexiya", "Chexiya", 49.8, 15.5),
    "GE": ("Грузия", "Gruziya", "Gruziya", 42.2, 43.5),
    "AM": ("Армения", "Armaniston", "Armeniya", 40.2, 44.9),
    "VN": ("Вьетнам", "Vyetnam", "Vetnam", 16.0, 107.8),
    "MY": ("Малайзия", "Malayziya", "Malayziya", 4.2, 102.0),
    "PE": ("Перу", "Peru", "Peru", -9.2, -75.0),
    "CO": ("Колумбия", "Kolumbiya", "Kolumbiya", 4.6, -74.3),
    "KE": ("Кения", "Keniya", "Keniya", 0.2, 37.9),
    "MA": ("Марокко", "Marokash", "Marokko", 31.8, -7.1),
}


def _city(country, name, lat, lng, population, capital, desc, history, industry):
    """history и industry — списки троек (ru, uz, qr) -> три списка по языкам."""
    return {
        "country": country,
        "name": name,
        "lat": lat,
        "lng": lng,
        "population": population,
        "capital": capital,
        "desc": desc,
        "history": tuple(list(lang) for lang in zip(*history)),
        "industry": tuple(list(lang) for lang in zip(*industry)),
    }


CITIES = [
    # ---------------------------------------------------------------- Польша
    _city(
        "PL", ("Варшава", "Varshava", "Varshava"), 52.2297, 21.0122, 1860000, True,
        (
            "Варшава — столица Польши на реке Висле, город, который после почти полного разрушения во Второй мировой войне был заново отстроен. Сегодня это крупнейший деловой и научный центр страны.",
            "Varshava — Vistula daryosi boʻyidagi Polsha poytaxti; Ikkinchi jahon urushida deyarli butunlay vayron boʻlgach, qaytadan qurilgan shahar. Bugun u mamlakatning eng yirik biznes va ilm markazi.",
            "Varshava — Vistula dáryası boyındaǵı Polsha paytaxtı; Ekinshi jáhán urısında derlik tolıq qıraǵannan keyin qaytadan qurılǵan qala. Búgin ol eldiń eń iri biznes hám ilim orayı.",
        ),
        [
            (
                "1596 — Король Сигизмунд III Ваза переносит столицу Польши из Кракова в Варшаву.",
                "1596 — Qirol Sigizmund III Vaza Polsha poytaxtini Krakovdan Varshavaga koʻchirdi.",
                "1596 — Korol Sigizmund III Vaza Polsha paytaxtın Krakovtan Varshavaǵa kóshirdi.",
            ),
            (
                "1944 — Варшавское восстание: 63 дня борьбы против оккупантов; после него город был почти полностью разрушен.",
                "1944 — Varshava qoʻzgʻoloni: bosqinchilarga qarshi 63 kun davom etgan kurash; undan soʻng shahar deyarli butunlay vayron qilindi.",
                "1944 — Varshava kóterilisi: basqınshılarǵa qarsı 63 kún dawam etken gúres; sonnan keyin qala derlik tolıq qıraldı.",
            ),
            (
                "1980 — Исторический центр, восстановленный после войны, включён в список Всемирного наследия ЮНЕСКО.",
                "1980 — Urushdan keyin tiklangan tarixiy markaz YuNESKO Jahon merosi roʻyxatiga kiritildi.",
                "1980 — Urıstan keyin tiklengen tariyxıy orayı YuNESKO Dúnya mereesi dizimine kiritildi.",
            ),
        ],
        [
            (
                "Варшавская фондовая биржа — Крупнейшая биржа Центральной и Восточной Европы по числу компаний.",
                "Varshava fond birjasi — Markaziy va Sharqiy Yevropadagi kompaniyalar soni boʻyicha eng yirik birja.",
                "Varshava fond birjası — Orayı hám Shıǵıs Evropadaǵı kompaniyalar sanı boyınsha eń iri birja.",
            ),
            (
                "PZU — Крупнейшая страховая группа Польши со штаб-квартирой в Варшаве.",
                "PZU — Bosh qarorgohi Varshavada joylashgan Polshaning eng yirik sugʻurta guruhi.",
                "PZU — Bas shtab-páteri Varshavada jaylasqan Polshanıń eń iri sugʻurta toparı.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Нидерланды
    _city(
        "NL", ("Амстердам", "Amsterdam", "Amsterdam"), 52.3676, 4.9041, 920000, True,
        (
            "Амстердам — столица Нидерландов, город концентрических каналов, велосипедов и узких кирпичных домов. Эпоха расцвета XVII века сделала его одним из богатейших торговых центров мира.",
            "Amsterdam — Niderlandiya poytaxti, konsentrik kanallar, velosipedlar va tor gʻishtin uylar shahri. XVII asrdagi gullab-yashnash davri uni dunyoning eng boy savdo markazlaridan biriga aylantirdi.",
            "Amsterdam — Niderlandiya paytaxtı, konsentrik kanallar, velosipedler hám tar g'ısh úyler qalası. XVII ásirdegi gúllep-jaynaw dáwiri onı dúnyanıń eń bay sawda orayların biri etti.",
        ),
        [
            (
                "1275 — Граф Флорис V освобождает жителей посёлка у плотины на реке Амстел от дорожных пошлин: так появляется Амстердам.",
                "1275 — Graf Florits V Amstel daryosidagi toʻgʻon yonidagi posyolka aholisini yoʻl toʻlovlaridan ozod qildi: Amsterdam shunday paydo boʻldi.",
                "1275 — Graf Floris V Amstel dáryasındaǵı bóget janındaǵı posyolka xalqın jol salıqlarınan azat etti: Amsterdam usılay payda boldı.",
            ),
            (
                "1602 — Основана Голландская Ост-Индская компания (VOC) — первая в мире компания, выпустившая публично торгуемые акции.",
                "1602 — Gollandiya Ost-Hindiston kompaniyasi (VOC) tashkil etildi — dunyoda ommaviy savdo qilinadigan aksiyalarni chiqargan birinchi kompaniya.",
                "1602 — Gollandiya Ost-Indiya kompaniyası (VOC) dúzildi — dúnyada ashıq sawdalanatuǵın akciyalardı shıǵarǵan birinshi kompaniya.",
            ),
            (
                "1613 — Начинается строительство кольца каналов, позднее внесённого в список Всемирного наследия ЮНЕСКО.",
                "1613 — Keyinchalik YuNESKO Jahon merosi roʻyxatiga kiritilgan kanallar halqasining qurilishi boshlandi.",
                "1613 — Keyin YuNESKO Dúnya mereesi dizimine kiritilgen kanallar saqıynasınıń qurılısı baslandı.",
            ),
        ],
        [
            (
                "Heineken — Одна из крупнейших пивоваренных компаний мира, основана в Амстердаме в 1864 году.",
                "Heineken — Dunyoning eng yirik pivo ishlab chiqaruvchi kompaniyalaridan biri, 1864-yilda Amsterdamda asos solingan.",
                "Heineken — Dúnyanıń eń iri piwo islep shıǵarıwshı kompaniyalarınan biri, 1864-jılı Amsterdamda tiykarlanǵan.",
            ),
            (
                "ING — Международная банковская группа со штаб-квартирой в Амстердаме.",
                "ING — Bosh qarorgohi Amsterdamda joylashgan xalqaro bank guruhi.",
                "ING — Bas shtab-páteri Amsterdamda jaylasqan xalıqaralıq bank toparı.",
            ),
        ],
    ),
    # ---------------------------------------------------------------- Греция
    _city(
        "GR", ("Афины", "Afina", "Afina"), 37.9838, 23.7275, 640000, True,
        (
            "Афины — столица Греции и один из старейших городов мира, колыбель демократии, философии и театра. Над городом возвышается Акрополь с Парфеноном.",
            "Afina — Gretsiya poytaxti va dunyodagi eng qadimiy shaharlardan biri, demokratiya, falsafa va teatr beshigi. Shahar ustida Parfenonli Akropol koʻtarilib turadi.",
            "Afina — Greciya paytaxtı hám dúnyadaǵı eń áyyemgi qalalardan biri, demokratiya, filosofiya hám teatr besigi. Qala ústinde Parfenonlı Akropol kóterilip turadı.",
        ),
        [
            (
                "508 до н. э. — Клисфен проводит реформы, закладывающие основы афинской демократии.",
                "Miloddan avvalgi 508-yil — Klisfen islohotlar oʻtkazib, Afina demokratiyasi poydevorini qoʻydi.",
                "Miladdan aldınǵı 508-jıl — Klisfen reformalar ótkerip, Afina demokratiyasınıń tiykarın saldı.",
            ),
            (
                "447–432 до н. э. — При Перикле на Акрополе строится Парфенон.",
                "Miloddan avvalgi 447–432-yillar — Perikl davrida Akropolda Parfenon qurildi.",
                "Miladdan aldınǵı 447–432-jıllar — Perikl dáwirinde Akropolda Parfenon qurıldı.",
            ),
            (
                "1834 — Афины становятся столицей новой независимой Греции.",
                "1834 — Afina yangi mustaqil Gretsiyaning poytaxtiga aylandi.",
                "1834 — Afina jańa ǵárezsiz Greciyanıń paytaxtına aylandı.",
            ),
            (
                "1896 — В Афинах проходят первые современные Олимпийские игры.",
                "1896 — Afinada birinchi zamonaviy Olimpiya oʻyinlari oʻtkazildi.",
                "1896 — Afinada birinshi zamanagóy Olimpiya oyınları ótkerildi.",
            ),
        ],
        [
            (
                "Порт Пирей — Один из крупнейших портов Средиземноморья, главные морские ворота Греции.",
                "Pireya porti — Oʻrta dengizdagi eng yirik portlardan biri, Gretsiyaning asosiy dengiz darvozasi.",
                "Pireya portı — Orta teńizdegi eń iri portlardan biri, Greciyanıń tiykarǵı teńiz dárwazası.",
            ),
            (
                "Национальный банк Греции — Старейший крупный банк страны, основан в 1841 году.",
                "Gretsiya Milliy banki — Mamlakatning eng qadimgi yirik banki, 1841-yilda tashkil etilgan.",
                "Greciya Milliy banki — Eldiń eń áyyemgi iri banki, 1841-jılı dúzilgen.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Португалия
    _city(
        "PT", ("Лиссабон", "Lissabon", "Lissabon"), 38.7223, -9.1393, 545000, True,
        (
            "Лиссабон — столица Португалии на холмах у устья реки Тежу, город жёлтых трамваев и мореплавателей. Отсюда в эпоху Великих географических открытий уходили корабли к берегам Африки, Индии и Бразилии.",
            "Lissabon — Portugaliya poytaxti, Tezu daryosi quyilishidagi tepaliklarda joylashgan, sariq tramvaylar va dengizchilar shahri. Buyuk geografik kashfiyotlar davrida bu yerdan kemalar Afrika, Hindiston va Braziliya sohillariga suzib ketgan.",
            "Lissabon — Portugaliya paytaxtı, Tezu dáryasınıń quyılısındaǵı tóbeliklerde jaylasqan, sarı tramvaylar hám teńizshiler qalası. Ullı geografiyalıq ashılıwlar dáwirinde bul jerden kemeler Afrika, Hindstan hám Braziliya jaǵalawlarına suzip ketken.",
        ),
        [
            (
                "1147 — Афонсу Энрикеш отвоёвывает Лиссабон у мавров.",
                "1147 — Afonsu Enrikesh Lissabonni mavrlardan qaytarib oldi.",
                "1147 — Afonsu Enrikesh Lissabondı mavrlardan qaytarıp aldı.",
            ),
            (
                "1 ноября 1755 — Сильнейшее землетрясение с цунами и пожарами разрушает большую часть города.",
                "1755-yil 1-noyabr — Tsunami va yongʻinlar bilan kechgan kuchli zilzila shaharning katta qismini vayron qildi.",
                "1755-jıl 1-noyabr — Cunami hám órtler menen birge bolǵan kúshli jer silkiniwi qalanıń úlken bólegin qırattı.",
            ),
            (
                "25 апреля 1974 — Революция гвоздик свергает диктатуру и открывает путь к демократии.",
                "1974-yil 25-aprel — Chinnigullar inqilobi diktaturani agʻdardi va demokratiyaga yoʻl ochdi.",
                "1974-jıl 25-aprel — Qalampır gúller revolyuciyası diktaturanı awdardı hám demokratiyaǵa jol ashtı.",
            ),
        ],
        [
            (
                "Galp — Крупнейшая энергетическая компания Португалии, штаб-квартира в Лиссабоне.",
                "Galp — Portugaliyaning eng yirik energetika kompaniyasi, bosh qarorgohi Lissabonda.",
                "Galp — Portugaliyanıń eń iri energetika kompaniyası, bas shtab-páteri Lissabonda.",
            ),
            (
                "EDP — Энергетический концерн, один из мировых лидеров по ветровой энергетике.",
                "EDP — Shamol energetikasi boʻyicha jahon yetakchilaridan biri boʻlgan energetika konserni.",
                "EDP — Samal energetikası boyınsha dúnyalıq jetekshilerden biri bolǵan energetika konserni.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Австрия
    _city(
        "AT", ("Вена", "Vena", "Vena"), 48.2082, 16.3738, 1980000, True,
        (
            "Вена — столица Австрии, бывший центр империи Габсбургов и мировая столица классической музыки. Здесь жили и работали Моцарт, Бетховен, Шуберт и Штраус.",
            "Vena — Avstriya poytaxti, Gabsburglar imperiyasining sobiq markazi va klassik musiqaning jahon poytaxti. Bu yerda Motsart, Betxoven, Shubert va Shtraus yashab ijod qilgan.",
            "Vena — Avstriya paytaxtı, Gabsburglar imperiyasınıń burınǵı orayı hám klassikalıq muzıkanıń dúnyalıq paytaxtı. Bul jerde Mocart, Betxoven, Shubert hám Shtraus jasap, dóretiwshilik etken.",
        ),
        [
            (
                "1683 — Битва за Вену: войско коалиции разбивает османскую армию, осаждавшую город.",
                "1683 — Vena uchun jang: koalitsiya qoʻshini shaharni qamal qilgan Usmonlilar armiyasini magʻlub etdi.",
                "1683 — Vena ushın gúres: koaliciya áskeri qalanı qorshaǵan Osmanlı armiyasın jeńdi.",
            ),
            (
                "1814–1815 — Венский конгресс устанавливает новый порядок в Европе после наполеоновских войн.",
                "1814–1815 — Vena kongressi Napoleon urushlaridan keyin Yevropada yangi tartib oʻrnatdi.",
                "1814–1815 — Vena kongressi Napoleon urısınan keyin Evropada jańa tártip ornattı.",
            ),
            (
                "1955 — В Вене подписан Государственный договор, восстановивший независимость Австрии.",
                "1955 — Venada Avstriya mustaqilligini tiklagan Davlat shartnomasi imzolandi.",
                "1955 — Venada Avstriya ǵárezsizligin tikleǵen Mámleket shártnaması qol qoyıldı.",
            ),
        ],
        [
            (
                "OMV — Австрийская нефтегазовая и химическая компания со штаб-квартирой в Вене.",
                "OMV — Bosh qarorgohi Venada joylashgan Avstriya neft-gaz va kimyo kompaniyasi.",
                "OMV — Bas shtab-páteri Venada jaylasqan Avstriya neft-gaz hám ximiya kompaniyası.",
            ),
            (
                "Erste Group — Один из крупнейших банков Центральной и Восточной Европы, основан в Вене в 1819 году.",
                "Erste Group — Markaziy va Sharqiy Yevropaning eng yirik banklaridan biri, 1819-yilda Venada tashkil etilgan.",
                "Erste Group — Orayı hám Shıǵıs Evropanıń eń iri banklerinen biri, 1819-jılı Venada dúzilgen.",
            ),
        ],
    ),
    # ----------------------------------------------------------------- Чехия
    _city(
        "CZ", ("Прага", "Praga", "Praga"), 50.0755, 14.4378, 1300000, True,
        (
            "Прага — столица Чехии, «город ста шпилей» на реке Влтаве. Исторический центр почти не пострадал в войнах, поэтому готика, ренессанс и барокко сохранились здесь рядом.",
            "Praga — Chexiya poytaxti, Vltava daryosi boʻyidagi «yuz shpilli shahar». Tarixiy markaz urushlarda deyarli shikastlanmagan, shu sabab gotika, uygʻonish davri va barokko bu yerda yonma-yon saqlangan.",
            "Praga — Chexiya paytaxtı, Vltava dáryası boyındaǵı «júz shpilli qala». Tariyxıy orayı urıslarda derlik zıyan kórmegen, sol sebepli gotika, oyanıw dáwiri hám barokko bul jerde janma-jan saqlanıp qalǵan.",
        ),
        [
            (
                "IX век — Основан Пражский Град, с тех пор резиденция чешских правителей.",
                "IX asr — Praga qalʼasi barpo etildi; shundan beri Chexiya hukmdorlarining qarorgohi.",
                "IX ásir — Praga qalası tiykarlandı; sodan berli Chexiya húkimdarlarınıń rezidenciyası.",
            ),
            (
                "1348 — Карл IV основывает Карлов университет — старейший университет Центральной Европы.",
                "1348 — Karl IV Karl universitetiga asos soldi — Markaziy Yevropadagi eng qadimgi universitet.",
                "1348 — Karl IV Karl universitetine tiykar saldı — Orayı Evropadaǵı eń áyyemgi universitet.",
            ),
            (
                "1618 — Пражская дефенестрация: выброс наместников из окна становится поводом к Тридцатилетней войне.",
                "1618 — Praga defenestratsiyasi: noiblarning derazadan tashlanishi Oltmish yillik urushga sabab boʻldi.",
                "1618 — Praga defenestraciyası: orınbasarlardıń aynadan taslanıwı Otız jıllıq urısqa sebep boldı.",
            ),
            (
                "17 ноября 1989 — Начинается Бархатная революция, которая завершает власть коммунистов.",
                "1989-yil 17-noyabr — Baxmal inqilob boshlandi va kommunistlar hokimiyatiga chek qoʻydi.",
                "1989-jıl 17-noyabr — Barqıt revolyuciyası baslandı hám kommunistler húkimetine shek qoydı.",
            ),
        ],
        [
            (
                "ČEZ — Крупнейшая энергетическая компания Чехии со штаб-квартирой в Праге.",
                "ČEZ — Chexiyaning eng yirik energetika kompaniyasi, bosh qarorgohi Pragada.",
                "ČEZ — Chexiyanıń eń iri energetika kompaniyası, bas shtab-páteri Pragada.",
            ),
            (
                "Киностудия «Баррандов» — Одна из старейших и крупнейших студий Европы, открыта в 1931 году.",
                "«Barrandov» kinostudiyasi — Yevropadagi eng qadimgi va yirik studiyalardan biri, 1931-yilda ochilgan.",
                "«Barrandov» kinostudiyası — Evropadaǵı eń áyyemgi hám iri studiyalardan biri, 1931-jılı ashılǵan.",
            ),
        ],
    ),
    # ---------------------------------------------------------------- Грузия
    _city(
        "GE", ("Тбилиси", "Tbilisi", "Tbilisi"), 41.7151, 44.8271, 1200000, True,
        (
            "Тбилиси — столица Грузии в долине реки Куры, известная серными банями, резными деревянными балконами и тысячелетними храмами. Город стоит на перекрёстке путей между Европой и Азией.",
            "Tbilisi — Gruziya poytaxti, Kura daryosi vodiysida joylashgan; oltingugurtli hammomlari, naqshinkor yogʻoch balkonlari va ming yillik ibodatxonalari bilan mashhur. Shahar Yevropa va Osiyo oʻrtasidagi yoʻllar chorrahasida joylashgan.",
            "Tbilisi — Gruziya paytaxtı, Kura dáryası jazıǵındaǵı, kükirtli hammamları, oyma aǵash balkonları hám mıń jıllıq ibadatxanaları menen belgili qala. Qala Evropa hám Aziya ortasındaǵı jollar kesilisinde jaylasqan.",
        ),
        [
            (
                "V век — По преданию, царь Вахтанг Горгасали основывает город на месте горячих источников.",
                "V asr — Rivoyatga koʻra, podshoh Vaxtang Gorgasali shaharni issiq buloqlar oʻrnida barpo etgan.",
                "V ásir — Rawayatqa kóre, patsha Vaxtang Gorgasali qalanı ıssı bulaqlar ornında tiykarlaǵan.",
            ),
            (
                "1122 — Давид IV Строитель освобождает Тбилиси от сельджуков и делает его столицей объединённой Грузии.",
                "1122 — Davit IV Quruvchi Tbilisini saljuqlardan ozod qilib, uni birlashgan Gruziya poytaxtiga aylantirdi.",
                "1122 — Davit IV Qurılısshı Tbilisini seljuklardan azat etip, onı birlesken Gruziyanıń paytaxtına aylandırdı.",
            ),
            (
                "1991 — Грузия провозглашает независимость, Тбилиси остаётся её столицей.",
                "1991 — Gruziya mustaqilligini eʼlon qildi, Tbilisi uning poytaxti boʻlib qoldi.",
                "1991 — Gruziya ǵárezsizligin járiyaladı, Tbilisi onıń paytaxtı bolıp qaldı.",
            ),
        ],
        [
            (
                "TBC Bank — Один из крупнейших банков Грузии, основан в Тбилиси в 1992 году.",
                "TBC Bank — Gruziyaning eng yirik banklaridan biri, 1992-yilda Tbilisida tashkil etilgan.",
                "TBC Bank — Gruziyanıń eń iri banklerinen biri, 1992-jılı Tbilisida dúzilgen.",
            ),
            (
                "Грузинская железная дорога — Национальный железнодорожный оператор; первая линия Поти — Тбилиси открыта в 1872 году.",
                "Gruziya temir yoʻli — Milliy temir yoʻl operatori; birinchi Poti — Tbilisi liniyasi 1872-yilda ochilgan.",
                "Gruziya temir jolı — Milliy temir jol operatorı; birinshi Poti — Tbilisi liniyası 1872-jılı ashılǵan.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Армения
    _city(
        "AM", ("Ереван", "Yerevan", "Yerevan"), 40.1792, 44.4991, 1100000, True,
        (
            "Ереван — столица Армении, один из старейших непрерывно населённых городов мира; его называют «розовым городом» за здания из розового туфа. Вдали виден библейский Арарат.",
            "Yerevan — Armaniston poytaxti, dunyodagi uzluksiz yashab kelayotgan eng qadimgi shaharlardan biri; pushti tuf binolari uchun «pushti shahar» deb ataladi. Uzoqda Bibliyadagi Ararat togʻi koʻrinadi.",
            "Yerevan — Armeniya paytaxtı, dúnyada úzliksiz jasap kiyatırǵan eń áyyemgi qalalardan biri; pushti tuf imaratları ushın «pushti qala» dep ataladı. Alısta Bibliyadaǵı Ararat taw kórinip turadı.",
        ),
        [
            (
                "782 до н. э. — Царь Аргишти I основывает крепость Эребуни — так принято отсчитывать возраст Еревана.",
                "Miloddan avvalgi 782-yil — Podshoh Argishti I Erebuni qalʼasiga asos soldi — Yerevan yoshi shundan hisoblanadi.",
                "Miladdan aldınǵı 782-jıl — Patsha Argishti I Erebuni qalasına tiykar saldı — Yerevan jası sodan esaplanadı.",
            ),
            (
                "1918 — Ереван становится столицей Первой Республики Армения.",
                "1918 — Yerevan Birinchi Armaniston Respublikasining poytaxtiga aylandi.",
                "1918 — Yerevan Birinshi Armeniya Respublikasınıń paytaxtına aylandı.",
            ),
            (
                "1924 — Архитектор Александр Таманян создаёт генеральный план, по которому застраивается современный центр.",
                "1924 — Arxitektor Aleksandr Tamanyan hozirgi markaz qurilgan bosh rejani yaratdi.",
                "1924 — Arxitektor Aleksandr Tamanyan házirgi oray qurılǵan bas jobanı jarattı.",
            ),
            (
                "1991 — Армения провозглашает независимость.",
                "1991 — Armaniston mustaqilligini eʼlon qildi.",
                "1991 — Armeniya ǵárezsizligin járiyaladı.",
            ),
        ],
        [
            (
                "Коньячный завод «Арарат» — Ереванский коньячный комбинат, основан в 1887 году; продукция известна по всему миру.",
                "«Ararat» konyak zavodi — Yerevan konyak kombinati, 1887-yilda tashkil etilgan; mahsuloti butun dunyoga mashhur.",
                "«Ararat» konyak zavodı — Yerevan konyak kombinatı, 1887-jılı dúzilgen; ónimi pútkil dúnyaǵa belgili.",
            ),
            (
                "Аэропорт «Звартноц» — Главные воздушные ворота Армении.",
                "«Zvartnots» aeroporti — Armanistonning asosiy havo darvozasi.",
                "«Zvartnots» aeroportı — Armeniyanıń tiykarǵı hawa dárwazası.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Вьетнам
    _city(
        "VN", ("Ханой", "Xanoy", "Hanoy"), 21.0285, 105.8542, 8400000, True,
        (
            "Ханой — столица Вьетнама, город озёр, французских бульваров и храмов на реке Хонгха. Это политический и культурный центр страны с тысячелетней историей.",
            "Xanoy — Vyetnam poytaxti, Xongxa daryosi boʻyidagi koʻllar, fransuz xiyobonlari va ibodatxonalar shahri. Bu mamlakatning ming yillik tarixga ega siyosiy va madaniy markazi.",
            "Hanoy — Vetnam paytaxtı, Xongxa dáryası boyındaǵı kóller, francuz bulvarları hám ibadatxanalar qalası. Ol eldiń mıń jıllıq tariyxqa iye siyasiy hám mádeniy orayı.",
        ),
        [
            (
                "1010 — Император Ли Тхай То переносит столицу в Тханглонг — так начинается история Ханоя.",
                "1010 — Imperator Li Tay To poytaxtni Tanglonga koʻchirdi — Xanoy tarixi shundan boshlandi.",
                "1010 — Imperator Li Tay To paytaxtın Tanglongqa kóshirdi — Hanoy tariyxı sodan baslandı.",
            ),
            (
                "1076 — Основан Храм литературы с Императорской академией — первый университет Вьетнама.",
                "1076 — Adabiyot ibodatxonasi va Imperator akademiyasi — Vyetnamning birinchi universiteti — tashkil etildi.",
                "1076 — Ádebiyat ibadatxanası hám Imperator akademiyası — Vetnamnıń birinshi universiteti — dúzildi.",
            ),
            (
                "2 сентября 1945 — На площади Бадинь Хо Ши Мин провозглашает независимость Вьетнама.",
                "1945-yil 2-sentabr — Badin maydonida Xo Shi Min Vyetnam mustaqilligini eʼlon qildi.",
                "1945-jıl 2-sentyabr — Badin maydanında Xo Shi Min Vetnam ǵárezsizligin járiyaladı.",
            ),
            (
                "1976 — Ханой становится столицей объединённого Вьетнама.",
                "1976 — Xanoy birlashgan Vyetnamning poytaxtiga aylandi.",
                "1976 — Hanoy birlesken Vetnamnıń paytaxtına aylandı.",
            ),
        ],
        [
            (
                "Viettel — Крупнейший вьетнамский телекоммуникационный оператор, штаб-квартира в Ханое.",
                "Viettel — Vyetnamning eng yirik telekommunikatsiya operatori, bosh qarorgohi Xanoyda.",
                "Viettel — Vetnamnıń eń iri telekommunikaciya operatorı, bas shtab-páteri Hanoyda.",
            ),
            (
                "Vietnam Airlines — Национальная авиакомпания Вьетнама, базируется в Ханое.",
                "Vietnam Airlines — Vyetnamning milliy aviakompaniyasi, Xanoyda joylashgan.",
                "Vietnam Airlines — Vetnamnıń milliy aviakompaniyası, Hanoyda jaylasqan.",
            ),
        ],
    ),
    # -------------------------------------------------------------- Малайзия
    _city(
        "MY", ("Куала-Лумпур", "Kuala-Lumpur", "Kuala-Lumpur"), 3.1390, 101.6869, 1800000, True,
        (
            "Куала-Лумпур — столица Малайзии, город небоскрёбов, мечетей и уличной еды на слиянии рек Кланг и Гомбак. Башни Петронас долго были самыми высокими зданиями мира.",
            "Kuala-Lumpur — Malayziya poytaxti, Klang va Gombak daryolari qoʻshilgan joydagi osmonoʻpar binolar, masjidlar va koʻcha taomlari shahri. Petronas minoralari uzoq vaqt dunyodagi eng baland binolar edi.",
            "Kuala-Lumpur — Malayziya paytaxtı, Klang hám Gombak dáryaları qosılatuǵın jerdegi kókke boylaǵan imaratlar, meshitler hám kósh awqatları qalası. Petronas minaraları uzaq waqıt dúnyadaǵı eń biyik imaratlar edi.",
        ),
        [
            (
                "1857 — Старатели, добывавшие олово, основывают посёлок на слиянии двух рек.",
                "1857 — Qalay qazuvchilar ikki daryo qoʻshiladigan joyda posyolka barpo etdilar.",
                "1857 — Qalay qazıwshılar eki dárya qosılatuǵın jerde posyolka tiykarladı.",
            ),
            (
                "31 августа 1957 — На стадионе Мердека провозглашена независимость Малайи.",
                "1957-yil 31-avgust — Merdeka stadionida Malaya mustaqilligi eʼlon qilindi.",
                "1957-jıl 31-avgust — Merdeka stadionında Malaya ǵárezsizligi járiyalandı.",
            ),
            (
                "1998 — Завершено строительство башен Петронас высотой 452 метра.",
                "1998 — Balandligi 452 metr boʻlgan Petronas minoralarining qurilishi yakunlandi.",
                "1998 — Biyikligi 452 metr bolǵan Petronas minaralarınıń qurılısı juwmaqlandı.",
            ),
        ],
        [
            (
                "Petronas — Государственная нефтегазовая компания Малайзии, основана в 1974 году.",
                "Petronas — Malayziyaning davlat neft-gaz kompaniyasi, 1974-yilda tashkil etilgan.",
                "Petronas — Malayziyanıń mámleketlik neft-gaz kompaniyası, 1974-jılı dúzilgen.",
            ),
            (
                "Maybank — Крупнейший банк Малайзии, штаб-квартира в Куала-Лумпуре.",
                "Maybank — Malayziyaning eng yirik banki, bosh qarorgohi Kuala-Lumpurda.",
                "Maybank — Malayziyanıń eń iri banki, bas shtab-páteri Kuala-Lumpurda.",
            ),
        ],
    ),
    # ------------------------------------------------------------------ Перу
    _city(
        "PE", ("Лима", "Lima", "Lima"), -12.0464, -77.0428, 10000000, True,
        (
            "Лима — столица Перу на берегу Тихого океана, крупнейший город страны. Основанная конкистадорами как «Город королей», она стала главным центром испанской власти в Южной Америке.",
            "Lima — Tinch okean sohilidagi Peru poytaxti, mamlakatning eng yirik shahri. Konkistadorlar «Qirollar shahri» sifatida asos solgan Lima Janubiy Amerikadagi ispan hokimiyatining asosiy markaziga aylandi.",
            "Lima — Tınısh okean jaǵasındaǵı Peru paytaxtı, eldiń eń iri qalası. Konkistadorlar «Korollar qalası» retinde tiykarlaǵan Lima Qubla Amerikadaǵı ispan húkimetiniń tiykarǵı orayına aylandı.",
        ),
        [
            (
                "18 января 1535 — Франсиско Писарро основывает Лиму как «Город королей».",
                "1535-yil 18-yanvar — Fransisko Pisarro Limaga «Qirollar shahri» sifatida asos soldi.",
                "1535-jıl 18-yanvar — Fransisko Pisarro Limanı «Korollar qalası» retinde tiykarladı.",
            ),
            (
                "1551 — Основан университет Сан-Маркос — один из старейших университетов Америки.",
                "1551 — San-Markos universiteti tashkil etildi — Amerikadagi eng qadimgi universitetlardan biri.",
                "1551 — San-Markos universiteti dúzildi — Amerikadaǵı eń áyyemgi universitetlerden biri.",
            ),
            (
                "28 июля 1821 — Хосе де Сан-Мартин провозглашает независимость Перу на площади Лимы.",
                "1821-yil 28-iyul — Xose de San-Martin Lima maydonida Peru mustaqilligini eʼlon qildi.",
                "1821-jıl 28-iyul — Xose de San-Martin Lima maydanında Peru ǵárezsizligin járiyaladı.",
            ),
        ],
        [
            (
                "Credicorp — Крупнейшая финансовая группа Перу (Banco de Crédito del Perú), штаб-квартира в Лиме.",
                "Credicorp — Peruning eng yirik moliyaviy guruhi (Banco de Crédito del Perú), bosh qarorgohi Limada.",
                "Credicorp — Perudıń eń iri finans toparı (Banco de Crédito del Perú), bas shtab-páteri Limada.",
            ),
            (
                "Порт Кальяо — Главный морской порт Перу рядом с Лимой.",
                "Kalyao porti — Lima yonidagi Peruning asosiy dengiz porti.",
                "Kalyao portı — Lima janındaǵı Perudıń tiykarǵı teńiz portı.",
            ),
        ],
    ),
    # ------------------------------------------------------------- Колумбия
    _city(
        "CO", ("Богота", "Bogota", "Bogota"), 4.7110, -74.0721, 7900000, True,
        (
            "Богота — столица Колумбии, расположенная в Андах на высоте около 2600 метров. Это крупнейший город страны, центр её политики, культуры и бизнеса.",
            "Bogota — Kolumbiya poytaxti, And togʻlarida taxminan 2600 metr balandlikda joylashgan. Bu mamlakatning eng yirik shahri, siyosat, madaniyat va biznes markazi.",
            "Bogota — Kolumbiya paytaxtı, And taw tizbeginde shama menen 2600 metr biyiklikte jaylasqan. Ol eldiń eń iri qalası, siyasat, mádeniyat hám biznes orayı.",
        ),
        [
            (
                "6 августа 1538 — Гонсало Хименес де Кесада основывает город Санта-Фе-де-Богота.",
                "1538-yil 6-avgust — Gonsalo Ximenes de Kesada Santa-Fe-de-Bogota shahriga asos soldi.",
                "1538-jıl 6-avgust — Gonsalo Ximenes de Kesada Santa-Fe-de-Bogota qalasın tiykarladı.",
            ),
            (
                "1819 — После победы Боливара в битве при Бояке Богота освобождена от испанской власти.",
                "1819 — Bolivarning Boyaka jangidagi gʻalabasidan soʻng Bogota ispan hokimiyatidan ozod qilindi.",
                "1819 — Bolivardıń Boyaka urısındaǵı jeńisinen keyin Bogota ispan húkimetinen azat etildi.",
            ),
            (
                "9 апреля 1948 — Убийство политика Хорхе Гайтана вызывает массовые беспорядки «Боготасо».",
                "1948-yil 9-aprel — Siyosatchi Xorxe Gaytanning oʻldirilishi «Bogotaso» ommaviy tartibsizliklarini keltirib chiqardi.",
                "1948-jıl 9-aprel — Siyasatshı Xorxe Gaytannıń óltiriliwi «Bogotaso» ammaviy tártipsizliklerin keltirip shıǵardı.",
            ),
        ],
        [
            (
                "Ecopetrol — Государственная нефтяная компания Колумбии, штаб-квартира в Боготе.",
                "Ecopetrol — Kolumbiyaning davlat neft kompaniyasi, bosh qarorgohi Bogotada.",
                "Ecopetrol — Kolumbiyanıń mámleketlik neft kompaniyası, bas shtab-páteri Bogotada.",
            ),
            (
                "Avianca — Одна из старейших авиакомпаний мира, основана в 1919 году; базируется в Боготе.",
                "Avianca — Dunyodagi eng qadimgi aviakompaniyalardan biri, 1919-yilda tashkil etilgan; Bogotada joylashgan.",
                "Avianca — Dúnyadaǵı eń áyyemgi aviakompaniyalardan biri, 1919-jılı dúzilgen; Bogotada jaylasqan.",
            ),
        ],
    ),
    # ---------------------------------------------------------------- Кения
    _city(
        "KE", ("Найроби", "Nayrobi", "Nayrobi"), -1.2921, 36.8219, 4400000, True,
        (
            "Найроби — столица Кении, единственная в мире столица с национальным парком на окраине: на фоне небоскрёбов здесь можно увидеть жирафов и львов. Крупнейший деловой центр Восточной Африки.",
            "Nayrobi — Keniya poytaxti, chekkasida milliy bogʻi boʻlgan dunyodagi yagona poytaxt: osmonoʻpar binolar fonida bu yerda jirafa va sherlarni koʻrish mumkin. Sharqiy Afrikaning eng yirik biznes markazi.",
            "Nayrobi — Keniya paytaxtı, shetinde milliy parkı bar dúnyadaǵı jalǵız paytaxt: kókke boylaǵan imaratlar fonında bul jerde jirafa hám arıslanlardı kóriwge boladı. Shıǵıs Afrikanıń eń iri biznes orayı.",
        ),
        [
            (
                "1899 — Железнодорожники Угандийской железной дороги основывают в этом месте станцию, из которой вырастает город.",
                "1899 — Uganda temir yoʻli quruvchilari bu yerda stansiya barpo etdilar, undan shahar oʻsib chiqdi.",
                "1899 — Uganda temir jolı qurılısshıları bul jerde stanciya tiykarladı, sonnan qala ósip shıqtı.",
            ),
            (
                "1946 — Открыт Национальный парк Найроби — первый национальный парк Кении.",
                "1946 — Nayrobi milliy bogʻi ochildi — Keniyadagi birinchi milliy bogʻ.",
                "1946 — Nayrobi milliy parkı ashıldı — Keniyadaǵı birinshi milliy park.",
            ),
            (
                "12 декабря 1963 — Кения получает независимость, Найроби становится её столицей.",
                "1963-yil 12-dekabr — Keniya mustaqillikka erishdi, Nayrobi uning poytaxtiga aylandi.",
                "1963-jıl 12-dekabr — Keniya ǵárezsizlikke erisip, Nayrobi onıń paytaxtına aylandı.",
            ),
        ],
        [
            (
                "Safaricom — Крупнейший оператор связи Кении; запустил систему мобильных платежей M-Pesa (2007).",
                "Safaricom — Keniyaning eng yirik aloqa operatori; M-Pesa mobil toʻlov tizimini ishga tushirgan (2007).",
                "Safaricom — Keniyanıń eń iri baylanıs operatorı; M-Pesa mobil tólew sistemasın iske túsirgen (2007).",
            ),
            (
                "Найробийская фондовая биржа — Главная биржа Кении, основана в 1954 году.",
                "Nayrobi fond birjasi — Keniyaning asosiy birjasi, 1954-yilda tashkil etilgan.",
                "Nayrobi fond birjası — Keniyanıń tiykarǵı birjası, 1954-jılı dúzilgen.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Марокко
    _city(
        "MA", ("Касабланка", "Kasablanka", "Kasablanka"), 33.5731, -7.5898, 3400000, False,
        (
            "Касабланка — крупнейший город и главный экономический центр Марокко на берегу Атлантики. Здесь стоит мечеть Хасана II, минарет которой — один из самых высоких в мире.",
            "Kasablanka — Atlantika sohilidagi Marokashning eng yirik shahri va asosiy iqtisodiy markazi. Bu yerda Hasan II masjidi joylashgan, uning minorasi dunyodagi eng balandlaridan biri.",
            "Kasablanka — Atlantika jaǵasındaǵı Marokkonıń eń iri qalası hám tiykarǵı ekonomikalıq orayı. Bul jerde Hasan II meshiti jaylasqan, onıń minarası dúnyadaǵı eń biyiklerinen biri.",
        ),
        [
            (
                "1755 — После землетрясения в Лиссабоне султан Мухаммед бен Абдаллах отстраивает город и называет его Дар-эль-Бейда.",
                "1755 — Lissabondagi zilziladan keyin sulton Muhammad ibn Abdulloh shaharni qayta qurib, uni Dor-ul-Bayzo deb atadi.",
                "1755 — Lissabondaǵı jer silkiniwinen keyin sultan Muhammed ibn Abdulla qalanı qayta qurıp, onı Dar-el-Beyda dep atadı.",
            ),
            (
                "Январь 1943 — Рузвельт и Черчилль проводят в Касабланке конференцию союзников.",
                "1943-yil yanvar — Ruzvelt va Cherchill Kasablankada ittifoqchilar konferensiyasini oʻtkazdilar.",
                "1943-jıl yanvar — Ruzvelt hám Cherchill Kasablankada awqamlaslar konferenciyasın ótkerdi.",
            ),
            (
                "1993 — Завершено строительство мечети Хасана II на берегу океана.",
                "1993 — Okean sohilidagi Hasan II masjidining qurilishi yakunlandi.",
                "1993 — Okean jaǵasındaǵı Hasan II meshitiniń qurılısı juwmaqlandı.",
            ),
        ],
        [
            (
                "Attijariwafa bank — Крупнейший банк Марокко, штаб-квартира в Касабланке.",
                "Attijariwafa bank — Marokashning eng yirik banki, bosh qarorgohi Kasablankada.",
                "Attijariwafa bank — Marokkonıń eń iri banki, bas shtab-páteri Kasablankada.",
            ),
            (
                "Порт Касабланки — Один из крупнейших портов Северной Африки.",
                "Kasablanka porti — Shimoliy Afrikadagi eng yirik portlardan biri.",
                "Kasablanka portı — Arqa Afrikadaǵı eń iri portlardan biri.",
            ),
        ],
    ),
]

# ------------------------------------------------- Новые города в старых странах
CITIES += [
    # ------------------------------------------------------------------ США
    _city(
        "US", ("Лос-Анджелес", "Los-Anjeles", "Los-Anjeles"), 34.0522, -118.2437, 3900000, False,
        (
            "Лос-Анджелес — крупнейший город Калифорнии и мировая столица кино. Здесь расположен Голливуд, а солнечный климат и океанское побережье притягивают людей со всего мира.",
            "Los-Anjeles — Kaliforniyaning eng yirik shahri va jahon kinosining poytaxti. Bu yerda Gollivud joylashgan, quyoshli iqlim va okean sohili butun dunyodan odamlarni oʻziga tortadi.",
            "Los-Anjeles — Kaliforniyanıń eń iri qalası hám dúnya kinosınıń paytaxtı. Bul jerde Gollivud jaylasqan, quyashlı klimat hám okean jaǵası pútkil dúnyadan adamlardı ózine tartadı.",
        ),
        [
            (
                "4 сентября 1781 — Испанские поселенцы основывают пуэбло Лос-Анджелес.",
                "1781-yil 4-sentabr — Ispan koʻchmanchilari Los-Anjeles pueblosiga asos soldilar.",
                "1781-jıl 4-sentyabr — Ispan kóshpendileri Los-Anjeles pueblosın tiykarladı.",
            ),
            (
                "1913 — Открыт Лос-Анджелесский акведук, давший городу воду и запустивший его бурный рост.",
                "1913 — Los-Anjeles akvedugi ochildi; u shaharni suv bilan taʼminlab, uning shiddatli oʻsishiga turtki berdi.",
                "1913 — Los-Anjeles akveduǵı ashıldı; ol qalanı suw menen támiyinlep, onıń tez ósiwine túrtki berdi.",
            ),
            (
                "1932 и 1984 — Лос-Анджелес принимает летние Олимпийские игры.",
                "1932 va 1984 — Los-Anjeles yozgi Olimpiya oʻyinlariga mezbonlik qildi.",
                "1932 hám 1984 — Los-Anjeles jazǵı Olimpiya oyınlarına mezbanlıq etti.",
            ),
        ],
        [
            (
                "Paramount Pictures — Одна из старейших киностудий США, основана в 1912 году; находится в Голливуде.",
                "Paramount Pictures — AQShdagi eng qadimgi kinostudiyalardan biri, 1912-yilda tashkil etilgan; Gollivudda joylashgan.",
                "Paramount Pictures — AQShtaǵı eń áyyemgi kinostudiyalardan biri, 1912-jılı dúzilgen; Gollivudta jaylasqan.",
            ),
            (
                "Порты Лос-Анджелеса и Лонг-Бич — Крупнейший портовый комплекс США, через него идёт значительная часть импорта страны.",
                "Los-Anjeles va Long-Bich portlari — AQShning eng yirik port majmuasi, mamlakat importining katta qismi shu yerdan oʻtadi.",
                "Los-Anjeles hám Long-Bich portları — AQShtıń eń iri port kompleksi, eldiń importınıń úlken bólegi usı jerden ótedi.",
            ),
        ],
    ),
    # ------------------------------------------------------------- Япония
    _city(
        "JP", ("Киото", "Kioto", "Kioto"), 35.0116, 135.7681, 1460000, False,
        (
            "Киото — древняя столица Японии, где сохранились тысячи храмов, святилищ и садов. Более тысячи лет здесь жил императорский двор, поэтому город считают хранителем традиционной японской культуры.",
            "Kioto — Yaponiyaning qadimiy poytaxti, bu yerda minglab ibodatxona, ziyoratgoh va bogʻlar saqlanib qolgan. Imperator saroyi bu yerda ming yildan ortiq turgan, shu sabab shahar anʼanaviy yapon madaniyatining qoʻriqchisi hisoblanadi.",
            "Kioto — Yaponiyanıń áyyemgi paytaxtı, bul jerde mıńlaǵan ibadatxana, ziyaratxana hám baǵlar saqlanıp qalǵan. Imperator saraydı bul jerde mıń jıldan artıq turǵan, sol sebepli qala dástúriy yapon mádeniyatınıń saqlawshısı sanaladı.",
        ),
        [
            (
                "794 — Император Камму переносит двор в Хэйан-кё (будущий Киото): начинается эпоха Хэйан.",
                "794 — Imperator Kammu saroyni Xeyan-kyoga (kelajakdagi Kioto) koʻchirdi: Xeyan davri boshlandi.",
                "794 — Imperator Kammu saraydı Xeyan-kyoǵa (keleshektegi Kioto) kóshirdi: Xeyan dáwiri baslandı.",
            ),
            (
                "1467–1477 — Война Онин разрушает большую часть города.",
                "1467–1477 — Onin urushi shaharning katta qismini vayron qildi.",
                "1467–1477 — Onin urısı qalanıń úlken bólegin qırattı.",
            ),
            (
                "1997 — В Киото принят Киотский протокол по ограничению выбросов парниковых газов.",
                "1997 — Kiotoda issiqxona gazlari chiqindilarini cheklash boʻyicha Kioto protokoli qabul qilindi.",
                "1997 — Kiotoda ıssıxana gazları shıǵındıların sheklew boyınsha Kioto protokolı qabıl etildi.",
            ),
        ],
        [
            (
                "Nintendo — Производитель видеоигр и консолей; основана в Киото в 1889 году как фабрика игральных карт ханафуда.",
                "Nintendo — Video oʻyinlar va konsollar ishlab chiqaruvchi; 1889-yilda Kiotoda hanafuda oʻyin kartalari fabrikasi sifatida tashkil topgan.",
                "Nintendo — Video oyınlar hám konsollar islep shıǵarıwshı; 1889-jılı Kiotoda hanafuda oyın kartaları fabrikası retinde dúzilgen.",
            ),
            (
                "Kyocera — Технологическая корпорация (керамика, электроника), основана в Киото в 1959 году.",
                "Kyocera — Texnologiya korporatsiyasi (keramika, elektronika), 1959-yilda Kiotoda tashkil etilgan.",
                "Kyocera — Texnologiya korporaciyası (keramika, elektronika), 1959-jılı Kiotoda dúzilgen.",
            ),
        ],
    ),
    _city(
        "JP", ("Осака", "Osaka", "Osaka"), 34.6937, 135.5023, 2750000, False,
        (
            "Осака — третий по величине город Японии и её торговая столица, славящийся уличной едой, особенно такояки. Исторически это купеческий город, «кухня нации».",
            "Osaka — Yaponiyaning uchinchi yirik shahri va savdo poytaxti, koʻcha taomlari, ayniqsa, takoyaki bilan mashhur. Tarixan savdogarlar shahri, «millat oshxonasi».",
            "Osaka — Yaponiyanıń úshinshi iri qalası hám sawda paytaxtı, kósh awqatları, ásirese takoyaki menen belgili. Tariyxan sawdagerler qalası, «millet asxanası».",
        ),
        [
            (
                "1583 — Тоётоми Хидэёси начинает строительство замка Осака.",
                "1583 — Toyotomi Xideyosi Osaka qasrining qurilishini boshladi.",
                "1583 — Toyotomi Xideyosi Osaka qalasınıń qurılısın basladı.",
            ),
            (
                "1615 — Осада Осаки завершается победой Токугава Иэясу и падением рода Тоётоми.",
                "1615 — Osaka qamali Tokugava Ieyasuning gʻalabasi va Toyotomi sulolasining qulashi bilan yakunlandi.",
                "1615 — Osaka qamalı Tokugava Ieyasuniń jeńisi hám Toyotomi áwladınıń qulawı menen juwmaqlandı.",
            ),
            (
                "1970 — В Осаке проходит Всемирная выставка Экспо-70.",
                "1970 — Osakada Expo-70 jahon koʻrgazmasi oʻtkazildi.",
                "1970 — Osakada Expo-70 dúnyalıq kórgesmesi ótkerildi.",
            ),
        ],
        [
            (
                "Panasonic — Электроника; основана в 1918 году Коносукэ Мацусита в Осаке, штаб-квартира в Кадомо (префектура Осака).",
                "Panasonic — Elektronika; 1918-yilda Konosuke Matsusita tomonidan Osakada asos solingan, bosh qarorgohi Kadomoda (Osaka prefekturasi).",
                "Panasonic — Elektronika; 1918-jılı Konosuke Matsusita tárepinen Osakada tiykarlanǵan, bas shtab-páteri Kadomoda (Osaka prefekturası).",
            ),
            (
                "Sharp — Производитель электроники со штаб-квартирой в Сакаи (префектура Осака); с 2016 года принадлежит Foxconn.",
                "Sharp — Bosh qarorgohi Sakaida (Osaka prefekturasi) joylashgan elektronika ishlab chiqaruvchi; 2016-yildan Foxconn tarkibida.",
                "Sharp — Bas shtab-páteri Sakaide (Osaka prefekturası) jaylasqan elektronika islep shıǵarıwshı; 2016-jıldan Foxconn quramında.",
            ),
        ],
    ),
    # ------------------------------------------------------------- Россия
    _city(
        "RU", ("Казань", "Qozon", "Qazan"), 55.7961, 49.1064, 1300000, False,
        (
            "Казань — столица Татарстана на берегу Волги, где соседствуют православный собор и мечеть Кул-Шариф в стенах кремля. Современный научный, спортивный и промышленный центр.",
            "Qozon — Volga boʻyidagi Tatariston poytaxti; kreml devorlari ichida pravoslav sobori va Kul-Sharif masjidi yonma-yon turadi. Zamonaviy ilmiy, sport va sanoat markazi.",
            "Qazan — Volga boyındaǵı Tatarstan paytaxtı; kreml diywalları ishinde pravoslav sobor hám Kul-Sharif meshiti janma-jan turadı. Házirgi zamanǵı ilimiy, sport hám sanaat orayı.",
        ),
        [
            (
                "2 октября 1552 — Войска Ивана Грозного штурмом берут Казань, и Казанское ханство вошло в состав Русского государства.",
                "1552-yil 2-oktabr — Ivan Grozniy qoʻshinlari Qozonni hujum bilan egalladi va Qozon xonligi Rus davlati tarkibiga kirdi.",
                "1552-jıl 2-oktyabr — Ivan Groznıy áskerleri Qazandı hújim menen iyeledi hám Qazan xanlıǵı Rus mámleketi quramına kirdi.",
            ),
            (
                "1804 — Основан Казанский университет, где преподавал математик Н. И. Лобачевский.",
                "1804 — Qozon universiteti tashkil etildi; matematik N. I. Lobachevskiy shu yerda dars bergan.",
                "1804 — Qazan universiteti dúzildi; matematik N. I. Lobachevskiy usı jerde sabaq bergen.",
            ),
            (
                "2013 — Казань принимает Всемирную летнюю Универсиаду.",
                "2013 — Qozon Jahon yozgi Universiadasiga mezbonlik qildi.",
                "2013 — Qazan Dúnyalıq jazǵı Universiadaǵa mezbanlıq etti.",
            ),
        ],
        [
            (
                "Казанский вертолётный завод — Производитель вертолётов Ми-8/17, основан в 1940 году.",
                "Qozon vertolyot zavodi — Mi-8/17 vertolyotlari ishlab chiqaruvchi, 1940-yilda tashkil etilgan.",
                "Qazan vertolyot zavodı — Mi-8/17 vertolyotların islep shıǵarıwshı, 1940-jılı dúzilgen.",
            ),
            (
                "Казаньоргсинтез — Один из крупнейших российских производителей полиэтилена.",
                "Kazanorgsintez — Rossiyadagi eng yirik polietilen ishlab chiqaruvchilardan biri.",
                "Kazanorgsintez — Rossiyadaǵı eń iri polietilen islep shıǵarıwshılardan biri.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Китай
    _city(
        "CN", ("Шанхай", "Shanxay", "Shanxay"), 31.2304, 121.4737, 24900000, False,
        (
            "Шанхай — крупнейший город Китая и один из главных финансовых центров мира. Набережная Бунд с колониальной архитектурой соседствует с небоскрёбами района Пудун.",
            "Shanxay — Xitoyning eng yirik shahri va dunyoning asosiy moliya markazlaridan biri. Mustamlaka meʼmorchiligidagi Bund qirgʻoqboʻyi Pudun tumanining osmonoʻpar binolari bilan yonma-yon turadi.",
            "Shanxay — Qıtaydıń eń iri qalası hám dúnyanıń tiykarǵı finans orayların biri. Koloniyal arxitekturalı Bund jaǵalawı Pudun rayonınıń kókke boylaǵan imaratları menen janma-jan turadı.",
        ),
        [
            (
                "1843 — После Первой опиумной войны Шанхай открывается для иностранной торговли.",
                "1843 — Birinchi afyun urushidan soʻng Shanxay xorijiy savdo uchun ochildi.",
                "1843 — Birinshi apiyin urısınan keyin Shanxay shet el sawdası ushın ashıldı.",
            ),
            (
                "Июль 1921 — В Шанхае проходит I съезд Коммунистической партии Китая.",
                "1921-yil iyul — Shanxayda Xitoy Kommunistik partiyasining I syezdi oʻtkazildi.",
                "1921-jıl iyul — Shanxayda Qıtay Kommunistlik partiyasınıń I sezdi ótkerildi.",
            ),
            (
                "1990 — Принято решение о развитии района Пудун, которое превратило болотистые земли в финансовый центр.",
                "1990 — Pudun tumanini rivojlantirish toʻgʻrisida qaror qabul qilindi; botqoq yerlar moliya markaziga aylandi.",
                "1990 — Pudun rayonın rawajlandırıw haqqında sheshim qabıl etildi; batpaqlı jerler finans orayına aylandı.",
            ),
        ],
        [
            (
                "SAIC Motor — Крупнейший китайский автопроизводитель, штаб-квартира в Шанхае.",
                "SAIC Motor — Xitoyning eng yirik avtomobil ishlab chiqaruvchisi, bosh qarorgohi Shanxayda.",
                "SAIC Motor — Qıtaydıń eń iri avtomobil islep shıǵarıwshısı, bas shtab-páteri Shanxayda.",
            ),
            (
                "Порт Шанхая — Самый загруженный контейнерный порт мира.",
                "Shanxay porti — Dunyodagi eng gavjum konteyner porti.",
                "Shanxay portı — Dúnyadaǵı eń bánt konteyner portı.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Индия
    _city(
        "IN", ("Мумбаи", "Mumbay", "Mumbay"), 19.0760, 72.8777, 12500000, False,
        (
            "Мумбаи (бывший Бомбей) — финансовая столица Индии на берегу Аравийского моря и центр кинематографа Болливуд. Это один из самых густонаселённых городов мира.",
            "Mumbay (sobiq Bombay) — Arab dengizi sohilidagi Hindistonning moliyaviy poytaxti va Bollivud kinematografiyasining markazi. Dunyoning eng gavjum shaharlaridan biri.",
            "Mumbay (burınǵı Bombay) — Arab teńizi jaǵasındaǵı Hindstannıń finans paytaxtı hám Bollivud kinematografiyasınıń orayı. Dúnyanıń eń tıǵız jasaytuǵın qalalarınan biri.",
        ),
        [
            (
                "1661 — Бомбей переходит к Англии как часть приданого Екатерины Браганса при браке с Карлом II.",
                "1661 — Bombay Qirol Karl II bilan nikoh chogʻida Ketrin Braganzaning sepi sifatida Angliyaga oʻtdi.",
                "1661 — Bombay Korol Karl II menen nekede Ketrin Braganzanıń sepi retinde Angliyaǵa ótti.",
            ),
            (
                "16 апреля 1853 — Между Бомбеем и Тханой открыта первая в Индии пассажирская железная дорога.",
                "1853-yil 16-aprel — Bombay va Tana oʻrtasida Hindistondagi birinchi yoʻlovchi temir yoʻli ochildi.",
                "1853-jıl 16-aprel — Bombay hám Tana ortasında Hindstandaǵı birinshi jolawshı temir jolı ashıldı.",
            ),
            (
                "1995 — Бомбей официально переименован в Мумбаи.",
                "1995 — Bombay rasman Mumbay deb qayta nomlandi.",
                "1995 — Bombay rásmiy túrde Mumbay dep qayta atalǵan.",
            ),
        ],
        [
            (
                "Tata Group — Крупнейший индийский конгломерат, основан Джамшеджи Тата в 1868 году; штаб-квартира в Мумбаи.",
                "Tata Group — Hindistonning eng yirik konglomerati, 1868-yilda Jamshedji Tata tomonidan asos solingan; bosh qarorgohi Mumbayda.",
                "Tata Group — Hindstannıń eń iri konglomeratı, 1868-jılı Jamshedji Tata tárepinen tiykarlanǵan; bas shtab-páteri Mumbayda.",
            ),
            (
                "Бомбейская фондовая биржа (BSE) — Старейшая биржа Азии, основана в 1875 году.",
                "Bombay fond birjasi (BSE) — Osiyodagi eng qadimgi birja, 1875-yilda tashkil etilgan.",
                "Bombay fond birjası (BSE) — Aziyadaǵı eń áyyemgi birja, 1875-jılı dúzilgen.",
            ),
            (
                "Болливуд — Центр хинди-язычного кинематографа, один из крупнейших в мире по числу выпускаемых фильмов.",
                "Bollivud — Hind tilidagi kinematografiya markazi, ishlab chiqariladigan filmlar soni boʻyicha dunyodagi eng yirik markazlardan biri.",
                "Bollivud — Hind tilindegi kinematografiya orayı, shıǵarılatuǵın filmler sanı boyınsha dúnyadaǵı eń iri orayların biri.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Германия
    _city(
        "DE", ("Мюнхен", "Myunxen", "Myunxen"), 48.1351, 11.5820, 1500000, False,
        (
            "Мюнхен — столица Баварии, город пивных садов, музеев и высоких технологий. Здесь проходит крупнейший в мире народный праздник Октоберфест.",
            "Myunxen — Bavariya poytaxti, pivo bogʻlari, muzeylar va yuqori texnologiyalar shahri. Bu yerda dunyodagi eng yirik xalq bayrami Oktoberfest oʻtkaziladi.",
            "Myunxen — Bavariya paytaxtı, piwo baǵları, muzeyler hám joqarı texnologiyalar qalası. Bul jerde dúnyadaǵı eń iri xalıq bayramı Oktoberfest ótkeriledi.",
        ),
        [
            (
                "1158 — Генрих Лев основывает Мюнхен как торговый город на соляном пути.",
                "1158 — Genrix Arslon Myunxenga tuz yoʻli ustidagi savdo shahri sifatida asos soldi.",
                "1158 — Genrix Arıslan Myunxendi duz jolı ústindegi sawda qalası retinde tiykarladı.",
            ),
            (
                "12 октября 1810 — Первый Октоберфест устроен в честь свадьбы кронпринца Людвига и принцессы Терезы.",
                "1810-yil 12-oktabr — Toj vorisi Lyudvig va malika Tereza toyi sharafiga birinchi Oktoberfest uyushtirildi.",
                "1810-jıl 12-oktyabr — Taj miyrasxorı Lyudvig hám prinsessa Tereza toyı húrmetine birinshi Oktoberfest ótkerildi.",
            ),
            (
                "1972 — В Мюнхене проходят летние Олимпийские игры.",
                "1972 — Myunxenda yozgi Olimpiya oʻyinlari oʻtkazildi.",
                "1972 — Myunxende jazǵı Olimpiya oyınları ótkerildi.",
            ),
        ],
        [
            (
                "BMW — Автопроизводитель, основан в 1916 году; штаб-квартира в Мюнхене.",
                "BMW — Avtomobil ishlab chiqaruvchi, 1916-yilda tashkil etilgan; bosh qarorgohi Myunxenda.",
                "BMW — Avtomobil islep shıǵarıwshı, 1916-jılı dúzilgen; bas shtab-páteri Myunxende.",
            ),
            (
                "Siemens — Технологический концерн (электротехника, автоматизация), штаб-квартира в Мюнхене.",
                "Siemens — Texnologiya konserni (elektrotexnika, avtomatlashtirish), bosh qarorgohi Myunxenda.",
                "Siemens — Texnologiya konserni (elektrotexnika, avtomatlastırıw), bas shtab-páteri Myunxende.",
            ),
        ],
    ),
    # ------------------------------------------------------------- Италия
    _city(
        "IT", ("Милан", "Milan", "Milan"), 45.4642, 9.1900, 1400000, False,
        (
            "Милан — экономическая столица Италии и мировой центр моды и дизайна. В его центре стоит величественный готический Дуомо, а в монастыре Санта-Мария-делле-Грацие хранится «Тайная вечеря» Леонардо да Винчи.",
            "Milan — Italiyaning iqtisodiy poytaxti va jahon moda hamda dizayn markazi. Markazida ulugʻvor gotik Duomo turadi, Santa-Mariya-delle-Gratsie monastirida esa Leonardo da Vinchining «Oxirgi kechlik» asari saqlanadi.",
            "Milan — Italiyanıń ekonomikalıq paytaxtı hám dúnyalıq moda hám dizayn orayı. Orayında ulıwma gotikalıq Duomo turadı, Santa-Mariya-delle-Gracie monastırında bolsa Leonardo da Vinchiniń «Sońǵı keshlik» shıǵarması saqlanadı.",
        ),
        [
            (
                "313 — Императоры Константин и Лициний издают Миланский эдикт о свободе вероисповедания.",
                "313 — Imperatorlar Konstantin va Litsiniy din erkinligi toʻgʻrisida Milan farmonini eʼlon qildilar.",
                "313 — Imperatorlar Konstantin hám Licinij diniy erkinlik haqqında Milan perman'ın járiyaladı.",
            ),
            (
                "1386 — Начинается строительство Миланского собора, которое продлится несколько веков.",
                "1386 — Milan soborining qurilishi boshlandi, u bir necha asr davom etdi.",
                "1386 — Milan soborınıń qurılısı baslandı, ol bir neshe ásir dawam etti.",
            ),
            (
                "Около 1498 — Леонардо да Винчи завершает фреску «Тайная вечеря».",
                "Taxminan 1498 — Leonardo da Vinchi «Oxirgi kechlik» freskasini yakunladi.",
                "Shama menen 1498 — Leonardo da Vinchi «Sońǵı keshlik» freskasın juwmaqladı.",
            ),
        ],
        [
            (
                "Pirelli — Производитель шин, основан в Милане в 1872 году.",
                "Pirelli — Shina ishlab chiqaruvchi, 1872-yilda Milanda asos solingan.",
                "Pirelli — Shina islep shıǵarıwshı, 1872-jılı Milanda tiykarlanǵan.",
            ),
            (
                "Prada — Модный дом, основан в Милане в 1913 году.",
                "Prada — Moda uyi, 1913-yilda Milanda asos solingan.",
                "Prada — Moda úyi, 1913-jılı Milanda tiykarlanǵan.",
            ),
        ],
    ),
    # ----------------------------------------------- Великобритания
    _city(
        "GB", ("Эдинбург", "Edinburg", "Edinburg"), 55.9533, -3.1883, 530000, False,
        (
            "Эдинбург — столица Шотландии, город на вулканических холмах, над которым возвышается замок. Старый и Новый город внесены в список Всемирного наследия ЮНЕСКО.",
            "Edinburg — Shotlandiya poytaxti, vulqon tepaliklarida joylashgan shahar, uning ustida qasr koʻtarilib turadi. Eski va Yangi shahar YuNESKO Jahon merosi roʻyxatiga kiritilgan.",
            "Edinburg — Shotlandiya paytaxtı, vulkan tóbeliklerinde jaylasqan qala, onıń ústinde qala kóterilip turadı. Eski hám Jańa qala YuNESKO Dúnya mereesi dizimine kiritilgen.",
        ),
        [
            (
                "1128 — Король Давид I основывает аббатство Холируд у подножия холма с крепостью.",
                "1128 — Qirol Devid I qalʼali tepalik etagida Xolirud abbatligiga asos soldi.",
                "1128 — Korol Devid I qalalı tóbelik etegindegi Xolirud abbatlıǵına tiykar saldı.",
            ),
            (
                "1707 — Акт об унии объединяет Шотландию и Англию в единое королевство.",
                "1707 — Ittifoq toʻgʻrisidagi akt Shotlandiya va Angliyani yagona qirollikka birlashtirdi.",
                "1707 — Awqam haqqındaǵı akt Shotlandiya hám Angliyanı birdey korollikke birlestirdi.",
            ),
            (
                "1947 — Проходит первый Эдинбургский международный фестиваль.",
                "1947 — Birinchi Edinburg xalqaro festivali oʻtkazildi.",
                "1947 — Birinshi Edinburg xalıqaralıq festivalı ótkerildi.",
            ),
        ],
        [
            (
                "NatWest Group — Банковская группа (бывший Royal Bank of Scotland, основан в 1727 году) со штаб-квартирой в Эдинбурге.",
                "NatWest Group — Bosh qarorgohi Edinburgda joylashgan bank guruhi (sobiq Royal Bank of Scotland, 1727-yilda asos solingan).",
                "NatWest Group — Bas shtab-páteri Edinburgte jaylasqan bank toparı (burınǵı Royal Bank of Scotland, 1727-jılı tiykarlanǵan).",
            ),
            (
                "Baillie Gifford — Инвестиционная компания, основана в Эдинбурге в 1908 году.",
                "Baillie Gifford — Investitsiya kompaniyasi, 1908-yilda Edinburgda tashkil etilgan.",
                "Baillie Gifford — Investiciya kompaniyası, 1908-jılı Edinburgte dúzilgen.",
            ),
        ],
    ),
    # --------------------------------------------------------------- Турция
    _city(
        "TR", ("Анкара", "Anqara", "Anqara"), 39.9334, 32.8597, 5700000, True,
        (
            "Анкара — столица Турции, расположенная в центре Анатолийского плато. Её сделал столицей Мустафа Кемаль Ататюрк, и именно здесь рождалась современная Турецкая Республика.",
            "Anqara — Anadolu platosi markazida joylashgan Turkiya poytaxti. Uni Mustafo Kamol Otaturk poytaxt qildi, zamonaviy Turkiya Respublikasi aynan shu yerda tugʻildi.",
            "Anqara — Anadolı platosınıń ortasında jaylasqan Túrkiya paytaxtı. Onı Mustafa Kemal Ataturk paytaxt etti, házirgi zamanǵı Túrkiya Respublikası dál usı jerde tuwıldı.",
        ),
        [
            (
                "23 апреля 1920 — В Анкаре открывается Великое национальное собрание Турции.",
                "1920-yil 23-aprel — Anqarada Turkiya Buyuk Milliy Majlisi ochildi.",
                "1920-jıl 23-aprel — Anqarada Túrkiya Ullı Milliy Májilisi ashıldı.",
            ),
            (
                "13 октября 1923 — Анкара объявлена столицей; через две недели провозглашена Турецкая Республика.",
                "1923-yil 13-oktabr — Anqara poytaxt deb eʼlon qilindi; ikki haftadan soʻng Turkiya Respublikasi eʼlon qilindi.",
                "1923-jıl 13-oktyabr — Anqara paytaxt dep járiyalandı; eki hápteden keyin Túrkiya Respublikası járiyalandı.",
            ),
            (
                "1953 — Завершено строительство Аныткабира — мавзолея Ататюрка.",
                "1953 — Otaturk maqbarasi Anıtkabirning qurilishi yakunlandi.",
                "1953 — Ataturk maqbarası Anıtkabirdiń qurılısı juwmaqlandı.",
            ),
        ],
        [
            (
                "TUSAŞ (Turkish Aerospace) — Авиакосмическая компания, создаёт самолёты, вертолёты и беспилотники.",
                "TUSAŞ (Turkish Aerospace) — Samolyotlar, vertolyotlar va uchuvchisiz apparatlar yaratadigan aviakosmik kompaniya.",
                "TUSAŞ (Turkish Aerospace) — Samolyotlar, vertolyotlar hám pilotsız apparatlar jaratatuǵın aviakosmoslıq kompaniya.",
            ),
            (
                "ASELSAN — Крупнейшая турецкая компания военной электроники, основана в Анкаре в 1975 году.",
                "ASELSAN — Turkiyaning eng yirik harbiy elektronika kompaniyasi, 1975-yilda Anqarada tashkil etilgan.",
                "ASELSAN — Túrkiyanıń eń iri áskeriy elektronika kompaniyası, 1975-jılı Anqarada dúzilgen.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Узбекистан
    _city(
        "UZ", ("Хива", "Xiva", "Xiywa"), 41.3783, 60.3639, 92000, False,
        (
            "Хива — древний город в Хорезме, где внутренний город Ичан-Кала сохранился почти полностью: глиняные стены, минареты, мечети и медресе. Один из самых цельных городов-музеев Великого шёлкового пути.",
            "Xiva — Xorazmdagi qadimiy shahar; Ichan-Qalʼa ichki shahri deyarli toʻliq saqlanib qolgan: loy devorlar, minoralar, masjidlar va madrasalar. Buyuk ipak yoʻlining eng yaxlit shahar-muzeylaridan biri.",
            "Xiywa — Xorezmdegi áyyemgi qala; Ishan-Qala ishki qalası derlik tolıq saqlanıp qalǵan: balshıq diywallar, minaralar, meshitler hám medreseler. Ullı jipek jolınıń eń pútin qala-muzeylerinen biri.",
        ),
        [
            (
                "1592 — Хива становится столицей Хорезмского (Хивинского) ханства.",
                "1592 — Xiva Xorazm (Xiva) xonligining poytaxtiga aylandi.",
                "1592 — Xiywa Xorezm (Xiywa) xanlıǵınıń paytaxtına aylandı.",
            ),
            (
                "1873 — Русские войска занимают Хиву, ханство становится протекторатом Российской империи.",
                "1873 — Rus qoʻshinlari Xivani egalladi, xonlik Rossiya imperiyasining protektoratiga aylandi.",
                "1873 — Rus áskerleri Xiywanı iyeledi, xanlıq Rossiya imperiyasınıń protektoratına aylandı.",
            ),
            (
                "1990 — Ичан-Кала включена в список Всемирного наследия ЮНЕСКО — первым объектом Узбекистана.",
                "1990 — Ichan-Qalʼa YuNESKO Jahon merosi roʻyxatiga kiritildi — Oʻzbekistonning birinchi obyekti.",
                "1990 — Ishan-Qala YuNESKO Dúnya mereesi dizimine kiritildi — Ózbekstannıń birinshi obyekti.",
            ),
        ],
        [
            (
                "Хорезмское ковроткачество — Традиционное ремесло: шерстяные и шёлковые ковры с местными орнаментами.",
                "Xorazm gilamdoʻzligi — Anʼanaviy hunarmandchilik: mahalliy naqshli jun va ipak gilamlar.",
                "Xorezm gilem toqıwshılıǵı — Dástúriy ónermentshilik: jergilikli oyıwlı jún hám jipek gilemler.",
            ),
            (
                "Резьба по дереву — Хивинские мастера создают резные колонны, двери и шкатулки; колонны мечети Джума относятся к X–XVIII векам.",
                "Yogʻoch oymakorligi — Xiva ustalari oyma ustunlar, eshiklar va qutichalar yasaydilar; Juma masjidi ustunlari X–XVIII asrlarga oid.",
                "Aǵash oymakarlıǵı — Xiywa sheberleri oyma kolonnalar, esikler hám qutishalar jasaydı; Juma meshiti kolonnaları X–XVIII ásirlerge tiyisli.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Казахстан
    _city(
        "KZ", ("Алматы", "Almaty", "Almatı"), 43.2389, 76.8897, 2100000, False,
        (
            "Алматы — крупнейший город Казахстана и его финансовый центр у подножия хребта Заилийский Алатау. Бывшая столица страны; высоко в горах расположены каток Медеу и горнолыжный курорт Шымбулак.",
            "Almaty — Qozogʻistonning eng yirik shahri va moliya markazi, Zayli Olatovi tizmasi etagida joylashgan. Mamlakatning sobiq poytaxti; togʻlarda Medeu muz maydoni va Shimbulak togʻ-changʻi kurorti joylashgan.",
            "Almatı — Qazaqstannıń eń iri qalası hám finans orayı, Zayli Alataw dizbegi etegide jaylasqan. Eldiń burınǵı paytaxtı; tawlarda Medeu muz maydanı hám Shımbulaq taw shańǵı kurortı jaylasqan.",
        ),
        [
            (
                "1854 — Основано военное укрепление Верное, из которого вырос город.",
                "1854 — Vernoye harbiy istehkomi barpo etildi, undan shahar oʻsib chiqdi.",
                "1854 — Vernoe áskeriy bekinisi tiykarlandı, sonnan qala ósip shıqtı.",
            ),
            (
                "1929 — Алма-Ата становится столицей Казахской АССР.",
                "1929 — Alma-Ota Qozoq ASSRning poytaxtiga aylandi.",
                "1929 — Alma-Ata Qazaq ASSRdiń paytaxtına aylandı.",
            ),
            (
                "Декабрь 1991 — В Алма-Ате подписана декларация о создании СНГ; Казахстан провозглашает независимость.",
                "1991-yil dekabr — Alma-Otada MDH tuzilishi toʻgʻrisidagi deklaratsiya imzolandi; Qozogʻiston mustaqilligini eʼlon qildi.",
                "1991-jıl dekabr — Alma-Atada MDH dúzilgeni haqqındaǵı deklaraciya qol qoyıldı; Qazaqstan ǵárezsizligin járiyaladı.",
            ),
        ],
        [
            (
                "Halyk Bank — Крупнейший банк Казахстана, штаб-квартира в Алматы.",
                "Halyk Bank — Qozogʻistonning eng yirik banki, bosh qarorgohi Almatida.",
                "Halyk Bank — Qazaqstannıń eń iri banki, bas shtab-páteri Almatıda.",
            ),
            (
                "Kaspi.kz — Финтех-супераприложение, основано в Алматы; акции торгуются на бирже Nasdaq.",
                "Kaspi.kz — Fintex superilova, Almatida tashkil etilgan; aksiyalari Nasdaq birjasida savdo qilinadi.",
                "Kaspi.kz — Fintex superqosımsha, Almatıda dúzilgen; akciyaları Nasdaq birjasında sawdalanadı.",
            ),
        ],
    ),
    # ------------------------------------------------------------ Австралия
    _city(
        "AU", ("Мельбурн", "Melburn", "Melburn"), -37.8136, 144.9631, 5200000, False,
        (
            "Мельбурн — второй по величине город Австралии, признанная столица кофе, уличного искусства и спорта. Здесь проходит Открытый чемпионат Австралии по теннису.",
            "Melburn — Avstraliyaning ikkinchi yirik shahri, qahva, koʻcha sanʼati va sport poytaxti sifatida tanilgan. Bu yerda Avstraliya ochiq tennis chempionati oʻtkaziladi.",
            "Melburn — Avstraliyanıń ekinshi iri qalası, qáhwe, kósh óneri hám sport paytaxtı retinde tanılǵan. Bul jerde Avstraliya ashıq tennis chempionatı ótkeriledi.",
        ),
        [
            (
                "1835 — Джон Бэтмен основывает поселение на реке Ярра; в 1837 году оно названо Мельбурн.",
                "1835 — Jon Betmen Yarra daryosi boʻyida aholi punktiga asos soldi; 1837-yilda u Melburn deb nomlandi.",
                "1835 — Djon Betmen Yarra dáryası boyında eliw punktin tiykarladı; 1837-jılı ol Melburn dep atalǵan.",
            ),
            (
                "1851 — Золотая лихорадка в Виктории превращает Мельбурн в один из богатейших городов мира.",
                "1851 — Viktoriyadagi oltin shov-shuvi Melburnni dunyoning eng boy shaharlaridan biriga aylantirdi.",
                "1851 — Viktoriyadaǵı altın dárbazlıǵı Melburndi dúnyanıń eń bay qalalarınan biri etti.",
            ),
            (
                "1901–1927 — Мельбурн служит временной столицей Австралии.",
                "1901–1927 — Melburn Avstraliyaning vaqtinchalik poytaxti boʻlib xizmat qildi.",
                "1901–1927 — Melburn Avstraliyanıń waqtınsha paytaxtı bolıp xizmet etti.",
            ),
        ],
        [
            (
                "BHP — Одна из крупнейших горнодобывающих компаний мира, штаб-квартира в Мельбурне.",
                "BHP — Dunyodagi eng yirik togʻ-kon kompaniyalaridan biri, bosh qarorgohi Melburnda.",
                "BHP — Dúnyadaǵı eń iri taw-kán kompaniyalarınan biri, bas shtab-páteri Melburnda.",
            ),
            (
                "National Australia Bank — Один из «большой четвёрки» банков Австралии, штаб-квартира в Мельбурне.",
                "National Australia Bank — Avstraliyaning «katta toʻrtlik» banklaridan biri, bosh qarorgohi Melburnda.",
                "National Australia Bank — Avstraliyanıń «úlken tórtlik» banklerinen biri, bas shtab-páteri Melburnda.",
            ),
        ],
    ),
]
