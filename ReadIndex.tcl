# Funktion Read Index

# Funktion liest die Indexwerte (Wertpapierwerte) ein.
# Datenformat: Datum, Open, High, Low, Close

proc ReadIndex {pResultDatumA pResultOpenA pResultHighA pResultLowA pResultCloseA indexFile} {

  upvar $pResultDatumA     datumA
  upvar $pResultOpenA      openA
  upvar $pResultHighA      highA
  upvar $pResultLowA       lowA
  upvar $pResultCloseA     closeA

  puts "> Lese Datei $indexFile ..."
  set indexFid [open "$indexFile" r]

  set i 0

  # Kursdaten einlesen
  while {[gets $indexFid zeile] != -1} {

    regsub -all {,} $zeile "." zeile

    set datumA($i)  [lindex $zeile 0]
    set openA($i)   [lindex $zeile 1]
    set highA($i)   [lindex $zeile 2]
    set lowA($i)    [lindex $zeile 3]
    set closeA($i)  [lindex $zeile 4]
  
    incr i
  }

  # Dateien schlieﬂen
  close $indexFid

  puts "  $i Zeilen eingelesen."
}
