import pikepdf
import ArialDict
import io
import os
import glob

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
# Get the input/output directories
input_directory = os.path.join(current_directory, 'input')
output_directory = os.path.join(current_directory, 'output')

os.makedirs(input_directory, exist_ok=True)
os.makedirs(output_directory, exist_ok=True)

# Find all .pdf files in the input directory
pdf_files = glob.glob(os.path.join(input_directory, "*.pdf"))

# Extract filenames only
pdf_files = [os.path.basename(pdf) for pdf in pdf_files]

if "latex_1_start.pdf" in pdf_files:
    pdf_files.remove("latex_1_start.pdf")

print(pdf_files)

for file_name in pdf_files:
    # path to file
    input_path = os.path.join(input_directory, file_name)
    # path to output file
    output_path = os.path.join(output_directory, file_name[:-4] + '_toUnicode.pdf')

    # skip already fixed files
    if file_name.endswith("_toUnicode.pdf"):
        continue

    x = b""
    fixable_fonts = []

    # get correct ToUnicode
    with (pikepdf.open('latex_1_start.pdf', allow_overwriting_input=True) as pdfl):
        for pageL in pdfl.pages:
            resources = pageL.Resources
            fonts = resources.Font
            for font_keyL, font_valL in fonts.items():
                if font_keyL == '/F21' and font_valL.ToUnicode is not None:
                    toUni = font_valL.ToUnicode
                    x = toUni

                    # get fixable fonts into a list
                    with pikepdf.open(input_path, allow_overwriting_input=True) as pdf:
                        for page in pdf.pages:
                            try:
                                resources = page.Resources
                                fonts = resources.Font
                            except:
                                continue

                            for font_key, font_val in fonts.items():
                                fontName = ''
                                try:
                                    fontName = str(font_val.FontDescriptor.FontName)
                                except:
                                    continue
                                if "Arial" in fontName:
                                    try:
                                        if font_val.Encoding is not None and font_val.Encoding.Differences is not None:
                                            if font_key not in fixable_fonts:
                                                fixable_fonts.append(font_key)
                                    except AttributeError:
                                        print("Differences attribute does not exist.")
                        pdf.save(output_path)

                    # fix fonts marked as fixable
                    for fixable_font in fixable_fonts:
                        with pikepdf.open(output_path, allow_overwriting_input=True) as pdf:
                            for page in pdf.pages:
                                try:
                                    resources = page.Resources
                                    fonts = resources.Font
                                except:
                                    continue
                                for font_key, font_val in fonts.items():

                                    toUni_generated = b'1 beginbfrange\n<D7> <D8> <03A5>\nendbfrange\n31 beginbfchar\n'
                                    if font_key == fixable_font:
                                        i = 1
                                        # get glyfs from differences
                                        for val in font_val.Encoding.Differences:
                                            # unicode from Dict
                                            uni_from_dict = ArialDict.arial_dict.get(str(val)[1:])
                                            if i < 16:
                                                toUni_generated += f"<0{hex(i)[2:].upper()}> <{uni_from_dict}>\n".encode()
                                            else:
                                                toUni_generated += f"<{hex(i)[2:].upper()}> <{uni_from_dict}>\n".encode()
                                            i += 1
                                        a = pdf.copy_foreign(x)
                                        font_val.ToUnicode = a
                                        font_val.ToUnicode.write(toUni_generated, filter=None, decode_parms=None,
                                                                     type_check=True)
                                        pdf.save(output_path)
                                        print(file_name + " fixed font " + font_key)
print("Hotovo.")