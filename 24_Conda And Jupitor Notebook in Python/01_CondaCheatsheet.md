# 🐍 Conda Environment Cheatsheet

A quick reference guide for managing Python environments with **conda**.

---

## 🆕 Create a New Environment

```bash
conda create --name myenv python=3.6
```

---

## 🚀 Activate an Environment

```bash
conda activate myenv
```

---

## ❌ Deactivate an Environment

```bash
conda deactivate
```

---

## 🗑️ Delete an Environment

```bash
conda remove --name myenv --all
```

---

## 📦 Install a Package

```bash
conda install --name myenv numpy
```

---

## 📋 List Packages in an Environment

```bash
conda list --name myenv
```

---

## 🌐 List All Environments

```bash
conda info --envs
```

---

> 💡 **Tip:** Use `conda env export > environment.yml` to save your environment, and `conda env create -f environment.yml` to recreate it.

