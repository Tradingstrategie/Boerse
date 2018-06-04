# Testdatei ReadIndex Einlesen

# Scripte einbinden
source "Scripts/Funktionen/ReadIndex.tcl"

# Kommandozeilen Parameter überprüpfen
if {[llength $argv]==0} {
  puts "\nSyntax: ReadIndexTest.tcl <Wertpapier-Datei>"
  puts "  Lese eine Wertpapierdatei ein (z.B. Index)."
  exit
}

# Dateien öffnen, vorbereiten
set eingabeDatei [lindex $argv 0]
set ausgabeDatei "$eingabeDatei.IndexTestEinlesedaten.txt"

# Ausführen der Funktionen
ReadIndex datumA openA highA lowA closeA $eingabeDatei

# Ergebnisausgabe in Ausgabedatei
puts "> Schreibe Ausgabedatei $ausgabeDatei ..."
set ausgabeFid [open "$ausgabeDatei" w]

set i 0
while {$i<[array size datumA]} {
  puts $ausgabeFid "$datumA($i) $openA($i) $highA($i) $lowA($i) $closeA($i)"
  incr i
}

# Ausgabedatei schließen
close $ausgabeFid
puts "Fertig."

exit
