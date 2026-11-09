# project-barbariki
A lightweight, autonomous full-screen multimedia kiosk application built on PyQt6 and WinAPI hooks for educational research and social experiments.
# PyQt6 Fullscreen Multimedia Kiosk Application

[**English**](#english) | [**Русский**](#русский)

---

## English

An autonomous, ultra-lightweight kiosk media application built with **Python 3.13** and **PyQt6**. This project serves as an educational showcase of low-level OS interaction, Windows hook implementations (`WH_KEYBOARD_LL`), and hardware-accelerated media rendering without relying on third-party video decoders.

### ⚙️ Features
* **Native Media Pipeline:** Uses Windows Media Foundation via PyQt6 for hardware-accelerated, lag-free loop playback.
* **Aggressive Focus Locking:** Keeps the application window strictly on top using native OS flags (`WindowStaysOnTopHint`), preventing unauthorized multitasking.
* **Low-Level Key Invalidation:** Intercepts system modifier keys (`Alt`, `Tab`, `Win`, `F1-F12`) at the OS level to maintain an uninterrupted kiosk state.
* **Automated Audio Leveling:** Dynamically configures the Windows master mixer to exactly 10% volume upon execution via Pycaw.
* **Zero-Admin Architecture:** Executes seamlessly within standard user privileges (no UAC prompt required on stock Windows configurations).
* **Hardcoded Self-Destruct:** Completely unhooks all system intercepts and terminates cleanly after exactly 178 seconds.

### 🚀 Technical Requirements
* **OS:** Windows 10 / 11 (64-bit)
* **Language environment:** Python 3.13+

### 🛠️ Dependency Installation
```bash
pip install PyQt6 pycaw keyboard
```

### 📦 Standalone Compilation Guide (Nuitka + UPX)
To compile the script into a tightly compressed, single executable with embedded media assets, make sure `upx.exe` is placed inside the project folder, then run:

```bash
python -m nuitka --onefile --onefile-no-compression --windows-console-mode=disable --enable-plugin=pyqt6 --enable-plugin=upx --upx-binary="upx.exe" --remove-output --include-data-files=video.mp4=video.mp4 "GET FREE ROBUX.py"
```
*Compiles down from ~122 MB to an optimized **34 MB** binary package.*

---

## Русский

Автономное, легковесное медиа-приложение для информационных киосков, разработанное на **Python 3.13** и **PyQt6**. Проект создан исключительно в образовательных целях для демонстрации низкоуровневого взаимодействия с ОС Windows, работы с глобальными хуками (`WH_KEYBOARD_LL`) и аппаратного декодирования медиапотоков без использования тяжелых сторонних плееров.

### ⚙️ Функционал и Особенности
* **Нативный медиа-движок:** Использует Windows Media Foundation через PyQt6 для плавного зацикленного воспроизведения без задержек.
* **Агрессивное удержание фокуса:** Принудительно удерживает окно поверх всех остальных окон с помощью флагов ОС (`WindowStaysOnTopHint`).
* **Низкоуровневая блокировка клавиш:** Перехватывает системные клавиши-модификаторы (`Alt`, `Tab`, `Win`, ряд `F1-F12`) на уровне операционной системы для защиты режима киоска.
* **Автоматическое управление звуком:** При запуске выставляет главный микшер Windows ровно на 10% громкости с помощью библиотеки Pycaw.
* **Запуск без прав администратора:** Работает в стандартном пользовательском контексте безопасности (UAC-окно не вызывается).
* **Таймер самоликвидации:** Скрипт полностью снимает все перехваты клавиатуры и завершает процесс ровно через 178 секунд.

### 🚀 Системные требования
* **ОС:** Windows 10 / 11 (64-bit)
* **Версия Python:** 3.13+

### 🛠️ Установка необходимых библиотек
```bash
pip install PyQt6 pycaw keyboard
```

### 📦 Компиляция в автономный .exe файл (Nuitka + UPX)
Чтобы собрать скрипт в один файл, вшив видео внутрь и максимально сжав бинарные библиотеки Qt, положите утилиту `upx.exe` в папку с проектом и выполните команду:

```bash
python -m nuitka --onefile --onefile-no-compression --windows-console-mode=disable --enable-plugin=pyqt6 --enable-plugin=upx --upx-binary="upx.exe" --remove-output --include-data-files=video.mp4=video.mp4 "GET FREE ROBUX.py"
```
*Сжимает итоговый исполняемый пакет со ~122 МБ до оптимизированных **34 МБ**.*

---
**Disclaimer:** *This repository is published for educational and research purposes only. The author is not responsible for any misuse or unauthorized modifications of the provided source code.*
