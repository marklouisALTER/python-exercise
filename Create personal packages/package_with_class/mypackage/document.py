# Define class with minimal attribute
class Document:  # it should be written in CamelCase 
    """ A minimal example class

    :param value: value to set as the ``attribute`` attribute
    :ivar attribute: contains the contents of the ``value`` passed in init
    """
    # add a comment to some person who gonna use the package -> help(my_class) it will prompt that documentation

    # Method to create a new instance of MyClass
    def __init__(self, value):
        # Define attribute with the contents of the value param
        self.text = value

# class Document:
#     def __init__(self, text):   
#         self.text = text
#         # pre tokenize the document with non-public tokenize method
#         self.tokens = self._tokenize()
#     # pre tokenize the document with non-public count_words
#         self.word_counts = self._count_words()

#     def _tokenize(self):
#         return tokenize(self.text)

#     # non-public method to tally document's word counts with Counter
#     def _count_words(self):
#         return Counter(self.tokens)
        
        # Define a SocialMedia class that is a child of the `Document class`
# class SocialMedia(Document):
#     def __init__(self, text):
#         Document.__init__(self, text)



