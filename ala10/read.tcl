
#set infile [open da_smd_tcl.out r]
#set mytraj [read $infile]
#close $infile

set contents(t) {}
set contents(z) {}
set contents(f) {}

foreach {tt zt ft} $mytraj {
	set w $contents(t)
	lappend w $tt
	set contents(t) $w

	set w $contents(z)
	lappend w $zt
	set contents(z) $w

	set w $contents(f)
	lappend w $ft
	set contents(f) $w
}

set t $contents(t)
set z $contents(z)
set f $contents(f)

