from openpyxl import Workbook

EXCEPTION_LIST = [' ', 'AEP-84 Volume II', 'Edition A Version 1']

def write_excel(filepath, text_from_pdf):
    wb = Workbook()
    ws = wb.active

    start_row = 1
    start_col = 1
    buffer = ''

    for page_number, text in enumerate(text_from_pdf):
        total_line = len(text.split('\n'))
        print('total_line: ', total_line)
        for line_number, line in enumerate(text.split('\n')):
            print('line: ', line)
            line_strip = line.strip()
            if (not line_strip in EXCEPTION_LIST) and (not line_strip == ''):                
                ascii = ord(line_strip[0])                
                print('ascii: ', ascii)
                print('type ascii: ', type(ascii))
                if (48 <= ascii) and (ascii <= 57):     # 숫자로 시작
                    if buffer != '':
                        ws.cell(row=start_row, column=start_col, value=buffer)
                        start_row += 1
                        buffer = ''
                        
                    ws.cell(row=start_row, column=start_col, value=line_strip)
                    start_row += 1

                else:
                    if buffer != '':
                        if ascii == 8226:
                            buffer = buffer + '\n' + line_strip
                        else:
                            buffer = buffer + ' ' + line_strip
                    else:
                        buffer = line_strip
                    print('line_number: ', line_number)
                    if line_number + 1 == total_line:
                        ws.cell(row=start_row, column=start_col, value=buffer)
                        start_row += 1
                        buffer = ''
                    continue

    wb.save(filename=filepath)