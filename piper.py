#!/usr/bin/env python3
#
# Author: Xi Chen < hypernewbie[at]gmail[dot]com >
#
# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

import os, sys, json

def process( fileName ):
	print( "[piper] %s" % fileName )
	with open( fileName, "r" ) as fp:
		
		skip = 0; state = 0
		data_dictionary = {}; template_dictionary = {}
		json_lines = []; template_lines = []; eval_lines = []; out_lines = []
		lastline_ = ""

		for line_ in fp.readlines():
			if state != 6:
				out_lines.append(line_);

			line = line_
			if line_.startswith("|| "):
				line = line_.strip()[3:]
				if line == "<json>": state = 1; continue
				if line == "</json>": state = 2;
				if line == "<template>": state = 3; continue
				if line == "</template>": state = 4;
				if line == "<eval>": state = 5; continue
				if line == "</eval>": state = 0; continue
				if line == "<output>": state = 6; skip = 0; continue
				if line == "</output>": state = 7;

			if state == 1: json_lines.append( line )
			if state == 2:
				newdata = json.loads( "\n".join( json_lines ) )
				data_dictionary = {**data_dictionary, **newdata}
				json_lines = []
			if state == 3: template_lines.append( line )
			if state == 4:
				template_dictionary[template_lines[0]] = "\n".join( template_lines[1:] )
			if state == 5: eval_lines.append( line )
			if state == 6:
				if skip == 0: skip += 1; out_lines.append( line_ ); continue
				for eval_line in eval_lines:
					ev = eval_line.strip().replace(")", "").split("(")
					for dictentry in data_dictionary[ev[1]]:
						result = template_dictionary[ev[0]]
						for ( k, v ) in dictentry.items():
							result = result.replace( "%" + k + "%", v )
							result = result.replace( "%" + k + "_UPPERCASE%", v.upper() )
							result = result.replace( "%" + k + "_LOWERCASE%", v.lower() )
						out_lines.append( result )
				eval_lines = []; lastline_ = line_
			if state == 7:
				out_lines.append( lastline_ );
				out_lines.append( line_ )
				state = 0

		fp.close()
		# print ( "".join( out_lines ) )

	with open( fileName, "w" ) as fp:
		fp.write( "".join( out_lines ) )
		fp.close()

for i in range( 1, len( sys.argv ) ):
	process( sys.argv[i] )

