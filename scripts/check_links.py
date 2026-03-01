#!/usr/bin/env python3
import requests
from pathlib import Path

def test_link(url):
    try:
        if 'youtube.com' in url or 'youtu.be' in url:
            return True, "YouTube OK"
        r = requests.head(url, timeout=5, allow_redirects=True)
        return r.status_code < 400, f"HTTP {r.status_code}"
    except:
        return False, "Falhou"

def process_playlist():
    caminho = Path("playlist_angostream.m3u")
    
    print("🔍 A testar links...")
    
    with open(caminho, 'r') as f:
        linhas = f.readlines()
    
    ok = 0
    falha = 0
    
    for linha in linhas:
        if linha.startswith('http'):
            linha = linha.strip()
            print(f"\nTestando: {linha[:50]}...")
            func, msg = test_link(linha)
            if func:
                ok += 1
                print(f"  ✅ {msg}")
            else:
                falha += 1
                print(f"  ❌ {msg}")
    
    print(f"\n✅ OK: {ok}")
    print(f"❌ Falha: {falha}")

if __name__ == "__main__":
    process_playlist()
