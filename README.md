# bc_toUniFix

Ke spuštění skriptu je nutné stáhnout a nainstalovat \texttt{Python} (Dostupný ze stránek \url{www.python.org}), k vzpracování této práce byl použit \texttt{Python} verze 3.11.
Po instalaci \texttt{Python}u je třeba nainstalovat balíčkový manažer \texttt{pip}, který se použije k instalaci knihovny \texttt{pikePDF}. Pro instalaci \texttt{pip} stačí napsat do příkazové řádky následující příkaz:

\begin{lstlisting}[language=bash]
  $ python get-pip.py
\end{lstlisting}

Při správné instalaci \texttt{pip} je možno stáhnout knihovnu \texttt{pikePDF} pomocí následujícího příkazu v příkazovém řádku:

\begin{lstlisting}[language=bash]
  $ pip install pikepdf
\end{lstlisting}

V tomto bodě je nainstalováno vše co je potřeba ke spuštění skriptu. Samotný skript je ke stažení na stránce \url{https://github.com/skerikpa/bc_toUniFix} pomocí tlačítka \textbf{Code} a následně \textbf{Download ZIP} dle obr.\ref{obr:gitdown}, případně je možno stáhnout skript pomocí aplikace \texttt{GitHub Desktop} nebo naklonovat z příkazové řádky aplikace \texttt{Git Bash}. 
Při stažení archivu se soubor ZIP extrahuje v požadované lokaci.

\begin{figure}[H]
    \centering
    \includegraphics[width=1\textwidth]{obrazky/gitdown.png}
    \caption{Tlačítko pro stažení skriptu}
    \label{obr:gitdown}
\end{figure}

Po extrakci se otevře složka se skriptem, která také obsahuje složky \texttt{input} a \texttt{output}. Do složky input se vloží soubory potřebující opravu a do složky \texttt{output} vygeneruje skript opravené soubory.
Skript se spustí pravým kliknutím do složky se skriptem a otevře se příkazový řádek tlačítkem \textbf{Open in terminal} (otevřít v konzoli) dle obr.\ref{obr:rightclick}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.4\textwidth]{obrazky/rightclick.png}
    \caption{Tlačítko ke spuštění konzole}
    \label{obr:rightclick}
\end{figure}

Do konzole stačí už pouze napsat následující příkaz a skript se spustí. Dokončení práce skriptu lze poznat podle posledního řádku výpisu, na kterém je napsáno \uv{Hotovo.}