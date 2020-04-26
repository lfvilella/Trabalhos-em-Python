import io
from html_pages import HtmlPagesConverter


def test_convert_quotes():
    fake_file = io.StringIO("quote: ' ")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_pages(0)
    assert converted_text == "quote: &#x27;<br />"


def test_access_second_page():
    fake_file = io.StringIO("""\
page_one
PAGE_BREAK
page_two
PAGE_BREAK
page_three
""")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_pages(1)
    assert converted_text == "page_two<br />"
