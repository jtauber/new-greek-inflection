AUGMENTS = [
    ("ἀνα+α", "ἀνη", "ἀνα"),
    ("ἀνα+", "ἀνε", "ἀνα"),
    ("ἀντι", "ἀντε", "ἀντι"),
    ("ἀπα", "ἀπη", "ἀπα"),
    ("ἀπ+ε", "ἀπει", "ἀπε"),
    ("ἀπο+", "ἀπε", "ἀπο"),
    ("ἀφο", "ἀφω", "ἀφο"),
    ("δια+α", "διη", "δια"),
    ("δια+", "διε", "δια"),
    ("διο", "διω", "διο"),
    ("ἐγκ", "ἐνεκ", "ἐγκ"),
    ("ἐκ", "ἐξε", "ἐκ"),
    ("ἐν", "ἐνε", "ἐν"),
    ("ἐνευ", "ἐνευ", "ἐνευ"),
    ("ἐνε", "ἐνει", "ἐνε"),
    ("ἐμβ", "ἐνεβ", "ἐμβ"),
    ("ἐμπ", "ἐνεπ", "ἐμπ"),
    ("ἐπ+ε", "ἐπη", "ἐπε"),
    ("ἐπιβ", "ἐπεβ", "ἐπιβ"),
    ("ἐπιγ", "ἐπεγ", "ἐπιγ"),
    ("ἐπιζ", "ἐπεζ", "ἐπιζ"),
    ("ἐπιθ", "ἐπεθ", "ἐπιθ"),
    ("ἐπιλ", "ἐπελ", "ἐπιλ"),
    ("ἐπιμ", "ἐπεμ", "ἐπιμ"),
    ("ἐπισ", "ἐπεσ", "ἐπισ"),
    ("ἐπιτ", "ἐπετ", "ἐπιτ"),
    ("ἐπιφ", "ἐπεφ", "ἐπιφ"),
    ("ἐπιχ", "ἐπεχ", "ἐπιχ"),
    ("εὐα", "εὐη", "εὐα"),
    ("εὑ", "ηὑ", "εὑ"),
    ("εὐ", "ηὐ", "εὐ"),
    ("κατα+α", "κατη", "κατα"),
    ("καται", "κατῃ", "καται"),
    ("κατευ", "κατευ", "κατευ"),
    ("κατε", "κατει", "κατε"),
    ("κατη", "κατη", "κατη"),
    ("κατα", "κατε", "κατα"),
    ("μετα", "μετε", "μετα"),
    ("παρα+α", "παρη", "παρα"),
    ("παραι", "παρῃ", "παραι"),
    ("παρε", "παρει", "παρε"),
    ("παρα", "παρε", "παρα"),
    ("περια", "περιη", "περια"),
    ("περι+", "περιε", "περι"),
    ("περιαι", "περιῃ", "περιαι"),
    ("προα", "προη", "προα"),
    ("προ+", "προε", "προ"),
    ("προσε", "προσει", "προσε"),
    ("προσ", "προσε", "προσ"),
    ("προϋπα", "προϋπη", "προϋπα"),
    ("συλλ", "συνελ", "συλλ"),
    ("συζ", "συνεζ", "συζ"),
    ("συγχ", "συνεχ", "συγχ"),
    ("συμβ", "συνεβ", "συμβ"),
    ("συμπ", "συνεπ", "συμπ"),
    ("συνα", "συνη", "συνα"),
    ("συνε", "συνει", "συνε"),
    ("συν", "συνε", "συν"),
    ("ὑπα", "ὑπη", "ὑπα"),
    ("ὑπο", "ὑπε", "ὑπο"),

    ("αὐ", "ηὐ", "αὐ"),
    ("αἰ", "ᾐ", "αἰ"),
    ("ἀ", "ἠ", "ἀ"),
    ("ἁ", "ἡ", "ἁ"),
    ("ἑ", "εἱ", "ἑ"),
    ("ἐ", "εἰ", "ἐ"),
    ("εἰ", "εἰ", "εἰ"),
    ("ἡ", "ἡ", "ἡ"),
    ("ὀ", "ὠ", "ὀ"),
    ("ὁ", "ὡ", "ὁ"),
    ("οἰ", "ᾠ", "οἰ"),
    ("ὑ", "ὑ", "ὑ"),
    ("ὠ", "ὠ", "ὠ"),
]


def augment(stem):
    for wo, w, wo2 in sorted(AUGMENTS, key=lambda x: -len(x[0])):
        if stem.startswith(wo):
            return w + stem[len(wo):]
    return "ἐ" + stem


def de_augment(stem):
    for wo, w, wo2 in sorted(AUGMENTS, key=lambda x: -len(x[1])):
        if stem.startswith(w):
            return wo2 + stem[len(w):]
    if stem.startswith("ἐ"):
        return stem[1:]
    elif stem == "?":
        return "?"
    else:
        raise Exception("can't de-augment {}".format(stem))


def no_augment(stem):
    for wo, w, wo2 in sorted(AUGMENTS, key=lambda x: -len(x[1])):
        if stem.startswith(wo):
            return wo2 + stem[len(wo):]
    return stem
