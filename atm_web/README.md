ATM Web (static)

Open `index.html` in Google Chrome, or serve the `atm_web` folder with a simple HTTP server and visit `http://localhost:8000/atm_web/`.

To serve using Python (from the workspace root):

```bash
cd /Users/aayushsagar/github/python-scripts/atm_web
python3 -m http.server 8000
# then open http://localhost:8000/ in Chrome and click index.html
```

Notes:
- Default demo PIN is `1234` (change in `app.js`).
- Withdraw allowed denominations: 10,20,30,40,50,60,70,80,90,100.
- This is a client-side demo only; no real security or persistence is provided.
