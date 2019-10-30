from collections import Counter, defaultdict


def find_dice_probalities(S, n_faces=6):
    if S > 2 * n_faces or S < 2:
        return None

    cdict = Counter()
    ddict = defaultdict(list)

