import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node0 = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node0, node1)

    def test_type_not_eq(self):
        node0 = TextNode("This is an italic text", TextType.ITALIC)
        node1 = TextNode("This is an italic text", TextType.TEXT)
        self.assertNotEqual(node0, node1)

    def test_text_not_eq(self):
        node0 = TextNode("This is an italic text", TextType.ITALIC)
        node1 = TextNode("This is not an italic text", TextType.ITALIC)
        self.assertNotEqual(node0, node1)

    def test_link_and_img_not_eq(self):
        node0 = TextNode("This is a link text", TextType.LINK, "https://www.google.com")
        node1 = TextNode(
            "This is an alt text for image",
            TextType.IMAGE,
            "https://www.image-repo.com/first-image",
        )
        self.assertNotEqual(node0, node1)

    def test_image_not_eq(self):
        node0 = TextNode(
            "This is an alt text",
            TextType.IMAGE,
            "https://www.some-image-domain.com/first-image",
        )
        node1 = TextNode("This is an alt text", TextType.IMAGE)
        self.assertNotEqual(node0, node1)


if __name__ == "__main__":
    unittest.main()
