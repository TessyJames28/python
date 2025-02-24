#!/usr/bin/python3

"""Write a function that prints a text with 2 new lines after each of these characters: ., ? and :"""

def text_indentation(text):
    """Function that prints new line based on specified characters"""
    try:
        chars = [".", ":", "?"]
        new_text = " ".join(text.split())
        for char in chars:
            new_text = new_text.replace(f"{char} ", char)

        if not isinstance(text, str):
            raise TypeError("text must be a string")
        else:
            for chr in new_text.strip():
                if chr == "." or chr == ":" or chr == "?":
                    new_val = "".join(chr.strip())
                    print(new_val + "\n")
                    continue
                print(chr, end="")
    except Exception:
        raise TypeError("text must be a string")


if __name__ == "__main__":
    # Input Data
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres""")
