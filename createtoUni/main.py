import pikepdf
import ArialDict
import io

x=b""

with pikepdf.open('latex_1_start.pdf', allow_overwriting_input=True) as pdfl:
    for page in pdfl.pages:
            resources = page.Resources
            fonts = resources.Font
            for font_key, font_val in fonts.items():
                if font_key == '/F21':
                    if font_val.ToUnicode is not None:
                        toUni = font_val.ToUnicode
                        print(toUni.read_bytes())
                        x = toUni

                        with pikepdf.open('_PE01_2010.pdf', allow_overwriting_input=True) as pdf:
                            for page in pdf.pages:
                                resources = page.Resources
                                fonts = resources.Font
                                for font_key, font_val in fonts.items():
                                    if font_key == '/F13':
                                        fontName = str(font_val.FontDescriptor.FontName)
                                        if "Arial" in fontName:
                                            print("This Font is Arial")
                                        else:
                                            print("This Font is not Arial")

                                        toUni_generated = b'/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo\n<< /Registry (TeX)\n/Ordering (cmex10-builtin)\n/Supplement 0\n>> def\n/CMapName /TeX-cmex10-builtin-0 def\n/CMapType 2 def\n1 begincodespacerange\n<00> <FF>\nendcodespacerange\n1 beginbfrange\n<D7> <D8> <03A5>\nendbfrange\n31 beginbfchar\n'


                                        i = 1
                                        for val in font_val.Encoding.Differences:
                                            uni_from_dict = ArialDict.arial_dict.get(str(val)[1:])
                                            toUni_generated += f"<{hex(i)[2:]}> <{uni_from_dict}>\n".encode()
                                            #print(uni_from_dict) if uni_from_dict is not None else 0
                                            i += 1

                                        toUni_generated += b'endbfchar\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n%%EndResource\n%%EOF\n'

                                        print(toUni_generated)

                                        a = pdf.copy_foreign(x)
                                        font_val.ToUnicode = a
                                        b = b'/CIDInit /ProcSet findresource begin\n12 dict begin\nbegincmap\n/CIDSystemInfo\n<< /Registry (TeX)\n/Ordering (cmex10-builtin)\n/Supplement 0\n>> def\n/CMapName /TeX-cmex10-builtin-0 def\n/CMapType 2 def\n1 begincodespacerange\n<00> <FF>\nendcodespacerange\n1 beginbfrange\n<D7> <D8> <03A5>\nendbfrange\n31 beginbfchar\n' \
                                            b'<2> <0046>\n' \
                                            b'<3> <0069>\n' \
                                            b'<4> <0072>\n' \
                                            b'<5> <006d>\n' \
                                            b'<6> <0061>\n' \
                                            b'<7> <0020>\n' \
                                            b'<8> <0043>\n' \
                                            b'<9> <006f>\n' \
                                            b'<a> <006e>\n' \
                                            b'<b> <0065>\n' \
                                            b'<c> <0063>\n' \
                                            b'<d> <0074>\n' \
                                            b'<e> <004f>\n' \
                                            b'<f> <0062>\n' \
                                            b'<10> <0079>\n' \
                                            b'<11> <006c>\n' \
                                            b'<12> <007a>\n' \
                                            b'<13> <017e>\n' \
                                            b'endbfchar\nendcmap\nCMapName currentdict /CMap defineresource pop\nend\nend\n%%EndResource\n%%EOF\n'
                                        font_val.ToUnicode.write(toUni_generated, filter=None, decode_parms=None, type_check=True)
                                        print(font_val.ToUnicode.read_bytes())

                            pdf.save('output.pdf')



