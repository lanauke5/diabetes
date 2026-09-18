"""Rebuild ad placement across every diabetes article.

Each article receives:
- one 300x250 script ad after the first paragraph, floated left;
- one 728x90 ad after approximately 35% of article paragraphs;
- one 728x90 ad after approximately 70% of article paragraphs.

All previous ad markup is removed first so rerunning this script is safe.
"""
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path("E:/diabetes")

AD_300_SCRIPT = (
    '<script async src="https://worldppc.click/ads.php?'
    'publisher_id=3&website_id=1&type=banner&size=300x250&format=js"></script>'
)

AD_300_BLOCK = (
    '<div class="ad-block" style="float:left;margin:0 36px 24px 0;width:300px;flex-shrink:0;">'
    '<div class="ad-label">Advertisement</div>'
    '<div class="ad-slot">' + AD_300_SCRIPT + '</div>'
    '</div>'
)

AD_728_1 = (
    '<!-- Ad Block 728x90 Slot 1 -->'
    '<div class="ad-leaderboard" style="width:728px;height:90px;margin:1.5rem auto;background:#F0EAE4;'
    'border:2px dashed #5A9898;display:flex;align-items:center;justify-content:center;overflow:hidden;">'
    '<iframe src="https://worldppc.click/ads.php?publisher_id=3&website_id=1&type=text&size=728x90" '
    'width="728" height="90" frameborder="0" scrolling="no" '
    'style="border:0;overflow:hidden;width:728px;height:90px;max-width:100%;" loading="lazy"></iframe>'
    '</div>'
)

AD_728_2 = (
    '<!-- Ad Block 728x90 Slot 2 -->'
    '<div class="ad-leaderboard" style="width:728px;height:90px;margin:1.5rem auto;background:#F0EAE4;'
    'border:2px dashed #5A9898;display:flex;align-items:center;justify-content:center;overflow:hidden;">'
    '<iframe src="https://worldppc.click/ads.php?publisher_id=3&website_id=2&type=banner&size=728x90" '
    'width="728" height="90" frameborder="0" scrolling="no" '
    'style="border:0;overflow:hidden;width:728px;height:90px;max-width:100%;" loading="lazy"></iframe>'
    '</div>'
)

AD_CLEARFIX = '<div class="ad-clearfix"></div>'
AD_TAGS = {"ad-block", "ad-label", "ad-slot", "ad-leaderboard", "ad-clearfix"}
CATEGORY_DIRS = [
    "best",
    "blood-sugar",
    "complications",
    "devices",
    "exercise",
    "monitoring",
    "nutrition",
    "prediabetes",
    "sleep-stress",
    "supplements",
    "type-2-diabetes",
    "weight-management",
    "reviews",
]


class ArticleParser(HTMLParser):
    """Collect one article while ignoring every old ad element."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_article = False
        self.suppress_depth = 0
        self.tokens = []
        self.paragraph_count = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if not self.in_article:
            if tag == "article":
                self.in_article = True
                self.tokens.append(self.get_starttag_text())
            return

        if tag in AD_TAGS:
            self.suppress_depth += 1

        if self.suppress_depth == 0:
            self.tokens.append(self.get_starttag_text())
            if tag == "p":
                self.paragraph_count += 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if not self.in_article:
            return

        if self.suppress_depth > 0:
            self.suppress_depth -= 1
        elif tag == "article":
            self.tokens.append(self.get_starttag_text().replace(">", "/>", 1) if False else "</article>")
            self.in_article = False
        else:
            self.tokens.append(self.get_starttag_text().replace(">", "/>", 1) if False else f"</{tag}>")

    def get_article(self):
        if not self.in_article and not self.tokens:
            return None, 0
        if not self.tokens:
            return None, 0
        if self.tokens[-1].lower() != "</article>":
            return None, 0
        return "".join(self.tokens[1:-1]), self.paragraph_count


def rebuild_article(article_html, paragraph_count):
    """Insert the three requested ad slots into a cleaned article body."""
    if paragraph_count < 2:
        return article_html

    paragraph_ends = [
        index for index, token in enumerate(article_html.split("</p>"))
        if index < len(article_html.split("</p>")) - 1
    ]
    # The list above is easier to reason about as end-tag offsets below.
    # Use the actual closing-paragraph offsets rather than token indices.
    paragraph_end_offsets = [
        match.end() for match in re.finditer(r"</p>", article_html)
    ]
    total = len(paragraph_end_offsets)
    if total < 2:
        return article_html

    slot_35_after = max(1, int(total * 0.35 + 0.5))
    slot_70_after = max(slot_35_after + 2, int(total * 0.70 + 0.5))
    if slot_70_after >= total:
        slot_70_after = total - 1
    if slot_35_after >= total:
        slot_35_after = total - 1

    insertions = []
    insertions.append((paragraph_end_offsets[slot_70_after - 1], "\n" + AD_728_2 + "\n"))
    insertions.append((paragraph_end_offsets[slot_35_after - 1], "\n" + AD_CLEARFIX + "\n" + AD_728_1 + "\n"))
    insertions.append((paragraph_end_offsets[0], "\n" + AD_300_BLOCK + "\n"))
    insertions.sort(key=lambda item: item[0], reverse=True)

    for offset, ad_html in insertions:
        article_html = article_html[:offset] + ad_html + article_html[offset:]

    return article_html


def fix_css(content):
    """Make the reusable ad rule float left with the requested margin."""
    content = re.sub(
        r"(\.ad-block\s*\{[^}]*?)float:\s*right",
        r"\1float:left",
        content,
        flags=re.IGNORECASE,
    )
    content = re.sub(
        r"(\.ad-block\s*\{[^}]*?)margin:\s*0\s*0\s*24px\s*36px",
        r"\1margin:0 36px 24px 0",
        content,
        flags=re.IGNORECASE,
    )
    return content


def process_file(filepath):
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    parser = ArticleParser()
    parser.feed(content)
    article, paragraph_count = parser.get_article()
    if article is None:
        return False

    article = rebuild_article(article, paragraph_count)
    new_content = content[: content.index("<article")] + article + content[content.index("</article>") + len("</article>") :]
    new_content = fix_css(new_content)

    if new_content == content:
        return False

    filepath.write_text(new_content, encoding="utf-8")
    return True


def main():
    processed = 0
    for directory in CATEGORY_DIRS:
        category_path = ROOT / directory
        if not category_path.exists():
            continue
        for filepath in sorted(category_path.glob("*.html")):
            if process_file(filepath):
                processed += 1
                content = filepath.read_text(encoding="utf-8", errors="ignore")
                print(
                    f"{filepath.relative_to(ROOT)}: "
                    f"300x250={content.count('format=js')}, "
                    f"728x90-slot1={content.count('Slot 1')}, "
                    f"728x90-slot2={content.count('Slot 2')}"
                )

    print(f"\nProcessed {processed} article files.")


if __name__ == "__main__":
    main()
