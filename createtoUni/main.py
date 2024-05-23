import pikepdf
import ArialDict
import io

x = b""
file_name = '_PE03_2010.pdf'

with (pikepdf.open('latex_1_start.pdf', allow_overwriting_input=True) as pdfl):
    for page in pdfl.pages:
        resources = page.Resources
        fonts = resources.Font
        for font_keyL, font_valL in fonts.items():
            if font_keyL == '/F21':
                if font_valL.ToUnicode is not None:
                    toUni = font_valL.ToUnicode
                    print(toUni.read_bytes())
                    x = toUni

                    with pikepdf.open(file_name, allow_overwriting_input=True) as pdf:
                        for page in pdf.pages:
                            resources = page.Resources
                            fonts = resources.Font
                            for font_key, font_val in fonts.items():
                                fixable35 = False
                                fontName = ''
                                try:
                                    fontName = str(font_val.FontDescriptor.FontName)
                                except:
                                    continue

                                fontName = str(font_val.FontDescriptor.FontName)

                                if "Arial" in fontName:
                                    try:
                                        if font_val.Encoding is not None and font_val.Encoding.Differences is not None:
                                            if "Arial035" in fontName:
                                                fixable35=True
                                    except AttributeError:
                                        print("Differences attribute does not exist.")

                                toUni_generated = b'1 beginbfrange\n<D7> <D8> <03A5>\nendbfrange\n31 beginbfchar\n'

                                if fixable35:
                                    i = 1
                                    for val in font_val.Encoding.Differences:
                                        uni_from_dict = ArialDict.arial_dict.get(str(val)[1:])
                                        toUni_generated += f"<{hex(i)[2:]}> <{uni_from_dict}>\n".encode()
                                        i += 1

                                    a = pdf.copy_foreign(x)
                                    font_val.ToUnicode = a

                                    font_val.ToUnicode.write(toUni_generated, filter=None, decode_parms=None,
                                                                 type_check=True)
                                    print(font_val.ToUnicode.read_bytes())



                        pdf.save(file_name[:-4] + '_toUnicode.pdf')

                    with pikepdf.open(file_name[:-4] + '_toUnicode.pdf', allow_overwriting_input=True) as pdf:
                        for page in pdf.pages:
                            resources = page.Resources
                            fonts = resources.Font
                            for font_key, font_val in fonts.items():
                                fixable37 = False
                                fontname = ''
                                try:
                                    fontName = str(font_val.FontDescriptor.FontName)
                                except:
                                    continue

                                fontName = str(font_val.FontDescriptor.FontName)

                                if "Arial" in fontName:
                                    try:
                                        if font_val.Encoding is not None and font_val.Encoding.Differences is not None:
                                            if "Arial037" in fontName:
                                                fixable37=True
                                    except AttributeError:
                                        print("Differences attribute does not exist.")

                                toUni_generated = b'1 beginbfrange\n<D7> <D8> <03A5>\nendbfrange\n31 beginbfchar\n'

                                if fixable37:
                                    i = 1
                                    for val in font_val.Encoding.Differences:
                                        uni_from_dict = ArialDict.arial_dict.get(str(val)[1:])
                                        toUni_generated += f"<{hex(i)[2:]}> <{uni_from_dict}>\n".encode()
                                        i += 1

                                    a = pdf.copy_foreign(x)
                                    font_val.ToUnicode = a

                                    font_val.ToUnicode.write(toUni_generated, filter=None, decode_parms=None,
                                                                 type_check=True)
                                    print(font_val.ToUnicode.read_bytes())

                        pdf.save(file_name[:-4] + '_toUnicode.pdf')
