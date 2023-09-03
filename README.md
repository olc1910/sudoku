Sudoku-Generator und -Löser

Dieses Python-Programm generiert und löst Sudoku-Puzzles. Es bietet auch die Möglichkeit, die generierten Puzzles im SVG-Format zu speichern und verfügt über eine Befehlszeilenschnittstelle zur Festlegung des Schwierigkeitsgrads des Puzzles.
Verwendung

    Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist.

    Klonen Sie das Repository oder laden Sie es auf Ihren lokalen Computer herunter.

    Öffnen Sie ein Terminal oder eine Eingabeaufforderung und navigieren Sie zum Verzeichnis, das die Datei sudoku.py enthält.

    Führen Sie das Programm mit dem folgenden Befehl aus:

    bash

    python sudoku.py [Schwierigkeitsgrad]

    Ersetzen Sie [Schwierigkeitsgrad] durch eine ganze Zahl von 1 bis 6, um den Schwierigkeitsgrad des Puzzles festzulegen (1 = einfach, 6 = teuflisch). Wenn kein Schwierigkeitsgrad angegeben wird, verwendet das Programm standardmäßig Schwierigkeitsstufe 3.

    Das Programm wird versuchen, ein Sudoku-Puzzle mit dem angegebenen Schwierigkeitsgrad zu generieren. Wenn dies erfolgreich ist, wird es das generierte Puzzle in der Konsole anzeigen, im SVG-Format speichern und auch Textdateien mit Punkten (.) oder Nullen (0) erstellen, um leere Zellen darzustellen.

    Die generierte SVG-Datei wird im Format sudoku-JJJJ_MM_TT_SS-Schwierigkeitsgrad.svg benannt, wobei JJJJ_MM_TT_SS das aktuelle Datum und die aktuelle Uhrzeit darstellt und Schwierigkeitsgrad den angegebenen Schwierigkeitsgrad angibt.

Beispiel

Um ein Sudoku-Puzzle mit einem Schwierigkeitsgrad von 4 zu generieren, verwenden Sie den folgenden Befehl:

bash

python sudoku.py 4

Hinweise

    Das Programm generiert Sudoku-Puzzles, indem es zuerst die diagonalen Quadrate mit zufälligen Werten füllt und dann das Puzzle löst, um sicherzustellen, dass es eine eindeutige Lösung hat. Anschließend entfernt es Zahlen aus dem Puzzle, um den gewünschten Schwierigkeitsgrad zu erreichen.

    Wenn das Programm innerhalb einer angemessenen Zeit (standardmäßig 10 Minuten) kein gültiges Sudoku-Puzzle finden kann, wird es eine Nachricht ausgeben und beenden.

    Die generierte SVG-Datei enthält das Sudoku-Puzzle, und Sie können sie bei Bedarf weiter anpassen.

    Die Textdateien mit Punkten und Nullen können für andere Sudoku-bezogene Anwendungen nützlich sein.

    Sie können die Variablen cell_size und line_color im Code anpassen, um das Aussehen des generierten SVG-Puzzles anzupassen.

    Um das Format leerer Zellen in der SVG-Datei zu ändern (Punkte oder Nullen), ändern Sie das Argument empty_as_zero, wenn Sie die Methode toSVG im Code aufrufen.

Fühlen Sie sich frei, den Code zu erkunden und anzupassen, um Ihren Anforderungen gerecht zu werden, oder integrieren Sie ihn in Ihre eigenen Projekte. Viel Spaß beim Lösen und Generieren von Sudoku-Puzzles!
