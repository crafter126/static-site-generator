import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        html_node = HTMLNode(
            "a",
            "Click here to go to search search engine",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        value = html_node.props_to_html()
        self.assertEqual(value, ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        html_node = HTMLNode(
            "p",
            "This is a normal paragraph",
            None,
            None,
        )
        self.assertEqual(html_node.tag, "p")
        self.assertEqual(html_node.value, "This is a normal paragraph")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_repr(self):
        html_node = HTMLNode(
            "div",
            "This text should go inside a div element",
            None,
            {"class": "primary"},
        )
        print(html_node.__repr__())
        self.assertEqual(
            html_node.__repr__(),
            "HTMLNode(div, This text should go inside a div element, None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"class": "main-div"})
        self.assertEqual(node.to_html(), '<div class="main-div">Hello, world!</div>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
