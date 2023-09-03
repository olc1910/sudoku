# SudokuGenerator

Dieses Python-Programm generiert und löst Sudoku-Puzzles. Es bietet auch die Möglichkeit, die generierten Puzzles im SVG-Format zu speichern und verfügt über eine Befehlszeilenschnittstelle zur Festlegung des Schwierigkeitsgrads des Puzzles.

## Verwendung

Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist.
Klonen Sie diese Repository oder laden Sie es auf Ihren lokalen Computer herunter.
Öffnen Sie ein Terminal oder eine Eingabeaufforderung und navigieren Sie zum Verzeichnis, das die Datei SudokuGenerator.py enthält.
Führen Sie das Programm mit dem folgenden Befehl aus:

    python sudoku.py [Schwierigkeitsgrad]

Ersetzen Sie [Schwierigkeitsgrad] durch eine ganze Zahl von 1 bis 4, um den Schwierigkeitsgrad des Puzzles festzulegen (1 = einfach, 4 = teuflisch). Wenn kein Schwierigkeitsgrad angegeben wird, verwendet das Programm standardmäßig Schwierigkeitsstufe 3.
Das Programm wird versuchen, ein Sudoku-Puzzle mit dem angegebenen Schwierigkeitsgrad zu generieren. Wenn dies erfolgreich ist, wird es das generierte Puzzle in der Konsole anzeigen, im SVG-Format speichern und auch Textdateien mit Punkten (.) oder Nullen (0) erstellen, um leere Zellen darzustellen.
Die generierte SVG-Datei wird im Format sudoku-JJJJ_MM_TT_SS-Schwierigkeitsgrad.svg benannt, wobei JJJJ_MM_TT_SS das aktuelle Datum und die aktuelle Uhrzeit darstellt und Schwierigkeitsgrad den angegebenen Schwierigkeitsgrad angibt.

## Beispiel

Um ein Sudoku-Puzzle mit einem Schwierigkeitsgrad von 4 zu generieren, verwenden Sie den folgenden Befehl:

    python sudoku.py 4

## Hinweise

Das Programm generiert Sudoku-Puzzles, indem es zuerst die diagonalen Quadrate mit zufälligen Werten füllt und dann das Puzzle löst, um sicherzustellen, dass es eine eindeutige Lösung hat. Anschließend entfernt es Zahlen aus dem Puzzle, um den gewünschten Schwierigkeitsgrad zu erreichen.
Wenn das Programm innerhalb einer angemessenen Zeit (standardmäßig 10 Minuten) kein gültiges Sudoku-Puzzle finden kann, wird es eine Nachricht ausgeben und beenden.
Die generierte SVG-Datei enthält das Sudoku-Puzzle, und Sie können sie bei Bedarf weiter anpassen.
Die Textdateien mit Punkten und Nullen können für andere Sudoku-bezogene Anwendungen nützlich sein.
Sie können die Variablen cell_size und line_color im Code anpassen, um das Aussehen des generierten SVG-Puzzles anzupassen.
Um das Format leerer Zellen in der SVG-Datei zu ändern (Punkte oder Nullen), ändern Sie das Argument empty_as_zero, wenn Sie die Methode toSVG im Code aufrufen.

# Sudoku Solver

Dies ist ein Python-Programm zur Lösung von Sudoku-Rätseln. Das Programm enthält auch eine Funktion zur Bewertung der Schwierigkeit des Rätsels.

## Verwendung

1. Stelle sicher, dass Python 3.x auf deinem Computer installiert ist.

2. Lade das Sudoku-Problem in das Programm, indem du die `board`-Liste in der `main`-Funktion änderst. Du kannst ein Sudoku-Rätsel als 9x9-Gitter darstellen, wobei leere Zellen als `0` dargestellt werden und die Zahlen 1 bis 9 die bereits bekannten Werte sind.

3. Führe das Programm aus, indem du die Python-Datei ausführst:

   ```bash
   python3 SudokuSolver.py

    Das Programm wird die Schwierigkeit des Sudoku-Rätsels bewerten und dann versuchen, es zu lösen. Es gibt Feedback zur Anzahl der gefundenen Lösungen.

## Bewertung der Schwierigkeit

Die Schwierigkeit des Sudoku-Rätsels wird anhand der Anzahl leerer Zellen bewertet:

    Weniger als 28 leere Zellen: "Sehr einfach"
    28 bis 39 leere Zellen: "Einfach"
    40 bis 53 leere Zellen: "Mittel"
    54 bis 64 leere Zellen: "Schwierig"
    65 bis 71 leere Zellen: "Sehr schwierig"
    Mehr als 71 leere Zellen: "Diabolisch"

Lösung des Sudoku-Rätsels

Das Programm verwendet eine rekursive Methode, um das Sudoku-Rätsel zu lösen. Wenn es mehrere Lösungen gibt, werden alle gefundenen Lösungen angezeigt.
Beispiel

Ein Beispiel für ein Sudoku-Rätsel ist bereits in der main-Funktion enthalten. Du kannst es verwenden, um das Programm zu testen, du kannst aber auch mit dem SudokuBoardGenerator die txt Datei, die von dem SudokuGenerator erstellt wurde in das Programm einfügen.

# SudokuBoardConverter

Dieses Python-Programm wurde entwickelt, um eine Textdatei in eine Python-Liste umzuwandeln. Jede Zeile in der Textdatei repräsentiert eine Zeile des Spielbretts, und die Zahlen in jeder Zeile werden aufgeteilt und in eine Python-Liste umgewandelt. Die resultierende Liste von Listen kann verwendet werden, um ein zweidimensionales Spielfeld oder Raster in Python darzustellen.

## Verwendung

1. Klonen oder laden Sie dieses Repository auf Ihren lokalen Computer herunter.

2. Erstellen Sie eine Textdatei, die das zu konvertierende Spielfeld enthält. Stellen Sie sicher, dass die Textdatei dem folgenden Format entspricht:
   - Jede Zeile repräsentiert eine Zeile des Spielfelds.
   - Zahlen auf jeder Zeile sind durch Leerzeichen getrennt.

3. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und navigieren Sie zum Verzeichnis, in dem das Skript `board_to_list.py` befindet.

4. Führen Sie das Programm aus, indem Sie den folgenden Befehl ausführen:
   ```python SudokuBoardConverter.py```

5. Sie werden aufgefordert, den Speicherort der Textdatei des Spielfelds einzugeben. Geben Sie den Pfad zu Ihrer Spielfelddatei ein und drücken Sie Enter.

6. Das Programm liest die Datei, analysiert ihren Inhalt und generiert eine Python-Liste, die das Spielfeld repräsentiert.

7. Die resultierende Liste von Listen wird in der Konsole angezeigt, wobei jede Zeile des Spielfelds als separate Liste angezeigt wird.

# Sudoku-GUI

Wenn du dein erstelltes Sudoku jetzt auch noch in einem Python Programm Spielen möchtest dann empfehle ich den [Sudoku-GUI by ProAnalyzer](https://github.com/ProAnalyzer/Sudoku-GUI-Solver-master) der mich überhaupt erst auf dieses Projekt gebracht hat, dass ich für eine Bewerbung entwickelt habe.
