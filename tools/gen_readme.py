#!/usr/bin/env python3
"""Generate README.md from data/repos.json (grouped index of board code repos)."""
import json, datetime, html, os

CAT_TITLES = {
    "frameworks-cores": ("Frameworks & Cores", "Фреймворки та ядра"),
    "displays-ui": ("Displays, LED & UI", "Дисплеї, світлодіоди та інтерфейси"),
    "sensors": ("Sensors & Cameras", "Сенсори та камери"),
    "connectivity": ("Connectivity (WiFi/BLE/LoRa/Zigbee/CAN)", "Зв'язок"),
    "iot-home-automation": ("IoT & Home Automation", "IoT та розумний дім"),
    "audio": ("Audio & Sound", "Аудіо та звук"),
    "robotics-motors": ("Robotics, Motors, CNC & 3D Printers", "Робототехніка, мотори, ЧПУ"),
    "power-storage": ("Power, Sleep & Storage", "Живлення, сон та зберігання"),
    "security-crypto": ("Security, Crypto & OTA", "Безпека, криптографія та OTA"),
    "games-graphics": ("Games & Graphics", "Ігри та графіка"),
    "weather-environment": ("Weather & Environment", "Погода та довкілля"),
    "awesome-collections": ("Meta Collections (Awesome lists)", "Мета-збірки (Awesome-списки)"),
    "other-platforms": ("Other Boards (Pico, STM32, micro:bit, nRF52...)", "Інші плати"),
}

CAT_ORDER = list(CAT_TITLES.keys())

def anchor(s):
    return s.lower().replace(" ", "-").replace("/", "").replace("&", "").replace(",", "").replace("(", "").replace(")", "").replace(".", "").replace("'", "").replace("...", "").replace("--", "-")

def fmt_num(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

def main():
    with open("data/repos.json", encoding="utf-8") as f:
        data = json.load(f)

    total = sum(len(v) for v in data.values())
    today = datetime.date.today().isoformat()

    lines = []
    a = lines.append
    a("# 🗺️ Plates Code Archive / Карта коду для плат")
    a("")
    a(f"**A curated, functionality-organized map of open-source code for microcontroller boards** — Arduino, ESP32, ESP8266, RP2040, STM32, micro:bit and more. One place to find the right repo instead of searching GitHub every time. ({total} repos, last refreshed {today})")
    a("")
    a("> **Українською:** кураторська карта відкритого коду для мікроконтролерних плат, зібрана за функціональністю. Кожен пункт — посилання на оригінальний репозиторій GitHub. Індекс оновлюється автоматично через офіційний GitHub Search API (див. [`tools/collect.py`](tools/collect.py)).")
    a("")
    a("> ⚠️ All links point to the **original repositories** — nothing is copied. Each repo keeps its own license. / Усі посилання ведуть на оригінальні репозиторії — нічого не копіюється, ліцензії зберігаються у авторів.")
    a("")
    a("---")
    a("")
    a("## 📑 Table of Contents")
    a("")
    for cat in CAT_ORDER:
        repos = data.get(cat, [])
        if not repos:
            continue
        en, _ = CAT_TITLES[cat]
        a(f'- [`{en}`](#cat-{cat}) — {len(repos)} repos')
    a("")
    a("---")
    a("")

    for cat in CAT_ORDER:
        repos = data.get(cat, [])
        if not repos:
            continue
        en, uk = CAT_TITLES[cat]
        a(f'<a id="cat-{cat}"></a>')
        a(f"## {en}")
        a(f"**{uk}**")
        a("")
        a("| Repository | ⭐ | Lang | Board | Description |")
        a("|---|---|---|---|---|")
        for r in repos:
            desc = html.escape((r["desc"] or "").replace("|", "/")) or "—"
            lang = r["lang"] or "—"
            plat = r.get("platform", "")
            a(f'| [{r["full_name"]}]({r["url"]}) | {fmt_num(r["stars"])} | {lang} | {plat} | {desc} |')
        a("")

    a("---")
    a("")
    a("## 🤝 Contributing")
    a("")
    a("Found a great repo that's missing? Open an issue or PR with: repo URL, target category, and one-line description. Quality bar: active (non-archived), ≥40 stars, real code (not just docs).")
    a("")
    a("## 🔁 How the index is built")
    a("")
    a("- Data collected automatically via the official **GitHub Search API** (`tools/collect.py`, results in `data/repos.json`).")
    a(f"- Filters: stars ≥ 40, not archived, deduplicated across categories. Snapshot date: **{today}**.")
    a("- Categories are grouped **by functionality** (display, sensors, connectivity, IoT, audio, robotics...) so you search by what you want to build, not by board name.")
    a("")
    a("## 📄 License")
    a("")
    a("This index: MIT. The linked projects keep their own licenses — check each repo before reuse.")

    os.makedirs("out", exist_ok=True)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"README.md written: {total} repos across {sum(1 for v in data.values() if v)} categories")

if __name__ == "__main__":
    main()
