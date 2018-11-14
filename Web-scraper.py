from urllib.parse import parse_qs

x = b'GET /announce?info_hash=wl%a6%0ebd%c6%e1%92%2fU%d1%d7%a36%b9%14%a6B%df&peer_id=-UM1870-%14%ab%e6~w%28%b2%2c%e9%b7%e3%24&port=26085&uploaded=0&downloaded=0&left=315534554&corrupt=0&key=221DF570&event=started&numwant=200&compact=1&no_peer_id=1&ipv6=fe80%3a%3ac48%3a2bfe%3a1656%3a6052 HTTP/1.1\r\nHost: localhost:5555\r\nUser-Agent: uTorrentMac/1870(43796)\r\nAccept-Encoding: gzip\r\nConnection: Close\r\n\r\n'
print(x)
print(type(x))
print(x.decode('utf-8'))
print(len(x))
y = str(x)
print(y.split('&'))
print(y[0])
print(len(y))


req = parse_qs('GET /announce?info_hash=wl%a6%0ebd%c6%e1%92%2fU%d1%d7%a36%b9%14%a6B%df&peer_id=-UM1870-%14%ab%e6~w%28%b2%2c%e9%b7%e3%24&port=26085&uploaded=0&downloaded=0&left=315534554&corrupt=0&key=221DF570&event=started&numwant=200&compact=1&no_peer_id=1&ipv6=fe80%3a%3ac48%3a2bfe%3a1656%3a6052 HTTP/1.1\r\nHost: localhost:5555\r\nUser-Agent: uTorrentMac/1870(43796)\r\nAccept-Encoding: gzip\r\nConnection: Close\r\n\r\n')
print(req)


hesh = (list(req.values())[0])
print(hesh)
z = str(hesh)

# val = list(req.values())
# print(val)
# print(val[0])
# print(type(val[0]))

print(x.decode())
print(type(x))
print(x[3])
# d = parse_qs(x)
# print(d)