/*
 * Ночная Земля — интерактивный 3D-глобус (Globe.gl) с описанием городов.
 * Языки интерфейса и контента: ru, uz, qr.
 *
 * Два режима камеры:
 *   «мир»   — издали видны только страны (подсветка и подписи), города скрыты;
 *   «город» — вблизи (или после клика по стране / выбора в поиске) появляются города.
 */
(() => {
  'use strict';

  const CFG = window.APP_CONFIG;
  const LANGS = ['ru', 'uz', 'qr'];
  const HTML_LANG = { ru: 'ru', uz: 'uz', qr: 'kaa' };
  const NUMBER_LOCALE = { ru: 'ru-RU', uz: 'uz-UZ', qr: 'uz-UZ' };
  const STORAGE_KEY = 'nightglobe.lang';
  const REDUCED_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const RAD = Math.PI / 180;

  const CAMERA = {
    overview: { lat: 38, lng: 62, altitude: 2.6 },
    // Высота камеры над поверхностью (в радиусах Земли).
    // Ближе citiesFrom — показываем города, дальше citiesTo — снова только страны.
    // Разные значения нужны, чтобы режим не мигал на границе.
    citiesFrom: 1.9,
    citiesTo: 2.1,
    countryMinAltitude: 0.8,
    countryMaxAltitude: 1.75,
    focusAltitude: 1.35,
    focusMs: REDUCED_MOTION ? 0 : 1600,
    releaseAltitude: 2.5,
    releaseMs: REDUCED_MOTION ? 0 : 1300,
  };

  /* ------------------------------------------------------------------ *
   *  Тексты интерфейса
   * ------------------------------------------------------------------ */
  const I18N = {
    ru: {
      pageTitle: 'Ночная Земля — города, история, производство',
      brandName: 'Ночная Земля',
      brandTagline: 'Города, история и производство',
      langGroup: 'Язык интерфейса',
      globeLabel: 'Интерактивный глобус: нажмите на страну, чтобы увидеть её города',
      hint: 'Нажмите на страну, чтобы увидеть её города',
      citiesNav: 'Города',
      capital: 'Столица',
      population: 'Население',
      coordinates: 'Координаты',
      sectionDescription: 'О городе',
      sectionHistory: 'История и великие события',
      sectionIndustry: 'Компании и производство',
      close: 'Закрыть панель',
      loading: 'Загружаем глобус…',
      errorLoad: 'Не удалось загрузить города. Проверьте соединение и повторите.',
      errorDetail: 'Не удалось загрузить описание города.',
      errorGlobe: 'Не удалось загрузить 3D-библиотеку. Проверьте подключение к интернету.',
      retry: 'Повторить',
      backToWorld: 'Весь мир',
      searchTitle: 'Поиск',
      searchOpen: 'Поиск городов и стран',
      searchPlaceholder: 'Найти город или страну',
      searchCountries: 'Страны',
      searchCities: 'Города',
      searchEmpty: 'Ничего не найдено',
      timelineOpen: 'Лента времени',
      timelineTitle: 'Путешествие во времени',
      timelineClose: 'Закрыть ленту времени',
      timelinePlay: 'Запустить',
      timelinePause: 'Пауза',
      timelinePrev: 'Предыдущее событие',
      timelineNext: 'Следующее событие',
      timelineRange: 'Событие на ленте времени',
      timelineOpenCity: 'Открыть город',
      errorTimeline: 'Не удалось загрузить события. Проверьте соединение и повторите.',
    },
    uz: {
      pageTitle: 'Tungi Yer — shaharlar, tarix, ishlab chiqarish',
      brandName: 'Tungi Yer',
      brandTagline: 'Shaharlar, tarix va ishlab chiqarish',
      langGroup: 'Interfeys tili',
      globeLabel: 'Interaktiv globus: shaharlarini koʻrish uchun davlatni bosing',
      hint: 'Shaharlarni koʻrish uchun davlatni bosing',
      citiesNav: 'Shaharlar',
      capital: 'Poytaxt',
      population: 'Aholisi',
      coordinates: 'Koordinatalar',
      sectionDescription: 'Shahar haqida',
      sectionHistory: 'Tarix va buyuk voqealar',
      sectionIndustry: 'Kompaniyalar va ishlab chiqarish',
      close: 'Panelni yopish',
      loading: 'Globus yuklanmoqda…',
      errorLoad: 'Shaharlarni yuklab boʻlmadi. Ulanishni tekshirib, qayta urinib koʻring.',
      errorDetail: 'Shahar tavsifini yuklab boʻlmadi.',
      errorGlobe: '3D kutubxonani yuklab boʻlmadi. Internet aloqasini tekshiring.',
      retry: 'Qayta urinish',
      backToWorld: 'Butun dunyo',
      searchTitle: 'Qidiruv',
      searchOpen: 'Shahar va davlatlarni qidirish',
      searchPlaceholder: 'Shahar yoki davlatni toping',
      searchCountries: 'Davlatlar',
      searchCities: 'Shaharlar',
      searchEmpty: 'Hech narsa topilmadi',
      timelineOpen: 'Vaqt chizigʻi',
      timelineTitle: 'Vaqt boʻylab sayohat',
      timelineClose: 'Vaqt chizigʻini yopish',
      timelinePlay: 'Ishga tushirish',
      timelinePause: 'Pauza',
      timelinePrev: 'Oldingi voqea',
      timelineNext: 'Keyingi voqea',
      timelineRange: 'Vaqt chizigʻidagi voqea',
      timelineOpenCity: 'Shaharni ochish',
      errorTimeline: 'Voqealarni yuklab boʻlmadi. Ulanishni tekshirib, qayta urinib koʻring.',
    },
    qr: {
      pageTitle: 'Túngi Jer — qalalar, tariyx, óndiris',
      brandName: 'Túngi Jer',
      brandTagline: 'Qalalar, tariyx hám óndiris',
      langGroup: 'Interfeys tili',
      globeLabel: 'Interaktiv globus: qalaların kóriw ushın mámleketti basıń',
      hint: 'Qalalardı kóriw ushın mámleketti basıń',
      citiesNav: 'Qalalar',
      capital: 'Paytaxt',
      population: 'Xalıq sanı',
      coordinates: 'Koordinatalar',
      sectionDescription: 'Qala haqqında',
      sectionHistory: 'Tariyx hám ullı waqıyalar',
      sectionIndustry: 'Kompaniyalar hám óndiris',
      close: 'Paneldi jabıw',
      loading: 'Globus júklenbekte…',
      errorLoad: 'Qalalardı júklep bolmadı. Baylanıstı tekserip, qayta urınıp kóriń.',
      errorDetail: 'Qala haqqındaǵı maǵlıwmattı júklep bolmadı.',
      errorGlobe: '3D kitapxananı júklep bolmadı. Internet baylanısın tekserip kóriń.',
      retry: 'Qayta urınıp kóriw',
      backToWorld: 'Pútkil dúnya',
      searchTitle: 'Izlew',
      searchOpen: 'Qala hám mámleketlerdi izlew',
      searchPlaceholder: 'Qala yamasa mámleketti tabıń',
      searchCountries: 'Mámleketler',
      searchCities: 'Qalalar',
      searchEmpty: 'Hesh nárse tabılmadı',
      timelineOpen: 'Waqıt sızıǵı',
      timelineTitle: 'Waqıt boylap sayaxat',
      timelineClose: 'Waqıt sızıǵın jabıw',
      timelinePlay: 'Iske túsiriw',
      timelinePause: 'Pauza',
      timelinePrev: 'Aldınǵı waqıya',
      timelineNext: 'Keyingi waqıya',
      timelineRange: 'Waqıt sızıǵındaǵı waqıya',
      timelineOpenCity: 'Qalanı ashıw',
      errorTimeline: 'Waqıyalardı júklep bolmadı. Baylanıstı tekserip, qayta urınıp kóriń.',
    },
  };

  /* ------------------------------------------------------------------ *
   *  Состояние и ссылки на DOM
   * ------------------------------------------------------------------ */
  const $ = (selector, root = document) => root.querySelector(selector);

  const els = {
    globe: $('#globe'),
    panel: $('#panel'),
    content: $('#panel-content'),
    close: $('#panel-close'),
    hint: $('#hint'),
    loader: $('#loader'),
    toast: $('#toast'),
    toastText: $('#toast-text'),
    toastRetry: $('#toast-retry'),
    countryBar: $('#country-bar'),
    countryBack: $('#country-back'),
    countryName: $('#country-name'),
    countryCount: $('#country-count'),
    search: $('#search'),
    searchToggle: $('#search-toggle'),
    searchInput: $('#search-input'),
    searchResults: $('#search-results'),
    timeline: $('#timeline'),
    timelineToggle: $('#tl-toggle'),
    tlClose: $('#tl-close'),
    tlYear: $('#tl-year'),
    tlPlace: $('#tl-place'),
    tlText: $('#tl-text'),
    tlPrev: $('#tl-prev'),
    tlPlay: $('#tl-play'),
    tlNext: $('#tl-next'),
    tlRange: $('#tl-range'),
    tlCount: $('#tl-count'),
    tlOpen: $('#tl-open'),
    langButtons: Array.from(document.querySelectorAll('[data-lang]')),
  };

  const state = {
    lang: detectInitialLang(),
    cities: [],
    countries: [], // только страны, в которых есть города: {code, name, latitude, longitude, count}
    countryByCode: new Map(),
    countryCodes: new Set(),
    featureByCode: new Map(),
    mode: 'world', // 'world' — видны страны, 'near' — видны города
    focusCountry: null, // страна, к которой приближена камера
    focusReached: false, // камера уже подлетела к стране (нужно, чтобы не сбросить фокус на старте полёта)
    activeCountry: null, // подсвеченная страна
    hoverCode: null,
    hovering: false, // курсор над маркером
    selectedId: null,
    searchOpen: false,
    hintDismissed: false,
    markersKey: '',
    detailCache: new Map(),
    detailToken: 0,
    globeReady: false,
    dataReady: false,
    timelineOpen: false,
    timelineByLang: new Map(),
    tlEvents: [], // события ленты времени на текущем языке, по возрастанию года
    tlIndex: 0,
    tlPlaying: false,
    tlCityId: null, // город текущего события ленты: подсвечивается на глобусе
  };

  let globe = null;
  let toastAction = null;
  let autoRotateTimer = null;
  let cameraFrame = 0;
  let tlPlayTimer = null;
  let tlFlyTimer = null;

  const t = (key) => (I18N[state.lang] && I18N[state.lang][key]) || I18N.ru[key] || key;

  function detectInitialLang() {
    const fromUrl = new URLSearchParams(window.location.search).get('lang');
    if (LANGS.includes(fromUrl)) return fromUrl;
    try {
      const stored = window.localStorage.getItem(STORAGE_KEY);
      if (LANGS.includes(stored)) return stored;
    } catch (err) {
      /* localStorage может быть недоступен — не критично */
    }
    return (navigator.language || '').toLowerCase().startsWith('uz') ? 'uz' : 'ru';
  }

  /* ------------------------------------------------------------------ *
   *  Вспомогательные функции
   * ------------------------------------------------------------------ */
  function h(tag, className = '', text = null, attrs = null) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== null && text !== undefined) node.textContent = text;
    if (attrs) {
      Object.entries(attrs).forEach(([name, value]) => node.setAttribute(name, value));
    }
    return node;
  }

  async function getJSON(url) {
    const response = await fetch(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`HTTP ${response.status}: ${url}`);
    return response.json();
  }

  const cityListUrl = () => `${CFG.urls.cities}?lang=${state.lang}`;
  const countryListUrl = () => `${CFG.urls.countries}?lang=${state.lang}`;
  const cityDetailUrl = (id) =>
    `${CFG.urls.cityDetail.replace(/0\/$/, `${id}/`)}?lang=${state.lang}`;

  const formatNumber = (value) => new Intl.NumberFormat(NUMBER_LOCALE[state.lang]).format(value);

  function formatCoords(lat, lng) {
    const ns = lat >= 0 ? 'N' : 'S';
    const ew = lng >= 0 ? 'E' : 'W';
    return `${Math.abs(lat).toFixed(2)}° ${ns}, ${Math.abs(lng).toFixed(2)}° ${ew}`;
  }

  /** Размер светящейся точки зависит от населения города. */
  function markerSize(population) {
    const p = Math.max(population || 150000, 100000);
    const size = 10 + (Math.log10(p) - 5) * 5.5;
    return Math.round(Math.min(22, Math.max(10, size)));
  }

  /** Угловое расстояние между двумя точками на сфере, в градусах. */
  function angularDistance(lat1, lng1, lat2, lng2) {
    const a = lat1 * RAD;
    const b = lat2 * RAD;
    const cos =
      Math.sin(a) * Math.sin(b) + Math.cos(a) * Math.cos(b) * Math.cos((lng2 - lng1) * RAD);
    return Math.acos(Math.min(1, Math.max(-1, cos))) / RAD;
  }

  /** Приводит текст к виду для поиска: без регистра, диакритики и апострофов. */
  function normalizeText(value) {
    return String(value)
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[ʻʼ’'`]/g, '')
      .replace(/ı/g, 'i')
      .trim();
  }

  /* ------------------------------------------------------------------ *
   *  Локализация интерфейса
   * ------------------------------------------------------------------ */
  function applyTranslations() {
    document.documentElement.lang = HTML_LANG[state.lang];
    document.title = t('pageTitle');
    document.querySelectorAll('[data-i18n]').forEach((node) => {
      node.textContent = t(node.dataset.i18n);
    });
    document.querySelectorAll('[data-i18n-aria]').forEach((node) => {
      node.setAttribute('aria-label', t(node.dataset.i18nAria));
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach((node) => {
      node.setAttribute('placeholder', t(node.dataset.i18nPlaceholder));
    });
    els.langButtons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.lang === state.lang));
    });
    updateTimelinePlay();
  }

  async function setLang(lang) {
    if (!LANGS.includes(lang) || lang === state.lang) return;
    state.lang = lang;
    try {
      window.localStorage.setItem(STORAGE_KEY, lang);
    } catch (err) {
      /* не критично */
    }
    applyTranslations();
    hideToast();

    try {
      await loadCities();
    } catch (err) {
      console.error(err);
      showToast(t('errorLoad'), () => loadCities());
    }
    if (state.timelineOpen) refreshTimeline();
    if (state.selectedId !== null) loadDetail(state.selectedId);
  }

  /* ------------------------------------------------------------------ *
   *  Уведомления и загрузчик
   * ------------------------------------------------------------------ */
  function showToast(message, action) {
    els.toastText.textContent = message;
    toastAction = action || null;
    els.toastRetry.hidden = !action;
    els.toast.dataset.open = 'true';
  }

  function hideToast() {
    els.toast.dataset.open = 'false';
    toastAction = null;
  }

  function maybeHideLoader() {
    if (state.globeReady && state.dataReady) els.loader.dataset.hidden = 'true';
  }

  /* ------------------------------------------------------------------ *
   *  Страны: подсветка и границы
   * ------------------------------------------------------------------ */
  const codeOf = (feature) => feature.properties.code;
  const hasCities = (feature) => state.countryCodes.has(codeOf(feature));
  const isActiveCountry = (feature) =>
    state.activeCountry !== null && codeOf(feature) === state.activeCountry;
  const isHoveredCountry = (feature) =>
    state.hoverCode !== null && codeOf(feature) === state.hoverCode;

  // Издали страны с городами мягко подсвечены, остальные почти не видны —
  // так глобус остаётся чистым. Вблизи границы проявляются сильнее.
  function capColor(feature) {
    if (isActiveCountry(feature)) return 'rgba(255, 191, 102, 0.10)';
    if (!hasCities(feature)) return 'rgba(0, 0, 0, 0.01)';
    if (isHoveredCountry(feature)) return 'rgba(255, 191, 102, 0.24)';
    return state.mode === 'world' ? 'rgba(255, 191, 102, 0.08)' : 'rgba(255, 191, 102, 0.03)';
  }

  function strokeColor(feature) {
    if (isActiveCountry(feature)) return 'rgba(255, 208, 138, 0.85)';
    if (!hasCities(feature)) {
      return state.mode === 'world' ? 'rgba(150, 182, 235, 0.18)' : 'rgba(150, 182, 235, 0.36)';
    }
    if (isHoveredCountry(feature)) return 'rgba(255, 208, 138, 0.8)';
    return state.mode === 'world' ? 'rgba(255, 200, 130, 0.5)' : 'rgba(255, 200, 130, 0.34)';
  }

  function refreshPolygons() {
    if (!globe) return;
    globe.polygonCapColor((feature) => capColor(feature));
    globe.polygonStrokeColor((feature) => strokeColor(feature));
  }

  function setHoverCountry(code) {
    state.hoverCode = code;
    els.globe.style.cursor = code ? 'pointer' : '';
    refreshPolygons();
    updateAutoRotate();
  }

  /** Высота камеры, с которой страна видна целиком: чем больше страна, тем выше. */
  function countryAltitude(code) {
    const feature = state.featureByCode.get(code);
    if (!feature) return CAMERA.focusAltitude;

    const polygons =
      feature.geometry.type === 'MultiPolygon'
        ? feature.geometry.coordinates
        : [feature.geometry.coordinates];

    // Берём самый большой участок суши: острова и заморские территории не должны раздувать охват.
    let best = null;
    polygons.forEach((polygon) => {
      let minLat = 90;
      let maxLat = -90;
      let minLng = 180;
      let maxLng = -180;
      polygon[0].forEach(([lng, lat]) => {
        minLat = Math.min(minLat, lat);
        maxLat = Math.max(maxLat, lat);
        minLng = Math.min(minLng, lng);
        maxLng = Math.max(maxLng, lng);
      });
      const midLat = (minLat + maxLat) / 2;
      const span = Math.max(maxLat - minLat, (maxLng - minLng) * Math.cos(midLat * RAD));
      if (!best || span > best) best = span;
    });

    const altitude = 0.55 + (best || 10) / 38;
    return Math.min(CAMERA.countryMaxAltitude, Math.max(CAMERA.countryMinAltitude, altitude));
  }

  /* ------------------------------------------------------------------ *
   *  Маркеры: подписи стран (издали) и города (вблизи)
   * ------------------------------------------------------------------ */
  function createCountryLabel(country) {
    const el = h('button', 'country-label');
    el.type = 'button';
    el.dataset.code = country.code;
    el.setAttribute('aria-label', country.name);
    el.append(h('span', 'country-label__dot'), h('span', 'country-label__name', country.name));
    el.addEventListener('click', (event) => {
      event.stopPropagation();
      focusCountry(country.code);
    });
    el.addEventListener('pointerdown', (event) => event.stopPropagation());
    el.addEventListener('pointerenter', () => {
      state.hovering = true;
      setHoverCountry(country.code);
    });
    el.addEventListener('pointerleave', () => {
      state.hovering = false;
      setHoverCountry(null);
    });
    return el;
  }

  function createCityMarker(city) {
    const classes = ['city-marker'];
    if (city.is_capital) classes.push('is-capital');
    if (city.id === state.selectedId || city.id === state.tlCityId) classes.push('is-active');

    const el = h('button', classes.join(' '));
    el.type = 'button';
    el.dataset.id = String(city.id);
    el.style.setProperty('--size', `${markerSize(city.population)}px`);
    el.setAttribute('aria-label', `${city.name}, ${city.country}`);
    el.append(
      h('span', 'city-marker__pulse'),
      h('span', 'city-marker__dot'),
      h('span', 'city-marker__label', city.name),
    );
    el.addEventListener('click', (event) => {
      event.stopPropagation();
      selectCity(city.id);
    });
    // Нажатие на маркер не должно начинать вращение глобуса.
    el.addEventListener('pointerdown', (event) => event.stopPropagation());
    // Пока курсор над маркером, глобус не вращается — в него легко попасть.
    el.addEventListener('pointerenter', () => {
      state.hovering = true;
      updateAutoRotate();
    });
    el.addEventListener('pointerleave', () => {
      state.hovering = false;
      updateAutoRotate(300);
    });
    return el;
  }

  const createMarker = (item) =>
    item.kind === 'country' ? createCountryLabel(item) : createCityMarker(item);

  /**
   * Расставляет подписи стран так, чтобы они не наезжали друг на друга:
   * сначала страны с большим числом городов, остальные ждут приближения.
   */
  function layoutCountryLabels(pov) {
    const horizon = Math.acos(1 / (1 + pov.altitude)) / RAD;
    const placed = [];
    const result = [];

    [...state.countries]
      .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name))
      .forEach((country) => {
        const distance = angularDistance(pov.lat, pov.lng, country.latitude, country.longitude);
        if (distance > horizon - 6) return; // обратная сторона планеты и край диска

        const point = globe.getScreenCoords(country.latitude, country.longitude);
        if (!point) return;

        const width = country.name.length * 8.6 + 26;
        const box = { x1: point.x - 8, x2: point.x - 8 + width, y1: point.y - 11, y2: point.y + 11 };
        const overlaps = placed.some(
          (other) =>
            box.x1 < other.x2 + 8 && box.x2 + 8 > other.x1 && box.y1 < other.y2 && box.y2 > other.y1,
        );
        if (overlaps) return;

        placed.push(box);
        result.push(country);
      });
    return result;
  }

  /**
   * Какие города показывать в режиме «вблизи»: все города выбранной страны,
   * выбранный город и ближайшие к центру экрана — без наложения подписей.
   */
  function layoutCities(pov) {
    // Если выбрана страна, показываем только её города — соседние не отвлекают.
    if (state.focusCountry !== null) {
      return state.cities.filter(
        (city) =>
          city.country_code === state.focusCountry ||
          city.id === state.selectedId ||
          city.id === state.tlCityId,
      );
    }

    const radius = Math.min(30, Math.max(10, pov.altitude * 15));
    const forced = (city) => city.id === state.selectedId || city.id === state.tlCityId;

    const candidates = state.cities
      .filter(
        (city) =>
          forced(city) ||
          angularDistance(pov.lat, pov.lng, city.latitude, city.longitude) < radius,
      )
      // Сначала обязательные, затем столицы и самые большие города.
      .sort(
        (a, b) =>
          Number(forced(b)) - Number(forced(a)) ||
          Number(b.is_capital) - Number(a.is_capital) ||
          (b.population || 0) - (a.population || 0),
      );

    const placed = [];
    return candidates.filter((city) => {
      if (forced(city)) return true;
      const point = globe.getScreenCoords(city.latitude, city.longitude);
      if (!point) return false;
      const box = {
        x1: point.x - 8,
        x2: point.x + 22 + city.name.length * 7.5,
        y1: point.y - 10,
        y2: point.y + 10,
      };
      const overlaps = placed.some(
        (other) => box.x1 < other.x2 && box.x2 > other.x1 && box.y1 < other.y2 && box.y2 > other.y1,
      );
      if (overlaps) return false;
      placed.push(box);
      return true;
    });
  }

  function renderMarkers(force = false) {
    if (!globe) return;
    const pov = globe.pointOfView();
    const items = state.mode === 'world' ? layoutCountryLabels(pov) : layoutCities(pov);
    const key = `${state.mode}:${items.map((item) => item.code || item.id).join(',')}`;
    if (!force && key === state.markersKey) return;
    state.markersKey = key;
    // Старые элементы удаляются без события pointerleave — сбрасываем наведение вручную.
    if (state.hovering) {
      state.hovering = false;
      setHoverCountry(null);
    }
    globe.htmlElementsData(items);
  }

  function markActive() {
    document.querySelectorAll('.city-marker').forEach((marker) => {
      const id = Number(marker.dataset.id);
      marker.classList.toggle('is-active', id === state.selectedId || id === state.tlCityId);
    });
  }

  /* ------------------------------------------------------------------ *
   *  Режим камеры
   * ------------------------------------------------------------------ */
  function syncMode(force = false) {
    if (!globe) return;
    const { altitude } = globe.pointOfView();
    const wasNear = state.mode === 'near';
    const isNear = wasNear ? altitude < CAMERA.citiesTo : altitude < CAMERA.citiesFrom;
    const changed = isNear !== wasNear;
    state.mode = isNear ? 'near' : 'world';

    if (isNear && state.focusCountry) state.focusReached = true;

    // Пользователь сам отдалил камеру от страны — возвращаемся к виду «мир».
    if (!isNear && state.focusCountry && state.focusReached && state.selectedId === null) {
      clearCountryFocus({ fly: false });
    }

    if (changed) {
      refreshPolygons();
      updateAutoRotate(900);
    }
    renderMarkers(force || changed);
  }

  function onCameraChange() {
    if (cameraFrame) return;
    cameraFrame = requestAnimationFrame(() => {
      cameraFrame = 0;
      syncMode();
    });
  }

  function updateAutoRotate(delay = 0) {
    if (!globe) return;
    clearTimeout(autoRotateTimer);
    const allowed =
      !REDUCED_MOTION &&
      state.mode === 'world' &&
      state.focusCountry === null &&
      state.selectedId === null &&
      state.hoverCode === null &&
      !state.hovering &&
      !state.searchOpen &&
      !state.timelineOpen;

    if (!allowed) {
      globe.controls().autoRotate = false;
    } else if (delay > 0) {
      globe.controls().autoRotate = false;
      autoRotateTimer = setTimeout(() => updateAutoRotate(), delay);
    } else {
      globe.controls().autoRotate = true;
    }
  }

  function updateCountryBar() {
    const country = state.focusCountry ? state.countryByCode.get(state.focusCountry) : null;
    if (country) {
      els.countryName.textContent = country.name;
      els.countryCount.textContent = `${t('citiesNav')}: ${country.count}`;
      els.countryBar.dataset.open = 'true';
      state.hintDismissed = true;
    } else {
      els.countryBar.dataset.open = 'false';
    }
    els.hint.dataset.hidden = String(state.hintDismissed);
  }

  function flyToCountry(country) {
    globe.pointOfView(
      {
        lat: country.latitude,
        lng: country.longitude,
        altitude: countryAltitude(country.code),
      },
      CAMERA.focusMs,
    );
  }

  /** Клик по стране: камера подлетает, появляются её города. */
  function focusCountry(code) {
    const country = state.countryByCode.get(code);
    if (!country) return;
    if (state.focusCountry === code && state.selectedId === null) return;

    closeSearch();
    if (state.selectedId !== null) closePanel({ fly: false });

    state.focusCountry = code;
    state.activeCountry = code;
    state.focusReached = false;
    state.hoverCode = null;
    els.globe.style.cursor = '';

    updateAutoRotate();
    updateCountryBar();
    refreshPolygons();
    flyToCountry(country);
    syncMode(true);
  }

  /** Кнопка «Весь мир» (или отдаление камеры): снова видны только страны. */
  function clearCountryFocus({ fly = true } = {}) {
    if (state.selectedId !== null) closePanel({ fly: false });
    state.focusCountry = null;
    state.activeCountry = null;
    state.focusReached = false;

    updateCountryBar();
    refreshPolygons();
    if (fly) {
      globe.pointOfView({ altitude: CAMERA.releaseAltitude }, CAMERA.releaseMs);
      updateAutoRotate(CAMERA.releaseMs + 200);
    } else {
      updateAutoRotate(900);
    }
  }

  function focusOn(city) {
    clearTimeout(autoRotateTimer);
    globe.controls().autoRotate = false;
    const altitude = Math.min(globe.pointOfView().altitude, CAMERA.focusAltitude);
    globe.pointOfView({ lat: city.latitude, lng: city.longitude, altitude }, CAMERA.focusMs);
  }

  /* ------------------------------------------------------------------ *
   *  Глобус
   * ------------------------------------------------------------------ */
  function initGlobe() {
    const instance = Globe()(els.globe)
      .backgroundColor('#04070f')
      .backgroundImageUrl(CFG.textures.sky)
      .globeImageUrl(CFG.textures.earth)
      .showAtmosphere(true)
      .atmosphereColor('#6f9be0')
      .atmosphereAltitude(0.22)
      // Страны: полупрозрачная заливка и границы; цвета зависят от режима камеры
      .polygonAltitude(0.004)
      .polygonCapColor((feature) => capColor(feature))
      .polygonSideColor(() => 'rgba(0, 0, 0, 0)')
      .polygonStrokeColor((feature) => strokeColor(feature))
      .polygonsTransitionDuration(0)
      .onPolygonHover((feature) => {
        const code = feature && hasCities(feature) ? codeOf(feature) : null;
        if (code !== state.hoverCode) setHoverCountry(code);
      })
      .onPolygonClick((feature) => {
        if (feature && hasCities(feature)) focusCountry(codeOf(feature));
      })
      // Подписи стран и города: HTML-слой (поддерживает кириллицу и латиницу)
      .htmlLat('latitude')
      .htmlLng('longitude')
      .htmlAltitude(0.012)
      .htmlTransitionDuration(0)
      .htmlElement(createMarker)
      .onGlobeReady(() => {
        state.globeReady = true;
        maybeHideLoader();
      });

    // Скрываем маркеры на обратной стороне планеты.
    if (typeof instance.htmlElementVisibilityModifier === 'function') {
      instance.htmlElementVisibilityModifier((el, isVisible) => {
        el.style.opacity = isVisible ? '1' : '0';
        el.style.pointerEvents = isVisible ? 'auto' : 'none';
      });
    }

    // Поверхность: тёмные материки, приглушённый холодный океан.
    const material = instance.globeMaterial();
    material.color.set('#a9bde3');
    material.emissive.set('#050b18');

    instance.renderer().setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    const controls = instance.controls();
    controls.autoRotate = !REDUCED_MOTION;
    controls.autoRotateSpeed = 0.35;
    controls.enablePan = false;
    controls.minDistance = 150;
    controls.maxDistance = 430;
    controls.addEventListener('change', onCameraChange);

    if (typeof instance.onZoom === 'function') instance.onZoom(onCameraChange);

    instance.pointOfView(CAMERA.overview);

    // Размер холста следует за контейнером (он сжимается, когда открыта панель).
    const resize = () => {
      const { clientWidth, clientHeight } = els.globe;
      if (clientWidth > 0 && clientHeight > 0) {
        instance.width(clientWidth).height(clientHeight);
        onCameraChange();
      }
    };
    new ResizeObserver(resize).observe(els.globe);
    resize();

    return instance;
  }

  async function loadGeometry() {
    const geo = await getJSON(CFG.urls.countriesGeoJson);
    geo.features.forEach((feature) => state.featureByCode.set(codeOf(feature), feature));
    globe.polygonsData(geo.features);
  }

  /** Собирает список стран, в которых есть города: название, центр и число городов. */
  function buildCountries(cities, apiCountries) {
    const centers = new Map(apiCountries.map((item) => [item.code, item]));
    const groups = new Map();
    cities.forEach((city) => {
      if (!groups.has(city.country_code)) groups.set(city.country_code, []);
      groups.get(city.country_code).push(city);
    });

    return Array.from(groups, ([code, list]) => {
      const api = centers.get(code);
      const mean = (key) => list.reduce((sum, city) => sum + city[key], 0) / list.length;
      return {
        kind: 'country',
        code,
        name: (api && api.name) || list[0].country,
        latitude: api ? api.latitude : mean('latitude'),
        longitude: api ? api.longitude : mean('longitude'),
        count: list.length,
      };
    });
  }

  async function loadCities() {
    const [cities, apiCountries] = await Promise.all([
      getJSON(cityListUrl()),
      // Центры стран нужны только для подписей: при ошибке обойдёмся координатами городов.
      getJSON(countryListUrl()).catch(() => []),
    ]);
    state.cities = cities;
    state.countries = buildCountries(cities, apiCountries);
    state.countryByCode = new Map(state.countries.map((country) => [country.code, country]));
    state.countryCodes = new Set(state.countryByCode.keys());

    state.markersKey = '';
    refreshPolygons();
    syncMode(true);
    updateCountryBar();
    renderSearch();
  }

  /* ------------------------------------------------------------------ *
   *  Лента времени: события из историй городов по годам
   * ------------------------------------------------------------------ */
  async function fetchTimeline() {
    const lang = state.lang;
    let events = state.timelineByLang.get(lang);
    if (!events) {
      events = await getJSON(`${CFG.urls.timeline}?lang=${lang}`);
      state.timelineByLang.set(lang, events);
    }
    return { lang, events };
  }

  function updateTimelinePlay() {
    const label = t(state.tlPlaying ? 'timelinePause' : 'timelinePlay');
    els.tlPlay.dataset.playing = String(state.tlPlaying);
    els.tlPlay.setAttribute('aria-label', label);
    els.tlPlay.title = label;
  }

  function setTimelineEvents(events) {
    state.tlEvents = events;
    els.tlRange.max = String(Math.max(0, events.length - 1));
  }

  function showTimelineEvent(index, { fly = true } = {}) {
    const events = state.tlEvents;
    if (!events.length) {
      els.tlText.textContent = t('searchEmpty');
      return;
    }
    const i = Math.max(0, Math.min(events.length - 1, index));
    const event = events[i];
    state.tlIndex = i;
    state.tlCityId = event.city_id;

    els.tlYear.textContent = event.label;
    els.tlPlace.textContent = `${event.city}, ${event.country}`;
    els.tlText.textContent = event.text;
    els.tlRange.value = String(i);
    els.tlCount.textContent = `${i + 1} / ${events.length}`;
    els.tlPrev.disabled = i === 0;
    els.tlNext.disabled = i === events.length - 1;
    markActive();

    if (!fly) return;
    // Небольшая задержка, чтобы при перетаскивании ползунка камера не дёргалась на каждом шаге.
    clearTimeout(tlFlyTimer);
    tlFlyTimer = setTimeout(() => {
      const city = state.cities.find((item) => item.id === event.city_id);
      if (!city || !state.timelineOpen) return;
      focusOn(city);
      renderMarkers();
    }, 120);
  }

  function stopTimelinePlay() {
    clearTimeout(tlPlayTimer);
    if (!state.tlPlaying) return;
    state.tlPlaying = false;
    updateTimelinePlay();
  }

  function scheduleTimelineStep() {
    clearTimeout(tlPlayTimer);
    if (!state.tlPlaying) return;
    const current = state.tlEvents[state.tlIndex];
    // Чем длиннее текст, тем дольше он остаётся на экране.
    const delay = Math.min(9000, 4200 + (current ? current.text.length : 0) * 18);
    tlPlayTimer = setTimeout(() => {
      if (!state.tlPlaying) return;
      if (state.tlIndex >= state.tlEvents.length - 1) {
        stopTimelinePlay();
        return;
      }
      showTimelineEvent(state.tlIndex + 1);
      scheduleTimelineStep();
    }, delay);
  }

  function toggleTimelinePlay() {
    if (state.tlPlaying) {
      stopTimelinePlay();
      return;
    }
    if (!state.tlEvents.length) return;
    if (state.tlIndex >= state.tlEvents.length - 1) showTimelineEvent(0);
    state.tlPlaying = true;
    updateTimelinePlay();
    scheduleTimelineStep();
  }

  async function openTimeline() {
    if (state.timelineOpen) return;
    closeSearch();
    if (state.selectedId !== null) closePanel({ fly: false });
    if (state.focusCountry !== null) clearCountryFocus({ fly: false });

    state.timelineOpen = true;
    els.timeline.dataset.open = 'true';
    els.timelineToggle.setAttribute('aria-expanded', 'true');
    updateAutoRotate();

    try {
      const { events } = await fetchTimeline();
      if (!state.timelineOpen) return;
      setTimelineEvents(events);
    } catch (err) {
      console.error(err);
      closeTimeline({ restoreCamera: false });
      showToast(t('errorTimeline'), () => openTimeline());
      return;
    }
    showTimelineEvent(state.tlIndex);
    els.tlPlay.focus({ preventScroll: true });
  }

  function closeTimeline({ restoreCamera = true } = {}) {
    if (!state.timelineOpen) return;
    stopTimelinePlay();
    clearTimeout(tlFlyTimer);
    state.timelineOpen = false;
    state.tlCityId = null;
    els.timeline.dataset.open = 'false';
    els.timelineToggle.setAttribute('aria-expanded', 'false');
    markActive();
    renderMarkers();

    if (restoreCamera && state.selectedId === null && state.focusCountry === null) {
      globe.pointOfView({ altitude: CAMERA.releaseAltitude }, CAMERA.releaseMs);
      updateAutoRotate(CAMERA.releaseMs + 200);
    } else {
      updateAutoRotate(300);
    }
    if (restoreCamera) els.timelineToggle.focus({ preventScroll: true });
  }

  /** Смена языка при открытой ленте: подписи обновляются, камера остаётся на месте. */
  async function refreshTimeline() {
    try {
      const { lang, events } = await fetchTimeline();
      if (!state.timelineOpen || lang !== state.lang) return;
      setTimelineEvents(events);
      showTimelineEvent(state.tlIndex, { fly: false });
    } catch (err) {
      console.error(err);
      showToast(t('errorTimeline'), () => refreshTimeline());
    }
  }

  /* ------------------------------------------------------------------ *
   *  Поиск городов и стран (кнопка в углу)
   * ------------------------------------------------------------------ */
  function openSearch() {
    if (state.searchOpen) return;
    state.searchOpen = true;
    els.search.dataset.open = 'true';
    els.searchToggle.setAttribute('aria-expanded', 'true');
    updateAutoRotate();
    renderSearch();
    els.searchInput.focus({ preventScroll: true });
  }

  function closeSearch({ restoreFocus = false } = {}) {
    if (!state.searchOpen) return;
    state.searchOpen = false;
    els.search.dataset.open = 'false';
    els.searchToggle.setAttribute('aria-expanded', 'false');
    els.searchInput.value = '';
    updateAutoRotate(300);
    if (restoreFocus) els.searchToggle.focus({ preventScroll: true });
  }

  function searchItem(kind, title, sub, onPick) {
    const button = h('button', 'search__item', null, { type: 'button' });
    button.append(
      h('span', `search__item-icon ${kind === 'country' ? 'is-country' : ''}`),
      h('span', 'search__item-main', title),
      h('span', 'search__item-sub', sub),
    );
    button.addEventListener('click', onPick);
    return button;
  }

  function renderSearch() {
    const query = normalizeText(els.searchInput.value);
    const collator = new Intl.Collator(NUMBER_LOCALE[state.lang]);
    const matches = (name) => !query || normalizeText(name).includes(query);
    // Совпадения с начала названия — выше, дальше по алфавиту.
    const rank = (name) => (normalizeText(name).startsWith(query) ? 0 : 1);
    const order = (a, b) => rank(a.name) - rank(b.name) || collator.compare(a.name, b.name);

    const countries = state.countries.filter((country) => matches(country.name)).sort(order);
    const cities = state.cities.filter((city) => matches(city.name)).sort(order);

    const fragment = document.createDocumentFragment();
    if (countries.length) {
      fragment.append(h('p', 'search__heading', t('searchCountries')));
      countries.forEach((country) =>
        fragment.append(
          searchItem('country', country.name, `${t('citiesNav')}: ${country.count}`, () =>
            focusCountry(country.code),
          ),
        ),
      );
    }
    if (cities.length) {
      fragment.append(h('p', 'search__heading', t('searchCities')));
      cities.forEach((city) =>
        fragment.append(searchItem('city', city.name, city.country, () => selectCity(city.id))),
      );
    }
    if (!countries.length && !cities.length) {
      fragment.append(h('p', 'search__empty', t('searchEmpty')));
    }
    els.searchResults.replaceChildren(fragment);
    els.searchResults.scrollTop = 0;
  }

  function onSearchKeydown(event) {
    const items = Array.from(els.searchResults.querySelectorAll('.search__item'));
    const index = items.indexOf(document.activeElement);

    if (event.key === 'ArrowDown') {
      event.preventDefault();
      if (items.length) items[Math.min(index + 1, items.length - 1)].focus();
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      if (index > 0) items[index - 1].focus();
      else els.searchInput.focus();
    } else if (event.key === 'Enter' && document.activeElement === els.searchInput) {
      event.preventDefault();
      if (items.length) items[0].click();
    }
  }

  /* ------------------------------------------------------------------ *
   *  Боковая панель
   * ------------------------------------------------------------------ */
  function openPanel() {
    document.body.classList.add('panel-open');
    els.panel.setAttribute('aria-hidden', 'false');
    els.panel.removeAttribute('inert');
  }

  /** Закрывает панель города; камера возвращается к виду на страну. */
  function closePanel({ fly = true } = {}) {
    if (state.selectedId === null) return;
    state.selectedId = null;
    state.detailToken += 1;

    document.body.classList.remove('panel-open');
    els.panel.setAttribute('aria-hidden', 'true');
    els.panel.setAttribute('inert', '');

    markActive();
    updateAutoRotate();

    const country = state.focusCountry ? state.countryByCode.get(state.focusCountry) : null;
    if (fly && country) {
      state.focusReached = false;
      flyToCountry(country);
    }
    if (fly) els.searchToggle.focus({ preventScroll: true });
  }

  async function selectCity(id) {
    const city = state.cities.find((item) => item.id === id);
    if (!city) return;

    closeSearch();
    closeTimeline({ restoreCamera: false });
    state.selectedId = id;
    state.focusCountry = city.country_code;
    state.activeCountry = city.country_code;
    state.focusReached = true;
    state.hoverCode = null;
    els.globe.style.cursor = '';

    openPanel();
    updateAutoRotate();
    updateCountryBar();
    refreshPolygons();
    focusOn(city);
    syncMode(true);
    renderSkeleton(city);
    els.close.focus({ preventScroll: true });

    await loadDetail(id);
  }

  async function loadDetail(id) {
    state.detailToken += 1;
    const token = state.detailToken;
    const cacheKey = `${state.lang}:${id}`;

    try {
      let detail = state.detailCache.get(cacheKey);
      if (!detail) {
        detail = await getJSON(cityDetailUrl(id));
        state.detailCache.set(cacheKey, detail);
      }
      // Пока шёл запрос, пользователь мог выбрать другой город или сменить язык.
      if (token !== state.detailToken || state.selectedId !== id) return;
      renderDetail(detail);
    } catch (err) {
      console.error(err);
      if (token !== state.detailToken || state.selectedId !== id) return;
      renderDetailError(id);
    }
  }

  /* ---------- Отрисовка содержимого панели ---------- */
  function fact(label, value) {
    const box = h('div');
    box.append(h('dt', 'text-slate-500', label), h('dd', 'mt-0.5 tabular-nums text-slate-100', value));
    return box;
  }

  function panelHeader(data) {
    const head = h('header', 'pr-10');

    const top = h('div', 'flex flex-wrap items-center gap-x-3 gap-y-2');
    top.append(h('p', 'text-sm text-slate-400', data.country));
    if (data.is_capital) {
      top.append(
        h(
          'span',
          'rounded-full border border-lamp-400/40 px-2.5 py-0.5 text-xs text-lamp-300',
          t('capital'),
        ),
      );
    }

    const title = h(
      'h2',
      'mt-2 font-serif text-4xl font-light leading-[1.05] tracking-tight text-white sm:text-[2.6rem]',
      data.name,
      { id: 'panel-title' },
    );

    const facts = h('dl', 'mt-5 flex flex-wrap gap-x-8 gap-y-3 text-sm');
    if (data.population) facts.append(fact(t('population'), `≈ ${formatNumber(data.population)}`));
    facts.append(fact(t('coordinates'), formatCoords(data.latitude, data.longitude)));

    head.append(top, title, facts);
    return head;
  }

  function section(title, body) {
    const wrapper = h('section', 'mt-9');
    body.classList.add('mt-4');
    wrapper.append(
      h('h3', 'border-b border-white/10 pb-2 font-serif text-lg text-white', title),
      body,
    );
    return wrapper;
  }

  function timeline(items) {
    const list = h('ol', 'relative ml-1.5 border-l border-white/10');
    items.forEach((item) => {
      const row = h('li', 'relative pb-5 pl-6 last:pb-0');
      row.append(
        h(
          'span',
          'absolute -left-[5px] top-[7px] h-[9px] w-[9px] rounded-full bg-lamp-400 shadow-[0_0_0_3px_#070c17,0_0_12px_2px_rgba(255,179,92,0.65)]',
        ),
      );
      if (item.label) {
        row.append(h('p', 'font-serif text-[15px] font-medium tabular-nums text-lamp-300', item.label));
      }
      row.append(h('p', 'mt-1 text-sm leading-6 text-slate-300', item.text));
      list.append(row);
    });
    return list;
  }

  function companies(items) {
    const list = h('ul', 'divide-y divide-white/[0.07]');
    items.forEach((item) => {
      const row = h('li', 'py-3.5 first:pt-0 last:pb-0');
      if (item.label) row.append(h('h4', 'text-[15px] font-semibold text-white', item.label));
      row.append(h('p', 'mt-1 text-sm leading-6 text-slate-400', item.text));
      list.append(row);
    });
    return list;
  }

  function renderDetail(data) {
    const fragment = document.createDocumentFragment();
    fragment.append(panelHeader(data));

    if (data.description) {
      fragment.append(
        section(
          t('sectionDescription'),
          h('p', 'font-serif text-[15px] leading-7 text-slate-300', data.description),
        ),
      );
    }
    if (data.history && data.history.length) {
      fragment.append(section(t('sectionHistory'), timeline(data.history)));
    }
    if (data.industry && data.industry.length) {
      fragment.append(section(t('sectionIndustry'), companies(data.industry)));
    }

    els.content.replaceChildren(fragment);
    els.content.scrollTop = 0;
  }

  function renderSkeleton(city) {
    const bar = (width) => h('div', `h-3 animate-pulse rounded bg-white/[0.07] ${width}`);
    const block = (rows) => {
      const box = h('div', 'mt-4 space-y-3');
      rows.forEach((width) => box.append(bar(width)));
      return box;
    };

    const fragment = document.createDocumentFragment();
    fragment.append(panelHeader(city));
    [t('sectionDescription'), t('sectionHistory'), t('sectionIndustry')].forEach((title) => {
      const wrapper = h('section', 'mt-9');
      wrapper.append(
        h('h3', 'border-b border-white/10 pb-2 font-serif text-lg text-white', title),
        block(['w-full', 'w-11/12', 'w-4/5']),
      );
      fragment.append(wrapper);
    });

    els.content.replaceChildren(fragment);
    els.content.scrollTop = 0;
  }

  function renderDetailError(id) {
    const box = h('div', 'mt-9 rounded-xl border border-white/10 bg-white/[0.03] p-4 text-sm text-slate-300');
    box.append(h('p', '', t('errorDetail')));
    const retry = h(
      'button',
      'mt-3 rounded-full border border-lamp-400/50 px-3 py-1 text-lamp-300 transition-colors hover:bg-lamp-400/10',
      t('retry'),
      { type: 'button' },
    );
    retry.addEventListener('click', () => loadDetail(id));
    box.append(retry);
    // Убираем «скелетон», оставляя заголовок города.
    els.content.querySelectorAll('section').forEach((node) => node.remove());
    els.content.append(box);
  }

  /* ------------------------------------------------------------------ *
   *  События интерфейса
   * ------------------------------------------------------------------ */
  function bindUI() {
    els.langButtons.forEach((button) => {
      button.addEventListener('click', () => setLang(button.dataset.lang));
    });
    els.close.addEventListener('click', () => closePanel());
    els.countryBack.addEventListener('click', () => clearCountryFocus());
    els.timelineToggle.addEventListener('click', () => {
      if (state.timelineOpen) closeTimeline();
      else openTimeline();
    });
    els.tlClose.addEventListener('click', () => closeTimeline());
    els.tlPlay.addEventListener('click', toggleTimelinePlay);
    els.tlPrev.addEventListener('click', () => {
      stopTimelinePlay();
      showTimelineEvent(state.tlIndex - 1);
    });
    els.tlNext.addEventListener('click', () => {
      stopTimelinePlay();
      showTimelineEvent(state.tlIndex + 1);
    });
    els.tlRange.addEventListener('input', () => {
      stopTimelinePlay();
      showTimelineEvent(Number(els.tlRange.value));
    });
    els.tlOpen.addEventListener('click', () => {
      const event = state.tlEvents[state.tlIndex];
      if (event) selectCity(event.city_id);
    });
    els.toastRetry.addEventListener('click', () => {
      const action = toastAction;
      hideToast();
      if (action) action();
    });

    els.searchToggle.addEventListener('click', () => {
      if (state.searchOpen) closeSearch();
      else openSearch();
    });
    els.searchInput.addEventListener('input', renderSearch);
    els.search.addEventListener('keydown', onSearchKeydown);
    // Клик мимо окна поиска закрывает его.
    document.addEventListener('pointerdown', (event) => {
      if (state.searchOpen && !els.search.contains(event.target)) closeSearch();
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        if (state.searchOpen) closeSearch({ restoreFocus: true });
        else if (state.timelineOpen) closeTimeline();
        else if (state.selectedId !== null) closePanel();
        else if (state.focusCountry !== null) clearCountryFocus();
      } else if (
        event.key === '/' &&
        !state.searchOpen &&
        !/^(input|textarea|select)$/i.test(document.activeElement.tagName)
      ) {
        event.preventDefault();
        openSearch();
      }
    });
  }

  /* ------------------------------------------------------------------ *
   *  Запуск
   * ------------------------------------------------------------------ */
  async function boot() {
    applyTranslations();
    bindUI();

    if (typeof window.Globe !== 'function') {
      els.loader.dataset.hidden = 'true';
      showToast(t('errorGlobe'), () => window.location.reload());
      return;
    }

    globe = initGlobe();

    // Страховка: onZoom не всегда срабатывает во время программного перелёта камеры.
    setInterval(() => syncMode(), 400);

    const [cities] = await Promise.allSettled([loadCities(), loadGeometry()]);
    if (cities.status === 'rejected') {
      console.error(cities.reason);
      showToast(t('errorLoad'), () => loadCities());
    }
    refreshPolygons();
    state.dataReady = true;
    maybeHideLoader();

    // Если текстура Земли не загрузилась (нет сети до CDN), всё равно показываем сцену.
    setTimeout(() => {
      state.globeReady = true;
      maybeHideLoader();
    }, 10000);
  }

  boot();
})();
