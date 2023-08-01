from colorama import Fore, init
from os import system
from requests import get
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor


fakeuseragent_client = UserAgent()
proxies_valid = []
user_agent = {"User-Agent": fakeuseragent_client.random}


def prints_init(proxies) -> str:
	try:
		init()
		with open("print_data.txt", "r") as file_print_data:
			data_print = file_print_data.read()
		file_print_data.close()
		system("cls||clear")
	except Exception:
		return f"\n{Fore.RED}$$${Fore.WHITE}\tDATA CORRUPTION"
		raise(Exception)
	return f"{Fore.RED}{data_print}{Fore.RED}\n\n$$${Fore.WHITE}\tTOTAL PROXIES: {len(proxies)}\n\n{Fore.RED}$$$\t{Fore.WHITE}CLOSE FILE IF YOU FINISHED(THREADS LAGG) VALID PROXY IN <proxies_valid.txt>"


def proxy_check(proxy) -> None:
	with open("proxies_valid.txt", "w") as file_valid_proxy:
		try:
			response = get(f"http://{proxy.split(':')[0]}")
			if response.status_code == 200:
				proxies_valid.append(proxy)
				file_valid_proxy.write("\n".join(proxies_valid))
				file_valid_proxy.close()
				print(f"{Fore.RED}$$$\t{Fore.WHITE}{proxy} STATUS:{Fore.GREEN} OK{Fore.WHITE}!")
		except Exception:		
			print(f"{Fore.RED}$$$\t{Fore.WHITE}{proxy} STATUS:{Fore.RED} INVALID{Fore.WHITE}!")


def main() -> None:
	try:
		with open("proxy_list.txt", "r") as file_proxy:
			proxies = file_proxy.read().split("\n")
		file_proxy.close()
	except Exception:
		print(f"\n{Fore.RED}$$${Fore.WHITE}\tNot enough proxies in <proxy_list.txt>")
		raise(Exception)
	while True:
		try:
			print(prints_init(proxies))
			threads = int(input(f"\n{Fore.RED}$$${Fore.WHITE}\tENTER THE COLLUMN OF THREADS (100-500)>>> "))
			break
		except Exception:
			print(f"\n{Fore.RED}$$${Fore.WHITE}\tEnter the number!")

	pool = ThreadPoolExecutor(max_workers=threads)
	[pool.submit(proxy_check, proxy).done() for proxy in proxies]


if __name__ == "__main__":
	main()