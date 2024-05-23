import pikepdf
import ArialDict
import io
import os
import glob

# Get the current directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))
input_directory = os.path.join(current_directory, 'input')
output_directory = os.path.join(current_directory, 'output')

os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

# Find all .pdf files in the current directory
pdf_files = glob.glob(os.path.join(input_directory, "*.pdf"))

# Extract just the filenames
pdf_files = [os.path.basename(pdf) for pdf in pdf_files]

if "latex_1_start.pdf" in pdf_files:
    pdf_files.remove("latex_1_start.pdf")

print(pdf_files)

for file_name in pdf_files:
    input_path = os.path.join(input_directory, file_name)
    output_path = os.path.join(output_directory, file_name[:-4] + '_toUnicode.pdf')
    if file_name.endswith("_toUnicode.pdf"):
        continue
    x = b""

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

                        with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
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
                                        #print(font_val.ToUnicode.read_bytes())

                            pdf.save(output_path)
                            print(file_name + "fixed")

                        with pikepdf.open(output_path, allow_overwriting_input=True) as pdf:
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
                                        #print(font_val.ToUnicode.read_bytes())

                            pdf.save(output_path)
                            print(file_name + "fixed")
