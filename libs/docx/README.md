# Python-Docx
* Create new document
```py
from docx import Document
d = Document()
```
* Save document
```py
d.save('demo.docx')
```
* Bulleted & Sub bulleted list [Source](https://python-docx.readthedocs.io/en/latest/api/enum/WdBuiltinStyle.html)
```py
from docx import Document
from docx.enum.style import WD_STYLE

d = Document()
p0 = d.add_paragraph('Item 1', style='List Bullet')
p1 = d.add_paragraph('Item A', style='List Bullet 2')
p2 = d.add_paragraph('Item 2', style='List Bullet')
p3 = d.add_paragraph('Item B', style='List Bullet 2')

```
__Output:__
```
•	Item 1
	•	Item A
•	Item 2
	•	Item B
```
* Align paragraph - Center, left, Right [Source](https://python-docx.readthedocs.io/en/latest/api/enum/WdAlignParagraph.html)
```py
from docx.enum.text import WD_ALIGN_PARAGRAPH

para = d.add_paragraph()
para.alignment = WD_ALIGN_PARAGRAPH.CENTER 		# center
para.alignment = WD_ALIGN_PARAGRAPH.LEFT 		# left
para.alignment = WD_ALIGN_PARAGRAPH.RIGHT 		# right
```