#!/usr/bin/env python3
"""Collect top GitHub repos for embedded/board code, grouped by functionality.
Uses `gh api search/repositories` (official free GitHub API). Writes data/repos.json.
"""
import json, subprocess, time, sys, os

# category -> list of (query, platform_hint)
CATEGORIES = {
    "frameworks-cores": [
        ("arduino+framework", "Arduino"), ("esp-idf", "ESP32/ESP8266"),
        ("platformio", "Cross-platform"), ("micropython", "Cross-platform"),
        ("circuitpython", "Cross-platform"), ("rust+embedded+no-std", "Rust/embedded"),
        ("topic:embedded-hal", "Rust/embedded"), ("tinygo", "Cross-platform"),
    ],
    "displays-ui": [
        ("topic:lvgl", "Cross-platform"), ("tft+esp32+display", "ESP32"),
        ("oled+ssd1306+arduino", "Arduino"), ("epaper+e-ink+arduino", "Arduino"),
        ("touchscreen+esp32", "ESP32"), ("topic:display+topic:esp8266", "ESP8266"),
        ("ili9341", "Cross-platform"), ("ws2812+led+strip", "Arduino"),
    ],
    "sensors": [
        ("topic:sensors+topic:esp32", "ESP32"), ("bme280+arduino", "Arduino"),
        ("topic:temperature-sensor", "Cross-platform"), ("imu+mpu6050+arduino", "Arduino"),
        ("camera+esp32-cam", "ESP32"), ("gps+arduino+library", "Arduino"),
        ("topic:air-quality+esp32", "ESP32"), ("rfid+rc522+arduino", "Arduino"),
    ],
    "connectivity": [
        ("esp-now+esp32", "ESP32"), ("lora+esp32", "ESP32"),
        ("zigbee+esp32", "ESP32"), ("topic:bluetooth+esp32", "ESP32"),
        ("nrf24l01+arduino", "Arduino"), ("wifi+manager+esp8266", "ESP8266"),
        ("can+bus+esp32", "ESP32"), ("gsm+sim800+arduino", "Arduino"),
    ],
    "iot-home-automation": [
        ("esphome", "ESP"), ("tasmota", "ESP"),
        ("topic:mqtt+topic:esp32", "ESP32"), ("home-assistant+esp32", "ESP32"),
        ("topic:home-automation+topic:esp8266", "ESP8266"), ("wled", "ESP8266/ESP32"),
        ("shelly+esp", "ESP"), ("matter+esp32", "ESP32"),
    ],
    "audio": [
        ("esp32+audio", "ESP32"), ("esp32+i2s", "ESP32"),
        ("arduino+mp3+player", "Arduino"), ("esp32+web+radio", "ESP32"),
        ("dsp+embedded+audio", "Cross-platform"),
    ],
    "robotics-motors": [
        ("arduino+robot", "Arduino"), ("esp32+robot", "ESP32"),
        ("stepper+motor+arduino", "Arduino"), ("servo+esp32", "ESP32"),
        ("grbl+cnc", "Arduino"), ("marlin+firmware", "3D printers"),
        ("klipper", "3D printers"), ("drone+esp32", "ESP32"),
    ],
    "power-storage": [
        ("esp32+deep+sleep", "ESP32"), ("battery+monitor+esp32", "ESP32"),
        ("sd+card+arduino+library", "Arduino"), ("littlefs", "ESP"),
        ("eeprom+emulation+arduino", "Arduino"), ("power+management+esp32", "ESP32"),
    ],
    "security-crypto": [
        ("esp32+security", "ESP32"), ("arduino+encryption+library", "Arduino"),
        ("esp32+tls+mbedtls", "ESP32"), ("nfc+arduino", "Arduino"),
        ("rfid+security+esp32", "ESP32"), ("ota+update+esp32", "ESP32"),
    ],
    "games-graphics": [
        ("esp32+game", "ESP32"), ("gameboy+arduino", "Arduino"),
        ("retro+handheld+esp32", "ESP32"), ("arduino+graphics+library", "Arduino"),
        ("esp32+emulator", "ESP32"), ("flappy+bird+arduino", "Arduino"),
    ],
    "weather-environment": [
        ("weather+station+esp32", "ESP32"), ("weather+station+esp8266", "ESP8266"),
        ("topic:weather-station", "Cross-platform"), ("greenhouse+esp32", "ESP32"),
        ("hydroponics+esp32", "ESP32"), ("aquarium+esp8266", "ESP8266"),
    ],
    "awesome-collections": [
        ("awesome+arduino", "meta"), ("awesome+esp32", "meta"),
        ("awesome+esp8266", "meta"), ("awesome+iot", "meta"),
        ("awesome+raspberry+pi+pico", "meta"), ("awesome+stm32", "meta"),
        ("awesome+microcontroller", "meta"), ("awesome+embedded", "meta"),
    ],
    "other-platforms": [
        ("raspberry+pi+pico+projects", "RP2040"), ("stm32+projects", "STM32"),
        ("microbit+projects", "micro:bit"), ("attiny+projects", "ATtiny"),
        ("teensy+projects", "Teensy"), ("nrf52+projects", "nRF52"),
        ("esp32-c3+projects", "ESP32-C3"), ("rp2040+firmware", "RP2040"),
    ],
}

def gh_search(query, per_page=10):
    q = query.replace(" ", "+") if "+" not in query else query
    out = subprocess.run(
        ["gh", "api", f"search/repositories?q={q}&sort=stars&order=desc&per_page={per_page}"],
        capture_output=True, text=True, timeout=60)
    if out.returncode != 0:
        print(f"  !! failed: {q}: {out.stderr.strip()[:200]}", flush=True)
        return []
    try:
        items = json.loads(out.stdout).get("items", [])
    except json.JSONDecodeError:
        print(f"  !! bad json: {q}", flush=True)
        return []
    res = []
    for it in items:
        res.append({
            "full_name": it["full_name"], "url": it["html_url"],
            "desc": (it.get("description") or "")[:220],
            "stars": it["stargazers_count"], "lang": it.get("language"),
            "topics": (it.get("topics") or [])[:6],
            "pushed": (it.get("pushed_at") or "")[:10],
            "archived": it.get("archived", False),
        })
    return res

def main():
    data = {}
    seen = {}
    total = 0
    for cat, queries in CATEGORIES.items():
        data[cat] = []
        print(f"== {cat}", flush=True)
        for q, plat in queries:
            repos = gh_search(q)
            time.sleep(7)  # search API: 10 req/min
            for r in repos:
                if r["archived"] or r["stars"] < 40:
                    continue
                if r["full_name"] in seen:
                    # already listed -> cross-link
                    prev = seen[r["full_name"]]
                    if prev != cat and r not in data[cat]:
                        pass
                    continue
                seen[r["full_name"]] = cat
                r["platform"] = plat
                r["matched_query"] = q
                data[cat].append(r)
                total += 1
            print(f"  {q} [{plat}]: +{len([r for r in repos if not r['archived'] and r['stars']>=40])}", flush=True)
        data[cat].sort(key=lambda r: -r["stars"])
        data[cat] = data[cat][:25]
    os.makedirs("data", exist_ok=True)
    with open("data/repos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"TOTAL unique repos: {total}; saved to data/repos.json")

if __name__ == "__main__":
    main()
