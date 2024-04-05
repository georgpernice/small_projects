# semorai_skilltest

## Task in German: 
1. Um deine Skills einschätzen zu können, würden wir uns freuen, wenn du einen kleinen Test abschließen könntest.
2. Anbei findest du einen Datensatz an Links zu Datenblättern für Kondensatoren.
3. Bitte schreibe einen Python-Code zum automatischen Downloaden der Datenblätter anhand der Links in Spalte B, speichere diese in einen Zielordner und gebe den Dateien den Namen „(Nummer aus Spalte A)-(Name des Herstellers).pdf“.
4. Bitte gib darüber hinaus eine Liste im Excel-Format der Nummern aus Spalte A aus, die keinen Link haben.
5. Bei manchen der Links könnte außerdem ein Fehler entstehen. Bitte gib hierfür eine Liste aus, bei welchen der Download nicht geklappt hat.

## Notes:
* What can happen when downloading from URLs?
  * no URL only "-"
  * invalid URL
    * http error
  * valid URL
    * url ending with pdf
        valid PDF (Yey)
    * url not ending with pdf
      * website contains no links with PDF because the PDF is no longer there on company website
      * website contains links to PDF
        * valid (most probably)
        * invalid
    
