ORIGIN = (0, 0)
FLAG_SIZE = (800, 600)
STRIPE_WIDTH = 64


def tag(name, attrs=None, content=None):
    return {
        "tag": name,
        "attrs": attrs if attrs is not None else {},
        "content": content if content is not None else "",
    }


def start_tag(tag, attrs):
    if attrs is not None:
        astring = " ".join(f"{k}='{v}'" for k, v in attrs.items())
    else:
        astring = ""
    return f"<{tag} {astring}>"


def close_tag(tag):
    return f"</{tag}>"


def as_xml_string(tag, attrs=None, content=None):
    if content is None:
        content = []
    return "\n".join(
        [
            start_tag(tag, attrs),
            content,
            close_tag(tag),
        ]
    )


def line(color, moveby):
    return tag(
        "line",
        {
            "x1": ORIGIN[0] + moveby[0],
            "x2": FLAG_SIZE[0] + moveby[0],
            "y1": ORIGIN[1] + moveby[1],
            "y2": FLAG_SIZE[1] + moveby[1],
            "stroke-width": STRIPE_WIDTH,
            "stroke": color,
        },
    )


dx = dy = STRIPE_WIDTH / 1.41421

LINES = [
    line("#37b17e", (2 * dx, -2 * dy)),
    line("#7bc2e1", (dx, -dy)),
    line("#eaeaea", (0, 0)),
    line("#efe078", (-dx, dy)),
    line("#d07381", (-2 * dx, 2 * dy)),
]


FLAGPARTS = [
    tag(
        "rect",
        {
            "width": "100%",
            "height": "100%",
            "fill": "#575757",
        },
    ),
    tag(
        "title",
        {"id": "disability-pride-flag-svg"},
        content="The disability pride flag",
    ),
    *LINES,
]

FLAG = tag(
    "svg",
    attrs={
        "width": FLAG_SIZE[0],
        "height": FLAG_SIZE[1],
        "version": "1.1",
        "xmlns": "http://www.w3.org/2000/svg",
    },
    content="\n".join(as_xml_string(**part) for part in FLAGPARTS),
)


if __name__ == "__main__":
    print("Saving...")
    with open("DisabilityPrideFlag.svg", "w") as outf:
        outf.write("""<?xml version="1.0" standalone="no"?>\n""")
        outf.write(as_xml_string(**FLAG))
    print("done")
