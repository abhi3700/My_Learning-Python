from docx import Document
from docx.enum.style import WD_STYLE
# from utility import *

d = Document()
p0 = d.add_paragraph('Item 1', style='List Bullet')
p1 = d.add_paragraph('Item A', style='List Bullet 2')
p2 = d.add_paragraph('Item 2', style='List Bullet')
p3 = d.add_paragraph('Item B', style='List Bullet 2')

d.save('demo.docx')