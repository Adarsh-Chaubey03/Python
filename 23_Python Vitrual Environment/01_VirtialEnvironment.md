# 🐍 Python Virtual Environment Cheatsheet

A quick reference guide for managing Python virtual environments.

---

## 🔧 Create a Virtual Environment

```bash
python -m venv env_name
```

---

## 🚀 Activate the Virtual Environment

- **Linux / macOS**:

  ```bash
  source env_name/bin/activate
  ```

- **Windows**:

  ```powershell
  .\env_name\Scripts\activate
  ```

---

## 📦 Install Packages

```bash
pip install package_name
```

---

## 📝 Save Installed Packages

Generate a list of installed packages:

```bash
pip freeze > requirements.txt
```

*Alternative (equivalent):*

```bash
pip freeze > requirements.txt

```

---

## 📂 Install from Requirements File

```bash
pip install -r requirements.txt
```

---

## ❌ Deactivate the Environment

```bash
deactivate
```

---

> 💡 **Tip:** Always use a virtual environment to avoid conflicts between project dependencies.
