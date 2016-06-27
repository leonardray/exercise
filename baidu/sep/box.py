sentace = raw_input("sentance:")
sentace_width = 80
text_width = len(sentace)
print text_width
box_width = text_width+6
print box_width
left_margin = (sentace_width-box_width)//2
print sentace_width

print
print ''* left_margin + '+'+'-'*(box_width-2)+'+'
raw_input("Press <enter>")
