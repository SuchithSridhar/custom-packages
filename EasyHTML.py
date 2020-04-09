def table_maker(table):
    html = '<table border=1 cellpadding=2 cellspacing=2>'
    flag = True
    for row in table:
        html += "<tr>"
        for item in row:
            if flag:
                html += "<th>" + str(item) + "</th>"
            else:
                html += "<td>" + str(item) + "</td>"
        html += '</tr>'
        flag = False

    html += "</table>"
    return html
