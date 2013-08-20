# \\	Backslash ()
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \r	ASCII Carriage Return (CR)
# \t	ASCII Horizontal Tab (TAB)
# \v	ASCII vertical tab (VT)
# \N	Character named name in the Unicode database (Unicode only)

while True:
    for i in ["M","A","T","T\v","M","A","T","T"]:
        print "%s\r" % i
