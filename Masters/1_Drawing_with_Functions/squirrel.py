def cigar_party(cigars, is_weekend):

    if cigars >= 40 and cigars <= 60 and not is_weekend:
        return True

    elif is_weekend and cigars >= 40:
        return True

    else:
        return False

print (cigar_party(30, True))
print (cigar_party(70, False))
print (cigar_party(50, True))
print (cigar_party(80, True))
