import re

cardinal_heading1 = r"^# ([ \S]*)"
repl_cardinal_heading1 = r"<h1>\1</h1>"

cardinal_heading2 = r"^## ([ \S]*)"
repl_cardinal_heading2 = r"<h2>\1</h2>"

cardinal_heading3 = r"^### ([ \S]*)"
repl_cardinal_heading3 = r"<h3>\1</h3>"

cardinal_heading4 = r"^#### ([ \S]*)"
repl_cardinal_heading4 = r"<h4>\1</h4>"

cardinal_heading5 = r"^##### ([ \S]*)"
repl_cardinal_heading5 = r"<h5>\1</h5>"

cardinal_heading6 = r"^###### ([ \S]*)"
repl_cardinal_heading6 = r"<h6>\1</h6>"

underline_heading1 = r"([ \S]*)\n=+"
repl_underline_heading1 = r"<h1>\1</h1>"

underline_heading2 = r"([ \S]*)\n-+"
repl_underline_heading2 = r"<h2>\1</h2>"

soft_line_break = r"([ \S]*)  \n"
repl_soft_line_break = r"\1<br />"


strike_through = r"~~([ \S]*?)~~"
repl_strike_through = r"<del>\1</del>"

italic_bold = r"(?:\*\*\*|___)([ \S]*?)(?:\*\*\*|___)"
repl_italic_bold = r"<strong><em>\1</em></strong>"

bold = r"(?:\*\*|__)([ \S]*?)(?:\*\*|__)"
repl_bold = r"<strong>\1</strong>"

italic = r"(?:\*|_)([ \S]*?)(?:\*|_)"
repl_italic = r"<em>\1</em>"

simple_patterns = [
	cardinal_heading1,
	cardinal_heading2,
	cardinal_heading3,
	cardinal_heading4,
	cardinal_heading5,
	cardinal_heading6,
	underline_heading1,
	underline_heading2,
	soft_line_break,
	strike_through,
	italic_bold,
	bold,
	italic
]

simple_repls = [
	repl_cardinal_heading1,
	repl_cardinal_heading2,
	repl_cardinal_heading3,
	repl_cardinal_heading4,
	repl_cardinal_heading5,
	repl_cardinal_heading6,
	repl_underline_heading1,
	repl_underline_heading2,
	repl_soft_line_break,
	repl_strike_through,
	repl_italic_bold,
	repl_bold,
	repl_italic
]

quote_block = r"(?:^> [ \S]*\n)+" # gets every line that starts with > consecutively
line_quote = r"^> ([ \S]*)"
repl_line_quote = r"\1"
repl_block_quote = r"<blockquote>%s</blockquote>" # gets every line that starts with > consecutively

list_block = r"(?:^(?:-|\*|\+) [ \S]*\n)+"
line_list = r"^(?:-|\*|\+) ([ \S]*)"
repl_line_list = r"<il>\1</il>"
repl_block_list = r"<ul>%s</ul>" # gets every line that starts with > consecutively

block_patterns = [
	quote_block,
	list_block
]

line_patterns = [
	line_quote,
	line_list
]

line_repl = [
	repl_line_quote,
	repl_line_list
]

block_repl = [
	repl_block_quote,
	repl_block_list
]

with open("input.md", "r", encoding="utf-8") as file:
	txt = file.read()
	output = txt
	
	for i in range(len(block_patterns)):
		block = re.findall(block_patterns[i], output, flags=re.M)
		for j in range(len(block)):
			block[j] = re.sub(line_patterns[i], line_repl[i], block[j], flags=re.M)
			block[j] = block_repl[i] % block[j]
		
		for bq in block:
			output = re.sub(block_patterns[i], bq, output, count=1, flags=re.M)

	for i in range(len(simple_patterns)):
		output = re.sub(simple_patterns[i], simple_repls[i], output, flags=re.M)


print (output)

with open("output.html", "w", encoding="utf-8") as file:
	file.write(output)