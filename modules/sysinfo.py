import getpass
import json
import platform
import socket
import sys
from urllib.request import urlopen

from openpyxl import Workbook


def get_local_ip():
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
		try:
			connection.connect(("8.8.8.8", 80))
			return connection.getsockname()[0]
		except OSError:
			return "127.0.0.1"


def get_geolocation():
	try:
		with urlopen("https://ipapi.co/json/", timeout=5) as response:
			location = json.loads(response.read().decode("utf-8"))

		city = location.get("city") or "Desconhecida"
		region = location.get("region") or "Desconhecida"
		country = location.get("country_name") or "Desconhecido"
		return f"{city}, {region}, {country}"
	except (OSError, ValueError, KeyError, json.JSONDecodeError):
		return "Indisponível"


def get_system_info():
	return {
		"Usuário": getpass.getuser() or "Desconhecido",
		"Computador": socket.gethostname() or "Desconhecido",
		"Sistema": platform.system() or "Desconhecido",
		"Versão do sistema": platform.release() or "Desconhecido",
		"Arquitetura": platform.machine() or "Desconhecido",
		"Processador": platform.processor() or "Desconhecido",
		"Python": sys.version.split()[0],
		"IP local": get_local_ip(),
		"Geolocalização": get_geolocation(),
	}


def export_system_info(file_path="sysinfo.xlsx", info=None):
	info = info or get_system_info()
	workbook = Workbook()
	worksheet = workbook.active
	worksheet.title = "Informações do sistema"
	worksheet.append(["Informação", "Valor"])

	for nome, valor in info.items():
		worksheet.append([nome, valor])

	worksheet.column_dimensions["A"].width = 24
	worksheet.column_dimensions["B"].width = 60
	workbook.save(file_path)
	return file_path
