import os
import time
import sys
from datetime import datetime

# Zyvola Premium kiber-yashil neon dizayn tizimi
class ZyvolaDesign:
    NEON_GREEN = '\033[38;5;46m'   # [████] - Premium Kvadrat (Radikal)
    EMERALD    = '\033[38;5;120m'  # ( ◯ ◯ ) - Zumrad Doira (Yaxshi)
    DEEP_GREEN = '\033[38;5;34m'   # ▲▲▲▲   - O'rmon Uchburchagi (Normal)
    WARN_GRAY  = '\033[90m'        # ❖❖❖❖   - Xira Romb (Yomon)
    FAIL_RED   = '\033[91m'        # ✦✦✦✦   - Qizil Yulduz (Ujasno)
    
    CYAN_TECH   = '\033[96m'
    WHITE_TEXT  = '\033[97m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'

# Chiroyli kiber-yashil ZYVOLA Logotipi (ASCII Art)
ZYVOLA_LOGO = f"""{ZyvolaDesign.NEON_GREEN}{ZyvolaDesign.BOLD}
 ███████╗██╗   ██╗██╗   ██╗ ██████╗ ██╗      ████╗ 
 ╚══███╔╝╚██╗ ██╔╝██║   ██║██╔═══██╗██║     ██╔══██╗
   ███╔╝  ╚████╔╝ ██║   ██║██║   ██║██║     ███████║
  ███╔╝    ╚██╔╝  ╚██╗ ██╔╝██║   ██║██║     ██╔══██║
 ███████╗   ██║    ╚████╔╝ ╚██████╔╝███████╗██║  ██║
 ╚══════╝   ╚═╝     ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
           PREMIUM SUBSCRIPTION CORE ENGINE v3.0
{ZyvolaDesign.ENDC}"""

def matrix_loader(text, duration=1.0, status_type="active"):
    sys.stdout.write(ZyvolaDesign.CYAN_TECH + text + " ")
    chars = ["◢", "◣", "◤", "◥", "█", "▒"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(0.08)
        sys.stdout.write("\b")
        i += 1
    if status_type == "active":
        print(ZyvolaDesign.NEON_GREEN + " ONLINE ✓" + ZyvolaDesign.ENDC)
    else:
        print(ZyvolaDesign.EMERALD + " SUCCESS ✓" + ZyvolaDesign.ENDC)

MULTILANG = {
    "en": {
        "welcome": "=== ZYVOLA PREMIUM BILLING GATEWAY ===",
        "pin_prompt": "ENTER SECURE 4-DIGIT SECURITY PIN-CODE: ",
        "pin_success": "🔓 Access Granted. Billing Tunnel Active.",
        "menu_title": "\n=== ZYVOLA SMART HUB ===",
        "m1": "1. 📝 Log Entry", "m2": "2. 📊 View Analytics", "m3": "3. 📅 View Heatmap",
        "m4": "4. ⚙️ Settings", "m5": "5. 🌐 Server Diagnostics", "m6": "6. 💳 Premium Subscriptions", "m7": "7. 🔒 Exit",
        "select": "Execute Node (1-7): ",
        "stripe_title": "\n--- 💳 STRIPE SECURE BILLING GATEWAY ---",
        "moods": [f"{ZyvolaDesign.NEON_GREEN}[████] Radical{ZyvolaDesign.ENDC}", f"{ZyvolaDesign.EMERALD}( ◯ ◯ ) Good{ZyvolaDesign.ENDC}"],
        "acts": ["🏃‍♂️ Sport", "💼 Coding"]
    },
    "ru": {
        "welcome": "=== ZYVOLA PREMIUM ПЛАТЕЖНЫЙ ШЛЮЗ ===",
        "pin_prompt": "ВВЕДИТЕ 4-ЗНАЧНЫЙ ЗАЩИТНЫЙ ПИН-КОД: ",
        "pin_success": "🔓 Доступ разрешен. Биллинг активен.",
        "menu_title": "\n=== ZYVOLA СМАРТ ПАНЕЛЬ ===",
        "m1": "1. 📝 Добавить запись", "m2": "2. 📊 Просмотр аналитики", "m3": "3. 📅 Тепловая карта",
        "m4": "4. ⚙️ Настройки", "m5": "5. 🌐 Диагностика серверов", "m6": "6. 💳 Премиум подписки", "m7": "7. 🔒 Выход",
        "select": "Выполнить шаг (1-7): ",
        "stripe_title": "\n--- 💳 БЕЗОПАСНЫЙ ПЛАТЕЖНЫЙ ШЛЮЗ STRIPE ---",
        "moods": [f"{ZyvolaDesign.NEON_GREEN}[████] Радикал{ZyvolaDesign.ENDC}", f"{ZyvolaDesign.EMERALD}( ◯ ◯ ) Хорошо{ZyvolaDesign.ENDC}"],
        "acts": ["🏃‍♂️ Спорт", "💼 Кодинг"]
    }
}

ui_lang = "en"
vault_storage = []
system_pin = "2026"
merchant_card = "4023 0602 0886 0212"

os.system('cls' if os.name == 'nt' else 'clear')
print(ZYVOLA_LOGO)
print(ZyvolaDesign.BOLD + ZyvolaDesign.WHITE_TEXT + MULTILANG[ui_lang]["welcome"] + ZyvolaDesign.ENDC)
input_pin = input(ZyvolaDesign.BOLD + ZyvolaDesign.WHITE_TEXT + MULTILANG[ui_lang]["pin_prompt"] + ZyvolaDesign.ENDC)

if input_pin != system_pin:
    sys.exit()
else:
    matrix_loader(MULTILANG[ui_lang]["pin_success"], 1.0, "success")

while True:
    txt = MULTILANG[ui_lang]
    print(ZyvolaDesign.BOLD + ZyvolaDesign.WHITE_TEXT + txt["menu_title"] + ZyvolaDesign.ENDC)
    print(txt["m1"] + "\n" + txt["m2"] + "\n" + txt["m3"] + "\n" + txt["m4"] + "\n" + txt["m5"] + "\n" + txt["m6"] + "\n" + txt["m7"])
    action = input(ZyvolaDesign.BOLD + txt["select"] + ZyvolaDesign.ENDC)
    
    if action == "6":
        print(ZyvolaDesign.BOLD + ZyvolaDesign.CYAN_TECH + txt["stripe_title"] + ZyvolaDesign.ENDC)
        matrix_loader(" Syncing with Stripe Production Billing Endpoints...", 0.8)
        print(f"\n{ZyvolaDesign.BOLD}🔒 TARGET MERCHANT MERGE CARD: {ZyvolaDesign.NEON_GREEN}{merchant_card}{ZyvolaDesign.ENDC}")
        print(f"{ZyvolaDesign.BOLD}💰 AVAILABLE PREMIUM SUBSCRIPTION TIERS:{ZyvolaDesign.ENDC}")
        print(f"  [Tier 1] Monthly Premium Access      -> {ZyvolaDesign.EMERALD}$2.00 / month{ZyvolaDesign.ENDC}")
        print(f"  [Tier 2] 6-Month Half-Year Bundle    -> {ZyvolaDesign.EMERALD}$9.00 / 6 months{ZyvolaDesign.ENDC}")
        print(f"  [Tier 3] 1-Year Standard License     -> {ZyvolaDesign.EMERALD}$16.00 / year{ZyvolaDesign.ENDC}")
        print(f"  [Tier 4] 1-Year Zyvola Super Premium -> {ZyvolaDesign.EMERALD}$22.00 / year{ZyvolaDesign.ENDC}")
        print(f"\n{ZyvolaDesign.WARN_GRAY}Status: Live billing node established via secure tokenized merchant bridge.{ZyvolaDesign.ENDC}")
        input("\nPress Enter to return to main control panel...")
    elif action == "7":
        break
