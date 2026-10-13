# 🦋 Butterfly-Launcher

**Butterfly-Launcher** is a lightweight, modern, and secure launcher developed in Python (`customtkinter`). It is designed for managing, securing, and orchestrating video game preservation builds (Fortnite Legacy Builds: v4.5, v6.21, v12.41...).

The tool simplifies running older versions while providing a clean and intuitive interface for modders, curators, and players.

---

## ✨ Key Features

* 🎮 **Version & Directory Selector:** Easily switch between builds or seasons without manually moving files around.
* 🔒 **Security & Integrity:** Built to work with sanitized setups (replacing suspicious binaries with official, original Epic Games executables).
* 🌐 **Local Server Redirection:** Automatic handling of network redirection (`127.0.0.1`) and command-line arguments (`-epicapp`, `-epicenv`, `-username`).
* 🖥️ **Unlocked UE Console (Optional):** Support for Unreal Engine developer console injection and unlocking.
* 🎨 **Modern Interface:** Dark-themed, responsive GUI designed specifically for gaming.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **GUI Framework:** `customtkinter`
* **Process Orchestration:** Native `subprocess` module
* **OS Compatibility:** Windows 10 / 11

---

## 🚀 Installation & Usage

### Prerequisites
Make sure you have Python 3.10 or higher installed on your system.

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/Butterfly-Launcher.git](https://github.com/your-username/Butterfly-Launcher.git)
cd Butterfly-Launcher

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the application
python launcher.py
