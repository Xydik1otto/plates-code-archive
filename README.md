# 🗺️ Plates Code Archive / Карта коду для плат

**A curated, functionality-organized map of open-source code for microcontroller boards** — Arduino, ESP32, ESP8266, RP2040, STM32, micro:bit and more. One place to find the right repo instead of searching GitHub every time. (310 repos, last refreshed 2026-11-05)

> **Українською:** кураторська карта відкритого коду для мікроконтролерних плат, зібрана за функціональністю. Кожен пункт — посилання на оригінальний репозиторій GitHub. Індекс оновлюється автоматично через офіційний GitHub Search API (див. [`tools/collect.py`](tools/collect.py)).

> ⚠️ All links point to the **original repositories** — nothing is copied. Each repo keeps its own license. / Усі посилання ведуть на оригінальні репозиторії — нічого не копіюється, ліцензії зберігаються у авторів.

---

## 📑 Table of Contents

- [`Frameworks & Cores`](#cat-frameworks-cores) — 21 repos
- [`Displays, LED & UI`](#cat-displays-ui) — 27 repos
- [`Sensors & Cameras`](#cat-sensors) — 25 repos
- [`Connectivity (WiFi/BLE/LoRa/Zigbee/CAN)`](#cat-connectivity) — 24 repos
- [`IoT & Home Automation`](#cat-iot-home-automation) — 25 repos
- [`Audio & Sound`](#cat-audio) — 29 repos
- [`Robotics, Motors, CNC & 3D Printers`](#cat-robotics-motors) — 26 repos
- [`Power, Sleep & Storage`](#cat-power-storage) — 23 repos
- [`Security, Crypto & OTA`](#cat-security-crypto) — 25 repos
- [`Games & Graphics`](#cat-games-graphics) — 22 repos
- [`Weather & Environment`](#cat-weather-environment) — 25 repos
- [`Meta Collections (Awesome lists)`](#cat-awesome-collections) — 15 repos
- [`Other Boards (Pico, STM32, micro:bit, nRF52...)`](#cat-other-platforms) — 23 repos

---

<a id="cat-frameworks-cores"></a>
## Frameworks & Cores
**Фреймворки та ядра**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [micropython/micropython](https://github.com/micropython/micropython) | 22.2k | C | Cross-platform | MicroPython - a lean and efficient Python implementation for microcontrollers and constrained systems |
| [espressif/esp-idf](https://github.com/espressif/esp-idf) | 19.4k | C | ESP32/ESP8266 | Espressif IoT Development Framework. Official development framework for Espressif SoCs. |
| [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo) | 17.9k | Go | Cross-platform | Go compiler for small places. Microcontrollers, WebAssembly (WASM/WASI), and command-line tools. Based on LLVM. |
| [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32) | 17.7k | C++ | ESP32/ESP8266 | Arduino core for the ESP32 family of SoCs |
| [rwaldron/johnny-five](https://github.com/rwaldron/johnny-five) | 13.4k | JavaScript | Arduino | JavaScript Robotics and IoT programming framework, developed at Bocoup. |
| [esphome/esphome](https://github.com/esphome/esphome) | 12.0k | C++ | Cross-platform | ESPHome is a system to control your ESP32, ESP8266, BK72xx, RP2040 by simple yet powerful configuration files and control them remotely through Home Automation systems. |
| [platformio/platformio-core](https://github.com/platformio/platformio-core) | 9.6k | Python | Cross-platform | Your Gateway to Embedded Software Development Excellence :alien: |
| [hybridgroup/gobot](https://github.com/hybridgroup/gobot) | 9.5k | Go | Arduino | Golang framework for robotics, drones, and the Internet of Things (IoT) |
| [blinker-iot/blinker-esp-idf](https://github.com/blinker-iot/blinker-esp-idf) | 4.3k | C | ESP32/ESP8266 | An IoT Solution,Blinker library for embedded hardware. Works with ESP8266, ESP32 (idf) |
| [hybridgroup/cylon](https://github.com/hybridgroup/cylon) | 4.2k | JavaScript | Arduino | JavaScript framework for robotics, drones, and the Internet of Things (IoT) |
| [ailyProject/aily-blockly](https://github.com/ailyProject/aily-blockly) | 3.9k | TypeScript | Cross-platform | AI IDE for hardware development, support Arduino, MicroPython, ESP32, STM32, RP2040, Nrf5x... |
| [crankyoldgit/IRremoteESP8266](https://github.com/crankyoldgit/IRremoteESP8266) | 3.7k | C++ | Cross-platform | Infrared remote library for ESP8266/ESP32: send and receive infrared signals with multiple protocols. Based on: https://github.com/shirriff/Arduino-IRremote/ |
| [davidmonterocrespo24/velxio](https://github.com/davidmonterocrespo24/velxio) | 3.6k | TypeScript | ESP32 | Emulate Arduino, ESP32 &amp; Raspberry Pi. in your browser. Write code, compile, and run on 19 real boards — Arduino Uno, ESP32, ESP32-C3, Raspberry Pi Pico, Raspberry Pi 3, and more. No hardware, no cloud, no limits.. Disco |
| [espressif/ESP8266_RTOS_SDK](https://github.com/espressif/ESP8266_RTOS_SDK) | 3.6k | C | ESP32/ESP8266 | Latest ESP8266 SDK based on FreeRTOS, esp-idf style. |
| [M-Abozaid/esp32-c3-adblock](https://github.com/M-Abozaid/esp32-c3-adblock) | 3.5k | C++ | Cross-platform | Pi-hole-class DNS ad-blocker on a $2 ESP32-C3 (no PSRAM): 537k domains as 40-bit FNV-1a hashes in flash, binary-searched. UDP DNS sinkhole + web dashboard. https://youtube.com/shorts/RaxszOUMi8E?feature=share |
| [HeyWillow/willow](https://github.com/HeyWillow/willow) | 3.1k | C | ESP32/ESP8266 | Open source, local, and self-hosted Amazon Echo/Google Home competitive Voice Assistant alternative |
| [RavenSystem/esp-homekit-devices](https://github.com/RavenSystem/esp-homekit-devices) | 3.0k | C | ESP32/ESP8266 | Advanced firmware to add native Apple HomeKit and custom configurations, compatible with any SoC based on ESP32, ESP32-S, ESP32-C and ESP8266 series. (Shelly, Sonoff, Electrodragon, Tuya...) |
| [micropython/micropython-lib](https://github.com/micropython/micropython-lib) | 2.9k | Python | Cross-platform | Core Python libraries ported to MicroPython |
| [agucova/awesome-esp](https://github.com/agucova/awesome-esp) | 2.8k | — | Cross-platform | 📶 A curated list of awesome ESP8266/32 projects and code |
| [martin-ger/esp32_nat_router](https://github.com/martin-ger/esp32_nat_router) | 2.3k | C | ESP32/ESP8266 | An AI-enabled NAT Router/Firewall for the ESP32 |
| [tbnobody/OpenDTU](https://github.com/tbnobody/OpenDTU) | 2.2k | C++ | Cross-platform | Software for ESP32 to talk to Hoymiles/TSUN/Solenso Inverters |

<a id="cat-displays-ui"></a>
## Displays, LED & UI
**Дисплеї, світлодіоди та інтерфейси**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [lvgl/lvgl](https://github.com/lvgl/lvgl) | 25.1k | C | Cross-platform | LVGL is a free, full-featured embedded UI library for devices from small MCUs to 3D-capable MPUs, enhanced by LVGL Pro, a professional editor and tooling. |
| [FASTSHIFT/X-TRACK](https://github.com/FASTSHIFT/X-TRACK) | 6.3k | C | Cross-platform | A GPS bicycle speedometer that supports offline maps and track recording  |
| [Bodmer/TFT_eSPI](https://github.com/Bodmer/TFT_eSPI) | 5.0k | C | Cross-platform | Arduino and PlatformIO IDE compatible TFT library optimised for the Raspberry Pi Pico (RP2040), STM32, ESP8266 and ESP32 that supports different driver chips |
| [ZSWatch/ZSWatch](https://github.com/ZSWatch/ZSWatch) | 3.4k | C | Cross-platform | ZSWatch - the Open Source Zephyr™ based Smartwatch, including both HW and FW. |
| [No-Chicken/OV-Watch](https://github.com/No-Chicken/OV-Watch) | 2.6k | C | Cross-platform | A powerful Smart Watch based on STM32, FreeRTOS, LVGL. |
| [0015/ThatProject](https://github.com/0015/ThatProject) | 2.5k | C | Cross-platform | *That Project&#x27;s project repository |
| [ThingPulse/esp8266-oled-ssd1306](https://github.com/ThingPulse/esp8266-oled-ssd1306) | 2.2k | C++ | Arduino | Driver for the SSD1306 and SH1106 based 128x64, 128x32, 64x48 pixel OLED display running on ESP8266/ESP32 |
| [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306) | 2.1k | C++ | Arduino | Arduino library for SSD1306 monochrome 128x64 and 128x32 OLEDs |
| [eez-open/studio](https://github.com/eez-open/studio) | 1.9k | JavaScript | Cross-platform | Cross-platform low-code GUI and automation |
| [juj/fbcp-ili9341](https://github.com/juj/fbcp-ili9341) | 1.8k | C++ | Cross-platform | A blazing fast display driver for SPI-based LCD displays for Raspberry Pi A, B, 2, 3, 4 and Zero |
| [OMOTE-Community/OMOTE-Firmware](https://github.com/OMOTE-Community/OMOTE-Firmware) | 1.8k | C++ | Cross-platform | Open Source Remote - Firmware |
| [Fr4nkFletcher/ESP32-Marauder-Cheap-Yellow-Display](https://github.com/Fr4nkFletcher/ESP32-Marauder-Cheap-Yellow-Display) | 1.8k | C | Cross-platform | ESP32Marauder Cheap Yellow Display |
| [fdivitto/FabGL](https://github.com/fdivitto/FabGL) | 1.7k | C++ | Cross-platform | ESP32 Display Controller (VGA, PAL/NTSC Color Composite, SSD1306, ST7789, ILI9341), PS/2 Mouse and Keyboard Controller, Graphics Library, Sound Engine, Game Engine and ANSI/VT Terminal |
| [ttrftech/NanoVNA](https://github.com/ttrftech/NanoVNA) | 1.4k | C | Cross-platform | Very Tiny Palmtop Vector Network Analyzer |
| [ImpulseAdventure/GUIslice](https://github.com/ImpulseAdventure/GUIslice) | 1.4k | C | ESP32 | GUIslice drag &amp; drop embedded GUI in C for touchscreen TFT on Arduino, Raspberry Pi, ARM, ESP8266 / ESP32 / M5stack using Adafruit-GFX / TFT_eSPI / UTFT / SDL |
| [lvgl/lv_esp_idf](https://github.com/lvgl/lv_esp_idf) | 1.3k | C | Cross-platform | LVGL ported to ESP32 including various display and touchpad drivers |
| [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | 1.1k | JavaScript | Cross-platform | A visual drag-and-drop editor for ESPHome displays (E-Ink, OLED, LCD, Touch), running as a Home Assistant integration or a standalone web app. |
| [MaxGramser/homeassistant_espscreen](https://github.com/MaxGramser/homeassistant_espscreen) | 1.0k | Python | Cross-platform | Tessera: beautiful, easy touch screens for Home Assistant on affordable ESP32 panels, 2.8 to 10.1 inch (CYD, Guition, Waveshare). Drag-and-drop editor, no YAML, no MQTT. |
| [yashmulgaonkar/halo](https://github.com/yashmulgaonkar/halo) | 958 | C++ | ESP32 | An open-source, ESP32-powered air quality monitor with an RGB ring, touchscreen, and comprehensive environmental sensors. Firmware installer: https://yashmulgaonkar.github.io/halo/ |
| [loboris/MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo) | 874 | C | ESP32 | MicroPython for ESP32 with psRAM support |
| [lexus2k/ssd1306](https://github.com/lexus2k/ssd1306) | 823 | C | Cross-platform | Driver for SSD1306, SSD1331, SSD1351, IL9163, ILI9341, ST7735, PCD8544, Nokia 5110 displays running on Arduino/ESP32/Linux (Rasperry) platforms |
| [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy) | 730 | Python | Cross-platform | Fast MicroPython driver for  ST7789 display module written in C |
| [DustinWatts/FreeTouchDeck](https://github.com/DustinWatts/FreeTouchDeck) | 717 | C | ESP32 | For interfacing with Windows/macOS/Linux using an ESP32, a touchscreen and BLE. |
| [rzeldent/esp32-smartdisplay](https://github.com/rzeldent/esp32-smartdisplay) | 705 | C | Cross-platform | PlatformIO library LVGL Drivers for Sunton Smart display boards (CYD Cheap Yellow Display). This library supports these boards without any effort. ESP32-2432S024N/R/C, ESP32-2432S028R/C, ESP32-3248S035R/C, ESP32_8048S070 |
| [RobertoBenjami/stm32_graphics_display_drivers](https://github.com/RobertoBenjami/stm32_graphics_display_drivers) | 703 | C | Cross-platform | STM32 LCD drivers (currently: spi(dma), gpio, fsmc(dma), st7735, st7783, ili9325, ili9328, ili9341, ili9486, ili9488, hx8347g) |
| [h-RAT/Willy_Firmware_V2_ESP32_Flipper_Zero_Alternative](https://github.com/h-RAT/Willy_Firmware_V2_ESP32_Flipper_Zero_Alternative) | 678 | HTML | ESP32 | Willy Firmware is an alternative to Flipper Zero. / Board: ESP32 T-Display-S3 - Module: CC1101 - Display: Touchscreen - Compatible Flipper Zero file. |
| [bitbank2/Thermal_Printer](https://github.com/bitbank2/Thermal_Printer) | 526 | C | Arduino | Arduino library to draw text and graphics on BLE thermal printers |

<a id="cat-sensors"></a>
## Sensors & Cameras
**Сенсори та камери**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [s60sc/ESP32-CAM_MJPEG2SD](https://github.com/s60sc/ESP32-CAM_MJPEG2SD) | 1.8k | C++ | ESP32 | ESP32 Camera motion capture application to record JPEGs to SD card as AVI files and stream to browser as MJPEG. If a microphone is installed then a WAV file is also created. Files can be uploaded via FTP or downloaded to |
| [easytarget/esp32-cam-webserver](https://github.com/easytarget/esp32-cam-webserver) | 1.5k | C | ESP32 | Expanded version of the Espressif ESP webcam |
| [devbis/z03mmc](https://github.com/devbis/z03mmc) | 1.5k | C | Cross-platform | Xiaomi LYWSD03MMC Zigbee Firmware |
| [mikalhart/TinyGPSPlus](https://github.com/mikalhart/TinyGPSPlus) | 1.3k | C++ | Arduino | A new, customizable Arduino NMEA parsing library |
| [21cncstudio/project_aura](https://github.com/21cncstudio/project_aura) | 784 | C | ESP32 | ESP32‑S3 air‑quality station with LVGL UI, MQTT, Home Assistant |
| [eried/flipperzero-mayhem](https://github.com/eried/flipperzero-mayhem) | 735 | C++ | ESP32 | Perfect companion for your Flipper Zero. ESP32 with WiFi, BT/BLE, micro-SD, camera+PSRAM, flashlight and extras: NRF24/CC1101, 3V/5V sensors |
| [yoursunny/esp32cam](https://github.com/yoursunny/esp32cam) | 689 | C++ | ESP32 | OV2640 camera on ESP32-CAM, Arduino library |
| [timmbogner/Farm-Data-Relay-System](https://github.com/timmbogner/Farm-Data-Relay-System) | 629 | C | ESP32 | A system that uses ESP-NOW, LoRa, and other protocols to transport sensor data in remote areas without relying on WiFi. |
| [lemariva/micropython-camera-driver](https://github.com/lemariva/micropython-camera-driver) | 567 | C | ESP32 | add camera support to MicroPython |
| [adafruit/Adafruit_GPS](https://github.com/adafruit/Adafruit_GPS) | 497 | C++ | Arduino | An interrupt-based GPS Arduino library for no-parsing-required use |
| [mikalhart/TinyGPS](https://github.com/mikalhart/TinyGPS) | 412 | C++ | Arduino | A compact Arduino NMEA (GPS) parsing library |
| [adafruit/Adafruit_BME280_Library](https://github.com/adafruit/Adafruit_BME280_Library) | 396 | C++ | Arduino | Arduino Library for BME280 sensors |
| [Tech1k/helloesp](https://github.com/Tech1k/helloesp) | 387 | HTML | Arduino | A public website hosted on an ESP32. |
| [hannseman/homebridge-mi-hygrothermograph](https://github.com/hannseman/homebridge-mi-hygrothermograph) | 272 | JavaScript | Cross-platform | Homebridge plugin for the Xiaomi Mi Bluetooth Temperature and Humidity Sensor |
| [finitespace/BME280](https://github.com/finitespace/BME280) | 249 | C++ | Arduino | Provides an Arduino library for reading and interpreting Bosch BME280 data over I2C, SPI or Sw SPI. |
| [shariltumin/esp32-cam-micropython-2022](https://github.com/shariltumin/esp32-cam-micropython-2022) | 245 | Python | ESP32 | MicroPython esp32-cam firmware with camera support compiled with esp-idf-4.4.0. Python script files for live streaming |
| [alanesq/CameraWifiMotion](https://github.com/alanesq/CameraWifiMotion) | 230 | C++ | ESP32 | Motion detecting security camera using a cheap ESP32-cam camera module |
| [liourej/CodeDroneDIY](https://github.com/liourej/CodeDroneDIY) | 227 | C++ | Arduino | The most simple, but working, quadricopter flight controller from scratch, using Arduino Uno/Nano. |
| [supergreenlab/SuperGreenOS](https://github.com/supergreenlab/SuperGreenOS) | 222 | C | ESP32 | 🧠 SuperGreenOS home farming automation software for esp32, all in one package, and controllable from your smartphone, pc, mac, linux, toaster, plumbus, whatnot... |
| [rzeldent/esp32cam-ready](https://github.com/rzeldent/esp32cam-ready) | 216 | C++ | ESP32 | Plug and Play firmware for the esp32cam. Connect with RTSP (for example VLC). Easy installation: Flash, provision and connect! |
| [M64GitHub/WireClaw](https://github.com/M64GitHub/WireClaw) | 213 | C++ | ESP32 | ESP32 AI agent with persistent memory and offline rule engine - chat to configure, run locally 24/7. (Telegram / Serial / NATS). |
| [omersiar/RFID522-Door-Unlock](https://github.com/omersiar/RFID522-Door-Unlock) | 208 | Arduino | Arduino | Arduino RC522 RFID Access Control |
| [cpainchaud/RFLink32](https://github.com/cpainchaud/RFLink32) | 197 | C | ESP32 | RFLink for ESP, with MQTT client |
| [dproldan/Esp32AutoCamera](https://github.com/dproldan/Esp32AutoCamera) | 194 | C++ | ESP32 | ESP32-CAM with an open wifi access point and a captive portal,  for fast deployment of a wireless camara. |
| [kevinmehall/rtlsdr-433m-sensor](https://github.com/kevinmehall/rtlsdr-433m-sensor) | 185 | Python | Cross-platform | Decoder for Oregon Scientific v1 protocol wireless temperature sensors with RTL-SDR and GNU Radio. |

<a id="cat-connectivity"></a>
## Connectivity (WiFi/BLE/LoRa/Zigbee/CAN)
**Зв'язок**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder) | 13.0k | C++ | ESP32 | A suite of WiFi/Bluetooth offensive and defensive tools for the ESP32 |
| [EmenstaNougat/ESP32-BlueJammer](https://github.com/EmenstaNougat/ESP32-BlueJammer) | 8.8k | — | ESP32 | The ESP32-BlueJammer (Bluetooth jammer, BLE jammer, WiFi jammer, RC jammer) disrupts 2.4GHz communications. Using an ESP32 and nRF24 modules, it generates noise and unnecessary packets, causing interference between the d |
| [meshtastic/firmware](https://github.com/meshtastic/firmware) | 8.5k | C++ | ESP32 | The official firmware for Meshtastic, an open-source, off-grid mesh communication system. |
| [tzapu/WiFiManager](https://github.com/tzapu/WiFiManager) | 7.3k | C++ | ESP8266 | ESP8266 WiFi Connection manager with web captive portal |
| [geo-tp/ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate) | 6.3k | C++ | ESP32 | A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol  |
| [ExpressLRS/ExpressLRS](https://github.com/ExpressLRS/ExpressLRS) | 5.5k | C | ESP32 | High Performance Open Source Radio Control Link |
| [cifertech/ESP32-DIV](https://github.com/cifertech/ESP32-DIV) | 4.3k | C++ | ESP32 | ESP32DIV is a multi-purpose wireless offensive and defensive toolkit powered by an ESP32 |
| [T-vK/ESP32-BLE-Keyboard](https://github.com/T-vK/ESP32-BLE-Keyboard) | 3.2k | C++ | ESP32 | Bluetooth LE Keyboard library for the ESP32 (Arduino IDE compatible) |
| [gioblu/PJON](https://github.com/gioblu/PJON) | 2.8k | C++ | ESP32 | PJON (Padded Jittering Operative Network) is an experimental, arduino-compatible, multi-master, multi-media network protocol. |
| [nRF24/RF24](https://github.com/nRF24/RF24) | 2.5k | C++ | Arduino | OSI Layer 2 driver for nRF24L01 on Arduino &amp; Raspberry Pi/Linux Devices |
| [vshymanskyy/TinyGSM](https://github.com/vshymanskyy/TinyGSM) | 2.2k | C++ | Arduino | A small Arduino library for GSM modules, that just works |
| [cifertech/nRFBox](https://github.com/cifertech/nRFBox) | 2.1k | C++ | Arduino | Open-source ESP32-powered tool to scan, jam, spoof, and master BLE, Wi-Fi, and 2.4GHz networks. |
| [cifertech/RF-Clown](https://github.com/cifertech/RF-Clown) | 1.9k | C++ | ESP32 | BLE and Bluetooth Jammer with nRF24L01 and ESP32 |
| [meshtastic/Meshtastic-Android](https://github.com/meshtastic/Meshtastic-Android) | 1.9k | Kotlin | ESP32 | Android application for Meshtastic |
| [JesseCHale/HaleHound-CYD](https://github.com/JesseCHale/HaleHound-CYD) | 1.9k | — | ESP32 | ESP32-DIV HaleHound Edition for Cheap Yellow Display - Multi-protocol offensive security toolkit |
| [whitecatboard/Lua-RTOS-ESP32](https://github.com/whitecatboard/Lua-RTOS-ESP32) | 1.3k | C | ESP32 | Lua RTOS for ESP32 |
| [DroneBridge/ESP32](https://github.com/DroneBridge/ESP32) | 1.1k | C | ESP32 | DroneBridge for ESP32. A secure &amp; transparent telemetry link with support for WiFi and ESP-NOW. Supporting MAVLink, MSP, LTM or any other protocol |
| [lyusupov/SoftRF](https://github.com/lyusupov/SoftRF) | 1.0k | C | ESP32 | :airplane:  Multi-functional, compatible DIY general aviation proximity awareness system |
| [W0rthlessS0ul/nRF24_jammer](https://github.com/W0rthlessS0ul/nRF24_jammer) | 1.0k | C | ESP32 | The nRF24 jammer is a powerful tool that requires an ESP32 and configurable numbers of NRF24 modules to assemble. It is designed to create interference, disrupting the normal operation of Bluetooth devices 🔊, BLE technol |
| [HelTecAutomation/Heltec_ESP32](https://github.com/HelTecAutomation/Heltec_ESP32) | 922 | C | ESP32 | Arduino library for Heltec ESP32 (or ESP32+LoRa) based boards |
| [rtlopez/esp-fc](https://github.com/rtlopez/esp-fc) | 887 | C | ESP32 | Flight controller software for hobbyist - build your own flight controller. |
| [espressif/esp-now](https://github.com/espressif/esp-now) | 818 | C | ESP32 | A connectionless Wi-Fi communication protocol |
| [ropg/heltec_esp32_lora_v3](https://github.com/ropg/heltec_esp32_lora_v3) | 715 | C++ | ESP32 | Proper working Arduino library for the Heltec ESP32 LoRa v3 board, as well as for Wireless Stick v3 and Wireless Stick Lite v3. Uses RadioLib |
| [atomic14/esp32-walkie-talkie](https://github.com/atomic14/esp32-walkie-talkie) | 653 | C++ | ESP32 | A Walkie-Talkie based around the ESP32 using UDP broadcast or ESP-NOW |

<a id="cat-iot-home-automation"></a>
## IoT & Home Automation
**IoT та розумний дім**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 102.5k | Rust | ESP32 | π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video. |
| [arendst/Tasmota](https://github.com/arendst/Tasmota) | 25.0k | C | ESP | Alternative firmware for ESP8266 and ESP32 based devices with easy configuration using webUI, OTA updates, automation using timers or rules, expandability and entirely local control over MQTT, HTTP, Serial or KNX. Full d |
| [wled/WLED](https://github.com/wled/WLED) | 19.0k | C++ | ESP8266/ESP32 | Control WS2812B and many more types of digital RGB LEDs with an ESP32 over WiFi! |
| [francescopace/espectre](https://github.com/francescopace/espectre) | 9.7k | Python | ESP | Wi-Fi motion sensing platform for ESP32. C++ SDK, ESPHome, Native, and Matter frontends, browser tools, and a CLI for the full device lifecycle. GPLv3 and commercial licensing. |
| [blinker-iot/blinker-library](https://github.com/blinker-iot/blinker-library) | 5.2k | C++ | ESP32 | An IoT Solution,Blinker library for embedded hardware. Works with Arduino R4, ESP32. |
| [1technophile/OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) | 4.1k | C++ | Cross-platform | MQTT gateway for ESP8266 or ESP32 with bidirectional 433mhz/315mhz/868mhz, Infrared communications, BLE, Bluetooth, beacons detection, mi flora, mi jia, LYWSD02, LYWSD03MMC, Mi Scale, TPMS, BBQ thermometer compatibility  |
| [hyperion-project/hyperion.ng](https://github.com/hyperion-project/hyperion.ng) | 4.0k | C++ | ESP8266/ESP32 | The successor to Hyperion aka Hyperion Next Generation |
| [smartHomeHub/SmartIR](https://github.com/smartHomeHub/SmartIR) | 2.9k | Python | ESP | Home Assistant integration to manage climate systems, TVs, fans and lights using IR/RF controllers. Compatible with Broadlink, Xiaomi, MQTT, LOOKin and ESPHome |
| [jxlarrea/kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) | 2.5k | Dart | ESP | Turn any Android device into a beautiful, dedicated Home Assistant kiosk. Purpose-built for Home Assistant from the ground up. |
| [openshwprojects/OpenBK7231T_App](https://github.com/openshwprojects/OpenBK7231T_App) | 2.3k | C | ESP | Open source firmware (Tasmota/Esphome replacement) for BK7231T, BK7231N, BL2028N, T34, XR809, W800/W801, W600/W601, BL602, LN882H, Realtek chips and more |
| [awawa-dev/HyperHDR](https://github.com/awawa-dev/HyperHDR) | 2.3k | C++ | ESP8266/ESP32 | Next-gen open source ambient lighting system featuring a high-precision floating-point color pipeline breaking legacy RGB 24-bit limits. Includes advanced smoothing with inertia and adaptive temporal dithering for perfec |
| [agittins/bermuda](https://github.com/agittins/bermuda) | 2.1k | Python | ESP | Bermuda Bluetooth/BLE Triangulation / Trilateration for HomeAssistant |
| [LedFx/LedFx](https://github.com/LedFx/LedFx) | 2.1k | Python | ESP8266/ESP32 | LedFx is a network based LED effect engine designed to deliver advanced real-time audio effects to a wide variety of devices. |
| [Blackymas/NSPanel_HA_Blueprint](https://github.com/Blackymas/NSPanel_HA_Blueprint) | 2.0k | C++ | ESP | This allows you to configure your complete NSPanel via Blueprint with UI and without changing anything in the code |
| [adonno/tagreader](https://github.com/adonno/tagreader) | 1.6k | Shell | ESP | Simple to build/use NFC tag reader, specially created for Home Assistant |
| [tasmota/tasmotizer](https://github.com/tasmota/tasmotizer) | 1.5k | Python | ESP | ESP... The time has come to... Tasmotize! |
| [ESPresense/ESPresense](https://github.com/ESPresense/ESPresense) | 1.5k | C | ESP32 | An ESP32 based node for gathering indoor positioning and transmitting to mqtt |
| [mysensors/MySensors](https://github.com/mysensors/MySensors) | 1.4k | C++ | ESP8266 | MySensors library and examples |
| [Madelena/esphome-weatherman-dashboard](https://github.com/Madelena/esphome-weatherman-dashboard) | 1.3k | — | ESP | A simple dashboard with weather and NYC subway information for ESPHome |
| [klaasnicolaas/home-assistant-glow](https://github.com/klaasnicolaas/home-assistant-glow) | 1.3k | — | ESP | ⚡ The power of energy measurements in your house |
| [jtenniswood/espcontrol](https://github.com/jtenniswood/espcontrol) | 1.1k | C++ | ESP32 | Esphome based smart home control panel |
| [joBr99/nspanel-lovelace-ui](https://github.com/joBr99/nspanel-lovelace-ui) | 997 | TypeScript | ESP | Custom Firmware for NsPanel with the design of HomeAssistant&#x27;s lovelace UI in mind, works with Tasmota. |
| [TasmoAdmin/TasmoAdmin](https://github.com/TasmoAdmin/TasmoAdmin) | 979 | PHP | ESP | TasmoAdmin is an administrative platform for devices flashed with Tasmota |
| [jziolkowski/tdm](https://github.com/jziolkowski/tdm) | 707 | Python | ESP | GUI application to discover and monitor devices flashed with https://github.com/arendst/tasmota |
| [benzino77/tasmocompiler](https://github.com/benzino77/tasmocompiler) | 627 | C | ESP | Web GUI for custom Tasmota compilation |

<a id="cat-audio"></a>
## Audio & Sound
**Аудіо та звук**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [pschatzmann/ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP) | 2.8k | C++ | Cross-platform | A Simple ESP32 Bluetooth A2DP Library (to implement a Music Receiver or Sender) that supports Arduino, PlatformIO and Espressif IDF |
| [earlephilhower/ESP8266Audio](https://github.com/earlephilhower/ESP8266Audio) | 2.4k | C | ESP32 | Arduino library to play MOD, WAV, FLAC, MIDI, RTTTL, OGG/Opus, MP3, and AAC files on I2S DACs or with a software emulated delta-sigma DAC on the ESP8266 and ESP32 and Pico |
| [schreibfaul1/ESP32-audioI2S](https://github.com/schreibfaul1/ESP32-audioI2S) | 1.7k | C | ESP32 | Play mp3 files from SD via I2S |
| [e2002/yoradio](https://github.com/e2002/yoradio) | 1.2k | C++ | ESP32 | Web-radio based on ESP32-audioI2S library |
| [korginc/logue-sdk](https://github.com/korginc/logue-sdk) | 1.1k | C | Cross-platform | This repository contains all the files and tools needed to build custom oscillators and effects for the prologue synthesizer. |
| [TMRh20/TMRpcm](https://github.com/TMRh20/TMRpcm) | 651 | C++ | Arduino | Arduino library for asynchronous playback of PCM/WAV files direct from SD card. Arduino Uno,Nano,Mega etc supported |
| [karawin/Ka-Radio32](https://github.com/karawin/Ka-Radio32) | 614 | C | ESP32 | esp32 version of Ka-Radio (https://github.com/karawin/Ka-Radio) by jp Cocatrix |
| [sonocotta/esp32-audio-dock](https://github.com/sonocotta/esp32-audio-dock) | 478 | C++ | ESP32 | ESP32 Audio Developent boards: HiFi-ESP32, Loud-ESP32, Amped-ESP32, Louder-ESP32 |
| [atomic14/esp32_audio](https://github.com/atomic14/esp32_audio) | 471 | C++ | ESP32 | Sample code for reading audio samples from the ESP32 ADC using I2S |
| [biologist79/ESPuino](https://github.com/biologist79/ESPuino) | 439 | C++ | ESP32 | RFID-controlled musicplayer powered by ESP32 |
| [trash80/Arduinoboy](https://github.com/trash80/Arduinoboy) | 375 | Max | Arduino | Official ArduinoBoy Repository for serial MIDI communication to the Nintendo Gameboy. |
| [Romkabouter/ESP32-Rhasspy-Satellite](https://github.com/Romkabouter/ESP32-Rhasspy-Satellite) | 373 | C++ | ESP32 | The repo has implementing an esp32 standalone MQTT audio streamer. Is is desinged to work as a satellite for Rhasspy (https://rhasspy.readthedocs.io/en/latest/). It supports multiple devices |
| [danilogcrf2-oss/ESP32Synth](https://github.com/danilogcrf2-oss/ESP32Synth) | 355 | C | ESP32 | Polyphonic synthesizer with up to 350 voices/channels for the ESP32 dual core family, offering high-fidelity audio (48kHz @ 32bit). |
| [marcel-licence/esp32_basic_synth](https://github.com/marcel-licence/esp32_basic_synth) | 320 | C++ | ESP32 | ESP32 based simple synthesizer project |
| [ikostoski/esp32-i2s-slm](https://github.com/ikostoski/esp32-i2s-slm) | 312 | C++ | ESP32 | Sound Level Meter with ESP32 and I2S MEMS microphone |
| [Edzelf/ESP32Radio-V2](https://github.com/Edzelf/ESP32Radio-V2) | 309 | C++ | ESP32 | New version of the well known ESP32 Radio.  Now optional I2S output! |
| [miketeachman/micropython-i2s-examples](https://github.com/miketeachman/micropython-i2s-examples) | 306 | Python | ESP32 | Examples for I2S support on microcontrollers that run MicroPython |
| [kodera2t/ESP32_OLED_webradio](https://github.com/kodera2t/ESP32_OLED_webradio) | 254 | C++ | ESP32 | OLED display support is added to ESP32 MP3 web radio/bluetotooth speaker code by MrBuddyCasino&#x27;s. Now webradio station switching is supported (implemented by n24bass) |
| [CoretechR/Retro-Audio](https://github.com/CoretechR/Retro-Audio) | 233 | C | Arduino | Portable MP3 Player for Music and Audiobooks |
| [Sukecz/esp32-birdnet-mic](https://github.com/Sukecz/esp32-birdnet-mic) | 228 | C++ | ESP32 | ESP32 audio streamer and standalone microSD field recorder. Stream to BirdNET-Go/Pi or record wildlife sounds offline, with browser setup and battery monitoring. |
| [cyberwisk/M5Cardputer_WebRadio](https://github.com/cyberwisk/M5Cardputer_WebRadio) | 136 | C++ | ESP32 | M5Cardputer_WebRadio |
| [thi-ng/synstack](https://github.com/thi-ng/synstack) | 134 | C | Cross-platform | Modular soft synth &amp; Forth based VM for audio DSL experiments aimed at embedded devices |
| [madsci1016/Sparkfun-MP3-Player-Shield-Arduino-Library](https://github.com/madsci1016/Sparkfun-MP3-Player-Shield-Arduino-Library) | 111 | C++ | Arduino | A nice and neat library for playing MP3s on your Arduino using Sparkfun&#x27;s MP3 Player Shield |
| [Slackadays/Chata](https://github.com/Slackadays/Chata) | 110 | C++ | Cross-platform | :guitar::long_drum::magic_wand: Make DSP Great Again. Powered by RISC-V! |
| [cifertech/Fennec](https://github.com/cifertech/Fennec) | 108 | C++ | ESP32 | Handheld AM / FM / SW receiver on ESP32-S3 and SI4732. SSTV, Morse, RSSI homing, and a web remote. |
| [Neutrino-1/Arduino-Soundpod](https://github.com/Neutrino-1/Arduino-Soundpod) | 85 | C++ | Arduino | An Arduino based MP3 player which uses a 1.3&quot; OLED display and DFPlayer |
| [michelep/ESP32_WebRadio](https://github.com/michelep/ESP32_WebRadio) | 65 | C++ | ESP32 | An Internet web radio based to ESP32 |
| [enjoyneering/DFPlayer](https://github.com/enjoyneering/DFPlayer) | 62 | C++ | Arduino | Small and fast Arduino library for DFPlayer Mini MP3 Player |
| [sleemanj/JQ6500_Serial](https://github.com/sleemanj/JQ6500_Serial) | 61 | C++ | Arduino | Arduino Library for the JQ6500 MP3 Player Modules |

<a id="cat-robotics-motors"></a>
## Robotics, Motors, CNC & 3D Printers
**Робототехніка, мотори, ЧПУ**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin) | 17.6k | C++ | 3D printers | Marlin is a firmware for RepRap 3D printers optimized for both 8 and 32 bit microcontrollers.  Marlin supports all common platforms.   Many commercial 3D printers come with Marlin installed.  Check with your vendor if yo |
| [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | 13.0k | Python | ESP32 | Open-source vacuum robot cleaner |
| [Klipper3d/klipper](https://github.com/Klipper3d/klipper) | 12.0k | C | 3D printers | Klipper is a 3d-printer firmware |
| [ClemensElflein/OpenMower](https://github.com/ClemensElflein/OpenMower) | 6.8k | Shell | Arduino | Let&#x27;s upgrade cheap off-the-shelf robotic mowers to modern, smart RTK GPS based lawn mowing robots! |
| [grbl/grbl](https://github.com/grbl/grbl) | 6.3k | C | Arduino | An open source, embedded, high performance g-code-parser and CNC milling controller written in optimized C that will run on a straight Arduino |
| [PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | 5.5k | C++ | Arduino | An open source quadruped robot pet framework for developing Boston Dynamics-style four-legged robots that are perfect for STEM, coding &amp; robotics education, IoT robotics applications, AI-enhanced robotics application ser |
| [dorianborian/sesame-robot](https://github.com/dorianborian/sesame-robot) | 5.0k | C | ESP32 | An open and affordable mini quadruped robot based on ESP32. |
| [dw-0/kiauh](https://github.com/dw-0/kiauh) | 4.6k | Python | 3D printers | Klipper Installation And Update Helper |
| [ob-f/OpenBot](https://github.com/ob-f/OpenBot) | 3.6k | Swift | Arduino | OpenBot leverages smartphones as brains for low-cost robots. We have designed a small electric vehicle that costs about $50 and serves as a robot body. Our software stack for Android smartphones supports advanced robotic |
| [simplefoc/Arduino-FOC](https://github.com/simplefoc/Arduino-FOC) | 3.1k | C++ | Arduino | Arduino FOC for BLDC and Stepper motors - Arduino Based Field Oriented Control Algorithm Library |
| [cncjs/cncjs](https://github.com/cncjs/cncjs) | 2.7k | JavaScript | Arduino | A web-based interface for CNC milling controller running Grbl, Marlin, Smoothieware, or TinyG. |
| [EtteGit/EnragedRabbitProject](https://github.com/EtteGit/EnragedRabbitProject) | 2.6k | Python | 3D printers | — |
| [okalachev/flix](https://github.com/okalachev/flix) | 2.5k | C++ | ESP32 | Making an ESP32-based quadcopter from scratch |
| [espressif/esp-drone](https://github.com/espressif/esp-drone) | 2.3k | C | ESP32 | Mini Drone/Quadcopter Firmware for ESP32 and ESP32-S Series SoCs. |
| [MarlinFirmware/Configurations](https://github.com/MarlinFirmware/Configurations) | 2.3k | C | 3D printers | Configurations for Marlin Firmware |
| [winder/Universal-G-Code-Sender](https://github.com/winder/Universal-G-Code-Sender) | 2.3k | Java | Arduino | A cross-platform G-Code sender for GRBL, Smoothieware, TinyG and G2core. |
| [mainsail-crew/mainsail](https://github.com/mainsail-crew/mainsail) | 2.2k | Vue | 3D printers | Mainsail is the popular web interface for managing and controlling 3D printers with Klipper. |
| [kyleisah/Klipper-Adaptive-Meshing-Purging](https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging) | 2.2k | — | 3D printers | A unique leveling solution for Klipper-enabled 3D printers! |
| [luc-github/ESP3D](https://github.com/luc-github/ESP3D) | 2.0k | C | Arduino | FW for ESP8266/ESP8285/ESP32 used with 3D printer |
| [bdring/Grbl_Esp32](https://github.com/bdring/Grbl_Esp32) | 2.0k | nesC | Arduino | A port of Grbl CNC Firmware for ESP32 |
| [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) | 1.8k | TypeScript | ESP32 | A JavaScript-driven M5Stack-embedded super-kawaii robot. |
| [fluidd-core/fluidd](https://github.com/fluidd-core/fluidd) | 1.8k | Vue | 3D printers | Fluidd, the klipper UI. |
| [Skythinker616/foc-wheel-legged-robot](https://github.com/Skythinker616/foc-wheel-legged-robot) | 1.8k | C | ESP32 | Open source materials for a novel structured legged robot, including mechanical design, electronic design, algorithm simulation, and software development.   /   一个新型结构的轮腿机器人开源资料，包含机械设计、电子设计、算法仿真、软件开发等材料 |
| [LuwuDynamics/xgoduck_hardware](https://github.com/LuwuDynamics/xgoduck_hardware) | 1.8k | Game Maker Language | Arduino | Build your own robot duck. XGO-Duck is a 3D-printable biped powered by Arduino UNO Q and 15 servos, adapted from Pollen Robotics&#x27; Microduck. Includes mechanical models, PCB designs, a BOM, and an assembly guide. Build it |
| [vlachoudis/bCNC](https://github.com/vlachoudis/bCNC) | 1.8k | Python | Arduino | GRBL CNC command sender, autoleveler and g-code editor |
| [Arksine/moonraker](https://github.com/Arksine/moonraker) | 1.5k | Python | 3D printers | Web API Server for Klipper |

<a id="cat-power-storage"></a>
## Power, Sleep & Storage
**Живлення, сон та зберігання**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [littlefs-project/littlefs](https://github.com/littlefs-project/littlefs) | 7.0k | C | ESP | A little fail-safe filesystem designed for microcontrollers |
| [thelastoutpostworkshop/ESPConnect](https://github.com/thelastoutpostworkshop/ESPConnect) | 2.2k | TypeScript | ESP | Zero-installation web application that lets you explore, back up, and manage your ESP32… right from your browser |
| [Lularible/storage-book](https://github.com/Lularible/storage-book) | 587 | C | ESP | An open-source book on storage technology and file systems. From knot records to Flash physics, from FAT to LittleFS — complete with KnotFS, a teaching-grade log-structured embedded file system (~1770 lines C). |
| [earlephilhower/arduino-littlefs-upload](https://github.com/earlephilhower/arduino-littlefs-upload) | 394 | TypeScript | ESP | Build and uploads LittleFS filesystems for the Arduino-Pico RP2040, RP2350, ESP8266, and ESP32 cores under Arduino IDE 2.2.1 or higher |
| [HelTecAutomation/ESP32_LoRaWAN](https://github.com/HelTecAutomation/ESP32_LoRaWAN) | 361 | Assembly | ESP32 | Transplanted from Semtech LoRaWAN(https://github.com/Lora-net/LoRaMac-node) protocol to &quot;ESP32 + Arduino&quot; platform. Use RTC, support deep sleep, only working with ESP32 + LoRa boards made by HelTec Automation(TM). Need a |
| [joltwallet/esp_littlefs](https://github.com/joltwallet/esp_littlefs) | 355 | C | ESP | LittleFS port for ESP-IDF |
| [earlephilhower/mklittlefs](https://github.com/earlephilhower/mklittlefs) | 235 | C++ | ESP | Utility for creating LittleFS images for upload on the ESP8266 and RP2040 Pico |
| [littlefs-project/littlefs-fuse](https://github.com/littlefs-project/littlefs-fuse) | 225 | C | ESP | A FUSE wrapper that puts the littlefs in user-space |
| [lorol/LITTLEFS](https://github.com/lorol/LITTLEFS) | 202 | C | ESP | LittleFS library for arduino-esp32 |
| [xreef/SimpleFTPServer](https://github.com/xreef/SimpleFTPServer) | 181 | C++ | ESP | A simple FTP server for Arduino, ArduinoSAMD WiFiNINA, esp8266, esp32, stm32 and Raspberry Pi Pico W |
| [adafruit/Adafruit_ImageReader](https://github.com/adafruit/Adafruit_ImageReader) | 141 | C++ | Arduino | Companion Arduino library for Adafruit_GFX to load images from SD card |
| [microbotsio/CodeCell](https://github.com/microbotsio/CodeCell) | 128 | C | ESP32 | CodeCell is a family of tiny boards that help you miniaturize your DIY robots, wearables, and IoT projects with ease! Designed for makers, each CodeCell features an Arduino-compatible ESP32 microcontroller, onboard senso |
| [futureshocked/KLP-5e-ESP32-sensor-board](https://github.com/futureshocked/KLP-5e-ESP32-sensor-board) | 125 | C++ | ESP32 | This project involves the design and development of a custom PCB for an IoT application powered by the ESP32-C3-02 SoC. The board includes integrated power management features using the TP4056 Li-ion battery charger IC,  |
| [SensorsIot/ESP32-Deep-Sleep](https://github.com/SensorsIot/ESP32-Deep-Sleep) | 89 | C++ | ESP32 | Material for video #149 |
| [jwrw/ESP_EEPROM](https://github.com/jwrw/ESP_EEPROM) | 87 | C++ | Arduino | An improved EEPROM emulation Arduino library for ESP8266 |
| [PRosenb/DeepSleepScheduler](https://github.com/PRosenb/DeepSleepScheduler) | 85 | C++ | ESP32 | DeepSleepScheduler is a lightweight, cooperative task scheduler library with configurable sleep and task supervision.  |
| [artkeller/ESP32Features](https://github.com/artkeller/ESP32Features) | 55 | Python | ESP32 | Datasheet-derived comparison of all 14 ESP32 SoC variants (ESP32 → S31): specs, deep sleep, security/PQC readiness, and reasoned multi-chip combinations. Community-maintained, not affiliated with Espressif. |
| [HwzLoveDz/AXP173-PMIC](https://github.com/HwzLoveDz/AXP173-PMIC) | 49 | C++ | ESP32 | AXP173 Power management IC（AXP173电源管理芯片） |
| [LucaPizzorno/esphome-touch-remote](https://github.com/LucaPizzorno/esphome-touch-remote) | 48 | — | ESP32 | Modular battery-powered touch remote for Home Assistant, built with ESPHome and LVGL on a Freenove ESP32-S3 2.8&quot; display. Pick your pages (lights, LED, Apple TV, appliances, power) and add as many entities as you like. D |
| [aleksei-severin/POV_Wheel_Display](https://github.com/aleksei-severin/POV_Wheel_Display) | 48 | Kotlin | ESP32 | Persistence of Vision (POV) display based on the ESP32-S3. This project drives a 6-arm LED rotor (SK9822-A LEDs) and features a fully autonomous BLE app for rendering static images and GIF animations, complete with advan |
| [HwzLoveDz/AXP202-PMIC](https://github.com/HwzLoveDz/AXP202-PMIC) | 47 | HTML | ESP32 | AXP202 Power management IC（AXP202电源管理芯片） |
| [bhuvanavijayaraj/Smart-Energy-Meter-Management](https://github.com/bhuvanavijayaraj/Smart-Energy-Meter-Management) | 45 | — | ESP32 | The Smart Energy Management System uses ESP32 to monitor real-time voltage, current, power, and motion data. Information is displayed on an LCD and remotely via a web dashboard and Blynk. It enables energy optimization,  |
| [Lightwell-bg/RGB-P4-Led-Matrix-Clock-based-on-ESP32](https://github.com/Lightwell-bg/RGB-P4-Led-Matrix-Clock-based-on-ESP32) | 44 | C | ESP32 | “RGB P4 Led Matrix Clock  based on ESP32” is a multifunctional clock with functions of displaying weather, weather forecast, receiving news feed, displaying any given information at the appointed time. Management is carr |

<a id="cat-security-crypto"></a>
## Security, Crypto & OTA
**Безпека, криптографія та OTA**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [rednblkx/HomeKey-ESP32](https://github.com/rednblkx/HomeKey-ESP32) | 1.1k | C++ | Arduino | ESP32 HomeKit Lock with support for Apple Home Key (reverse-engineered) |
| [ayushsharma82/ElegantOTA](https://github.com/ayushsharma82/ElegantOTA) | 1.0k | C++ | ESP32 | The original over-the-air update library for wireless microcontrollers (since 2019). |
| [krauseler/muxcard](https://github.com/krauseler/muxcard) | 1.0k | — | Arduino | A literal credit-card sized computer with E-Paper display,  ESP32 and NFC. |
| [lukeswitz/AntiHunter](https://github.com/lukeswitz/AntiHunter) | 725 | C++ | ESP32 | AntiHunter Perimeter Defense Systems - DIGI Node Firmware |
| [polhenarejos/pico-hsm](https://github.com/polhenarejos/pico-hsm) | 592 | C | ESP32 | Hardware Security Module (HSM) for Raspberry Pico and ESP32 |
| [Chrismettal/flipper-zero-backpacks](https://github.com/Chrismettal/flipper-zero-backpacks) | 454 | C++ | ESP32 | Backpack-style addon boards for the Flipper Zero! |
| [Fishwaldo/esp_ghota](https://github.com/Fishwaldo/esp_ghota) | 448 | C | ESP32 | esp32 OTA Component to update firmware from Github Releases |
| [scottchiefbaker/ESP-WebOTA](https://github.com/scottchiefbaker/ESP-WebOTA) | 440 | C++ | ESP32 | Simple web based Over-the-Air (OTA) updates for ESP based projects |
| [ESP32-Musings/OTA_update_STM32_using_ESP32](https://github.com/ESP32-Musings/OTA_update_STM32_using_ESP32) | 436 | Python | ESP32 | Program STM32Fxx MCUs Over-the-Air using ESP32 |
| [chrisjoyce911/esp32FOTA](https://github.com/chrisjoyce911/esp32FOTA) | 422 | C++ | ESP32 | Experiments in firmware OTA updates for ESP32 dev boards |
| [DavyLandman/AESLib](https://github.com/DavyLandman/AESLib) | 366 | C | Arduino | Arduino Library for AES Encryption (source based on avr-crypto-lib) |
| [don/NDEF](https://github.com/don/NDEF) | 313 | C++ | Arduino | NDEF Library for Arduino. Read and Write NDEF Messages to NFC tags with Arduino. |
| [fbiego/ESP32_BLE_OTA_Arduino](https://github.com/fbiego/ESP32_BLE_OTA_Arduino) | 279 | C++ | ESP32 | OTA update on ESP32 via BLE |
| [MatthewKuKanich/ChimeraBLE](https://github.com/MatthewKuKanich/ChimeraBLE) | 271 | C++ | ESP32 | Advanced BLE security &amp; reverse-engineering tool for ESP32: scan, GATT dump, HID decode, clone/emulate, foxhunt, and MITM - via serial CLI or Cardputer UI. |
| [ElectronicCats/HunterCatNFC](https://github.com/ElectronicCats/HunterCatNFC) | 234 | C++ | Arduino | The Hunter Cat NFC is the latest security tool for contactless (Near Field Communication) used in access control, identification and bank cards. Specially created to identify NFC readers and sniffing tools, with this too |
| [D3CRYPT-1/Infiltra-Firmware](https://github.com/D3CRYPT-1/Infiltra-Firmware) | 207 | C++ | ESP32 | Infiltra Firmware is an open-source firmware for wireless security testing, network analysis, and hardware hacking. FLASH IT BELOW USING OUR WEB FLAHSER! |
| [ElectronicCats/BomberCat](https://github.com/ElectronicCats/BomberCat) | 186 | HTML | Arduino | BomberCat is the latest security tool that combines the most common card technologies: NFC technology (Near Field Communication) and magnetic stripe technology used in access control, identification, and banking cards. S |
| [classycodeoss/esp32-ota-https](https://github.com/classycodeoss/esp32-ota-https) | 165 | C | ESP32 | Secure over-the-air updates for the ESP32 platform |
| [giovi321/smalltv-mod](https://github.com/giovi321/smalltv-mod) | 154 | C++ | ESP32 | Custom firmware for the GeekMagic SmallTV that replaces the stock apps with five modes: a stock/crypto ticker, a Claude usage meter, a live plane radar, a Home Assistant driven display and a clock with themes. Also, you  |
| [turfptax/ugit](https://github.com/turfptax/ugit) | 145 | Python | ESP32 | Micropython OTA update from github  |
| [XaviTorello/mifare-classic-toolkit](https://github.com/XaviTorello/mifare-classic-toolkit) | 116 | Arduino | Arduino | RFID / NFC :: Mifare Classic 1k info and tools |
| [soonuse/pn532-lib](https://github.com/soonuse/pn532-lib) | 107 | C | Arduino | PN532 NFC Library for Raspberry Pi, STM32, Arduino |
| [abderraouf-adjal/ArduinoSpritzCipher](https://github.com/abderraouf-adjal/ArduinoSpritzCipher) | 76 | C | Arduino | Spritz encryption system portable C library, CSPRNG, cryptographic hash and MAC functions, symmetric-key data encryption, and general-purpose functions.  It&#x27;s also an Arduino library. |
| [unsurv/unsurv-offline](https://github.com/unsurv/unsurv-offline) | 72 | C++ | Arduino | Offline portable GNSS device based on the ESP32 |
| [esp-rs/mbedtls-rs](https://github.com/esp-rs/mbedtls-rs) | 58 | Rust | ESP32 | Rust wrappers for MbedTLS |

<a id="cat-games-graphics"></a>
## Games & Graphics
**Ігри та графіка**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [adafruit/Adafruit-GFX-Library](https://github.com/adafruit/Adafruit-GFX-Library) | 2.9k | C | Arduino | Adafruit GFX graphics core Arduino library, this is the &#x27;core&#x27; class that all our other graphics libraries derive from |
| [lemmingDev/ESP32-BLE-Gamepad](https://github.com/lemmingDev/ESP32-BLE-Gamepad) | 1.6k | C++ | ESP32 | Bluetooth LE Gamepad library for the ESP32 |
| [ducalex/retro-go](https://github.com/ducalex/retro-go) | 1.4k | C | ESP32 | Retro emulation for the ODROID-GO and other ESP32 devices |
| [olikraus/u8glib](https://github.com/olikraus/u8glib) | 1.3k | C | Arduino | Arduino Monochrom Graphics Library for LCDs and OLEDs |
| [rossumur/esp_8_bit](https://github.com/rossumur/esp_8_bit) | 1.2k | C | ESP32 | Atari 8 bit computers, NES and SMS game consoles on your TV with nothing more than a ESP32 and a sense of nostalgia |
| [mikroverk/esp32sim](https://github.com/mikroverk/esp32sim) | 1.1k | Rust | ESP32 | Open-source ESP32 emulator. Run real firmware locally or in your browser — no hardware, no cloud, no subscription. |
| [hchunhui/tiny386](https://github.com/hchunhui/tiny386) | 755 | C | ESP32 | tiny 386 PC emulator; running win9x on esp32 |
| [retro-esp32/RetroESP32](https://github.com/retro-esp32/RetroESP32) | 744 | C | ESP32 | Retro ESP32 is a turbo charged Odroid Go Launcher, Emulator and ROM Manager |
| [lcgamboa/picsimlab](https://github.com/lcgamboa/picsimlab) | 680 | C++ | ESP32 | PICSimLab - Programmable IC Simulator Laboratory ⚠️ Please note: The official distribution of the PICSimLab simulator binaries is available on github.com and SourceForge.net. Be cautious of unofficial sites, such as pics |
| [espressif/esp32-nesemu](https://github.com/espressif/esp32-nesemu) | 638 | C | ESP32 | Proof-of-concept NES emulator for the ESP32 |
| [Shim06/Anemoia-ESP32](https://github.com/Shim06/Anemoia-ESP32) | 618 | C++ | ESP32 | A performant NES emulator for the ESP32 |
| [pebri86/esplay-retro-emulation](https://github.com/pebri86/esplay-retro-emulation) | 530 | C | ESP32 | Retro Emulation Collection for ESPlay Hardware, an ESP32 based game console |
| [cifertech/TamaFi](https://github.com/cifertech/TamaFi) | 476 | C | ESP32 | TamaFi is an open-source, WiFi-enabled virtual pet project built with an ESP32-s3 |
| [mofosyne/arduino-gameboy-printer-emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) | 366 | C++ | Arduino | Code to emulate a gameboy printer via the gameboy link cable |
| [r00li/CarCluster](https://github.com/r00li/CarCluster) | 278 | C | ESP32 | Control car instrument clusters from your computer for gaming or other purposes using ESP32 |
| [EstebanFuentealba/MALVEKE-Flipper-Zero](https://github.com/EstebanFuentealba/MALVEKE-Flipper-Zero) | 277 | C | ESP32 | GAME BOY Tools for Flipper Zero. The perfect companion for your Flipper Zero. Equipped with ESP32-S2 for WiFi. MALVEKE allows you to connect all GAME BOY peripherals and additional accessories such as NRF24, CC1101, and  |
| [garagetinkering/Video_Game_Mini_Maps](https://github.com/garagetinkering/Video_Game_Mini_Maps) | 266 | C | ESP32 | A small app for the ESP32-P4 that allows you to display local live (offline) mapping |
| [pebri86/esplay_micro_hardware](https://github.com/pebri86/esplay_micro_hardware) | 261 | Prolog | ESP32 | Micro version of esplay hardware, ESP32 based gaming console |
| [lualiliu/esp32-gameboy](https://github.com/lualiliu/esp32-gameboy) | 247 | C | Arduino | ESP32 Gameboy emulation based on Arduino |
| [drhelius/arduinogameboy](https://github.com/drhelius/arduinogameboy) | 171 | C++ | Arduino | Arduino based Game Boy cartridge reader and writer. It can dump ROM and RAM to SD card. |
| [GoergPflug/AttinyStreamGfxApi](https://github.com/GoergPflug/AttinyStreamGfxApi) | 159 | C | Arduino | Fast Graphics Library for Attiny85 and SSD1306 over I2c |
| [RudolphRiedel/FT800-FT813](https://github.com/RudolphRiedel/FT800-FT813) | 152 | C | Arduino | Multi-Platform C code Library for EVE graphics controllers from FTDI / Bridgetek (FT810, FT811, FT812, FT813, BT815, BT816, BT817, BT818) |

<a id="cat-weather-environment"></a>
## Weather & Environment
**Погода та довкілля**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [mfactory-osaka/ESPTimeCast](https://github.com/mfactory-osaka/ESPTimeCast) | 1.6k | C++ | Cross-platform | ESPTimeCast™ is a sleek, WiFi-connected LED matrix clock and weather display built on ESP8266/ESP32 and MAX7219. It combines real-time NTP time sync, live OpenWeatherMap updates, and a modern web-based configuration inte |
| [ThingPulse/esp8266-weather-station](https://github.com/ThingPulse/esp8266-weather-station) | 1.1k | C++ | ESP8266 | ESP8266 Weather Station library supporting OpenWeatherMap, Aeris and other sources |
| [meteostat/meteostat](https://github.com/meteostat/meteostat) | 666 | Python | Cross-platform | Access and analyze historical weather and climate data with Python. |
| [vbguyny/ws4kp](https://github.com/vbguyny/ws4kp) | 596 | JavaScript | Cross-platform | WeatherStar 4000+ |
| [n0bel/PiClock](https://github.com/n0bel/PiClock) | 588 | Python | Cross-platform | A Fancy Clock built around a monitor and a Raspberry Pi |
| [earthobservations/wetterdienst](https://github.com/earthobservations/wetterdienst) | 455 | Python | Cross-platform | Open weather data for humans. |
| [hugokernel/esphome-weather-station](https://github.com/hugokernel/esphome-weather-station) | 344 | OpenSCAD | ESP32 | ESPHome version of Elektor weather station v2 |
| [naofireblade/homebridge-weather-plus](https://github.com/naofireblade/homebridge-weather-plus) | 329 | JavaScript | Cross-platform | A comprehensive weather plugin for homebridge. |
| [poblabs/weewx-belchertown](https://github.com/poblabs/weewx-belchertown) | 224 | Python | Cross-platform | A clean and modern weewx skin with real time streaming updates, forecast data and interactive charts. View it in action at BelchertownWeather.com |
| [bruxy70/Home-Assistant-ESPHome-Weather-Station](https://github.com/bruxy70/Home-Assistant-ESPHome-Weather-Station) | 186 | — | ESP8266 | Nextion display with ESP8266 microcontroller (Wemos D1 mini) showing Home Assistant temperature sensors and weather forecast |
| [duck531a98/esp8266-weather-station-epaper](https://github.com/duck531a98/esp8266-weather-station-epaper) | 183 | C++ | ESP8266 | use esp8266 to show weather forecast on 2.9inch e-paper |
| [TheAustrian/Wemos-D1-Mini-BME280-Weather-Station](https://github.com/TheAustrian/Wemos-D1-Mini-BME280-Weather-Station) | 161 | JavaScript | ESP8266 | Simple Weather Station Code using an ESP8266 and a BME280 sensor. Data is handled via PHP and stored in a MySQL database |
| [byte4geek/weatherstation](https://github.com/byte4geek/weatherstation) | 154 | C++ | ESP8266 | A feature-rich, high-precision ESP8266-based Smart Weather Station with a modern responsive Web Dashboard, dynamic sensor detection, customizable moving-average filters, Home Assistant MQTT Auto-Discovery, full backup/re |
| [3KUdelta/Solar_WiFi_Weather_Station](https://github.com/3KUdelta/Solar_WiFi_Weather_Station) | 117 | C++ | ESP8266 | Based on the work of Open Green Energy: First solar Zambretti Forecaster |
| [NC22/Volna42BW](https://github.com/NC22/Volna42BW) | 93 | C | ESP32 | Weather station Volna 42BW, Arduino Framework, ESP8266 or ESP32 |
| [artem-smotrakov/esp32-weather-google-sheets](https://github.com/artem-smotrakov/esp32-weather-google-sheets) | 74 | Python | ESP32 | Weather station based on ESP32 and MicroPython with sending data to Google Sheets |
| [HomeKidd/ESP8266-HomeKit-Weather-Station-BME280-Elgato-Eve](https://github.com/HomeKidd/ESP8266-HomeKit-Weather-Station-BME280-Elgato-Eve) | 73 | — | ESP8266 | ESP8266 based  HomeKit Weather Station using Bosch BME280 temperature, humidity, barometric pressure sensor🔥 🌡 |
| [mayaculpa/hapi](https://github.com/mayaculpa/hapi) | 70 | Python | ESP32 | Hydro­ponic Automa­tion Plat­form Ini­tia­tive (HAPI) |
| [neptune2/esp8266-weather-station-oled-DST](https://github.com/neptune2/esp8266-weather-station-oled-DST) | 65 | Objective-C | ESP8266 | Customized version of Squix78 ESP8266 OLED Weather Station w/ Auto Daylight Saving Time Adjust and other mods using SSD1306 OLED. See https://github.com/squix78/esp8266-weather-station for original code and library  |
| [kndnsow/Roomy](https://github.com/kndnsow/Roomy) | 57 | C++ | ESP8266 | A simple but multi controller IOT project with ESP8266 for Aquarium Light and Filter/oxygenator control. |
| [AndroidCrypto/ESP32_CYD_Weather_Station_With_Forecast](https://github.com/AndroidCrypto/ESP32_CYD_Weather_Station_With_Forecast) | 53 | C++ | ESP32 | A internet based Weather Station is running on a Cheap Yellow Display (CYD) device. The data is retrieved from OpenWeatherMap.org for an individual location. |
| [ThingPulse/esp32-weather-station-touch](https://github.com/ThingPulse/esp32-weather-station-touch) | 51 | C | ESP32 | Sample application for the ThingPulse ESP32 Color Kit Grande |
| [alvarowolfx/weather-station-gcp-mongoose-os](https://github.com/alvarowolfx/weather-station-gcp-mongoose-os) | 49 | JavaScript | ESP32 | A Weather station made with an ESP32, sending data through Google Cloud IoT Core and storing in BigQuery |
| [educ8s/Arduino-Color-E-Paper-Weather-Station](https://github.com/educ8s/Arduino-Color-E-Paper-Weather-Station) | 47 | C | ESP32 | ESP32 Arduino Color E Paper Weather Station project |
| [vladkorotnev/plasma-clock](https://github.com/vladkorotnev/plasma-clock) | 41 | C++ | ESP32 | Plasma dot matrix display based wall clock/weather station/etc, powered by an ESP32 |

<a id="cat-awesome-collections"></a>
## Meta Collections (Awesome lists)
**Мета-збірки (Awesome-списки)**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [nhivp/Awesome-Embedded](https://github.com/nhivp/Awesome-Embedded) | 9.3k | — | meta | A curated list of awesome embedded programming. |
| [rust-embedded/awesome-embedded-rust](https://github.com/rust-embedded/awesome-embedded-rust) | 8.2k | — | meta | Curated list of resources for Embedded and Low-level development in the Rust programming language |
| [alphaSeclab/awesome-reverse-engineering](https://github.com/alphaSeclab/awesome-reverse-engineering) | 5.2k | — | meta | Reverse Engineering Resources About All Platforms(Windows/Linux/macOS/Android/iOS/IoT) And Every Aspect! (More than 3500 open source tools and 2300 posts&amp;videos) |
| [phodal/awesome-iot](https://github.com/phodal/awesome-iot) | 4.6k | Python | meta | Awesome IoT. A collaborative list of great resources about IoT Framework, Library,  OS, Platform |
| [HQarroum/awesome-iot](https://github.com/HQarroum/awesome-iot) | 4.5k | — | meta | 🤖 A curated list of awesome Internet of Things projects and resources. |
| [iDoka/awesome-canbus](https://github.com/iDoka/awesome-canbus) | 3.5k | — | meta | :articulated_lorry: Awesome CAN bus tools, hardware and resources for Cyber Security Researchers, Reverse Engineers, and Automotive Electronics Enthusiasts. |
| [fkie-cad/awesome-embedded-and-iot-security](https://github.com/fkie-cad/awesome-embedded-and-iot-security) | 2.5k | — | meta | A curated list of awesome embedded and IoT security resources. |
| [nebgnahz/awesome-iot-hacks](https://github.com/nebgnahz/awesome-iot-hacks) | 2.4k | — | meta | A Collection of Hacks in IoT Space so that we can address them (hopefully). |
| [esp-rs/awesome-esp-rust](https://github.com/esp-rs/awesome-esp-rust) | 1.7k | — | meta | Curated list of resources for ESP32 development in the Rust programming language |
| [iDoka/awesome-embedded-software](https://github.com/iDoka/awesome-embedded-software) | 1.1k | — | meta | :stars: List of software (HW interfaces, libs, protocols, etc) specifically suitable for resource-constrained Embedded Systems (low-memory and low-power) like 8-bit, 16-bit and 32-bit microcontrollers. |
| [Lembed/Awesome-arduino](https://github.com/Lembed/Awesome-arduino) | 731 | Shell | meta | A curated list of awesome Arduino hardwares, libraries and softwares with update script |
| [s0lness/awesome-esp32](https://github.com/s0lness/awesome-esp32) | 705 | — | meta | Hand-picked ESP32 projects worth building, copying, or watching run |
| [iDoka/awesome-linbus](https://github.com/iDoka/awesome-linbus) | 249 | — | meta | :articulated_lorry: An awesome LIN bus tools, hardware and resources. It helps a reverse engineering LIN bus devices with lightly specializing in automotive embedded controller software and communication understanding. |
| [golioth/awesome-zephyr-rtos](https://github.com/golioth/awesome-zephyr-rtos) | 230 | — | meta | 🪁 A curated list of awesome projects and resources for the Zephyr RTOS project. |
| [Luyi365/awesome-embedded](https://github.com/Luyi365/awesome-embedded) | 227 | — | meta | 嵌入式开源库速查表，快速定位所需功能。300+ libraries for embedded dev, modularly organized, covering the common ground. |

<a id="cat-other-platforms"></a>
## Other Boards (Pico, STM32, micro:bit, nRF52...)
**Інші плати**

| Repository | ⭐ | Lang | Board | Description |
|---|---|---|---|---|
| [OpenStickCommunity/GP2040-CE](https://github.com/OpenStickCommunity/GP2040-CE) | 2.6k | C++ | RP2040 | Multi-Platform Gamepad Firmware for Raspberry Pi Pico and other RP2040 boards |
| [MaJerle/stm32f429](https://github.com/MaJerle/stm32f429) | 2.5k | C | STM32 | Keil projects and libraries for STM32F4xx devices |
| [rmk-rs/rmk](https://github.com/rmk-rs/rmk) | 1.8k | Rust | RP2040 | A modern, easy-to-use, and feature-rich keyboard firmware written in Rust. |
| [kritishmohapatra/100_Days_100_IoT_Projects](https://github.com/kritishmohapatra/100_Days_100_IoT_Projects) | 1.6k | Python | RP2040 | A 100-day challenge exploring IoT and embedded systems using ESP32, ESP8266, and Raspberry Pi Pico with MicroPython. Each day covers a new sensor or module with complete code, circuit diagram, and explanation. |
| [WeebLabs/DSPi](https://github.com/WeebLabs/DSPi) | 1.4k | C | RP2040 | A fully featured audio DSP firmware for the Raspberry Pi Pico (RP2040) and Pico 2 (RP2350).  Official Discord: https://discord.gg/RCyqxAQ5xS |
| [STMicroelectronics/STM32CubeF4](https://github.com/STMicroelectronics/STM32CubeF4) | 1.4k | C | STM32 | STM32Cube MCU Full Package for the STM32F4 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)) |
| [raspberrypi/debugprobe](https://github.com/raspberrypi/debugprobe) | 1.3k | C | RP2040 | Firmware source and binaries for the RP2040-based Debug Probe accessory |
| [swiftlang/swift-embedded-examples](https://github.com/swiftlang/swift-embedded-examples) | 1.0k | Swift | STM32 | A collection of example projects using Embedded Swift |
| [STMicroelectronics/STM32CubeH7](https://github.com/STMicroelectronics/STM32CubeH7) | 778 | C | STM32 | STM32Cube MCU Full Package for the STM32H7 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)) |
| [MYaqoobEmbedded/STM32-Tutorials](https://github.com/MYaqoobEmbedded/STM32-Tutorials) | 757 | C | STM32 | This folder contains all my STM32 programming projects shared on YouTube |
| [STMicroelectronics/STM32CubeF1](https://github.com/STMicroelectronics/STM32CubeF1) | 749 | HTML | STM32 | STM32Cube MCU Full Package for the STM32F1 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)) |
| [STMicroelectronics/STM32Cube_MCU_Overall_Offer](https://github.com/STMicroelectronics/STM32Cube_MCU_Overall_Offer) | 739 | — | STM32 | This repo describes all STM32 MCU related GitHub projects. The open source offer for the STM32 MCU products |
| [zacharyweiss/magspoof_flipper](https://github.com/zacharyweiss/magspoof_flipper) | 734 | C | STM32 | Port of Samy Kamkar&#x27;s MagSpoof project (http://samy.pl/magspoof/) to the Flipper Zero. Enables wireless emulation of magstripe data, primarily over GPIO, with additional experimental internal TX. |
| [ffenix113/zigbee_home](https://github.com/ffenix113/zigbee_home) | 672 | Go | nRF52 | Project to provide functionality similar to ESPHome but for Zigbee instead of WiFi for nRF52, nRF53 &amp; nRF54L |
| [mcknly/breadboard-os](https://github.com/mcknly/breadboard-os) | 602 | C | RP2040 | A firmware platform aimed at quick prototyping, built around FreeRTOS and a feature-packed CLI |
| [picoruby/prk_firmware](https://github.com/picoruby/prk_firmware) | 597 | C | RP2040 | A keyboard firmware platform in PicoRuby |
| [controllerstech/STM32-HAL](https://github.com/controllerstech/STM32-HAL) | 472 | C | STM32 | STM32 Projects |
| [heliosproj/HeliOS](https://github.com/heliosproj/HeliOS) | 413 | C | Teensy | A community delivered, open source embedded operating system project. |
| [paulober/MicroPico](https://github.com/paulober/MicroPico) | 393 | TypeScript | RP2040 | MicroPico (aka Pico-W-Go) is a Visual Studio Code extension designed to simplify and speed up the development of MicroPython projects for the Raspberry Pi Pico (2) and Pico (2) W boards. |
| [raspberrypi/pico-vscode](https://github.com/raspberrypi/pico-vscode) | 300 | TypeScript | RP2040 | The official VS Code extension for Raspberry Pi Pico development. It includes several features to simplify project creation and deployment. |
| [r-morato/HASS-epaper-display](https://github.com/r-morato/HASS-epaper-display) | 283 | — | ESP32-C3 | This project displays key smart home and server stats on a 7.5&quot; e-paper screen using an ESP32-C3 board running ESPHome. |
| [dawsonjon/101Things](https://github.com/dawsonjon/101Things) | 231 | G-code | RP2040 | A collection of cool projects to make! |
| [espressif/book-esp32c3-iot-projects](https://github.com/espressif/book-esp32c3-iot-projects) | 191 | Swift | ESP32-C3 | 《ESP32-C3 物联网工程开发实战》配套代码 |

---

## 🤝 Contributing

Found a great repo that's missing? Open an issue or PR with: repo URL, target category, and one-line description. Quality bar: active (non-archived), ≥40 stars, real code (not just docs).

## 🔁 How the index is built

- Data collected automatically via the official **GitHub Search API** (`tools/collect.py`, results in `data/repos.json`).
- Filters: stars ≥ 40, not archived, deduplicated across categories. Snapshot date: **2026-11-05**.
- Categories are grouped **by functionality** (display, sensors, connectivity, IoT, audio, robotics...) so you search by what you want to build, not by board name.

## 📄 License

This index: MIT. The linked projects keep their own licenses — check each repo before reuse.
