import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "YaBrowser/24.1.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7"
}

def get_domain_info(domain: str) -> (dict, bool):
    try:
        res = requests.head(url=f"http://{domain}", headers=headers, stream=True, allow_redirects=True, timeout=5)
        try:
            res.raise_for_status()
            ip, port = res.raw._connection.sock.getpeername()
            serv = res.headers.get("Server")
            x_powered_by = res.headers.get('X-Powered-By')
            via = res.headers.get('Via')
            return {"ip": ip, "port": port, "addr": res.url, "server": serv, "x_powered_by": x_powered_by, "via": via}
        except Exception:
            return False
    except Exception:
        return False
def main() -> None:
    domain = input("Введите домен:")
    print(get_domain_info(domain))

if __name__== "__main__":
    main()
    