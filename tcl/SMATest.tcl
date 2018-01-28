# Testdatei SMA-Indikator

# Scripte einbinden
source "Scripts/Funktionen/ReadIndex.tcl"
#source "Scripts/Funktionen/Delta.tcl"
source "Scripts/Indikatoren/SMA.tcl"

# Kommandozeilen Parameter überprüpfen
if {[llength $argv]==0} {
  puts "\nSyntax: SMATest.tcl <Wertpapier-Datei> \[n\]"
  puts "  Berechnet den SMA-Indikator n-Tage."
  puts "  Voreingestellt sind 20 Tage SMA.\n"
  exit
}

# Parameter übergeben
set N  20
if {[llength $argv]>=2} {set N  [lindex $argv 1]}

# Dateien öffnen, vorbereiten
set eingabeDatei [lindex $argv 0]
set ausgabeDatei "$eingabeDatei.SMA.$N.txt"

# Ausführen der Funktionen
ReadIndex datumA openA highA lowA closeA $eingabeDatei
SMA smaA closeA $N
#Delta smaDeltaA smaA

# Ergebnisausgabe in Ausgabedatei
puts "> Schreibe Ausgabedatei $ausgabeDatei ..."
set ausgabeFid [open "$ausgabeDatei" w]

set i 0
while {$i<[array size smaA]} {
  puts $ausgabeFid "$datumA($i) $smaA($i)"
#  puts $ausgabeFid "$datumA($i) $smaA($i) $smaDeltaA($i)"
  incr i
}

# Ausgabedatei schließen
close $ausgabeFid
puts "Fertig."

exit
