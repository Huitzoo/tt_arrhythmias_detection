import os
script = ""
path = os.listdir()
print(len(path))

for nombre in path[:int(len(path)/4)]:
    script += """\\begin{figure}[H]
            \centering
            \includegraphics[width=11.5cm]{ReporteTT/capitulos/apendice/jupyter/"""+nombre+"""}
            \caption{Gráfica de comparación entre arritmias cardiacas.}
        \end{figure}
    """

a = open("t.txt","w")
a.write(script)
print(script)