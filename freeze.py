import os
from flask_frozen import Freezer
from app import app

app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = False

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

    # remove ".html" from links
    # TODO #1 Account for external links ending in .html
    for file in os.listdir("./app/build"):
        _, ext = os.path.splitext(file)
        if ext == ".html":
            
            with open(f"app/build/{file}", "r") as f:
                lines = f.readlines()

            lines = [
                line for line in
                map(
                    lambda i:
                        i.replace(".html", "")
                        .replace("index", "/"),
                    lines
                )
            ]
            
            with open(f"app/build/{file}", "w") as f:
                f.writelines(lines)