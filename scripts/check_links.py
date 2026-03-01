name: Robô Automático AngoStream

on:
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:
  push:
    paths:
      - 'playlist_angostream.m3u'
      - 'scripts/check_links.py'

jobs:
  verificar-links:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install requests
      - run: python scripts/check_links.py
      - run: |
          git config --global user.name "Robô"
          git config --global user.email "bot@angostream.ao"
          git add playlist_angostream.m3u
          git add relatorio.txt 2>/dev/null || true
          git diff --staged --quiet || git commit -m "Atualização automática"
          git push
