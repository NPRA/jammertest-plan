import json

def esc(strng):
    #\& \% \$ \# \_ \{ \}
    #~ \textasciitilde
    #^ \textasciicircum
    #\ \textbackslash
    if not isinstance(strng, str):
        return strng
    #strng = strng.replace("µ", "\mu")
    strng = strng.replace("&","\\&")
    strng = strng.replace("%","\\%")
    strng = strng.replace("$","\\$")
    strng = strng.replace("#","\\#")
    strng = strng.replace("_","\\_")
    strng = strng.replace("{","\\{")
    strng = strng.replace("}","\\}")
    strng = strng.replace("~", "\\textasciitilde")
    strng = strng.replace("^", "\\textasciicircum")
    strng = strng.replace("\\n", "\\\\")
    strng = strng.replace("\n", "\\\\")
    strng = strng.replace(" \\ ", " \\textbackslash ")
    strng = strng.replace("[","{[")
    strng = strng.replace("]","]}")
    return strng


json_equipment_file = open('equipment.json')
List_of_equipment = json.load(json_equipment_file)

def create_equipment(tex,eq):
    print(f"Processing {eq['id']}")

    tex.write(f'\\subsection{{{eq["title"]}}}\n')
    if eq["image"] != "":
        tex.write(f'\\includegraphics[scale=0.4]{{graphics/{eq["image"]}}}\\\\ \\\\ \n')
    #Description
    tex.write(f'{esc(eq["desc"])}\\\\\n')
    #table:
    if len(eq["table"]) > 0:
        cols = len(eq['table'][0])
        tex.write("\\begin{table}[H]\\centering\n")
        tex.write("\\begin{tabular}{"+"|c"*cols+"|}\\rowcolor[HTML]{C0C0C0} \n")
        for row in eq['table']:
            tex.write("\\hline\n")
            for cell in row:
                tex.write("\\makecell{"+esc(cell.replace(",","."))+"}")
                if row.index(cell) < cols-1:
                    tex.write(" & ")
                else:
                    tex.write("\\\\ \n")
        tex.write("\\hline\\end{tabular}\\caption{Technical characteristics of "+eq["id"]+" jammer}\\label{table:tech_char_"+eq["id"]+"}\\end{table}\n")

    for image in eq['images']:
        tex.write("\\begin{figure}[H]")
        tex.write(f'\\includegraphics[width=\\textwidth]{{graphics/{image["path"]}}} \n')
        tex.write("\\caption{"+image["desc"]+"}")
        tex.write("\\end{figure}")
        #\\caption{Technical characteristics of "+eq["id"]+" jammer}\\label{table:tech_char_"+eq["id"]+"}

# create a text file for writing
with open('./Latex/equipment.tex', 'w') as tex:
    tex.write('% Content below is autogenerated \n')
    for eq in List_of_equipment:
        create_equipment(tex, eq)
    print("Equipment appendix created successfully.")