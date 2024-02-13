![language](https://img.shields.io/badge/python-grey?style=for-the-badge&logo=python)

![GitHub Repo stars](https://img.shields.io/github/stars/HexaCodeX/hexa-attack)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/HexaCodeX/hexa-attack?label=size)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/HexaCodeX/hexa-attack)

# Hexa Attack
an open source tool for carrying out DDOS and also provides several additional features that are useful for identifying a website

## installation

```shell
git clone https://github.com/HexaCodeX/hexa-attack
cd hexa-attack
pip install -r requirements.txt
```

## configuration
you can change the basic configuration at `~/config.json` file

```json
{
  "name": "hexa-attack",
  "author": "HexaCodeX",
  "version": "1.7.0",
  "workers": 50,
  "environment": "production",
  "useProxy": true
}
```

## how to usage

### run the program

```shell
python main.py
```

## preview

<img src="./assets/preview.jpg" alt="hexa-attack's preview" />

> built with ♥️ by HexaCodeX