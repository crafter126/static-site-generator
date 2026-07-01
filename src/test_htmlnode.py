import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        html_node = HTMLNode(
            "a",
            "Click here to go to search search engine",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        value = html_node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', value)

    def test_values(self):
        html_node = HTMLNode(
            "p",
            "This is a normal paragraph",
            None,
            None,
        )
        self.assertEqual("p", html_node.tag)
        self.assertEqual("This is a normal paragraph", html_node.value)
        self.assertEqual(None, html_node.children)
        self.assertEqual(None, html_node.props)

    def test_repr(self):
        html_node = HTMLNode(
            "div",
            "This text should go inside a div element",
            None,
            {"class": "primary"},
        )
        print(html_node.__repr__())
        self.assertEqual(
            "HTMLNode(div, This text should go inside a div element, None, {'class': 'primary'})",
            html_node.__repr__(),
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual("<p>Hello, world!</p>", node.to_html())

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual("<span>Hello, world!</span>", node.to_html())

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"class": "main-div"})
        self.assertEqual('<div class="main-div">Hello, world!</div>', node.to_html())

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual("Hello, world!", node.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual("<div><span>child</span></div>", parent_node.to_html())

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("span", "child", {"class": "child-span"})
        parent_node = ParentNode("div", [child_node], {"class": "main-div"})
        self.assertEqual(
            '<div class="main-div"><span class="child-span">child</span></div>',
            parent_node.to_html(),
        )

    def test_to_html_with_children_with_multiple_props(self):
        child_node = LeafNode("span", "child", {"class": "child-span", "id": "child"})
        parent_node = ParentNode(
            "div", [child_node], {"class": "main-div", "id": "main"}
        )
        self.assertEqual(
            '<div class="main-div" id="main"><span class="child-span" id="child">child</span></div>',
            parent_node.to_html(),
        )

    def test_to_html_with_one_grandchild(self):
        grand_child_node = LeafNode("p", "Grand child")
        child_node = ParentNode("div", [grand_child_node])
        parent_node = ParentNode("section", [child_node])
        self.assertEqual(
            "<section><div><p>Grand child</p></div></section>", parent_node.to_html()
        )

    def test_to_html_with_two_grandchildren(self):
        grand_child_node0 = LeafNode("p", "Grand child 0")
        grand_child_node1 = LeafNode("span", "Grand child 1")
        child_node = ParentNode("div", [grand_child_node0, grand_child_node1])
        parent_node = ParentNode("section", [child_node, LeafNode("div", "Hello")])
        self.assertEqual(
            "<section><div><p>Grand child 0</p><span>Grand child 1</span></div><div>Hello</div></section>",
            parent_node.to_html(),
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
