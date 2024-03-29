# CSV File Reading and Writing

The csv module's reader and writer objects read and write sequences. 

_ Programmers can also read and write data in dictionary form using
#DictReader & #DectWriter classes.

csv.reader(csvfile, dialect='excel', **fmtparams)
_ Return a #reader_object: that will process lines from a csvfile.  
  _ A ssvfile must be an iterable of strings, each in the reader's
  csv format and is commonly a list[]. 
  _ If csvfile is an object, it must be opened with newline=' '.
