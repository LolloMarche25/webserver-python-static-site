# Web Server in Python e sito statico su Watchmen

Questo progetto consiste nella realizzazione di un web server minimale scritto in Python, in grado di servire contenuti statici (HTML, CSS, immagini).  
È stato sviluppato come esercitazione per il corso di Programmazione di Reti, Università di Bologna.

## Contenuto del progetto

- `server.py`: web server TCP che gestisce richieste HTTP GET e serve contenuti statici.
- `www/`: contiene il sito statico composto da tre pagine:
  - `index.html`
  - `Eroi.html`
  - `Partecipa.html`
  - `styles.css`
  - immagini nella cartella `images/`
- `relazione.pdf`: relazione tecnica del progetto

## Tema del sito

Il sito è dedicato al fumetto *Watchmen* e ha lo scopo di promuovere i vigilanti, criticati nella narrazione dalla società e dalla politica attraverso il *Keene Act*.

## Avvio del server

Per avviare il server, assicurarsi di avere Python installato e digitare da terminale:

```bash
python server.py
