#!/usr/bin/env python3
"""Curation pass over data/repos.json: remove off-topic repos, move misplaced ones."""
import json

REMOVE = {
    # off-topic meta lists
    "fighting41love/funNLP", "Awesome-HarmonyOS/HarmonyOS", "jakejarvis/awesome-shodan-queries",
    "benedekrozemberczki/awesome-graph-classification", "ttt30ga/awesome-product-design",
    "chihming/awesome-network-embedding",
    "guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising",
    "Hironsan/awesome-embedding-models", "barthap/expo-mega-demo",
    "Awesome-Embedded-Learning-Studio/Tutorial_AwesomeModernCPP",
    # not board code
    "rhaiscript/rhai",
    # Switch modchip firmware (device-specific hacking, off-topic for a general archive)
    "Ansem-SoD/Picofly",
    # junk / stale duplicates
    "Guitarman9119/Raspberry-Pi-Pico-", "maniacbug/RF24", "gnea/grbl",
}

# full_name -> (from_cat, to_cat)
MOVE = {
    "davidmonterocrespo24/velxio": ("games-graphics", "frameworks-cores"),
    "makerspet/oomwoo": ("iot-home-automation", "robotics-motors"),
    "TMRh20/TMRpcm": ("power-storage", "audio"),
    "Sukecz/esp32-birdnet-mic": ("power-storage", "audio"),
    "Bodmer/TFT_eSPI": ("frameworks-cores", "displays-ui"),
    "PetoiCamp/OpenCat-Quadruped-Robot": ("frameworks-cores", "robotics-motors"),
    "pschatzmann/ESP32-A2DP": ("frameworks-cores", "audio"),
    "1technophile/OpenMQTTGateway": ("frameworks-cores", "iot-home-automation"),
    "bitbank2/Thermal_Printer": ("games-graphics", "displays-ui"),
    "trash80/Arduinoboy": ("games-graphics", "audio"),
}

def main():
    with open("data/repos.json", encoding="utf-8") as f:
        data = json.load(f)
    removed, moved = [], []
    for cat in list(data):
        kept = []
        for r in data[cat]:
            fn = r["full_name"]
            if fn in REMOVE:
                removed.append(fn)
                continue
            if fn in MOVE and MOVE[fn][0] == cat:
                r["platform"] = r["platform"]  # unchanged
                moved.append((fn, cat, MOVE[fn][1]))
                data[MOVE[fn][1]].append(r)
                continue
            kept.append(r)
        data[cat] = kept
    for cat in data:
        seen, uniq = set(), []
        for r in data[cat]:
            if r["full_name"] in seen:
                continue
            seen.add(r["full_name"])
            uniq.append(r)
        uniq.sort(key=lambda r: -r["stars"])
        data[cat] = uniq[:30]
    with open("data/repos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"removed {len(removed)}: {removed}")
    print(f"moved {len(moved)}: {[m[0] for m in moved]}")
    print(f"totals: { {k: len(v) for k, v in data.items()} }, sum={sum(len(v) for v in data.values())}")

if __name__ == "__main__":
    main()
