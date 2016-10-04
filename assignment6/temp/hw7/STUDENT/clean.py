import sys

# file for cleaning raw IMDB data. Call as "python3 <INPUT FILE> <OUTPUT FILE> <thresh>"
#
# <INPUT FILE> is raw input from IMDB with actor/actress information
# <OUTPUT FILE> is where the cleaned output goes
# all individuals with less than thresh credits is removed


# check for non-ascii characters
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

f_input = open(sys.argv[1], 'r', encoding="latin-1")
f_out = open(sys.argv[2], 'w')

# we remove any actor with less than thresh credits
thresh = int(sys.argv[3])

new = True

for line in f_input.readlines():
    if new:
        tokens = line.split('\t',1)
        person_raw = (tokens[0].split('('))[0].strip()
        names = person_raw.split(',')
        if len(names) == 1:
            out_str = names[0].strip()
        else:
            out_str = names[1].strip() + ' ' + names[0].strip()
        
        if not is_ascii(out_str) or len(out_str.strip()) == 0:
            continue

        acted = 0
        if len(tokens) > 1:
            next_tokens = tokens[1].split(')')
            movie = next_tokens[0].strip()+')'
            acted = acted + 1
            out_str = out_str + ' # ' + movie
            new = False
    else:
        if len(line.strip()) == 0:
            if acted > thresh:
                f_out.write(out_str+'\n')
            new = True
        else:
            tokens = line.split(')')
            movie = tokens[0].strip()+')'
            if not is_ascii(movie):
                continue
            if len(movie) > 0 and movie[0] != '\"' \
                    and movie.find('Awards') == -1 \
                    and len(movie.split()) < 8:
                acted = acted+1
                out_str = out_str + ' # ' + movie

f_input.close()
f_out.close()
